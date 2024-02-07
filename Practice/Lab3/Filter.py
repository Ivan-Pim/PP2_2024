def is_prime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def filter(nums):
    result = [el for el in nums if is_prime(el)]
    return result

inp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
x = lambda a : filter(a)
res = x(inp)

print(inp)
print(res)