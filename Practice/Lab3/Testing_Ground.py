import Functions1

print(Functions1.grams_to_ounces(300))
print(Functions1.F_to_C(180))

chickens_rabbits = Functions1.solve(12, 30)
if chickens_rabbits == (0, 0):
    print("It is impossible to solve")
else:
    answer = "There are {} chickens and {} rabbits"
    print(answer.format(chickens_rabbits[0], chickens_rabbits[1]))

numstr = "2 12 3 13 5 15 23"
new_numstr = Functions1.filter_prime(numstr)
print(new_numstr)

print(Functions1.all_permutations("hare"))
print(Functions1.reverse("This is the correct order"))

print(Functions1.has_33([5, 3, 3]),
Functions1.has_33([1, 3, 10, 3]),
Functions1.has_33([3, 31, 1]))

print(Functions1.spy_game([1,2,4,0,0,7,5]),
Functions1.spy_game([1,0,2,4,0,5,7]),
Functions1.spy_game([1,7,2,0,4,5,0]))

print(Functions1.volume(3))

nul = ["abacaba", 156, "abacaba", 12.3, "abacaba", 1, 1]
print(Functions1.unique_list(nul))

maybe_pal = "mister"
if Functions1.is_palindrome(maybe_pal):
    print("It's a palindrome!")
else:
    print("It isn't a palindrome...")

Functions1.histogram([7, 12, 18])

print('Do you want to play "Guess the Number"? Please reply y/n')
consent = input()
if consent == 'y':
    Functions1.guess_the_number()