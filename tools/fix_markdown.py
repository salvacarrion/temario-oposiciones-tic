#!/usr/bin/env python3
"""
fix_markdown.py — Homogeneiza el formato Markdown de los archivos en src/
para mejorar el renderizado en MkDocs Material.

Transformaciones aplicadas:
1. Eliminar <span class="indexref"...> tags
2. Eliminar atributos Pandoc de imágenes {width=... height=...}
3. Eliminar tags <u></u>
4. Unir líneas soft-wrapped (párrafos y bullets partidos en ~72 cols)
5. Eliminar líneas en blanco redundantes entre bullet points
6. Normalizar listas numeradas de "1.  " a "1. "
7. Convertir pseudo-encabezados en negrita a ###
8. Eliminar líneas en negrita duplicadas bajo H2 existentes
9. Convertir patrones **Título**\\ a ### Título

Usage:
    python3 tools/fix_markdown.py [--dry-run] [file1.md file2.md ...]
    
    Without file arguments, processes all .md files in src/
    --dry-run shows what would change without writing
"""

import re
import sys
import glob
import os
from pathlib import Path


def remove_indexref_spans(text: str) -> str:
    """Remove <span class="indexref" ...></span> tags."""
    return re.sub(r'<span\s+class="indexref"[^>]*>\s*</span>\n?', '', text)


def remove_pandoc_image_attrs(text: str) -> str:
    """Remove Pandoc-style image attributes {width=... height=...}."""
    return re.sub(r'(\!\[[^\]]*\]\([^)]+\))\{[^}]*\}', r'\1', text)


def remove_underline_tags(text: str) -> str:
    """Remove <u></u> HTML tags, keeping inner text."""
    text = re.sub(r'<u>(.*?)</u>', r'\1', text, flags=re.DOTALL)
    return text


def normalize_numbered_lists(text: str) -> str:
    """Normalize '1.  ' (double space) to '1. ' (single space) in numbered lists."""
    return re.sub(r'^(\s*\d+\.)\s{2,}', r'\1 ', text, flags=re.MULTILINE)


def is_bullet_line(line: str) -> bool:
    """Check if a line starts with a bullet marker (-, *, or numbered)."""
    stripped = line.lstrip()
    return bool(re.match(r'^[-*]\s', stripped) or re.match(r'^\d+\.\s', stripped))


def is_heading_line(line: str) -> bool:
    """Check if a line is a markdown heading."""
    return line.lstrip().startswith('#')


def is_html_block_line(line: str) -> bool:
    """Check if a line is part of an HTML block (table, etc.)."""
    stripped = line.strip()
    return bool(re.match(r'^</?(?:table|thead|tbody|tr|td|th|colgroup|col|div)\b', stripped, re.IGNORECASE))


def is_table_line(line: str) -> bool:
    """Check if a line is a markdown table row (starts with optional whitespace and '|')."""
    return line.lstrip().startswith('|')


def is_continuation_line(line: str) -> bool:
    """Check if a line looks like a continuation of a previous paragraph/bullet."""
    if not line or line.isspace():
        return False
    if is_heading_line(line):
        return False
    if is_bullet_line(line):
        return False
    if is_html_block_line(line):
        return False
    if is_table_line(line):
        return False
    # A line that starts with spaces (indentation) and then text
    if line[0] == ' ' and line.strip():
        return True
    return False


def get_indent(line: str) -> int:
    """Get the indentation level of a line."""
    return len(line) - len(line.lstrip())


def join_soft_wrapped_lines(text: str) -> str:
    """Join lines that were soft-wrapped by Pandoc at ~72 columns.
    
    Handles both:
    - Indented continuation lines in bullet items
    - Non-indented paragraph continuation lines
    """
    lines = text.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Skip blank lines, headings, HTML blocks, table lines
        if not line.strip() or is_heading_line(line) or is_html_block_line(line) or is_table_line(line):
            result.append(line)
            i += 1
            continue
        
        # Start accumulating a logical line
        current = line
        current_indent = get_indent(line)
        current_is_bullet = is_bullet_line(line)
        
        # Look ahead for continuation lines
        while i + 1 < len(lines):
            next_line = lines[i + 1]
            
            # Stop at blank lines
            if not next_line.strip():
                break
            # Stop at headings
            if is_heading_line(next_line):
                break
            # Stop at HTML blocks
            if is_html_block_line(next_line):
                break
            # Stop at table lines
            if is_table_line(next_line):
                break
            # Stop at new bullet items
            if is_bullet_line(next_line):
                break
            
            # For indented continuation lines (inside bullets)
            if is_continuation_line(next_line):
                current = current.rstrip() + ' ' + next_line.strip()
                i += 1
            # For non-indented continuation lines (paragraph wrapping)
            elif get_indent(next_line) == 0 and not current_is_bullet and current_indent == 0:
                # Next line is a plain non-indented text line continuing a paragraph
                current = current.rstrip() + ' ' + next_line.strip()
                i += 1
            else:
                break
        
        result.append(current)
        i += 1
    
    return '\n'.join(result)


def remove_redundant_blank_lines_between_bullets(text: str) -> str:
    """Remove blank lines between bullet points at the same or nested level."""
    lines = text.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        result.append(line)
        
        if is_bullet_line(line) and i + 1 < len(lines) and not lines[i + 1].strip():
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            
            if j < len(lines) and (is_bullet_line(lines[j]) or is_continuation_line(lines[j])):
                i = j
                continue
        
        i += 1
    
    return '\n'.join(result)


def is_standalone_bold(line: str) -> bool:
    """Check if a line is just **Some Text** on its own."""
    stripped = line.strip()
    return bool(re.match(r'^\*\*[^*]+\*\*$', stripped))


def is_bold_with_linebreak(line: str) -> bool:
    """Check if a line is **Some Text**\\ (bold with trailing backslash)."""
    stripped = line.strip()
    return bool(re.match(r'^\*\*[^*]+\*\*\\\\?$', stripped))


def extract_bold_text(line: str) -> str:
    """Extract the text from a **Text** or **Text**\\\\ pattern."""
    stripped = line.strip()
    m = re.match(r'^\*\*(.+?)\*\*\\*$', stripped)
    if m:
        return m.group(1)
    return ''


def convert_pseudo_headings(text: str) -> str:
    """Convert standalone bold text acting as headings to headings or lists."""
    lines = text.split('\n')
    result = []
    i = 0
    extra_indent = ''
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # If we see a real markdown heading, we reset the extra indentation
        if line.lstrip().startswith('#'):
            extra_indent = ''
            result.append(line)
            i += 1
            continue
            
        is_pseudo = False
        bold_text = ''
        
        if is_bold_with_linebreak(stripped) and stripped.endswith('\\'):
            bold_text = extract_bold_text(stripped)
            is_pseudo = True
        elif is_standalone_bold(stripped):
            bold_text = extract_bold_text(stripped)
            is_pseudo = True
            
        if is_pseudo and bold_text:
            is_article = bool(re.search(r'\b(Art|Artículo)\b', bold_text))
            
            if is_article:
                # Normalize "Artículo" to "Art."
                normalized_text = re.sub(r'\bArtículo\b', 'Art.', bold_text)
                result.append(f'- **{normalized_text}**:')
                extra_indent = '    '
                i += 1
                continue
            else:
                extra_indent = ''
                prev_heading = None
                for j in range(len(result) - 1, -1, -1):
                    if result[j].strip():
                        if result[j].strip().startswith('## '):
                            prev_heading = result[j].strip()[3:].strip()
                        break
                
                if prev_heading and _texts_similar(prev_heading, bold_text):
                    i += 1
                    if i < len(lines) and not lines[i].strip():
                        i += 1
                    continue
                    
                result.append(f'### {bold_text}')
                i += 1
                continue
                
        if extra_indent and line.strip():
            result.append(extra_indent + line)
        else:
            result.append(line)
            
        i += 1
        
    return '\n'.join(result)


def _texts_similar(a: str, b: str) -> bool:
    """Check if two texts are similar enough to be considered duplicates."""
    def normalize(s):
        s = s.lower().strip()
        s = re.sub(r'\s+', ' ', s)
        s = re.sub(r'\s*\([^)]*\)', '', s)
        return s
    
    na = normalize(a)
    nb = normalize(b)
    
    if na == nb:
        return True
    if na in nb or nb in na:
        return True
    
    return False


def ensure_blank_line_before_heading(text: str) -> str:
    """Ensure there's a blank line before every heading (##, ###)."""
    lines = text.split('\n')
    result = []
    
    for i, line in enumerate(lines):
        if i > 0 and is_heading_line(line) and not line.startswith('# '):
            if result and result[-1].strip():
                result.append('')
        result.append(line)
    
    return '\n'.join(result)


def ensure_blank_line_after_heading(text: str) -> str:
    """Ensure there's a blank line after every heading."""
    lines = text.split('\n')
    result = []
    
    for i, line in enumerate(lines):
        result.append(line)
        if is_heading_line(line) and i + 1 < len(lines):
            next_line = lines[i + 1]
            if next_line.strip():
                result.append('')
    
    return '\n'.join(result)


def convert_2space_to_4space_indent(text: str) -> str:
    """Convert list indentation to exactly level * 4 spaces.
    
    Python-Markdown (used by MkDocs) requires 4 spaces for nested list items.
    This stack-based approach tracks list hierarchy levels (0, 1, 2...)
    and sets indentation to exactly level * 4 spaces.
    """
    lines = text.split('\n')
    result = []
    list_stack = []
    
    for line in lines:
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        
        if not stripped:
            result.append(line)
            continue
            
        is_bullet = bool(re.match(r'^[-*]\s', stripped) or re.match(r'^\d+\.\s', stripped))
        
        if is_bullet:
            while list_stack and indent <= list_stack[-1]:
                list_stack.pop()
            list_stack.append(indent)
            level = len(list_stack) - 1
            new_indent = level * 4
            result.append(' ' * new_indent + stripped)
        else:
            if list_stack and indent > 0:
                level = len(list_stack) - 1
                bullet_indent = list_stack[-1]
                extra_indent = max(0, indent - bullet_indent)
                new_indent = level * 4 + extra_indent
                result.append(' ' * new_indent + stripped)
            else:
                list_stack = []
                result.append(line)
                
    return '\n'.join(result)


def remove_empty_html_comments(text: str) -> str:
    """Remove empty HTML comment tags <!-- -->."""
    return re.sub(r'<!-- -->\n?', '', text)


def clean_headings(text: str) -> str:
    """Clean non-standard patterns from heading lines.
    
    1. Remove `<br />` or `<br>` inside headings.
    2. Remove Pandoc-style identifier attributes like `{#identifier}`.
    3. Delete completely empty/dummy headings like `## <br /> {#section}`.
    """
    lines = text.split('\n')
    result = []
    
    for line in lines:
        if line.lstrip().startswith('#'):
            # Check if heading is essentially empty (only containing br, spaces, or section ids)
            cleaned = re.sub(r'<br\s*/?>', '', line)
            cleaned = re.sub(r'\{#[^}]*\}', '', cleaned)
            header_content = cleaned.lstrip('#').strip()
            if not header_content:
                # Skip this entire empty heading
                continue
            
            # Otherwise, clean the header line
            line = re.sub(r'\s*<br\s*/?>\s*', ' ', line)
            line = re.sub(r'\s*\{#[^}]*\}\s*', '', line)
            parts = line.split(None, 1)
            if len(parts) == 2:
                line = parts[0] + ' ' + re.sub(r'\s+', ' ', parts[1]).strip()
                
        result.append(line)
        
    return '\n'.join(result)


def replace_non_breaking_spaces(text: str) -> str:
    """Replace non-breaking spaces (\xa0) with normal spaces."""
    return text.replace('\xa0', ' ')


def clean_multiple_blank_lines(text: str) -> str:
    """Replace 3+ consecutive blank lines with 2."""
    return re.sub(r'\n{4,}', '\n\n\n', text)


def ensure_trailing_newline(text: str) -> str:
    """Ensure file ends with exactly one newline."""
    return text.rstrip('\n') + '\n'


def process_file(filepath: str, dry_run: bool = False) -> dict:
    """Process a single markdown file. Returns stats about changes."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()
    
    text = original
    
    # Apply transformations in order
    # Note: convert_pseudo_headings must run BEFORE join_soft_wrapped_lines
    # because **Title**\\ patterns would get merged with paragraph text otherwise
    text = remove_indexref_spans(text)
    text = remove_pandoc_image_attrs(text)
    text = remove_underline_tags(text)
    text = remove_empty_html_comments(text)
    text = clean_headings(text)
    text = replace_non_breaking_spaces(text)
    text = normalize_numbered_lists(text)
    text = convert_pseudo_headings(text)
    text = join_soft_wrapped_lines(text)
    text = remove_redundant_blank_lines_between_bullets(text)
    text = convert_2space_to_4space_indent(text)
    text = ensure_blank_line_before_heading(text)
    text = ensure_blank_line_after_heading(text)
    text = clean_multiple_blank_lines(text)
    text = ensure_trailing_newline(text)
    
    changed = text != original
    stats = {
        'file': filepath,
        'changed': changed,
        'original_lines': original.count('\n'),
        'new_lines': text.count('\n'),
    }
    
    if changed and not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
    
    print_path = os.path.basename(filepath)
    if stats['changed']:
        delta = stats['new_lines'] - stats['original_lines']
        sign = '+' if delta >= 0 else ''
        print(f"  ✓ {print_path}: {stats['original_lines']} → {stats['new_lines']} lines ({sign}{delta})")
    else:
        print(f"  · {print_path}: no changes")
    
    return stats


def main():
    dry_run = '--dry-run' in sys.argv
    args = [a for a in sys.argv[1:] if a != '--dry-run']
    
    if args:
        files = args
    else:
        src_dir = Path(__file__).parent.parent / 'src'
        files = sorted(glob.glob(str(src_dir / '*.md')))
        files = [f for f in files if not f.endswith('SUMMARY.md')]
    
    if dry_run:
        print("=== DRY RUN — no files will be modified ===\n")
    
    changed_count = 0
    total_count = 0
    
    for filepath in files:
        total_count += 1
        stats = process_file(filepath, dry_run=dry_run)
        if stats['changed']:
            changed_count += 1
    
    print(f"\n{'DRY RUN: ' if dry_run else ''}Processed {total_count} files, {changed_count} modified.")


if __name__ == '__main__':
    main()
