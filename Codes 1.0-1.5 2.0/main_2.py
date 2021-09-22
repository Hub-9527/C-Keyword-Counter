from typing import TextIO
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
    temp = re.findall('[\s\)}]'+keywords[i]+'[;:({\s]', c_file_text)
    if temp is None:
        continue
    print(temp)
    counter[i] = len(temp)

total = sum(counter)
print('total:', total)
for i in range(32):
    if counter[i] > 0:
        print(keywords[i], ':', counter[i])


