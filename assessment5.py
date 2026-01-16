# 1
for i in range(1,11):
    print(i)

# 2
n=int(input("Enter the number:"))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

# 3
n=int(input("Enter the number:"))
fact = 1

for i in range(1,n+1):
    fact *= i

print(f"factorial of {n} = {fact}")

# 4
n=int(input("Enter the number of N:"))

a, b = 0,1
print("fibonacci series:")

for i in range(n):
    print(a, end=" ")
    a , b = b , a + b

# 5
n=int(input("Enter a number:"))

if n <= 1:
    print("not a prime number")
else:
    for i in range(2, n):
        if n%i==0:
            print("not a prime number")
            break
    else:
        print("prime number")

# 6
n=int(input("Enter a number:"))
rev = 0

while n != 0:
    rev = rev * 10 + (n % 10)
    n = n // 10
print("reversed number = ", rev)

# 7
n=int(input("Enter a number: "))
count = 0
num = n

if n == 0:
    count = 1
else:
    while n != 0:
        n = n // 10
        count += 1

print(f"Number of digits in {num} = {count}")

# 8
sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum += i

print("Sum of even numbers between 1 and 100 =", sum)

# 9
row = int(input("Enter number of rows: "))

for i in range (1, row+1):
    print(" " * (row - i) , end ="")
    print(" *" * i)

# 10
n=int(input("Enter a number:"))

for i in range(1, n+1):
    if n%i==0:
        print(i) 