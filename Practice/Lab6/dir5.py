import os

filename = input()
innput = list(input().split())

with open(filename, 'w') as file:
    for el in innput:
        file.write(el + '\n')

