message = " Welcome To Python Programming Class "

# Remove extra spaces
clean_msg = message.strip()
print(clean_msg)

# Convert everything to lowercase
lower_msg = message.lower()
print(lower_msg)

# Convert everything to uppercase
upper_msg = message.upper()
print(upper_msg)

# Convert to title case
title_msg = message.title()
print(title_msg)

# Replace "Python" with "Advanced Python"
replace_msg = message.replace("Python" , "Advanced Python")
print(replace_msg)

# Check whether the string starts with "Welcome"
check_msg = message.startswith("Welcome")
print(check_msg)

# Check whether it ends with "Class"
check_msg = message.endswith("Class")
print(check_msg)

# Count occurrences of "o"
count_msg = message.count("o")
print(count_msg)

# Find the position of "Programming"
find_msg = message.find("Programming")
print(find_msg)

# Split the sentence into words
split_msg = message.split()
print(split_msg)