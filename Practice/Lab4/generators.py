#1a
print('1a')

N = int(input())

x = (i ** 2 for i in range(N))

for i in x:
    print(i,end = " ")

#1b
print('\n1b')
N = int(input())

def squares(a, b):
    for i in range(a, b):
        yield i ** 2

for i in squares(0, N):
    print(i, end=" ")

#2
print('\n2')
def evens(n):
    for i in range(0, n, 2):
        yield i

n = int(input())
for i in evens(n):
    print(i, end = ", ")

#3a
print('\n3a')
n = int(input())

x = (i for i in range(0, n, 12))

for i in x:
    print(i, end = " ")

#3b
print('\n3b')
n = int(input())

def tri_or_4(n):
    for i in range(n):
        if i % 3 == 0 or i % 4 == 0:
            yield i

for i in tri_or_4(n):
    print(i, end = " ")

#4
print('\n4')
### accidentally already made squares in 1
a = int(input())
b = int(input())

for i in squares(a, b):
    print(i)

#5
print(5)
n = int(input())
down = (x for x in range(n, -1, -1))
for i in down:
    print(i, end = " ")