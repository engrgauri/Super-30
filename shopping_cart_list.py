cart = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]

# Display all products
print(cart)
# Access first and last products
print(cart[0],cart[-1])
# Add "Webcam"
cart.append("Webcam")
print(cart)
# Insert "USB Hub" at index 2
cart.insert(2,"USB Hub")
print(cart)
# Remove "Mouse"
cart.remove("Mouse")
print(cart)
# Remove the last item using pop()
cart.pop()
print(cart)
# Find the index of "Monitor"
index_monitor = cart.index("Monitor")
print(index_monitor)
# Count occurrences of "Laptop"
count_laptop = cart.count("Laptop")
print(count_laptop)
# Create a copy of the cart
cart_copy = cart.copy()
print(cart)
# Reverse the cart
cart = cart[::-1]
print(cart)
# Sort the products alphabetically
cart.sort()
print(cart)