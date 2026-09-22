# Questions

# Create function that returns the addition of two numbers.


# def add(a, b)
def add(a,b):
    return num1 +num2

num1 = int(input("Enter the First Number"))
num2 = int(input("Enter the Second Number"))
addition = add(num1,num2)
print("Sum of numbers :",num1+num2)

# Create functions for addition subtraction multiplication division
def add():
    num1 = int(input("Enter the First Number"))
    num2 = int(input("Enter the Second Number"))
    return num1 +num2
def substract():
    num1 = int(input("Enter the First Number"))
    num2 = int(input("Enter the Second Number"))
    return num1 -  num2
def multiply():
    num1 = int(input("Enter the First Number"))
    num2 = int(input("Enter the Second Number"))
    return num1 * num2
def divide():
    num1 = int(input("Enter the First Number"))
    num2 = int(input("Enter the Second Number"))
    return num1 // num2

addition = add()
print("Sum of numbers :",addition)

substraction = substract()
print("Substraction of numbers :",substraction)

multiplication = multiply()
print("Multiplication of numbers :",multiplication)

division = divide()
print("Division of numbers :",division)

# Create a function that determines whether a number is even or odd.
def fun_check(a):
    if a == 1:
        print("Number is pime")
    elif a % 2 == 0:
        print("Number is Even !!!")
    else:
        print("Number is odd")

number = int(input("Enter the Number"))
fun_check(number)
# Create a function that returns the largest of three numbers without using max().
def find_largest(a, b, c):
    """
    Returns the largest of three numbers without using the built-in max() function.
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(find_largest(10, 24, 12))  # Output: 24
print(find_largest(5, 5, 3))     # Output: 5

# Create a function that calculates factorial.
def factorial(number):
    fact = 1
    while number > 0:
        fact = fact * number
        number = number -1
    return fact
value = factorial(int(input("Enter the Number")))
print("Factorial is ",value)
# Create a function that checks whether a number is prime.
def is_prime(n):
    """
    Returns True if n is prime, False otherwise.
    Time Complexity: O(√n)
    """
    # 1. Handle base cases
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3 are prime
        
    # 2. Eliminate even numbers and multiples of 3
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    # 3. Check factors up to the square root of n
    # All primes greater than 3 are of the form 6k ± 1
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True

print(is_prime(11))  # Output: True
print(is_prime(4))   # Output: False
print(is_prime(1))   # Output: False

# Create

# def calculate_discount(price, discount=10)

# where the default discount is 10%.
def calculate_discount(price, discount=10):
    pay = price*discount/100
    return pay

cust_pay = calculate_discount(int(input("Enter the Price")))
print("Discount is ",cust_pay)
# Create a function that accepts a list and returns its sum without using sum().
def sum_nums(list1):
    sum = 0
    for i in list1:
        sum = sum + i 
    return sum

value = sum_nums([1,2,3,5])
print("Sum of list of Numbers is :",value)
# Create a function that accepts a string and returns the number of vowels.
def vowels_check(str):
    count = 0
    for i in str:
        if i in ['a','e','i','o','u']:
            count = count + 1 
    return count

value = vowels_check(input("Enter the String "))
print("Vowels of String are :",value)

# Create a function that accepts a string and determines whether it is a palindrome.
def is_palindrome(text: str) -> bool:
    # Reverse the string and compare it to the original
    return text == text[::-1]

# Examples
print(is_palindrome("racecar"))  # True
print(is_palindrome("radar"))    # True
print(is_palindrome("hello"))    # False

# Create a function that accepts

# name

# age

# course

# and returns a formatted student profile.

# Use both positional and keyword arguments while calling it.

def create_student_profile(name, age, course):
    return f"""
    --- Student Profile ---
    Name:   {name}
    Age:    {age}
    Course: {course}
    -----------------------
    """
