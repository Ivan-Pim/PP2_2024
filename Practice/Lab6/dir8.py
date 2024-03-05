import os

path = input()

exists = os.path.exists(path)
read = os.access(path, os.R_OK)
write = os.access(path, os.W_OK)
execute = os.access(path, os.X_OK)

if exists and write:
    os.remove(path)