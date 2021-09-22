import re


# 读取并清除注释等
def read_file(path):
    c_file = open(path, 'r')
    c_file_text = c_file.read()
    c_file_text = re.sub('\n\n', "\n", c_file_text)
    c_file_text = re.sub('\\\\\n', "", c_file_text)
    c_file_text = re.sub('/\*[\s\S]*\*/', "", c_file_text)
    c_file_text = re.sub('".*"', "", c_file_text)
    c_file_text = re.sub('//.*\n', "\n", c_file_text)
    return c_file_text


def count_keywords(text):
    keywords = \
        [
            'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
            'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
            'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
            'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while'
        ]
    counter = [0] * 32
    for i in range(32):
        temp = re.findall('[\s\t\n]' + keywords[i] + '[;:({\s]', text)
        if temp is None:
            continue
        counter[i] = len(temp)
    total = sum(counter)
    return total


def count_switch(text):
    case_counter = []
    for i in re.findall('switch.*{[^}]+}', text):
        case_counter.append(len(re.findall('[\s]case[\s]', i)))
    return case_counter


def count_if_else(text):
    if_else_counter = 0
    for i in re.findall('[^(else)][\s]if.*{.*}\s*else\s*{[^}]*}', text):
        if_else_counter += 1
    return if_else_counter


def remove_if_else(text):
    return re.sub('[^(else)][\s]if.*{.*}\s*else\s*{[^}]*}', "", text)


def count_if_elseif_else(text):
    if_else_if_else_counter = 0
    while re.findall('(if\s*\(.+\)\s*{[^(else)\s\S]*\s*}\s*else\s*)+{[^(else)\s\S]*\s*}', text):
        if_else_if_else_counter += 1
        text = re.sub('(if\s*\(.+\)\s*{[^(else)\s\S]*\s*}\s*else\s*)+{[^(else)\s\S]*\s*}', "", text)
    return if_else_if_else_counter


c_path = 'demo.c'
text_temp = read_file(c_path)
print("total:", count_keywords(text_temp))
print("case:", end='')
for i in count_switch(text_temp):
    print(i, end=' ')
print()
print('if-else:', count_if_else(text_temp))
text_temp = remove_if_else(text_temp)
print('if-elseif-else:', count_if_elseif_else(text_temp))
