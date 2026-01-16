# 1
text = input("Enter a string: ")
print("Length =", len(text))

# 2
sentence = input("Enter a sentence: ")
print(sentence.lower())

# 3
text = input("Enter a string: ")
print(text.replace(" ", "_"))

# 4
text = input("Enter a string: ")
print("First character:", text[0])
print("Last character:", text[-1])

# 5
text = input("Enter a string: ")
print("Reversed string:", text[-1:-8:-1])
                        #   ( text [::-1] )

# 6
text = input("Enter a string: ")
letter = input("Enter a letter: ")
print("Count =", text.count(letter))

# 7
sentence = input("Enter a sentence: ")
word = input("Enter a word: ")

if word in sentence:
    print("Word found")
else:
    print("Word not found")

# 8
name = input("Enter name: ")
age = int(input("Enter age: "))
print(f"My name is {name} and I am {age} years old.")

# 9
text = input("Enter a string: ")
print(text.strip())

10
words = ["Python", "is", "easy"]
result = "-".join(words)
print(result)

# 11
movies = ["3 idiots", "chhichhore", "MS Dhoni", "Dhamaal" ]
print(movies)

# 12
movies.append("Lagaan")
print(movies)

# 13
movies.pop(0)
print(movies)

# 14
numbers = [15, 12, 19, 11, 17]
numbers.sort()
print(numbers)

# 15
numbers.reverse()
print(numbers)

# 16
numbers = [20, 51, 12, 97, 24]
print("Largest number =", max(numbers))

# 17
list1 = [31, 22, 13]
list2 = [24, 15, 36]
merged = list1 + list2
print(merged)

# 18
numbers = [12, 25, 37, 43]
print(numbers[-1])

# 19
nested_list = [[1, 2, 3], [4, 5, 6]]
print(nested_list[1][2])

# 20
numbers = [1, 3, 2, 3, 4, 2]
print(numbers.count(3))