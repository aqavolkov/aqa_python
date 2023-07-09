"""
HW:9 fix[Volkov Anton].

write script that will read "input.txt" file and find there all characters
from english alphabet
collect these letter characters and their positions in file
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
add_print = ''
positions = []
# Read from files alphabet letter and their positions
with open('input.txt', 'r') as fh:
    text = fh.read()
    for match in re.finditer(r'(?<![A-Za-z])[A-Za-z](?![A-Za-z])', text):
        letter = match.group()
        position = match.start()
        positions.append((letter, position))
    for letter, pos in positions:
        add_print += f'{letter} -> pos{pos}\n'

# Write f'{letter} -> pos{pos}\n' to output.txt file
with open('output.txt', 'w') as letters_info:
    letters_info.write(SEPARATOR)
    letters_info.write(add_print)
    letters_info.write(SEPARATOR)
