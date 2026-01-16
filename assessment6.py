# 1
n=int(input("Enter a number:"))

if n>=18:
    print("The person is eligible to vote.")
else:
    print("The person is not eligible to vote.") 

# 2
n=int(input("Enter a number:"))

if n>=90:
    print("Grade:A")
elif n>=80:
    print("Grade:B")
else:
    print("Grade:C")

# 3
n=input("Enter the traffic light color (red/yellow/green):")

if n=="red":
    print("Stop")
elif n=="yellow":
    print("Wait")
elif n=="green":
    print("Go")
else:
    print("the traffic light color is invalid")

# 4
balance=int(input("Enter Amount:"))
withdraw=int(input("Enter Withdrawal Amount:"))

if withdraw <= balance:
    print("Withdrawal Successful")
    print("Remaining Balance=", balance-withdraw)
else:
    print("Insufficient Balance")

# 5
n=int(input("Enter the number:"))

if n>=1:
    print("it is a positive number")
elif n<0:
    print("it is a negative number")
else:
    print("it is a zero")

# 6
num=int(input("Enter a number"))
low=int(input("Enter a number"))
high=int(input("Enter a number"))

if low <= num <= high:
    print("number lies within the range")
else:
    print("number is outside the range")

# 7
username="cheritipatel"
password="cheriti123"

u=input("Enter Username:")
p=input("Enter Password:")

if u==username and p==password:
    print("Login Successful")
else:
    print("Invalid Username and Password.")

# 8
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + (units - 100) * 3
else:
    bill = (100 * 2) + (100 * 3) + (units - 200) * 5

print("Electricity Bill =", bill)

# 9
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("choose operation:")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

n=int(input("Enter a number (1-4) :"))

if n==1:
    print("result =", num1 + num2)
elif n==2:
    print("result = ", num1 - num2)
elif n==3:
    print("result =", num1 * num2)
elif n==4:
    if num2 != 0:
        print("result=" , num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid choice")

# 10
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")