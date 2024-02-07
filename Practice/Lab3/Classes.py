# 1
class StringCheese:
    def getString(self, string):
        self.string = string

    def printString(self):
        print(self.string)

test = StringCheese()

test.getString(input())
test.printString()

# 2
class Shape:
    def area(self):
        own_area = 0
        print(own_area)

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        own_area = self.length ** 2
        print(own_area)

crown = Shape()
crown.area()

watermelon = Square(int(input()))
watermelon.area()

# 3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        own_area = self.width * self.length
        print(own_area)

bus = Rectangle(10, 2)
bus.area()

# 4
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"The point's coordinates are ({self.x}; {self.y})")
    
    def move(self, newx, newy):
        self.x = newx
        self.y = newy

    def dist(self, point2):
        sqx = (self.x - point2.x) ** 2
        sqy = (self.y - point2.y) ** 2
        print((sqx + sqy) ** 0.5) 

start = Point(2, 5)
start.show()
start.move(0, 0)

end = Point(4, 3)
start.dist(end)

# 5
class Account():
    def __init__(self, owner = "Default", balance = 0.0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, sum):
        self.balance += sum
    
    def withdraw(self, sum):
        if self.balance >= sum:
            self.balance -= sum
            print(f"{self.owner} withdrew {sum} tenge.")
        else:
            print("Insufficient funds!")

acc1 = Account("Ivan", 1000)

acc1.withdraw(100000)

acc1.deposit(9000)
acc1.withdraw(5000)

acc2 = Account("Nurdaulet", 100000)

acc2.withdraw(30000)
acc2.withdraw(40000)
acc2.withdraw(50000)