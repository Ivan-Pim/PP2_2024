#7.1
print(10 > 9)
## answer: True

#7.2
print(10 == 9)
## answer: False

#7.3
print(10 < 9)
## answer: False

#7.4
print(bool("abc"))
## answer: True

#7.5
print(bool(0))
## answer: False


#8.1
print(10 * 5)

#8.2
print(10 / 2)

#8.3
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#8.4
if 5 != 10:
  print("5 and 10 is not equal")

#8.5
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")


#9.1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#9.2
fruits = ["apple", "banana", "cherry"]
fruits[0] =  "kiwi"

#9.3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#9.4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#9.5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#9.6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#9.7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#9.8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))


#10.1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#10.2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#10.3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#10.4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#11.1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#11.2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#11.3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#11.4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#11.5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")


#12.1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#12.2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#12.3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#12.4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#12.5

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#13.1
a = 50
b = 10
if a > b:
  print("Hello World")

#13.2
a = 50
b = 10
if a != b:
  print("Hello World")

#13.3
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")

#13.4
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")

#13.5
if a == b and c == d:
  print("Hello")

#13.6
if a == b or c == d:
  print("Hello")

#13.7
if 5 > 2:
  print("YES")

#13.8

a = 2
b = 5
print("YES")if a == b else print("NO")

#13.9
a = 2
b = 50
c = 2
if a == c or b == c:
  print("YES")


#14.1
i = 1
while i < 6:
  print(i)
  i += 1

#14.2

i = 1
while i < 6:
  if i == 3:
    break
  i += 1

#14.3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#14.4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#15.1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#15.2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#15.3
for x in range(6):
  print(x)

#15.4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)