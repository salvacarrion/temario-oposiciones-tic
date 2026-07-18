#!/usr/bin/env python3
"""
linkify_temas.py — Convierte referencias textuales a temas (ej. "tema 29", "temas 44 y 51")
en hipervínculos relativos dentro de los archivos Markdown en src/.

Uso:
    python3 tools/linkify_temas.py [--dry-run] [--check] [file1.md file2.md ...]

    Sin argumentos de archivo, procesa todos los archivos .md en src/ (excepto index.md o referencias.md).
    --dry-run muestra lo que cambiaría sin escribir en disco.
    --check   no escribe nada: detecta referencias elípticas a temas sin enlazar
              (ej. "…en el tema 71, y las redes inalámbricas en el 76") y las lista
              para revisión manual. No se linkifican automáticamente porque el número
              elíptico puede arrastrar una numeración antigua y el enlace apuntaría
              en silencio al tema equivocado.
"""

import re
import sys
import os
from pathlib import Path

# Colores para consola
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def build_theme_map(src_dir: Path) -> dict:
    """Escanea src/ y mapea el número del tema al nombre del archivo .md."""
    theme_map = {}
    for path in src_dir.glob("*.md"):
        # Ignorar archivos generales
        if path.name in ("index.md", "referencias.md", "prologo.md"):
            continue
        # Buscar temas que empiecen por dígitos (ej. "01-", "102-")
        match = re.match(r"^(\d+)-", path.name)
        if match:
            num = int(match.group(1))
            theme_map[num] = path.name
    return theme_map

def linkify_text(text: str, theme_map: dict, file_name: str, dry_run: bool) -> tuple:
    """
    Busca referencias a temas y las convierte en hipervínculos relativos.
    Omitirá coincidencias que ya estén dentro de un enlace Markdown.
    Retorna (nuevo_texto, num_cambios, lista_detalles).
    """
    # Patrón para enlaces Markdown existentes: [texto](url)
    markdown_link_pattern = r"(\[[^\]]+\]\([^)]+\))"
    
    # Patrón para temas: "tema/s" seguido de números separados por comas, "y", "o", "u", "a"
    # Ej: "tema 29", "temas 44 y 51", "temas 80 a 82"
    target_pattern = r"\b(temas?)\s+(\d+(?:(?:,\s*|\s+(?:y|o|u|a)\s*)\d+)*)\b"
    
    combined_pattern = re.compile(markdown_link_pattern + "|" + target_pattern, re.IGNORECASE)
    
    changes = 0
    details = []
    
    # Separar en líneas para poder dar un reporte con número de línea
    lines = text.splitlines(keepends=True)
    new_lines = []
    
    for line_idx, line in enumerate(lines, 1):
        modified_line = line
        
        def replace(match):
            nonlocal changes
            # Si coincide el grupo 1, es un enlace Markdown existente. Lo dejamos intacto.
            if match.group(1):
                return match.group(1)
            
            # En caso contrario, es una referencia de tema para linkificar
            tema_word = match.group(2)  # "tema" o "temas"
            numbers_part = match.group(3)  # ej. "44 y 51"
            
            # Buscar cada número de forma individual e intentar linkificarlo
            had_replacement = False
            
            def replace_num(num_match):
                nonlocal had_replacement
                num_str = num_match.group(0)
                num_val = int(num_str)
                if num_val in theme_map:
                    had_replacement = True
                    return f"[{num_str}]({theme_map[num_val]})"
                return num_str
            
            new_numbers_part = re.sub(r"\b\d+\b", replace_num, numbers_part)
            
            if had_replacement:
                changes += 1
                replacement = f"{tema_word} {new_numbers_part}"
                # Guardar el detalle del cambio
                details.append({
                    "line": line_idx,
                    "original": match.group(0),
                    "replaced": replacement
                })
                return replacement
            
            return match.group(0)
        
        # Realizar el sub en la línea
        modified_line = combined_pattern.sub(replace, line)
        new_lines.append(modified_line)
        
    return "".join(new_lines), changes, details

def check_orphans(text: str, theme_map: dict) -> list:
    """
    Detecta referencias elípticas a temas que quedaron sin hipervínculo:
    números de tema precedidos de artículo ("en el 76", "los 71 y 79") en líneas
    con contexto de tema (mencionan "tema" o ya enlazan a un fichero NN-*.md).
    Retorna lista de dicts {line, num, context} para revisión manual.
    """
    markdown_link_pattern = re.compile(r"\[[^\]]*\]\([^)]*\)")
    tema_link_pattern = re.compile(r"\]\(\d+-[^)]+\.md\)")
    # Número precedido de artículo/conector típico de referencia elíptica
    candidate_pattern = re.compile(
        r"\b(?:en el|en los|y el|y los|o el|y en el|el|los|al)\s+(\d{1,3})\b(?![.,]?\d)"
    )
    # Tras el número debe venir puntuación o conjunción ("…en el 76, …", "…en el 79.");
    # si sigue otra palabra ("los 4 hosts", "el 21 de febrero") no es referencia a tema
    after_ok_pattern = re.compile(r"^\s*$|^\s*[.,;:)…]|^\s+(?:y|e|o|u)\b")

    findings = []
    for line_idx, line in enumerate(text.splitlines(), 1):
        if not (re.search(r"\btemas?\b", line, re.IGNORECASE) or tema_link_pattern.search(line)):
            continue
        # Quitar los enlaces existentes para no re-detectar sus números
        stripped = markdown_link_pattern.sub(" <LINK> ", line)
        for match in candidate_pattern.finditer(stripped):
            num = int(match.group(1))
            if num not in theme_map:
                continue
            if not after_ok_pattern.match(stripped[match.end():]):
                continue
            ctx_start = max(0, match.start() - 40)
            context = stripped[ctx_start:match.end() + 40].strip()
            findings.append({"line": line_idx, "num": num, "context": context})
    return findings

def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    if dry_run:
        args.remove("--dry-run")
    check_mode = "--check" in args
    if check_mode:
        args.remove("--check")
        
    project_root = Path(__file__).resolve().parent.parent
    src_dir = project_root / "src"
    
    if not src_dir.exists():
        print(f"Error: No se encontró la carpeta 'src/' en {src_dir}")
        sys.exit(1)
        
    theme_map = build_theme_map(src_dir)
    if not theme_map:
        print(f"Error: No se encontraron temas en {src_dir}")
        sys.exit(1)
        
    # Seleccionar archivos a procesar
    if args:
        files_to_process = [Path(f) for f in args]
    else:
        # Por defecto procesamos todos los archivos md del directorio src/
        files_to_process = sorted(list(src_dir.glob("*.md")))
        
    total_files_changed = 0
    total_replacements = 0
    
    mode = "CHECK" if check_mode else ("DRY-RUN" if dry_run else "REAL")
    print(f"=== Iniciando Linkify Temas ({mode}) ===")
    print(f"Mapeados {len(theme_map)} temas en 'src/'.")
    
    for file_path in files_to_process:
        if file_path.name in ("index.md", "referencias.md", "prologo.md"):
            continue
            
        if not file_path.exists():
            print(f"Advertencia: El archivo {file_path} no existe.")
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if check_mode:
            findings = check_orphans(content, theme_map)
            if findings:
                total_files_changed += 1
                total_replacements += len(findings)
                print(f"\nArchivo: {file_path.relative_to(project_root)} ({len(findings)} candidatos)")
                for d in findings:
                    print(f"  Línea {d['line']}: [{d['num']}] …{d['context']}…")
            continue

        new_content, num_changes, details = linkify_text(content, theme_map, file_path.name, dry_run)
        
        if num_changes > 0:
            total_files_changed += 1
            total_replacements += num_changes
            print(f"\nArchivo: {file_path.relative_to(project_root)} ({num_changes} cambios)")
            for d in details:
                print(f"  Línea {d['line']}: {d['original']} -> {d['replaced']}")
                
            if not dry_run:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                    
    print("\n" + "="*50)
    if check_mode:
        print("Comprobación finalizada.")
        print(f"Archivos con referencias sin enlazar: {total_files_changed}")
        print(f"Total de candidatos a revisar: {total_replacements}")
    elif dry_run:
        print("Simulación finalizada.")
        print(f"Archivos que cambiarían: {total_files_changed}")
        print(f"Total de referencias que se linkificarían: {total_replacements}")
    else:
        print("Proceso completado exitosamente.")
        print(f"Archivos modificados: {total_files_changed}")
        print(f"Total de referencias linkificadas: {total_replacements}")

if __name__ == "__main__":
    main()
