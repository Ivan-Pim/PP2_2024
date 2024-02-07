from itertools import permutations
import math
from random import randrange

#1
def grams_to_ounces(grams):
    ounces = grams / 28.3495231
    return ounces

#2
def F_to_C(F):
    C = (5 / 9) * (F - 32)
    return C

#3
def solve(numheads, numlegs):
    chickens = 0
    assumed_legs = 2 * chickens + 4 * (numheads - chickens)
    while (assumed_legs > numlegs):
        chickens += 1
        assumed_legs -= 2
    if (assumed_legs == numlegs):
        return chickens, (numheads - chickens)
    else:
        return 0, 0

#4
def is_prime(number):
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

def filter_prime(nums):
    if isinstance(nums, str):
        nums = list(map(int, nums.split()))
        result = []
    for i in nums:
        if is_prime(i):
            result.append(i)
    return result

#5
def all_permutations(user_input):
    result = [''.join(p) for p in permutations(user_input)]
    return result

#6
def reverse(user_input):
    broken = user_input.split()
    broken = broken[::-1]
    result = ' '.join(broken)
    return result

#7
def has_33(nums):
    result = '33' in ''.join(list(map(str, nums)))
    return result

#8
def spy_game(nums):
    result = '007' in ''.join(list(map(str, nums)))
    return result    

#9
def volume(radius):
    result = (4 / 3) * math.pi * radius**3
    return result

#10
def unique_list(user_input):
    result = []
    for i in user_input:
        unique = True
        for el in result:
            if el == i:
                unique = False
                break
        if unique:
            result.append(i)
    return result

#11
def is_palindrome(user_input):
    check = user_input[::-1]
    result = (user_input == check)
    return result

#12
def histogram(rows):
    for i in rows:
        print('*' * i)

#13
def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    num = randrange(1, 21)
    print("Well, KBTU, I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    guess = int(input())
    guess_count = 1

    while guess != num:
        msg = "Your guess is too {}"
        if guess < num:
            print(msg.format("low"))
        else:
            print(msg.format("high"))
        print("Take a guess.")
        guess = int(input())
        guess_count += 1
    
    congrats = "Good job, {}! You guessed my number in {} guesses!"
    print(congrats.format(name, guess_count))