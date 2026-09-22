# Print numbers from 1–100 but skip numbers divisible by 5 using continue.
for i in range(1,101):
    if i % 5 == 0:
        continue
    #print(i)

# Iterate from 1–100 and stop when you encounter the first number divisible by both 7 and 11.
for i in range(1,101):
    if i%7 == 0 and i%11 == 0:
        print("Stopping execution. First number found: ",i)
        break
    print(i)
# Search for a user-provided number inside a list. Use for-else to print:
lst = [2,3,4,5,6]

search_target = int(input("Enter a number to search: "))

for num in lst:
    if num == search_target:
        print(f"Success: {search_target} was found in the list!")
        break  
else:
    print(f"Failed: {search_target} is not present in the list.")

# Given

names = ["Aman", "Ravi", "Sudhanshu", "Priya", "Anjali"]

for name, count  in enumerate(names, start=1):
    print(f"{name} {count}")


# Print the following pattern

# *

# **

# ***

# ****

# *****

# Print

# *****

# ****

# ***

# **

# *
print("--- Increasing Pattern ---")
# Loop from 1 to 5
for i in range(1, 6):
    print("*" * i)

print("\n--- Decreasing Pattern ---")
# Loop from 5 down to 1
for i in range(5, 0, -1):
    print("*" * i)

# Generate multiplication tables from 1 to 10 using nested loops.
for i in range(1, 11):
    print(f"=== Multiplication Table of {i} ===")
    
    # Inner loop performs the multiplication (1 to 10)
    for j in range(1, 11):
        product = i * j
        print(f"{i} x {j} = {product}")
        
    # Print an empty line between tables for clean separation
    print()
# Find all numbers between 1 and 200 divisible by both 3 and 5.
for i in range (1,201):
    if i%3 == 0 and i%5 == 0:
        print(f"Number {i} is divisible by 3 and 5")
# Given a list containing duplicate elements, create another list containing only unique elements without using set().
lst = [2,3,2,1,44,22,12,55]
unq_lst = []
for i in lst:
    if i not in unq_lst:
        unq_lst.append(i)
print(unq_lst)
# Given

numbers = [10, -4, 8, -2, 0, 15, -9, 21]

# count
print(len(numbers))
# positive numbers
positive_num = []
for i in numbers:
    if i > 0 :
        positive_num.append(i)
# negative numbers
negative_num = []
for i in numbers:
    if i < 0 :
        negative_num.append(i)
# zeros
for i in numbers:
    if i == 0 :
        print(f"List contains {i}")
# Write a program to determine whether a number is prime using a loop.

# Print all prime numbers between 1 and 100.

# 1. Accept an integer input from the user
num = 101

# 1. Outer loop to check each number from 2 up to 100 (1 is not prime)
for num in range(2, 101):
    
    # 2. Inner loop to check if the current 'num' has any factors
    # We only need to check up to num // 2 for factors
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            break  # Found a factor, stop checking this number
    else:
        # Executes only if the inner loop finishes without breaking
        print(num, end=" ")
