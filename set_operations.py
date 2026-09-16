# Initializing the sets
python_students = {"Rahul", "Aman", "Priya", "Karan", "Neha"}
java_students = {"Priya", "Karan", "Rohit", "Simran"}

# 1. Print both sets
print("Python Students:", python_students)
print("Java Students:", java_students)

# 2. Find students learning either Python or Java
either_student = python_students.union(java_students)
print("\nStudents learning either Python or Java:", either_student)

# 3. Find students learning both
both_students = python_students.intersection(java_students)
print("Students learning both Python and Java:", both_students)

# 4. Find students learning only Python
only_python = python_students.difference(java_students)
print("Students learning only Python:", only_python)

# 5. Find students learning only Java
only_java = java_students.difference(python_students)
print("Students learning only Java:", only_java)

# 6. Find students belonging to exactly one group
exactly_one = python_students.symmetric_difference(java_students)
print("Students in exactly one group:", exactly_one)

# 7. Add a new student
python_students.add("Sneha")
print("\nAfter adding 'Sneha' to Python:", python_students)

# 8. Remove a student
python_students.remove("Rahul")
print("After removing 'Rahul' from Python:", python_students)

# 9. Demonstrate discard()
python_students.discard("Aman")
print("After discarding 'Aman' from Python:", python_students)

# Demonstration of discard vs remove when item doesn't exist
print("\nDemonstrating discard() behavior with a non-existent student:")
python_students.discard("NonExistentStudent")  # Will NOT raise an error
print("discard() executed successfully without crashing.")
