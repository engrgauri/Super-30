technologies = ("Python", "Java", "Python", "C++", "JavaScript", "Python")

# 1. Inspect the tuple
print("Tuple:", technologies)
print("Type:", type(technologies))

# 2. Access elements
print("First item:", technologies[0])
print("Last item:", technologies[-1])

# 3. Slice the tuple (returns elements at index 0 and 1)
print("Sliced tuple (0:2):", technologies[0:2])

# 4. Search and Count
print("Count of 'Python':", technologies.count("Python"))
print("Index of 'C++':", technologies.index("C++"))
print("Tuple length:", len(technologies))

# 5. Modify data by converting to a list
tech_list = list(technologies)
tech_list.append("Go")
print("Updated List:", tech_list)

# 6. Convert it back into a tuple
technologies = tuple(tech_list)
print("Updated Tuple:", technologies)
