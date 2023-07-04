"""
HW:9[Volkov Anton].

write script that will read "input.txt" file and find there all characters
from english alphabet
collect these letteracters and their positions in file
after info collected this info as text
write to "output.txt" file in such format
####################
<first found letter> -> pos1
<next_letter> -> pos2
<next_letter -> pos3
etc
#######################
"""
import re

SEPARATOR = '#' * 15 + '\n'
with open('input.txt', 'r') as fh:
    text = fh.read()
    result = re.findall('[a-zA-Z]', text)
    positions = []
    for letter in result:
        position = text.find(letter)
        positions.append((letter, position))
    add_print = ''
    for letter, pos in positions:
        add_print += f'{letter} -> pos{pos}\n'

with open('output.txt', 'x') as letters_info:
    letters_info.write(SEPARATOR)
    letters_info.write(add_print)
    letters_info.write(SEPARATOR)
