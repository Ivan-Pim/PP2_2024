import math

def to_radians(degrees):
    #original function, do not steal!!!
    return math.radians(degrees)

def trapezoid(height, base1, base2):
    return height * (base1 + base2) / 2

def regular(sides, length):
    perimetr = sides * length
    apothem = length / (2 * math.tan(to_radians(180 / sides)))
    print(perimetr, 180 / sides)
    return perimetr / 2 * apothem

def parallelogram(base, height):
    return base * height

print(to_radians(15))

print(trapezoid(5, 5, 6))

print(regular(4, 25))

print(parallelogram(5, 6))
