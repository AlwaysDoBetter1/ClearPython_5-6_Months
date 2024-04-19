"""
While and recursion
"""

z = 1

# while
while z <=5:
    if z == 5:
        print('base case')
    else:
        print('repeated text')
    z += 1

# rewrite while to recursion
def func(z):
    if z == 5:
        print('base case')
    else:
        print('repeated text')
        return func(z+1)

func(1)

