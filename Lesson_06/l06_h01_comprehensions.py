"""
HW:6[Volkov Anton].

we have two lists with equal or different size
ex. l1=[1,3,5,7]  l2=[1,4,5]
task:
create list that will store such values list_target
= [(1,1), (3,4), (5,5), (7,0)]
zero (0) is our default value that we set
if no such element by index was found in certain list.
code should work and vise versa
ex. l1=[1,4,5] l2=[1,3,5,7] input data should produce
list_target = [(1,1), (4,3), (5,5), (0,7)]
your solution should include comprehension constructions

Advices:
set of (list1 indexes union list2 indexes)
could be helpful to get larger indexes scope ( or use if-else)
dict as you remember has default value
if key was not found d1.get(key, 0)
"""
l1 = [2, 4, 6, 8, 10]
l2 = [1, 2, 3]
l1_copy = l1[:]
l2_copy = l2[:]
if len(l1_copy) > len(l2_copy):
    while len(l1_copy) > len(l2_copy):
        l2_copy.append(0)
else:
    while len(l1_copy) < len(l2_copy):
        l1_copy.append(0)

result = [(l1_copy[i], l2_copy[i]) for i in range(len(l1_copy))]
print(result)
