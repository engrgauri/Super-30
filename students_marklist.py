marks = [78, 85, 90, 67, 88, 92, 76]

# Print the complete list
print(marks)
# Print the first element
print(marks[0])
# Print the last element
print(marks[-1])
# Print elements from index 2 to 5
print(marks[2:6])
# Find the number of elements
print(len(marks))
# Find maximum marks
print(max(marks))
# Find minimum marks
print(min(marks))
# Find total marks
print(sum(marks))
# Sort marks in ascending order
print(sorted(marks))
# Sort marks in descending order
print(sorted(marks,reverse=True))
# Add 95
marks.append(95)
print(marks)
# Add [81, 84]
marks.extend([81,84])
print(marks)
# Remove 67
marks.remove(67)
print(marks)
# Count how many times 90 occurs
print(marks.count(90))
# Find the index of 88
print(marks.index(88))