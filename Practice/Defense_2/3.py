import re

pattern = r'ab*'

while True:
    x = input()
    if x == "stop":
        break
    if re.search(pattern, x):
        print("found a match")
        print(re.search(pattern, x))
    else:
        print("no match :<")