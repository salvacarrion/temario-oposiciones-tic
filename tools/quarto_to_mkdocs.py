#!/usr/bin/env python3
import os
import yaml
import re

def get_md_title(filepath):
    """Reads the first H1 heading from a markdown/qmd file as the title."""
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('# '):
                    title = line[2:].strip()
                    # Remove Quarto curly bracket attributes, e.g. {#sec-xxx} or {.unnumbered}
                    title = re.sub(r'\s*\{[^}]*\}\s*$', '', title)
                    return title
    except Exception as e:
        print(f"Warning: Could not read title from {filepath}: {e}")
    
    # Fallback to prettified filename
    basename = os.path.basename(filepath)
    name_without_ext = os.path.splitext(basename)[0]
    # Remove numbers prefix if any (like 01-, 02-)
    name_clean = re.sub(r'^\d+-', '', name_without_ext)
    return name_clean.replace('-', ' ').capitalize()

def get_numbered_title(filepath):
    """Reads the title and prefixes it with the topic number from the filename."""
    title = get_md_title(filepath)
    if not title:
        return None
    basename = os.path.basename(filepath)
    match = re.match(r'^(\d+)-', basename)
    if match:
        num = int(match.group(1))
        return f"Tema {num}: {title}"
    return title

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    quarto_yml_path = os.path.join(base_dir, '_quarto.yml')
    mkdocs_yml_path = os.path.join(base_dir, 'mkdocs.yml')
    
    if not os.path.exists(quarto_yml_path):
        print(f"Error: _quarto.yml not found at {quarto_yml_path}")
        return
        
    with open(quarto_yml_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
        
    book_cfg = config.get('book', {})
    title = book_cfg.get('title', 'Temario de Oposiciones TIC')
    subtitle = book_cfg.get('subtitle', '')
    author = book_cfg.get('author', 'Salvador Carrión Ponz')
    
    # Build nav structure
    nav = []
    
    chapters = book_cfg.get('chapters', [])
    appendices = book_cfg.get('appendices', [])
    
    for item in chapters:
        if isinstance(item, str):
            if item == 'index.qmd':
                nav.append({"Inicio": "index.md"})
            else:
                filepath = os.path.join(base_dir, item)
                t = get_numbered_title(filepath) or "Capítulo"
                rel_path = item.replace('src/', '')
                nav.append({t: rel_path})
        elif isinstance(item, dict):
            part_title = item.get('part')
            part_chapters = item.get('chapters', [])
            part_nav = []
            for chap in part_chapters:
                filepath = os.path.join(base_dir, chap)
                t = get_numbered_title(filepath) or "Capítulo"
                rel_path = chap.replace('src/', '')
                part_nav.append({t: rel_path})
            if part_title:
                nav.append({part_title: part_nav})
            else:
                nav.extend(part_nav)
                
    if appendices:
        app_nav = []
        for app in appendices:
            filepath = os.path.join(base_dir, app)
            t = get_md_title(filepath) or "Apéndice"
            rel_path = app.replace('src/', '')
            app_nav.append({t: rel_path})
        nav.append({"Apéndices": app_nav})
        
    # Add PDF download link
    nav.append({"Descargar PDF": "temario-oposiciones-tic.pdf"})
        
    mkdocs_config = {
        'site_name': title,
        'site_description': subtitle,
        'site_author': author,
        'repo_name': 'salvacarrion/temario-oposiciones-tic',
        'repo_url': 'https://github.com/salvacarrion/temario-oposiciones-tic',
        'copyright': 'Copyright &copy; 2026 Salva Carrión &mdash; Licencia <a href="https://creativecommons.org/licenses/by-nc/4.0/deed.es" target="_blank" rel="noopener">CC BY-NC 4.0</a> (puedes compartir y adaptar el material dando crédito al autor y sin fines comerciales)',
        'theme': {
            'name': 'material',
            'logo': 'logos/monkey128.png',
            'favicon': 'favicon/favicon.ico',
            'custom_dir': 'theme_overrides',
            'palette': [
                {
                    'media': '(prefers-color-scheme: light)',
                    'scheme': 'default',
                    'primary': 'teal',
                    'accent': 'teal',
                    'toggle': {
                        'icon': 'material/brightness-7',
                        'name': 'Switch to dark mode'
                    }
                },
                {
                    'media': '(prefers-color-scheme: dark)',
                    'scheme': 'slate',
                    'primary': 'teal',
                    'accent': 'teal',
                    'toggle': {
                        'icon': 'material/brightness-4',
                        'name': 'Switch to light mode'
                    }
                }
            ],
            'features': [
                'navigation.instant',
                'navigation.sections',
                'navigation.expand',
                'navigation.top',
                'navigation.tracking',
                'navigation.indexes',
                'toc.integrate',
                'content.code.copy',
                'search.suggest',
                'search.highlight'
            ]
        },
        'markdown_extensions': [
            'admonition',
            'pymdownx.details',
            'pymdownx.superfences',
            'pymdownx.arithmatex',
            'attr_list'
        ],
        'extra_javascript': [
            'javascripts/mathjax.js',
            'https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js'
        ],
        'docs_dir': 'src',
        'site_dir': 'book-mkdocs',
        'nav': nav
    }
    
    with open(mkdocs_yml_path, 'w', encoding='utf-8') as f:
        yaml.dump(mkdocs_config, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        
    print(f"Created {mkdocs_yml_path}")

if __name__ == '__main__':
    main()
