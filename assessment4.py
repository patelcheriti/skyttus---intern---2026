# 1
t = (10, 20, 30, 40, 50)
print(t)

# 2
print(t[2])

# 3
a, b, c, d, e = t
print(a, b, c, d, e)

# 4
fruits = {"apple", "banana", "mango", "orange", "grapes"}
print(fruits) 

# 5
fruits.add("papaya")
print(fruits)

# 6
fruits.remove("banana")
print(fruits)

# 7
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)

# 8
print(set1 & set2)

# 9
print({1, 2}.issubset(set1))

# 10
numbers = [1, 2, 2, 3, 4, 4]
unique = set(numbers)
print(unique)

# 11
students = {"cheriti": 85, "rutu": 90, "vrutti": 78}
print(students)

# 12
students["diya"] = 88
print(students)

# 13
del students["vrutti"] 
print(students)

# 14
d1 = {"a": 11, "b": 22}
d2 = {"c": 33}
merged = {**d1, **d2}
print(merged)

# 15
print("cheriti" in students)

# 16
text = "python is easy and python is powerful"
words = text.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)

# 17
print(max(students, key=students.get))

# 18
reversed_dict = {v: k for k, v in students.items()}
print(reversed_dict)

# 19
students["cheriti"] = 95
print(students)

# 20
data = [("a", 1), ("b", 2), ("c", 3)]
dict_data = dict(data)
print(dict_data)