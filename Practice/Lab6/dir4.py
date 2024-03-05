import os

filename = input()

with open(filename, 'r') as file:
    num_lines = len(file.readlines())

print(num_lines)