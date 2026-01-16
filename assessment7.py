# 1
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result =", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

# 2
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Error: Invalid integer input")

# 3
try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found")

# 4
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")

# 5
try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")

# 6
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    print("Valid age")
except InvalidAgeError as e:
    print(e)

# 7
try:
    nums = [1, 2, 3]
    print(nums[5])
except IndexError:
    print("Error: Index out of range")

# 8
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result =", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
except Exception:
    print("Some other error occurred")

# 9
import logging

logging.basicConfig(filename="error.log", level=logging.ERROR)

try:
    a = int(input("Enter number: "))
    b = int(input("Enter another number: "))
    print(a / b)
except Exception as e:
    logging.error(e)

# 10
class InvalidEmailError(Exception):
    pass

try:
    email = input("Enter email: ")
    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email format")
    print("Valid email")
except InvalidEmailError as e:
    print(e)
