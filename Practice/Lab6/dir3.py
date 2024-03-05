import os

path = input()

exists = os.path.exists(path)

if exists:
    directory, filename = os.path.split(path)
    print(directory)
    print(filename)