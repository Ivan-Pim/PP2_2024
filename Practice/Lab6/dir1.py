import os

def dirs(path):
    lst = os.listdir(path)
    result = [x for x in lst if os.path.isdir(path + '/' + x)]
    print(result)

def files(path):
    lst = os.listdir(path)
    result = [x for x in lst if os.path.isfile(path + '/' + x
    )]
    print(result)

def dirs_files(path):
    print(os.listdir(path))

mode = input()


if mode == 'back':
    steps = int(input())
    path = os.getcwd() + "/.." * steps
    dirs(path)
    files(path)
    dirs_files(path)




elif mode == 'full':
    path = input()
    dirs(path)
    files(path)
    dirs_files(path)