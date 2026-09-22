# Write a program to print numbers from 1 to 100 using a for loop.

for i in range(1,101):
    print(i)
# Print all even numbers from 1 to 100.
for i in range(1,101):
    if i % 2 == 0:
        print(f"Even Number {i}") 
# Print all odd numbers from 1 to 100.
for i in range(1,101):
    if i % 2 != 0:
        print(f"Odd Number {i}") 
# Take an integer n and print its multiplication table from 1 to 20.
num = int(input("Enter the Number"))
for i in range (1,21):
    print(f"Multiplication {num} * {i} : {num * i}")
# Calculate the sum of numbers from 1 to n using a loop.
num = int(input("Enter the Number"))
sum = 0
for i in range(1,num):
    sum = sum + i
print(f"Sum of Number from 1 to {num}: {sum}") 
# Calculate the factorial of a number without using any built-in factorial function.

# Given

numbers = [12, 7, 9, 20, 33, 42, 8, 15]

# Print only the numbers divisible by 3.
for i in numbers:
    if i % 3 == 0:
        print(f"Number {i} is Divisible by 3")
# Given

languages = ["Python", "Java", "C++", "JavaScript", "Go"]

# Print every language along with its length.
leng = 0
for i in languages:
    print(i)
    leng = leng + 1
print("Length of List of Languages is ",leng)
# Iterate through

student = {"name": "Rahul","age": 22,"course": "Data Science","city": "Bangalore"}

# and print every key and value.
print(f"Students keys are :{student.keys()} values: {student.values()}")
# Count how many vowels exist in a user-provided string.
string = str(input("Enter the String :"))
vowels = ['a','e','i','o','u']
count_vowels = 0
for i in string:
    if i in vowels:
        count_vowels = count_vowels + 1
print(count_vowels)
# Reverse a string using a for loop without using [::-1] or reversed().
string = str(input("Enter the String :"))
reverse_str = ""
str_lst = list(string)
for i in range(len(string)-1,-1,-1):
    reverse_str = reverse_str + str_lst[i] 
print(reverse_str)
# Find the largest number from a list without using max().
lst = [2,3,1,55,33,76,25]
largest = lst[0]
for i in range(0,len(lst)):
    if lst[i] > largest:
        largest = lst[i]
print(largest)

# Submission Guidelines

# Create a public GitHub repository named

# super30-python-loop-task-1

# Your repository must contain

# Python source code for all questions

# Proper filenames or clearly separated programs

# Comments explaining important logic

# README.md explaining the task

# Sample input/output wherever applicable

# Record a YouTube video explaining your solutions. Do not simply read the code. Explain the logic, execution flow, inputs, outputs, and at least one test case.