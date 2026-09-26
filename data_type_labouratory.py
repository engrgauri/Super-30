# 1. int (Integer)
age = 25
item_count = -150

# 2. float (Floating-point number)
price = 19.99
pi_value = 3.14159

# 3. str (String)
user_name = "Alice"
greeting = 'Hello, World!'

# 4. bool (Boolean)
is_active = True
has_discount = False

# 5. list (List)
shopping_list = ["apple", "banana", "orange"]
prime_numbers = [2, 3, 5, 7, 11]

# 6. tuple (Tuple)
coordinates = (40.7128, -74.0060)
rgb_color = (255, 0, 128)

# 7. set (Set)
unique_ids = {101, 102, 103}
vowels = {'a', 'e', 'i', 'o', 'u'}

# 8. dict (Dictionary)
user_profile = {"username": "coder123", "score": 95}
currency_symbols = {"USD": "$", "EUR": "€"}

# Identifying and displaying the data type of each variable
print(type(age))
print(type(item_count))
print(type(price))
print(type(pi_value))
print(type(user_name))
print(type(greeting))
print(type(is_active))
print(type(has_discount))
print(type(shopping_list))
print(type(prime_numbers))
print(type(coordinates))
print(type(rgb_color))
print(type(unique_ids))
print(type(vowels))
print(type(user_profile))
print(type(currency_symbols))

# 1. String to Integer
converted_int = int("100")
print(f"Value: {converted_int}, Type: {type(converted_int)}")
# Explanation: Converts a string containing numeric characters into an actual mathematical integer. The string quotes are removed, enabling mathematical operations like addition or subtraction.

# 2. String to Float
converted_float = float("45.67")
print(f"Value: {converted_float}, Type: {type(converted_float)}")
# Explanation: Converts a string containing a decimal number into a floating-point number. This preserves the fractional part so Python can use it in precise decimal calculations.

# 3. Integer to String
converted_str = str(500)
print(f"Value: '{converted_str}', Type: {type(converted_str)}")
# Explanation: Converts a numeric integer into a string of text characters. The number 500 becomes text, which allows you to concatenate (glue) it to other text strings.

# 4. Integer to Boolean
converted_bool = bool(1)
print(f"Value: {converted_bool}, Type: {type(converted_bool)}")
# Explanation: Converts an integer into a truth value. In Python, any non-zero number converts to True, while zero (0) converts to False.

# 5. Tuple to List
converted_list = list((1, 2, 3))
print(f"Value: {converted_list}, Type: {type(converted_list)}")
# Explanation: Converts an unchangeable (immutable) tuple into a changeable (mutable) list. The parentheses () are replaced by square brackets [], allowing you to add, remove, or modify items.

# 6. List to Tuple
converted_tuple = tuple([1, 2, 3])
print(f"Value: {converted_tuple}, Type: {type(converted_tuple)}")
# Explanation: Converts a changeable (mutable) list into an unchangeable (immutable) tuple. The square brackets [] become parentheses (), locking the collection so its elements and order cannot be altered.

# 7. List to Set
converted_set = set([1, 2, 2, 3])
print(f"Value: {converted_set}, Type: {type(converted_set)}")
# Explanation: Converts a list into a set, which automatically strips away any duplicate values (the duplicate 2 is removed). The result is a collection of unique items enclosed in curly braces {}.
