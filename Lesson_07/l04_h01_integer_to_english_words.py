"""
HW:7[Volkov Anton].

Convert a non-negative integer num to its English words representation.
Example 1:
Input: num = 123
Output: 'One Hundred Twenty Three'
let's take that number always > 100 and only three digits
100 <= num <= 999
"""
num = 123
number = ['', 'One', 'Two', 'Three', 'Four', 'Five',
          'Six', 'Seven', 'Eight', 'Nine']
numbers = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty',
           'Sixty', 'Seventy', 'Eighty', 'Ninety']
numbers_0 = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
             'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

digits_00 = num // 100
digits_0 = (num % 100) // 10
digit = num % 10

if 100 <= num <= 999:
    result = ' '.join([number[digits_00] + ' Hundred ']
                      if digits_00 > 0 else [])
    result += ' '.join([numbers_0[digit]]
                       if digits_0 == 1
                       else [numbers[digits_0], number[digit]])
    print(result)
else:
    print('Error. Please: enter integer between 100 and 999')
