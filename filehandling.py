# 1
file = open("Assessments/file.txt", "r")
content = file.read()
print(content)
file.close() 

# 2
file = open("Assessments/file.txt", "r")
lines = file.readlines()
print("Number of lines:", len(lines))
file.close()

# 3
file = open("Assessments/file.txt", "r")
text = file.read()
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
file.close()

# 4
file = open("sentences.txt", "w")

for i in range(5):
    sentence = input("Enter sentence: ")
    file.write(sentence + "\n")

file.close()
print("Sentences saved successfully.")

# 5
strings = ["Apple", "Banana", "Mango"]

file = open("Assessments/file.txt", "a")
for item in strings:
    file.write(item + "\n")

file.close()
print("Data appended.")

# 6
word = input("Enter word to search: ")

file = open("Assessments/file.txt", "r")
for line in file:
    if word in line:
        print(line.strip())
file.close()

# 7
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

file = open("Assessments/file.txt", "r")
text = file.read()
file.close()

text = text.replace(old_word, new_word)

file = open("Assessments/file.txt", "w")
file.write(text)
file.close()

print("Word replaced successfully.")

# 8
file1 = open("Assessments/file1.txt", "r")
file2 = open("Assessments/file2.txt", "r")
file3 = open("Assessments/merged.txt", "w")

file3.write(file1.read())
file3.write(file2.read())

file1.close()
file2.close()
file3.close()

print("Files merged.")

# 9
import csv

file = open("Assessments/data.csv", "r")
reader = csv.reader(file)

for row in reader:
    print(" | ".join(row))

file.close()

# 10
source = open("Assessments/file1.txt", "r")
backup = open("Assessments/file2.txt", "w")

backup.write(source.read())

source.close()
backup.close()

print("Backup created successfully.")
