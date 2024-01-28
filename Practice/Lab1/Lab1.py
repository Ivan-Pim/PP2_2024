print("Hello, World!")

# indentation example
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
# variables example
x = 5
y = "Hello, World!"
print(x)
print(y)
# no need for a comment example
"""
this is an example of a multiline comment,
as python ignores unassigned strings
"""
# reassigning a variable
x = "Sally"
print(x)
# casting
x = str(3)
y = int(3)
z = float(3)
# you can ask for a type
print(type(x))
# single and double quotes are the same
# variables are case senstive
X = 5
print(x, X)
# you can assign multiple values at once
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)
# or assign one value to multiple variables
x = y = z = "Apple"
print(x, y, z)
# or unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)
# you can concatenate strings in print
print(x + y + z)
# or add numbers
print(5 + 8)
# but not when they're different types

#variables can be local and global
x = "cool, i guess"

def myfunc():
        x = "not horrible"
        print("Python is " + x)

myfunc()
print("Python is " + x)

# here i declare a global variable in a function
def myfunc2():
        global x
        x = "one of the programming languages"

myfunc2()

print("Python is " + x)

# here are all the existing data types
"""
Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: list, tuple, range
Mapping Type: 	dict
Set Types: 	set, frozenset
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview
None Type: 	NoneType
"""

# integer and float numbers are self-explanatory
# complex is written with j
c = 3 + 5j

#typecasting has been explained before

### strings ###
a = "Hello, World!"

# you can take a single character(starts at 0)
print(a[1])

# you can loop through chars in a string
for x in 'banana':
    print(x)

# you can get the legth of a string
print(len(a))

# you can check if a string contains a substring
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# you can "slice" and get from x to y - 1 with a step of y, default is from beggining to end with step 1
## negative indexes are counted from the end
print(a[2:11:2])
print(a[-6:-1])

## upper puts the string in uppercase
## lower puts the string in lowercase

print(a.lower())
print(a.upper())

## strip removes whitespace before and after the string
txt = "  The best things in life are free!      "
print(txt.strip())

# you can replace any substrings with different ones
print(a.replace("l", "w"))

# you can split a string into a list with an arbitrary separator
print(txt.split('e'))

# adding string up is called concatenation and writes one after another
print("This" + "isonelongword")

# format string allows you to insert a non string instead of {n}
myorder = "I want to pay {2} dollars for {0} pieces of {1}"
print(myorder.format(3, "cheese", 49.95))

# use an escape character to insert an illegal character into a string

example = "We are the so called \"Bikings\" from the north"
print(example)

# there are many string methods to find