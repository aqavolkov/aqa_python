"""
HW:3[Volkov Anton].

we have four values w,x,y,z
write if-elif-else statement that will search minimum value
and print smth aka "'y' is minimum value'
advice use python debugger and different values to check your algorithm
w, x, y, z = 100, 200, 40, 300
"""
w, x, y, z = 100, 200, 40, 300
# 1. I've written my solution use python debugger to check my algorithm
if w <= x:
    if w <= y:
        if w <= z:
            print("'w' is minimum value")
        else:
            print("'z' is minimum value")
    elif y <= z:
        print("'y' is minimum value")
    else:
        print("'z' is minimum value")
elif x <= y:
    if x <= z:
        print("'x' is minimum value")
    else:
        print("'z' is minimum value")
elif y <= z:
    print("'y' is minimum value")
else:
    print("'z' is minimum value")
# 2. I've optimized my code by making it shorter
if w <= x and w <= y and w <= z:
    print("'w' is minimum value")
elif x <= w and x <= y and x <= z:
    print("'x' is minimum value")
elif y <= w and y <= x and y <= z:
    print("'y' is minimum value")
else:
    print("'z' is minimum value")
