student = { "name": "Rahul","age": 22,"course": "Python","city": "Bangalore","marks": 88 }

# Print the complete dictionary
print(student)
# Print the student's name
print(student["name"])
# Print their course
print(student["course"])
# Print all keys
print(student.keys())
# Print all values
print(student.values())
# Print all key-value pairs
print(student.items())
# Change marks from 88 to 92
student.update({"marks":92})
print(student)
# Add "email"
student.update({"email": "abc@gmail.com"})
print(student)
# Add "phone"
student.update({"phone":"0000000000"})
# Remove "city"
student.pop("city")
# Use get() to retrieve "name"
print(student.get("name"))
# Create a copy of the dictionary
stud_copy = student.copy()
print(stud_copy)