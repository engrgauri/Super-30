# Create a function using *args that accepts any number of values and returns their total.
def calculate_total(*args) -> float:
    """
    Accepts any number of numeric values using *args 
    and returns their aggregated total.
    """
    total = 0.0
    
    for value in args:
        total += value
        
    return total
# Test Case 1: Pass 3 integers
print(calculate_total(10, 20, 30))       # Output: 60.0

# Test Case 2: Pass 5 mixed numbers (ints & floats)
print(calculate_total(1.5, 2.5, 4, 2))   # Output: 10.0

# Test Case 3: Pass no arguments at all
print(calculate_total())                 # Output: 0.0

# Create a function using *args that returns the largest supplied number.
def find_largest(*args):
    """
    Accepts an arbitrary number of numeric values using *args
    and returns the largest supplied number.
    """
    # Guard clause: Return None if no numbers were provided
    if not args:
        return None
        
    # Assume the first item in the tuple is the largest initially
    largest = args[0]
    
    # Loop through the remaining values to find a higher ceiling boundary
    for num in args:
        if num > largest:
            largest = num
            
    return largest

# Create
# def create_profile(**kwargs) that accepts dynamic user information and prints all provided attributes.

def create_profile(**kwargs):
    """
    Accepts dynamic user information via keyword arguments (**kwargs)
    and cleanly prints out all provided attributes.
    """
    # Guard clause: Check if any attributes were supplied
    if not kwargs:
        print("\n--- Empty Profile ---")
        return None

    print("\n--- 🧑‍💼 Dynamic User Profile ---")
    
    # Iterate through the packed dictionary key-value items
    for attribute, value in kwargs.items():
        # Clean up key formatting (e.g., changing 'first_name' to 'First Name')
        formatted_key = attribute.replace("_", " ").title()
        print(f"• {formatted_key:<15}: {value}")
        
    print("---------------------------------")
# Test Case 1: Standard basic profile details
create_profile(name="John Doe", age=28, city="Mumbai")

# Test Case 2: Professional profile with structural underscore attributes
create_profile(
    first_name="Priya",
    last_name="Sharma",
    job_title="Software Engineer",
    department="IT Operations",
    years_of_experience=5
)

# Test Case 3: Empty argument baseline validation call
create_profile()

# Create a function that accepts another function as an argument.

# Example idea

# calculate(add, 10, 20)

# calculate(multiply, 10, 20)
# 1. Define the operational math functions
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b


# 2. Create the master calculator function
# It accepts a function reference as its first parameter
def calculate(operation_func, x, y):
    """
    Accepts a mathematical function and two numbers,
    executes the function with those numbers, and returns the result.
    """
    # Execute the passed function reference directly
    return operation_func(x, y)

# Test Case 1: Pass the add function
result_add = calculate(add, 10, 20)
print(f"Addition Result: {result_add}")        # Output: 30

# Test Case 2: Pass the multiply function
result_mul = calculate(multiply, 10, 20)
print(f"Multiplication Result: {result_mul}")  # Output: 200

# Test Case 3: Pass the subtract function
result_sub = calculate(subtract, 50, 15)
print(f"Subtraction Result: {result_sub}")     # Output: 35

# Create a lambda function for calculating the square of a number.
x = int(input("Enter the Number for finding Square : "))
sq_num = lambda x : x** 2
print("Square of number : ",sq_num(x))
# Use lambda with map() to square

# Initialize a sample list of integers
numbers = [1, 2, 3, 4, 5, 6]

squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Use lambda with filter() to extract even numbers.
# Initialize a sample list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() to keep elements where the lambda conditional evaluates to True
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Display the output
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Write a recursive function to calculate factorial.
def calculate_factorial_recursive(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer using recursion.
    """
    # 1. Base Case: The stopping condition to prevent infinite loops
    if n == 0 or n == 1:
        return 1
        
    # 2. Recursive Case: The function calling itself with a smaller value
    return n * calculate_factorial_recursive(n - 1)
# Test Case 1: Standard positive integer
print(calculate_factorial_recursive(5))   # Output: 120 (5 * 4 * 3 * 2 * 1)

# Test Case 2: Base case edge validation
print(calculate_factorial_recursive(1))   # Output: 1
print(calculate_factorial_recursive(0))   # Output: 1

# Write a recursive function to calculate

# 1 + 2 + 3 + ... + n
def calculate_recursive_sum(n: int) -> int:
    """
    Calculates the sum of numbers from 1 to n using recursion.
    """
    # 1. Base Case: Stop when n drops to 1
    if n <= 1:
        return n
        
    # 2. Recursive Case: Add current n to the sum of (n - 1)
    return n + calculate_recursive_sum(n - 1)
# Test Case 1: Sum from 1 to 5 (1 + 2 + 3 + 4 + 5)
print(calculate_recursive_sum(5))   # Output: 15

# Test Case 2: Sum from 1 to 10
print(calculate_recursive_sum(10))  # Output: 55

# Test Case 3: Base case edge handling
print(calculate_recursive_sum(1))   # Output: 1

# Write a recursive function to generate the Fibonacci sequence or calculate the nth Fibonacci number.
def fibonacci_nth(n: int) -> int:
    """
    Returns the n-th Fibonacci number using recursion.
    Assumes 0-indexed sequence (e.g., 0th = 0, 1st = 1, 2nd = 1, 3rd = 2).
    """
    # Base Cases: The first two numbers in the sequence are 0 and 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
        
    # Recursive Case: F(n) = F(n-1) + F(n-2)
    return fibonacci_nth(n - 1) + fibonacci_nth(n - 2)

# Examples
print("5th Fibonacci number:", fibonacci_nth(5))  # Output: 5
print("7th Fibonacci number:", fibonacci_nth(7))  # Output: 13

# Demonstrate local and global variable scope using a small program.
# --- GLOBAL SCOPE ---
# This variable is created in the main body of the script.
# It can be read by any function anywhere in the program.
tracking_msg = "Hello from the Global Scope!"

def check_local_scope():
    # --- LOCAL SCOPE ---
    # This variable is created inside a function.
    # It exists ONLY while this function is running.
    local_val = 500
    
    print("\n[Inside check_local_scope function]")
    print("Can I access the global variable?", tracking_msg)  # Works fine
    print("Can I access my local variable?", local_val)     # Works fine

def try_modifying_global():
    print("\n[Inside try_modifying_global function]")
    try:
        # Trying to access the local variable from the other function will fail
        print(local_val)
    except NameError as e:
        print("❌ Error trying to read 'local_val':", e)
        print("Reason: Variables created inside one function cannot be seen by other functions.")

# --- Running the Program ---
if __name__ == "__main__":
    print("==========================================")
    print("         VARIABLE SCOPE DEMO              ")
    print("==========================================")
    
    # Run the functions
    check_local_scope()
    try_modifying_global()
    
    # Checking access from the main program body
    print("\n[Inside Main Program Body]")
    print("Reading global variable:", tracking_msg)  # Works fine
    
    try:
        print(local_val)
    except NameError:
        print("❌ Error: The main program cannot read 'local_val' either because it belongs strictly to its function.")
    print("==========================================")

# Create a mini calculator where each mathematical operation is implemented as a separate function and a main function controls the program.
# ----------------- OPERATIONAL MATH FUNCTIONS -----------------

def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns the difference between two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b

def divide(a: float, b: float):
    """Returns the quotient of two numbers, protecting against division by zero."""
    if b == 0:
        print("❌ Arithmetic Error: Division by zero is undefined.")
        return None
    return a / b


# ----------------- MASTER CONTROLLER FUNCTION -----------------

def main_calculator():
    """Main application loop managing user selections and operations."""
    while True:
        print("\n==========================================")
        print("             📱 MINI CALCULATOR           ")
        print("==========================================")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit Application")
        print("==========================================")
        
        choice = input("Select an operation (1-5): ").strip()
        
        # Immediate exit check
        if choice == "5":
            print("\nShutting down calculator. Goodbye!")
            break
            
        # Validate that the menu option matches a mathematical operation
        if choice not in ["1", "2", "3", "4"]:
            print("❌ Input Error: Please choose a valid menu number between 1 and 5.")
            continue
            
        # Safely collect and parse numeric inputs
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("❌ Input Error: Please enter valid numeric values.")
            continue
            
        # Execute the chosen mathematical function
        if choice == "1":
            result = add(num1, num2)
            print(f"\n✨ Result: {num1} + {num2} = {result}")
            
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"\n✨ Result: {num1} - {num2} = {result}")
            
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"\n✨ Result: {num1} * {num2} = {result}")
            
        elif choice == "4":
            result = divide(num1, num2)
            # Only print if a valid calculation occurred (avoids printing None on zero division)
            if result is not None:
                print(f"\n✨ Result: {num1} / {num2} = {result}")


main_calculator()
