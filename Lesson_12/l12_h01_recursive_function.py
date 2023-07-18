"""
HW:12[Volkov Anton].

Given list of list of list etc of integers
write recursive function that will accept as argument target list
and return sum of all integers inside it
Input: [[[[1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
Output: Target sum = 72
"""
target_list = [[[[1, 4, 5], [[6, 9], [[[8, 1],
               7], 3], 2], 7], 5, 2], 9, [1, 2]]


def get_list_sum(digits_list, sum_of_numbers=0):
    """Get the sum of all elements from digits_list using recursion."""
    for i in digits_list:
        # recursion call if type(i) == list:
        if type(i) == list:
            sum_of_numbers += get_list_sum(i)
        else:
            # Addition a number to a sum
            sum_of_numbers += i
    return sum_of_numbers


# Get result from get_obj_sum function in "result_sum"
result_sum = get_list_sum(target_list)
# Print result with sum of numbers
print(f'Target sum = {result_sum}')
