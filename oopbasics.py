# 1
class Car:
    def __init__(self,brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed
    def accelerate(self):
        self.speed += 10
        print("speed after accelerating:", self.speed)
    def brake(self):
        self.speed -= 10
        print("speed after braking:", self.speed)
car = Car("Honda", "City", 50)
car.accelerate()
car.brake()

# 2
class Bankaccount:
    def __init__(self, balance):
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount
        print("balance after deposit:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("balance after withdrawal:", self.balance)
        else:
            print("Insufficient Balance")

account = Bankaccount(1000)
account.deposit(500)
account.withdraw(300)

# 3
class Students:
    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    
    def average(self):
        avg = (self.marks1 + self.marks2 + self.marks3) / 3
        print("Average Marks:", avg)

s = Students(70, 80, 60)
s.average()

# 4
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)
    
    def perimeter(self):
        print("Perimeter", 2 * (self.length + self.width))

r = Rectangle(5,4)
r.area()
r.perimeter()

# 5
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print('Name:', self.name)
        print("Salary:", self.salary)

e = Employee("Cheriti", 20000)
e.display()

# 6
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

b = Book("Python Basics", "John", 299)
b.display()

# 7
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area:", 3.14 * self.radius * self.radius)

    def circumference(self):
        print("Circumference:", 2 * 3.14 * self.radius)

c = Circle(7)
c.area()
c.circumference()

# 8
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def discount(self, percent):
        self.price -= self.price * percent / 100
        print("Price after discount:", self.price)

l = Laptop("Dell", 50000)
l.discount(10)

# 9
class Flight:
    def __init__(self, seats):
        self.seats = seats

    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            print("Seat booked. Remaining seats:", self.seats)
        else:
            print("No seats available")

f = Flight(2)
f.book_seat()
f.book_seat()
f.book_seat()

# 10
class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        print("Products in shop:")
        for p in self.products:
            print(p)

s = Shop()
s.add_product("Pen")
s.add_product("Book")
s.show_products()
