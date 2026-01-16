# 1
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

remainder =( a % b)
print(remainder)

# 2
n=int(input("Enter a number:"))

if n % 2 == 0:
    print("even number")
else:
    print("odd number")

# 3
a = int(input("enter a number:"))
b = int(input("enter a number:"))

if a > b:
    print("large number is :" , a)
else:
    print("large number is :" , b)

# 4
num=int(input("enter a number:"))

square= (num * num)
cube= ( num * num * num)

print(" square = ", square)
print(" cube = " , cube)

# 5
a = int(input("enter a number:"))
b = int(input("enter a number:"))

if a == b:
    print("both numbers are equal")
else:
    print("both numbers are not equal")

# 6
a = int(input("enter a number:"))
b = int(input("enter a number:"))

if a > 0 and b > 0:
    print("True")
else:
    print("False")

# 7
num = float(input("enetr a value:"))
print(int(num)) 

# 8
num = input("Enter a number: ")
num = int(num)
print(num * 10)

# 9
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

if age >= 18 and marks >= 50:
    print("Eligible")
else:
    print("Not eligible")

# 10
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

quotient = a // b
remainder = a % b

print("Quotient =", quotient)
print("Remainder =", remainder)