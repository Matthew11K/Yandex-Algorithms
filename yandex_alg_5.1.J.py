import re

def parse_input(input_data):
    lines = input_data.strip().split('\n')
    w, h, c = map(int, lines[0].split())
    paragraphs = re.split(r'\n\s*\n', '\n'.join(lines[1:]))  # Разделение на абзацы
    return w, h, c, paragraphs

def parse_paragraph(paragraph):
    elements = []
    pattern = re.compile(r'\(image .+?\)|\S+')
    for match in pattern.finditer(paragraph):
        text = match.group()
        if text.startswith('(image'):
            elements.append(parse_image(text))
        else:
            elements.append(('word', len(text)))
    return elements

def parse_image(image_str):
    attributes = {}
    # Исправленный фрагмент: удаление скобок и пробелов перед разбором атрибутов
    image_str = image_str.strip('()')  # Удаление открывающей и закрывающей скобок
    for part in re.findall(r'(\w+)=(\S+)', image_str):
        value = part[1].rstrip(')')  # Удаление закрывающей скобки и других символов справа от значения
        attributes[part[0]] = int(value) if part[0] in ['width', 'height', 'dx', 'dy'] else part[1]
    return ('image', attributes)


input_data = """120 10 8
start (image layout=embedded width=12 height=5)
(image layout=surrounded width=25 height=58)
and word is 
(image layout=floating dx=18 dy=-15 width=25 height=20)
here new 
(image layout=embedded width=20 height=22)
another
(image layout=embedded width=40 height=19)
longword

new paragraph
(image layout=surrounded width=5 height=30)
(image layout=floating width=20 height=35 dx=50 dy=-16)"""

w, h, c, raw_paragraphs = parse_input(input_data)
paragraphs = [parse_paragraph(p) for p in raw_paragraphs]

print(w, h, c)
print(paragraphs)
