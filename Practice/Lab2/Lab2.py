## boleans
# these are values that can be True or False
# for example, the results of comparisons are bools
print(10 > 9)
print(10 == 9)
print(10 < 9) 

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 

# you can use the bool() function to evaluate any variable as a boolean
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# everything is True, except for 0 and empty strings, lists, tuples, sets and dictionaries
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# here are all False values
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 

# also any object with _len_() = 0 is False
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) 

# functions can return booleans
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") 

# there are built-in functions, that return booleans, for example isinstance
x = 200
print(isinstance(x, int)) 


## operators
# there are too many operartors in python to list them all here
# this is a list of operator types
"""
    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators
"""
# operators have a precedence order, otherwise they are read from left to right


## lists
# lists are used to store multiple items in a single variable
# lists are ordered, changeable and allow duplicate values
# list items are indexed, starting from 0
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
print(thislist[1])

# lists can be any type and can include multiple types
list1 = ["abc", 34, True, 40, "male"] 

### types of arrays
"""
 There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

# refer to an index to change a value
# it is possible to replace any numbers of values with any number of values, e.g replace 3 values with one or inversely
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]

# use the insert() method to insert a value into a desired position
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") 

# use append() to add an item to the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")

# use extend() to add items from another list or any iterable object(tuple, set, etc.)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)


# use remove() to delete the first occurence of the specified item
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")

# use pop to remove an item at a specified index, or the last item if unspecified
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)

thislist = ["apple", "banana", "cherry"]
thislist.pop()

# use the keyword del to delete items at an index, range or the whole list
thislist = ["apple", "banana", "cherry"]
del thislist[0]
del thislist

#use clear() to remove all items but keep the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()

### Ways to loop through a list
# by element
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 

# by index
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) 

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# using list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 

### list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# this allows you to create a list using a shorthand

# newlist = [expression for item in iterable if condition == True]
# some examples
newlist = [x for x in fruits if x != "apple"] 
newlist = [x for x in fruits] 
newlist = [x for x in range(10)] 
newlist = ['hello' for x in fruits] 
newlist = [x if x != "banana" else "orange" for x in fruits] 

# use sort to sort a list in ascending order
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()

# use the keyword reverse = True for descending order
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)

# use key = function to sort a list with your own function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)

#use reverse to reverse a list without sorting it
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()

## copying a list
# if you write list1 = list2, list1 will be a reference to list2, and any changes will aplly to both lists
# to create a copy that is a different item use copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
# or list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)

# join lists with +, append() or extend()

## tuples
# A tuple is a collection which is ordered and unchangeable. Allows duplicates
# use round brackets to create a tuple
# use len() to find out the tuple's length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# to create a tuple with one item you HAVE TO INCLUDE A COMMA, otherwise it will not be recognised as a tuple
thistuple = ("apple",)
print(type(thistuple))

# tuples can contain any data type and multiple at once
tuple1 = ("abc", 34, True, 40, "male")

# tuples are unchangeable, so you cannot change, remove or add items
# you can unpack values from a tuple, and even make one a list with *, if there are more values than variables
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

# you can join tuples and multiply them by natural numbers

## sets
# sets are unordered, unchangeable*, unindexed arrays
# they are written with curly brackets
thisset = {"apple", "banana", "cherry"}

# you cannot access values in a set without a for or in keyword
# add items to set with add() or update()

# use remove() discard() or pop() to remove items
# use clear to remove all items

# union combines two sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)

# intersection update intersects two sets within the first one
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

# intersection creates a new set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

# symmetric difference keeps all except duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

## dictionaries
## dictionaries are list of pairs key, value
# instead of indexes, use keys
# you can use keys() to get a list of keys and values() to get values or item to get a list of tuples
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
x = thisdict.keys() 
x = thisdict.values() 

## if else elif
# self explanatory

## for, while loops
# use break, continue, pass, otherwise selfexplanatory