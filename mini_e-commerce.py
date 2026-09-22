products = [
{"name": "Laptop","price": 70000,"brand": "Dell"},
{"name": "Phone","price": 40000,"brand": "Samsung"},
{"name": "Tablet","price": 30000,"brand": "Apple"}
]
# Print all products
print(products)
# Print first product
print(products[0])
# Print second product's price
print(products[1])
# Print third product's brand
print(products[2])
# Change first product's price
products[0]["price"] = 80000
print(products[0])
# Add "rating" to the second product
products[1]["rating"] = "4*"
# Add another product manually
products.append({"name": "iphone","price": 90000,"brand": "Apple"})
# Print the final dataset
print(products)
