# 1
def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(prime(7))

# 2
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))

# 3
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))

# 4
def simple_interest(p, r, t):
    return (p * r * t) / 100

print(simple_interest(1000, 5, 2))

# 5
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("madam"))

# 6
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

print(count_vowels("education"))

# 7
def merge_lists(list1, list2):
    return list1 + list2

print(merge_lists([1, 2], [3, 4]))

# 8
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(12, 18))

# 9
def area_rectangle(length, width):
    return length * width

print(area_rectangle(5, 4))

# 10
def is_armstrong(num):
    temp = num
    sum = 0
    digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    return sum == num

print(is_armstrong(153))
