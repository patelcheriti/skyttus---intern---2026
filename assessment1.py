# 1
name="Cheriti"
age="21"
city="Chikhli"

print(name, age, city)

# 2
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

sum = num1 + num2
print(sum)

# 3
celsius= float(input("Enter the temperature in celsius:"))

fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit =", fahrenheit) 

# 4
name = "cheriti"
print(name.upper())

# 5
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print("Your age is:", age)

# 6
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

# 7
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of rectangle =", area)

# 8
n=int(input("enter a number:"))

if n > 0:
    print("positive number")
elif n < 0:
    print("negative number")
else:
    print("zero")

# 9
a=float(input("enetr first number:"))
b=float(input("enetr second number:"))

average= (a + b) / 2
print(average)