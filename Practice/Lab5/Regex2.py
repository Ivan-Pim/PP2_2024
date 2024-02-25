## didnt want to create a really big file like always
import re

#6
def just_colon(string):
    string = re.sub('[ ,.]', ';', string)
    return string

#7 not solved
def toUpper(match):
    return match.group(1).upper()

def snake_to_camel(string):
    p = re.compile(r"_([a-z])")
    
    string = p.sub(toUpper, string)
    return string

#8
def at_upper(string):
    p = re.compile(r"[A-Z]")
    string = p.split(string)
    return string

#9

def add_spaces(string):
    p = re.compile(r"([A-Z])")
    string = p.sub(r' \1', string)
    return string

#10

def toLower(match):
    return '_' + match.group(1).lower()

def CamelToSnake(string):
    p = re.compile(r'([A-Z])')
    string = p.sub(toLower, string)
    return string

print(just_colon(input("Turn everything into colons!\n")))

print(snake_to_camel(input("Convert snake_case to camelCase\n")))

print(at_upper(input("Split strings at uppercase letters\n")))

print(add_spaces(input("Add spaces in CamelCase\n")))

print(CamelToSnake(input("Convert CamelCase to snake_case\n")))