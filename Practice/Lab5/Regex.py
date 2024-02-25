import re

#1
def a_then_bs(string):
    x = re.search("ab*", string)
    return x

#2
def two_to_3(string):
    s = "ab{2,3}"
    x = re.search(s, string)
    return x

#3
def con_under(string):
    s = "([a-z]*_?)*"
    p = re.compile(s)
    x = re.search(p, string)
    return x

#4
def one_then_lower(string):
    s = "[A-Z][a-z]+"
    p = re.compile(s)
    x = re.search(p, string)
    return x

#5
def a_to_b(string):
    s = "a.*b"
    p = re.compile(s)
    x = re.search(p, string)
    return x

print(a_then_bs(input("A then any amount of b's\n"))) 

print(two_to_3(input("A then 2 to 3 b's\n")))

print(con_under(input("Lowercase letters connected by underscores\n")))

print(one_then_lower(input("An uppercase letter followed by lowercase ones\n")))

print(a_to_b(input("anything betweena an a and b\n")))