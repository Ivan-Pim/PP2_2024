import math
def pythagoreas(a, b):
    c2 = a ** 2 + b ** 2
    c = math.sqrt(c2)
    return c

def square(a):
    return a ** 2

a = int(input())
b = int(input())

print(pythagoreas(a, b))
print(square(a))