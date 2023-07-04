"""
HW:8[Volkov Anton].

Given the list of integers ( positive , negative, zeros)
Find max multiplication of three values in list
l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]

Input: [-1, 1, 2, 0, 3, 12, 4, 5, -1, 6]
Output: Max value = "360". Nums are: (12, 5, 6)

Input: [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
Output: Max value = "2016". Nums are: (-7, 12, -24)
"""
l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
multiplication_numbers = ()
max_value = 0

for i in range(len(l1) - 2):
    for x in range(i + 1, len(l1) - 1):
        for y in range(x + 1, len(l1)):
            result = l1[i] * l1[x] * l1[y]
            if result > max_value:
                max_value = result
                multiplication_numbers = (l1[i], l1[x], l1[y])

print(f'Max value = "{max_value}". Nums are: {multiplication_numbers}')
