# 1.create a custom math module and import it in another file.
import mymath

print(mymath.add(6, 3))
print(mymath.sub(6, 3))

# 2.create a modeul to perform string operation.
import string_ops

print(string_ops.upper_case("python"))
print(string_ops.lower_case("PYTHON"))
print(string_ops.length("python"))

# 3.use random module to generate 5 random integers.
import random

for i in range(5):
    print(random.randint(1, 100))

# 4.use datetime module to display current date and time.
import datetime

now =  datetime.datetime.now()
print("Current date and time:", now)

# 5.use math module to find factorial of a number.
import math

num = 5
print("Factorial:", math.factorial(num)) 

# 6.create a package shapes with modules for circle and rectangle.
from shapes.circle import area as circle_area
from shapes.rectangle import area as rect_area

print(circle_area(5))
print(rect_area(4, 6))

# 7. import multiple functions from one module and use them.
from calc import add, mul

print(add(2, 3))
print(mul(2, 3))

# 8. write a program to suffle a list using random module.
import random

lst = [1,2,3,4,5]
random.shuffle(lst)

print("Shuffled List:", lst)

# 9. write a program to calculate the difference between two dates.
from datetime import date

d1 = date(2024, 1, 1)
d2 = date(2024, 1, 10)

diff = d2 - d1
print("Difference in days:", diff.days)

# 10. use os module to list files in a dictionary.
import os

files = os.listdir(".")
print("Files in directory:")
for f in files:
    print(f)
