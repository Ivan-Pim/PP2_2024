import math
import time

#1

if input() == 'Y':
    nums = list(map(int, input().split()))
    prod = math.prod(nums)
    print(prod)

#2
if input() == 'Y':
    ans2 = {'up' : 0, 'low' : 0}
    wtr = input()
    for i in wtr:
        if i.isalpha():
            if i.isupper():
                ans2['up'] += 1
            else:
                ans2['low'] += 1

    print(ans2['up'], ans2['low'])

#3
def ispalindrome(string):
    string = string.lower()
    return string == ''.join(reversed(string))

if input() == 'Y':
    given = input()
    if ispalindrome(given):
        print("This is a palindrome")
    else:
        print("Ohh, it's not a palindrome :<")

#4
if input() == 'Y':
    square = int(input())
    wait = int(input())

    root = math.sqrt(square)

    time.sleep(wait * 0.001)
    print(f"Square root of {square} after {wait} miliseconds is {root}")

#5

if input() == "Y":
    tup = tuple(map(int, input().split()))
    val = all(tup)
    print(val)