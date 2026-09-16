# 1. Initialize the laptop dictionary
laptop = {
    "brand": "Dell",
    "model": "XPS 15",
    "price": 120000,
    "ram": "16GB",
    "storage": "512GB SSD",
    "available": True
}

print("Original Laptop Details:")
print(laptop)

# 2. Access specific specifications
print(f"\nBrand: {laptop['brand']}")
print(f"Model: {laptop['model']}")
print(f"Price: ₹{laptop['price']}")

# 3. Modify and add specifications
laptop["price"] = 115000  # Corrected price change (assuming a realistic price reduction from 1,20,000)
laptop["processor"] = "Intel i7"
laptop["gpu"] = "NVIDIA RTX 4050"  # Cleaned up naming convention

laptop["ram"] = "32GB" 

print("\nLaptop after updates and modifications:")
print(laptop)

# 4. Remove a specification safely
# Using pop() with a default value prevents crashes if the key doesn't exist
laptop.pop("available", None) 
print("\nLaptop after removing availability status:")
print(laptop)

# 5. Extract dictionary views
print("\n--- Dictionary Structure ---")
print("Keys:", list(laptop.keys()))
print("Values:", list(laptop.values()))
# FIXED: Changed from printing the dictionary to printing the actual key-value tuples
print("Items:", list(laptop.items()))

# 6. Create a consistent secondary product dictionary (Mobile Phone)
# Matches the lowercase key naming convention used in the laptop dictionary
mobile = {
    "brand": "Apple",
    "model": "iPhone 17",
    "storage": "256GB",
    "available": True
}

print("\nMobile Phone Details:")
print(mobile)
