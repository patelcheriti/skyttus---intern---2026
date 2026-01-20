# 1
class Animal:
    def speak(self):
        print("Animal makes a sound")
    
class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.speak()
d.speak()
c.speak()

# 2
class Vehicles:
    def start(self):
        print("Vehicle Started")

class Car(Vehicles):
    def drive(self):
        print("Car is Driving")

class Electriccar(Car):
    def charge(self):
        print("Electric Car is Charging")

e =  Electriccar()   
e.start()
e.drive()
e.charge()

# 3
class Shape:
    def area(self):
        print("Area not defined")

class Rectangle(Shape):
    def area(self):
        print("Area = length * width")

r = Rectangle()
r.area()

# 4
class Father:
    def skill1(self):
        print("Farmer")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    def skill3(self):
        print("Programming")

c = Child()
c.skill1()
c.skill2()
c.skill3()

# 5
class Circle:
    def draw(self):
        print("Drawing Circle")

class Square:
    def draw(self):
        print("Drawing Square")

def draw_shape(shape):
    shape.draw()

draw_shape(Circle())
draw_shape(Square())

# 6
class BankAccount:
    def account_type(self):
        print("Bank Account")

class SavingsAccount(BankAccount):
    def account_type(self):
        print("Savings Account")

class CurrentAccount(BankAccount):
    def account_type(self):
        print("Current Account")

s = SavingsAccount()
c = CurrentAccount()

s.account_type()
s.account_type()

# 7
class Person:
    def __init__(self):
        self.__age = 0
    
    def set_age(self, age):
        self.__age = age
    
    def get_age(self):
        return self.__age
    
p = Person()
p.set_age(21)
print("Age:", p.get_age())

# 8
class Person:
    def role(self):
        print("Person")

class Teacher(Person):
    def role(self):
        print("Teacher")

class Student(Person):
    def role(self):
        print("Student")

t = Teacher()
s = Student()

t.role()
s.role()

# 9
class MusicPlayer:
    def play(self):
        print("Playing Music")

class Spotify(MusicPlayer):
    def play(self):
        print("Playing Music on Spotify")

m = MusicPlayer()
s = Spotify()

m.play()
s.play()

# 10
class Animal:
    def __init__(self):
        print("Animal created")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog Created")

d = Dog()