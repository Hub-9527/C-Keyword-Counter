import re

keywords = \
    [
        'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
        'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
        'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
        'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while'
    ]

counter = [0] * 32
total = 0

c_file = open('demo.c', 'r')
c_file_text = c_file.read()
print(c_file_text)

for i in range(32):
    temp = re.findall('[\s\t\n]' + keywords[i] + '[;:({\s]', c_file_text)
    if temp is None:
        continue
    # print(temp)
    counter[i] = len(temp)

total = sum(counter)
print('total:', total)
# for i in range(32):
#     if counter[i] > 0:
#         print(keywords[i], ':', counter[i])
#

case_counter = []
for i in re.findall('switch.*{[^}]+}', c_file_text):
    case_counter.append(len(re.findall('[\s]case[\s]', i)))
print('case:', end=' ')
for i in case_counter:
    print(i, end=' ')
print()

if_else_counter = 0
for i in re.findall('[^(else)][\s]if.*{.*}\s*else\s*{[^}]*}', c_file_text):
    if_else_counter += 1
print('if else:', if_else_counter)
