from typing import TextIO

keywords = \
    [
        'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
        'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
        'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
        'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while'
    ]

counter = [0] * 32

c_file = open('demo.c', 'r')
c_file_text = c_file.read()
print(c_file_text)

for i in range(32):
    if c_file_text.find(keywords[i]) > 0:
        temp = c_file_text.find(keywords[i])
        while c_file_text.find(keywords[i], temp + 1):
            counter[i] += 1
            temp = c_file_text.find(keywords[i], temp + 1)
            if temp < 0:
                break

for i in range(32):
    if counter[i] > 0:
        print(keywords[i], ':', counter[i])
