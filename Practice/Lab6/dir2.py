import os

path = input()

exists = os.path.exists(path)
read = os.access(path, os.R_OK)
write = os.access(path, os.W_OK)
execute = os.access(path, os.X_OK)

if exists:
    print("This is an existing file")
    if read:
        print("This is a readable file!")
    else:
        print("This is not a readable file")
    
    if write:
        print("This is a file you can write in!")
    else:
        print("This is not a file you can write in")
    
    if execute:
        print("You can execute this file!")
    else:
        print("You cannot execute this file")
else:
    print("Sorry, no such file found")