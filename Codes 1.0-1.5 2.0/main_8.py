import re


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


def count_if_else_etc(text):
    if_else_total = re.findall('if|else\s+if|else', text)
    print(if_else_total)
    temp_if_else_stack = []
    if_else_count = 0
    if_elseif_else_count = 0
    for i in if_else_total:
        if i == 'if':
            temp_if_else_stack.append(i)
        elif i == 'else if':
            temp_if_else_stack.append(i)
        elif i == 'else':
            temp_last = temp_if_else_stack.pop()
            if temp_last == 'if':
                if_else_count += 1
            elif temp_last == 'else if':
                if_elseif_else_count += 1
                while True:
                    temp_last = temp_if_else_stack.pop()
                    if temp_last == 'if':
                        break
    return [if_else_count, if_elseif_else_count]


c_path = 'demo.c'
text_temp = read_file(c_path)
print("total:", count_keywords(text_temp))
print("case:", end='')
for i in count_switch(text_temp):
    print(i, end=' ')
print()
print(count_if_else_etc(text_temp))
