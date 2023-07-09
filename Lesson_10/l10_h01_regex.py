"""
HW:10[Volkov Anton].

open input.txt file and find all small english letters
that match such conditions:
target small letter round exactly with three capital english
letters on the left and on the right
Match examples:
sdTRYaUVKn  -> matches "a"
NTRSjARTb   -> no match ( not exactly 3 capital letters on the left)
zDFGbOPNq   -> matches "b"
Print Output as : "Result: "<your_found_human_readable_string">
"""
import re

# 1. Write regex pattern
pattern = r'(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])'
# 2. Open input.txt to read
with open('input.txt', 'r') as fh:
    text = fh.read()
# 3. Find characters use regex pattern from input.txt
find_ch = re.findall(pattern, text)
# 4. List -> string
result = ' '.join(find_ch)
# 5. Print output as : "Result: "<your_found_human_readable_string">
print(f'Result: {result}')
