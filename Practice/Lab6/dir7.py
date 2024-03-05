import os

filename_from = input()
filename_to = input()

with open(filename_from, 'r') as file:
    content = file.readlines()

with open(filename_to, 'w') as file:
    for el in content:
        file.write(el)