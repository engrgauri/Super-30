# Questions

# 1 Student Result Management System

# Create functions to
# accept student marks
# calculate total
# calculate percentage
# assign grade
# determine pass/fail
# display result
# Use loops wherever appropriate.

def stud_marks(name:str, science_mrks : int, Maths_mrks: int, English_mrks : int):
    print("Marks of Science :",science_mrks)
    print("Marks of Science :",Maths_mrks)
    print("Marks of Science :",English_mrks)

    total_marks = science_mrks + Maths_mrks + English_mrks
    print("Total Marks :",total_marks)

    percentage = round((total_marks / 300) * 100, 2)
    print("Percentage :",percentage)
                       
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    print("Grade :",grade)

    return {
        "Student Name": name,
        "Total Marks": f"{total_marks}/{300}",
        "Percentage": f"{percentage}%",
        "Grade": grade,
        "Status": "PASSED" if grade != "F" else "FAILED"
    }


student_report = stud_marks("Jane Smith", 92, 88, 95)

import json
print(json.dumps(student_report, indent=4))# 2
# Banking Application

# Create a menu-driven banking program supporting

# Check balance

# Deposit

# Withdraw

# Transaction history

# Exit

def banking_system():
    # Initializing account state
    balance = 0.0
    history = []

    while True:
        # Display Menu
        print("\n=== WELCOME TO THE BANK ===")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        # 1. Check Balance
        if choice == "1":
            print(f"\nYour current balance is: ${balance:,.2f}")

        # 2. Deposit
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: $"))
                if amount <= 0:
                    print("Error: Deposit amount must be greater than zero.")
                else:
                    balance += amount
                    history.append(f"Deposited: +${amount:,.2f}")
                    print(f"Successfully deposited ${amount:,.2f}!")
            except ValueError:
                print("Error: Please enter a valid numeric amount.")

        # 3. Withdraw
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: $"))
                if amount <= 0:
                    print("Error: Withdrawal amount must be greater than zero.")
                elif amount > balance:
                    print(f"Error: Insufficient funds. Your balance is ${balance:,.2f}.")
                else:
                    balance -= amount
                    history.append(f"Withdrew: -${amount:,.2f}")
                    print(f"Successfully withdrew ${amount:,.2f}!")
            except ValueError:
                print("Error: Please enter a valid numeric amount.")

        # 4. Transaction History
        elif choice == "4":
            print("\n--- Transaction History ---")
            if not history:
                print("No transactions recorded yet.")
            else:
                for record in history:
                    print(record)
            print("---------------------------")

        # 5. Exit
        elif choice == "5":
            print("\nThank you for banking with us. Goodbye!")
            break

        # Invalid Input Handling
        else:
            print("Invalid choice! Please select an option between 1 and 5.")

banking_system()


# Use functions for each operation and while for the application menu.

# 3
# Inventory Management

# Maintain products containing

# product name

# price

# quantity

# Provide functions to

# add product

# display products

# search product

# update quantity

# calculate total inventory value

inventory = {}

def add_product():
    """Accepts and adds a new product to the inventory."""
    name = input("Enter product name: ").strip().lower()
    if name in inventory:
        print(f"Error: '{name.title()}' already exists. Use 'Update Quantity' instead.")
        return
        
    try:
        price = float(input("Enter price per unit: $"))
        quantity = int(input("Enter initial stock quantity: "))
        
        if price < 0 or quantity < 0:
            print("Error: Price and quantity cannot be negative.")
            return
            
        inventory[name] = {"price": price, "quantity": quantity}
        print(f"Success: '{name.title()}' added to inventory!")
    except ValueError:
        print("Error: Invalid numeric input for price or quantity.")

def display_products():
    """Displays all products currently stored in the inventory."""
    if not inventory:
        print("\nInventory is empty.")
        return
        
    print("\n" + "="*45)
    print(f"{'Product Name':<20} | {'Price':<10} | {'Quantity':<8}")
    print("="*45)
    for name, info in inventory.items():
        print(f"{name.title():<20} | ${info['price']:<9,.2f} | {info['quantity']:<8}")
    print("="*45)

def search_product():
    """Searches for a specific product and prints its current metrics."""
    name = input("Enter product name to search: ").strip().lower()
    if name in inventory:
        info = inventory[name]
        print(f"\n--- Product Found ---")
        print(f"Name:     {name.title()}")
        print(f"Price:    ${info['price']:,.2f}")
        print(f"Quantity: {info['quantity']}")
    else:
        print(f"Product '{name.title()}' not found in inventory.")

def update_quantity():
    """Updates the stock levels for an existing product."""
    name = input("Enter product name to update: ").strip().lower()
    if name not in inventory:
        print(f"Product '{name.title()}' not found.")
        return
        
    try:
        new_qty = int(input(f"Enter new quantity for {name.title()}: "))
        if new_qty < 0:
            print("Error: Quantity cannot be negative.")
            return
        inventory[name]["quantity"] = new_qty
        print(f"Success: Updated '{name.title()}' quantity to {new_qty}.")
    except ValueError:
        print("Error: Quantity must be a whole number.")

def calculate_total_value():
    """Computes and displays the sum total financial value of the entire inventory."""
    total_value = sum(item["price"] * item["quantity"] for item in inventory.values())
    print(f"\nTotal Financial Value of Inventory: ${total_value:,.2f}")


def main_menu():
    """Application menu driven by a while loop."""
    while True:
        print("\n=== INVENTORY MANAGEMENT SYSTEM ===")
        print("1. Add Product")
        print("2. Display All Products")
        print("3. Search Product")
        print("4. Update Product Quantity")
        print("5. Calculate Total Inventory Value")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_product()
        elif choice == "2":
            display_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_quantity()
        elif choice == "5":
            calculate_total_value()
        elif choice == "6":
            print("\nExiting System. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter a number between 1 and 6.")

# Run the system
main_menu()



    
# 4
# Quiz Application

# Create at least 5 Python questions.

# The application should

# display one question at a time

# accept answers

# check answers

# maintain score

# show final percentage

# A list of dictionaries containing the quiz database
quiz_questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) func", "B) define", "C) def", "D) function"],
        "correct": "C"
    },
    {
        "question": "What is the correct output of print(type([]) ) in Python?",
        "options": ["A) <class 'list'>", "B) <class 'tuple'>", "C) <class 'dict'>", "D) <class 'array'>"],
        "correct": "A"
    },
    {
        "question": "Which data type in Python is mutable?",
        "options": ["A) string", "B) tuple", "C) integer", "D) list"],
        "correct": "D"
    },
    {
        "question": "How do you insert an element at the end of a list?",
        "options": ["A) list.insert()", "B) list.append()", "C) list.add()", "D) list.push()"],
        "correct": "B"
    },
    {
        "question": "What character is used to start a comment line in Python?",
        "options": ["A) //", "B) /*", "C) #", "D) !"],
        "correct": "C"
    }
]

def ask_question(question_data, question_num):
    """Displays a single question and captures a validated user answer."""
    print(f"\nQuestion {question_num}: {question_data['question']}")
    for option in question_data['options']:
        print(option)
        
    while True:
        user_ans = input("Your answer (A, B, C, or D): ").strip().upper()
        if user_ans in ["A", "B", "C", "D"]:
            return user_ans
        print("Invalid choice! Please type a letter matching one of the options.")

def calculate_results(score, total_questions):
    """Computes and prints the final score summary and performance percentage."""
    percentage = (score / total_questions) * 100
    print("\n" + "="*35)
    print("           QUIZ COMPLETED           ")
    print("="*35)
    print(f"Correct Answers: {score} out of {total_questions}")
    print(f"Final Score:     {percentage:.2f}%")
    
    if percentage >= 80:
        print("Performance:     Excellent! 🌟")
    elif percentage >= 50:
        print("Performance:     Good effort! 👍")
    else:
        print("Performance:     Keep practicing! 📚")
    print("="*35 + "\n")

def run_quiz():
    """Main function driven by a while loop to step through the application."""
    print("=== Welcome to the Python Quiz Application ===")
    input("Press Enter to begin...")
    
    score = 0
    total = len(quiz_questions)
    index = 0
    
    # Process each question one at a time using a while loop
    while index < total:
        current_q = quiz_questions[index]
        
        # Ask question and collect choice
        user_choice = ask_question(current_q, index + 1)
        
        # Check answer
        if user_choice == current_q["correct"]:
            print("✨ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was {current_q['correct']}.")
            
        index += 1  # Move onto the next question
        
    # Show summary metric report
    calculate_results(score, total)

# Start the game
run_quiz()


# 5
# Number Analysis Tool

# Create a function that accepts a list and returns

# largest number

# smallest number

# total

# average

# even count

# odd count

# positive count

# negative count

# Do not use min(), max(), or sum().
def analyze_numbers(numbers: list) -> dict:
    """
    Analyzes a list of numbers without using min(), max(), or sum().
    Returns a dictionary filled with statistical metrics.
    """
    # Guard clause for empty list input tracking
    if not numbers:
        return {
            "Largest Number": None, "Smallest Number": None, "Total": 0,
            "Average": 0, "Even Count": 0, "Odd Count": 0,
            "Positive Count": 0, "Negative Count": 0
        }

    # Initialize tracking pointers using the first index element value
    largest = numbers[0]
    smallest = numbers[0]
    total = 0
    
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0

    # Process all values inside a single execution block loop
    for num in numbers:
        # Accumulate structural total
        total += num
        
        # Track largest ceiling boundaries
        if num > largest:
            largest = num
            
        # Track smallest floor boundaries
        if num < smallest:
            smallest = num
            
        # Parity analysis (even/odd checking)
        # Note: Integers only are checked for parity, floats skip parity grouping safely if needed
        if isinstance(num, int) or num.is_integer():
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
        # Sign polarity checking (ignoring absolute zero for pure sign counts)
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1

    # Compute metric average precision values
    average = round(total / len(numbers), 2)

    return {
        "Largest Number": largest,
        "Smallest Number": smallest,
        "Total": total,
        "Average": average,
        "Even Count": even_count,
        "Odd Count": odd_count,
        "Positive Count": positive_count,
        "Negative Count": negative_count
    }
# Sample testing dataset list configuration
dataset = [12, -7, 5, 0, 23, -14, 8, -1]

# Run assessment pipeline analysis
analysis_report = analyze_numbers(dataset)

# Display pretty printed tracking metrics format
import json
print(json.dumps(analysis_report, indent=4))

# 6
# Employee Salary Analyzer

# Given employee salaries, create functions to determine

# total payroll

# average salary

# highest salary

# lowest salary

# employees earning above average

def analyze_payroll(employee_data: dict) -> dict:
    """
    Analyzes employee payroll data and computes key salary metrics.
    """
    # Guard clause for empty input data
    if not employee_data:
        return {
            "Total Payroll": 0.0,
            "Average Salary": 0.0,
            "Highest Salary": None,
            "Lowest Salary": None,
            "Employees Above Average": []
        }

    # Extract all salary values
    salaries = list(employee_data.values())
    
    # Calculate core mathematical metrics
    total_payroll = sum(salaries)
    average_salary = round(total_payroll / len(salaries), 2)
    
    # Find highest salary details
    highest_emp = max(employee_data, key=employee_data.get)
    highest_val = employee_data[highest_emp]
    
    # Find lowest salary details
    lowest_emp = min(employee_data, key=employee_data.get)
    lowest_val = employee_data[lowest_emp]
    
    # Extract employees earning strictly above average
    above_average_list = [
        name for name, salary in employee_data.items() if salary > average_salary
    ]

    return {
        "Total Payroll": total_payroll,
        "Average Salary": average_salary,
        "Highest Salary": f"{highest_emp} (₹{highest_val:,.2f})",
        "Lowest Salary": f"{lowest_emp} (₹{lowest_val:,.2f})",
        "Employees Above Average": above_average_list
    }

# Sample Employee Database
staff_salaries = {
    "Rahul Sharma": 45000,
    "Priya Patel": 95000,
    "Amit Verma": 62000,
    "Sneha Reddy": 120000,
    "Vikram Singh": 38000
}

# Run the analysis profile
report = analyze_payroll(staff_salaries)

# Output the metrics clearly
print("==========================================")
print("        EMPLOYEE SALARY REPORT            ")
print("==========================================")
print(f"Total Payroll:      ₹{report['Total Payroll']:,.2f}")
print(f"Average Salary:     ₹{report['Average Salary']:,.2f}")
print(f"Highest Paid:       {report['Highest Salary']}")
print(f"Lowest Paid:        {report['Lowest Salary']}")
print("\nEmployees Earning Above Average:")
for emp in report['Employees Above Average']:
    print(f"  - {emp} (₹{staff_salaries[emp]:,.2f})")
print("==========================================")

# 7
# Shopping Cart

# Create a simple cart where users can

# add products

# remove products

# view cart

# calculate bill

# exit
# Simulated Product Catalog with available prices
PRODUCT_CATALOG = {
    "laptop": 45000.00,
    "headphones": 2500.00,
    "mouse": 800.00,
    "keyboard": 1500.00,
    "monitor": 12000.00
}

# The active user shopping cart
# Structure: { product_name: quantity }
shopping_cart = {}

def display_catalog():
    """Helper function to show available store inventory."""
    print("\n--- Available Products ---")
    for item, price in PRODUCT_CATALOG.items():
        print(f"  - {item.title()}: ₹{price:,.2f}")
    print("--------------------------")

def add_to_cart():
    """Adds a valid catalog product to the user's active shopping cart."""
    display_catalog()
    item = input("Enter the product name to add: ").strip().lower()
    
    if item not in PRODUCT_CATALOG:
        print("❌ Error: Product not found in our catalog.")
        return
        
    try:
        qty = int(input(f"Enter quantity for {item.title()}: "))
        if qty <= 0:
            print("❌ Error: Quantity must be at least 1.")
            return
            
        # Update cart quantity dynamically
        shopping_cart[item] = shopping_cart.get(item, 0) + qty
        print(f"✨ Success: Added {qty}x {item.title()} to your cart.")
    except ValueError:
        print("❌ Error: Quantity must be a valid whole number.")

def remove_from_cart():
    """Reduces item quantities or completely eliminates them from the cart selection."""
    if not shopping_cart:
        print("\nYour shopping cart is currently empty.")
        return
        
    item = input("Enter product name to remove: ").strip().lower()
    
    if item not in shopping_cart:
        print("❌ Error: That item is not in your cart.")
        return
        
    try:
        qty_to_remove = int(input(f"You have {shopping_cart[item]}x in cart. How many to remove? "))
        if qty_to_remove <= 0:
            print("❌ Error: Quantity to remove must be greater than zero.")
            return
            
        if qty_to_remove >= shopping_cart[item]:
            del shopping_cart[item]
            print(f"🗑️ Complete: {item.title()} removed entirely from cart.")
        else:
            shopping_cart[item] -= qty_to_remove
            print(f"📉 Updated: Removed {qty_to_remove} units. Remaining: {shopping_cart[item]}x.")
    except ValueError:
        print("❌ Error: Quantity must be a valid whole number.")

def view_cart():
    """Displays items currently inside the shopping cart structural frame."""
    if not shopping_cart:
        print("\n🛒 Your shopping cart is empty.")
        return
        
    print("\n" + "="*45)
    print(f"{'Item Description':<18} | {'Qty':<5} | {'Unit Price':<10} | {'Total':<10}")
    print("="*45)
    for item, qty in shopping_cart.items():
        unit_price = PRODUCT_CATALOG[item]
        item_total = unit_price * qty
        print(f"{item.title():<18} | {qty:<5} | ₹{unit_price:<9,.2f} | ₹{item_total:<9,.2f}")
    print("="*45)

def calculate_bill():
    """Calculates, aggregates, and summarizes items for checkout payment processing."""
    if not shopping_cart:
        print("\n🛒 Cannot generate bill. Your shopping cart is empty.")
        return 0.0
        
    view_cart()
    subtotal = sum(PRODUCT_CATALOG[item] * qty for item, qty in shopping_cart.items())
    
    # Optional commercial taxes (e.g., GST at 18%)
    gst_amount = subtotal * 0.18
    grand_total = subtotal + gst_amount
    
    print(f"  Subtotal:     ₹{subtotal:,.2f}")
    print(f"  GST (18%):    ₹{gst_amount:,.2f}")
    print(f"  Grand Total:  ₹{grand_total:,.2f}")
    print("="*45)
    return grand_total

def main_cart_menu():
    """Main application loop managing shopping selections."""
    while True:
        print("\n==========================================")
        print("           🛒 DIGITAL SHOPPING CART        ")
        print("==========================================")
        print("1. Add Product to Cart")
        print("2. Remove Product from Cart")
        print("3. View Cart Items")
        print("4. Calculate Checkout Bill")
        print("5. Exit Application")
        print("==========================================")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            add_to_cart()
        elif choice == "2":
            remove_from_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            calculate_bill()
        elif choice == "5":
            print("\nThank you for visiting! Emptying runtime cart streams. Goodbye!")
            break
        else:
            print("❌ Invalid input! Please enter a choice matching numbers 1 to 5.")

main_cart_menu()

# 8
# Password Strength Checker

# Create a function that checks whether a password contains

# uppercase

# lowercase

# number

# special character

# minimum 8 characters

# Return a meaningful strength/result.

def check_password_strength(password: str) -> dict:
    """
    Evaluates a password string against 5 security criteria.
    Returns structural checklist feedback along with a descriptive rating.
    """
    # 1. Run criteria parameter checks
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)
    has_length = len(password) >= 8

    # 2. Aggregate structural score metric
    score = sum([has_upper, has_lower, has_digit, has_special, has_length])

    # 3. Establish structural descriptive evaluations
    if score == 5:
        verdict = "🟢 VERY STRONG"
    elif score == 4:
        verdict = "🟢 STRONG"
    elif score == 3:
        verdict = "🟡 MEDIUM"
    elif score == 2:
        verdict = "🟠 WEAK"
    else:
        verdict = "🔴 VERY WEAK"

    return {
        "score": score,
        "verdict": verdict,
        "breakdown": {
            "At least 8 characters": has_length,
            "Uppercase letters (A-Z)": has_upper,
            "Lowercase letters (a-z)": has_lower,
            "Numeric digits (0-9)": has_digit,
            "Special characters (e.g. @, #, $, !)": has_special
        }
    }

def password_checker_app():
    """Persistent menu runner that loops continuously until Exit is explicitly triggered."""
    while True:
        print("\n==========================================")
        print("         🔐 PASSWORD STRENGTH CHECKER     ")
        print("==========================================")
        print("1. Analyze a Password")
        print("2. Exit Application")
        print("==========================================")
        
        choice = input("Select an option (1-2): ").strip()
        
        if choice == "1":
            user_password = input("\nEnter the password to test: ")
            if not user_password:
                print("❌ Error: Password input cannot be completely empty.")
                continue
                
            # Run calculations
            report = check_password_strength(user_password)
            
            # Display results panel layout
            print("\n--- 📊 Analysis Summary ---")
            print(f"Overall Rating: {report['verdict']} ({report['score']}/5 Criteria Met)")
            print("-" * 30)
            for rule, passed in report['breakdown'].items():
                status_icon = "✅ Passed" if passed else "❌ Missing"
                print(f"• {rule:<36}: {status_icon}")
            print("---------------------------")
            
        elif choice == "2":
            print("\nClosing security audit tools safely. Goodbye!")
            break
        else:
            print("❌ Invalid input! Please choose option 1 or 2.")

if __name__ == "__main__":
    password_checker_app()

# 9
# Prime Number Analyzer

# Take two numbers representing a range.

# Create functions to

# find prime numbers

# count primes

# calculate their sum

# display the largest prime found

import math

def is_prime(num: int) -> bool:
    """Helper function to test if a number is prime."""
    if num <= 1:
        return False
    # Check factors up to the square root of the number
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start: int, end: int) -> list:
    """Returns a list of all prime numbers found within the given boundaries (inclusive)."""
    # Swap variables if the user input start is greater than end
    if start > end:
        start, end = end, start
        
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

def analyze_prime_range():
    """Accepts range inputs, processes computations, and displays structural analysis."""
    print("\n--- 🔢 Analyze a New Range ---")
    try:
        start = int(input("Enter the START of the range: "))
        end = int(input("Enter the END of the range: "))
        
        # Calculate the list of primes
        prime_list = find_primes_in_range(start, end)
        
        # Compute metrics using isolated parameters
        prime_count = len(prime_list)
        prime_sum = sum(prime_list)
        largest_prime = prime_list[-1] if prime_count > 0 else "None"
        
        # Display the formatted metric layout panel
        print("\n" + "="*45)
        print(f"      PRIME METRIC REPORT [{start} to {end}]     ")
        print("="*45)
        print(f"• Primes Found  : {prime_list if prime_count <= 15 else f'{prime_list[:15]}... (truncated)'}")
        print(f"• Total Count   : {prime_count}")
        print(f"• Sum of Primes : {prime_sum:,}")
        print(f"• Largest Prime : {largest_prime}")
        print("="*45)
        
    except ValueError:
        print("❌ Error: Range bounds must be valid whole integers.")

def main_prime_menu():
    """Persistent framework engine running loop blocks continuously until Exit chosen."""
    while True:
        print("\n==========================================")
        print("          ✨ PRIME NUMBER ANALYZER        ")
        print("==========================================")
        print("1. Analyze Range for Primes")
        print("2. Exit Application")
        print("==========================================")
        
        choice = input("Select an option (1-2): ").strip()
        
        if choice == "1":
            analyze_prime_range()
        elif choice == "2":
            print("\nShutting down calculation engines safely. Goodbye!")
            break
        else:
            print("❌ Invalid input! Please type 1 or 2.")

main_prime_menu()

# 10
# Expense Tracker

# Allow a user to repeatedly enter

# expense name

# amount

# Provide options to

# add expense

# view expenses

# calculate total

# find highest expense

# exit
# Master repository to store expense objects
# Structure: [{"name": str, "amount": float}]
expenses = []

def add_expense():
    """Accepts and appends a new expense object with structural input protection."""
    print("\n--- 💸 Record New Expenditure ---")
    name = input("Enter expense name/description: ").strip()
    if not name:
        print("❌ Error: Expense description cannot be completely empty.")
        return

    try:
        amount = float(input(f"Enter amount spent on '{name}': ₹"))
        if amount <= 0:
            print("❌ Error: Financial values must be strictly greater than zero.")
            return
            
        # Append structured dictionary block directly into list array
        expenses.append({"name": name, "amount": amount})
        print(f"✅ Success: Added '{name}' costing ₹{amount:,.2f} to records.")
    except ValueError:
        print("❌ Error: Invalid input. Please enter a clean decimal or whole number.")

def view_expenses():
    """Displays all itemized expenses currently recorded in the active session repository."""
    if not expenses:
        print("\n📭 Tracker Summary: No expenses recorded yet in this session.")
        return

    print("\n" + "="*45)
    print(f"{'Expense Name/Description':<28} | {'Amount Spent':<12}")
    print("="*45)
    for exp in expenses:
        print(f"{exp['name']:<28} | ₹{exp['amount']:<12,.2f}")
    print("="*45)

def calculate_total():
    """Aggregates and reports the mathematical sum total of expenses."""
    if not expenses:
        print("\n📭 Total Spending: ₹0.00 (No recorded items found)")
        return 0.0
        
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n📊 Aggregate Financial Expenditure: ₹{total:,.2f}")
    return total

def find_highest_expense():
    """Identifies and details the single most expensive entry using a lambda lookup."""
    if not expenses:
        print("\n📭 Analysis: No items registered to evaluate.")
        return

    # Extract maximum value record using amount subkey comparison parameters
    highest = max(expenses, key=lambda x: x["amount"])
    
    print("\n" + "-"*40)
    print("        🏆 COSTLIEST RECORD FOUND        ")
    print("-"*40)
    print(f"• Item Description : {highest['name']}")
    print(f"• Financial Impact : ₹{highest['amount']:,.2f}")
    print("-"*40)

def main_expense_app():
    """Primary utility execution controller driven by a continuous while loop."""
    while True:
        print("\n==========================================")
        print("        💰 PERSONAL EXPENSE TRACKER        ")
        print("==========================================")
        print("1. Add Expense")
        print("2. View All Stored Expenses")
        print("3. Calculate Cumulative Total Bill")
        print("4. Find Highest Expense Record")
        print("5. Exit Application Workspace")
        print("==========================================")
        
        choice = input("Select a dashboard option (1-5): ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            find_highest_expense()
        elif choice == "5":
            print("\nSafely committing temporary tracking buffers to zero. Goodbye!")
            break
        else:
            print("❌ Selection error! Please choose an accurate path identifier from 1 to 5.")

main_expense_app()


# Master repository to store expense objects
# Structure: [{"name": str, "amount": float}]
expenses = []

def add_expense():
    """Accepts and stores an expense item with numeric validation."""
    name = input("Enter expense description/name: ").strip()
    if not name:
        print("Error: Expense name cannot be empty.")
        return

    try:
        amount = float(input(f"Enter amount spent on '{name}': ₹"))
        if amount <= 0:
            print("Error: Amount must be greater than zero.")
            return
            
        expenses.append({"name": name, "amount": amount})
        print(f"Success: Added '{name}' costing ₹{amount:,.2f} to tracker.")
    except ValueError:
        print("Error: Please enter a valid decimal or integer number.")

def view_expenses():
    """Prints out all stored expense records in a aligned layout table."""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n" + "="*40)
    print(f"{'Expense Item':<25} | {'Amount Spent':<12}")
    print("="*40)
    for exp in expenses:
        print(f"{exp['name']:<25} | ₹{exp['amount']:<12,.2f}")
    print("="*40)

def calculate_total():
    """Computes and summarizes the aggregated financial sum total spent."""
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nAggregate Total Expenditure: ₹{total:,.2f}")
    return total

def find_highest_expense():
    """Finds and highlights the single costliest layout expense item."""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    # Use max utility matching by target dictionary property key values
    highest = max(expenses, key=lambda x: x["amount"])
    print(f"\n--- Highest Expense Record ---")
    print(f"Item Description: {highest['name']}")
    print(f"Amount Trailed:   ₹{highest['amount']:,.2f}")
    print("------------------------------")


def main_tracker_menu():
    """Primary application structural layout runtime driven by a loop."""
    while True:
        print("\n==========================================")
        print("           PERSONAL EXPENSE TRACKER       ")
        print("==========================================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Spending")
        print("4. Find Highest Cost Expense")
        print("5. Exit Application")
        print("==========================================")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            find_highest_expense()
        elif choice == "5":
            print("\nSafely saving transactional records. Goodbye!")
            break
        else:
            print("Invalid tracking index selection! Pick a number between 1 and 5.")

main_tracker_menu()


# 11
# Mini Authentication System

# Create a small application supporting

# predefined username/password

# maximum login attempts

# successful login

# failed login

# logout

# retry logic

# Use functions and loops appropriately.
# System configurations
PREDEFINED_USERNAME = "admin"
PREDEFINED_PASSWORD = "SecurePassword123"
MAX_ATTEMPTS = 3

# Application tracking states
is_logged_in = False
failed_attempts = 0

def login():
    """Handles credential validation, tracking thresholds, and security states."""
    global is_logged_in, failed_attempts
    
    # Check if a user is already authenticated
    if is_logged_in:
        print("\n⚠️ Notification: A user is already logged in. Please log out first.")
        return

    # Check if system has exhausted max attempts
    if failed_attempts >= MAX_ATTEMPTS:
        print(f"\n🚨 Access Denied: Account locked due to {MAX_ATTEMPTS} failed attempts.")
        print("Please contact system administrators.")
        return

    print("\n--- 🔐 System Login ---")
    username_input = input("Enter Username: ").strip()
    password_input = input("Enter Password: ").strip()

    # Credential evaluation check
    if username_input == PREDEFINED_USERNAME and password_input == PREDEFINED_PASSWORD:
        print(f"\n✨ Success: Welcome back, {PREDEFINED_USERNAME}! Login successful.")
        is_logged_in = True
        failed_attempts = 0  # Reset counter upon safe clearance
    else:
        failed_attempts += 1
        remaining = MAX_ATTEMPTS - failed_attempts
        print("\n❌ Error: Invalid username or password.")
        
        if remaining > 0:
            print(f"🔄 Retry Logic: You have {remaining} attempt(s) remaining.")
        else:
            print("🚨 Security Warning: Maximum attempts exceeded. Dashboard locked down.")

def logout():
    """Safely terminates the active user session loop."""
    global is_logged_in
    if not is_logged_in:
        print("\n⚠️ Notification: No user is currently logged in.")
    else:
        is_logged_in = False
        print("\n🚪 Success: You have logged out safely.")

def view_dashboard():
    """A sample protected area only accessible to verified accounts."""
    if not is_logged_in:
        print("\n🔒 Access Denied: You must be logged in to view secure system content.")
    else:
        print(f"\n--- 📊 Welcome to the Secure Admin Panel ({PREDEFINED_USERNAME}) ---")
        print("System status: Optimal")
        print("Database sync: 100% complete")
        print("-------------------------------------------------")


def main_auth_menu():
    """Main application manager driven by a continuous while loop."""
    while True:
        print("\n==========================================")
        print("        MINI AUTHENTICATION SYSTEM        ")
        print("==========================================")
        print(f"Status: [{'CONNECTED as ' + PREDEFINED_USERNAME if is_logged_in else 'LOCKED / DISCONNECTED'}]")
        print("------------------------------------------")
        print("1. Log In")
        print("2. Log Out")
        print("3. View Protected Dashboard")
        print("4. Exit Application")
        print("==========================================")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            login()
        elif choice == "2":
            logout()
        elif choice == "3":
            view_dashboard()
        elif choice == "4":
            print("\nTerminating background authentication loops. Goodbye!")
            break
        else:
            print("Invalid input! Please select a valid option between 1 and 4.")

main_auth_menu()

# 12
# Super30 Python Utility Application

# Create your own menu-driven application containing at least five utilities.

# Examples

# Calculator

# Palindrome checker

# Prime checker

# Factorial calculator

# Multiplication table

# Number analyzer

# Password checker

# Students are encouraged to add their own features.
import math

# ----------------- UTILITY FUNCTIONS -----------------

def check_palindrome():
    """Utility 1: Normalises and checks if a string reads the same backwards."""
    print("\n--- 🔄 Palindrome Checker ---")
    text = input("Enter a string or sentence: ").strip()
    
    # Clean the text: alphanumeric characters only, converted to lowercase
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    
    if not cleaned:
        print("Error: Input must contain alphanumeric characters.")
        return

    if cleaned == cleaned[::-1]:
        print(f"✨ Success! \"{text}\" is a palindrome.")
    else:
        print(f"❌ \"{text}\" is NOT a palindrome.")

def check_prime():
    """Utility 2: Checks if a positive whole number is prime."""
    print("\n--- 🔢 Prime Number Checker ---")
    try:
        num = int(input("Enter an integer to check: "))
        if num <= 1:
            print(f"❌ {num} is not a prime number (primes must be greater than 1).")
            return
            
        # Optimization: Only check factors up to the square root of the number
        is_prime = True
        for i in range(2, int(math.isqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
                
        if is_prime:
            print(f"✨ Success! {num} is a PRIME number.")
        else:
            print(f"❌ {num} is a composite number (not prime).")
    except ValueError:
        print("Error: Please enter a valid whole integer.")

def calculate_factorial():
    """Utility 3: Computes the product of all integers up to n."""
    print("\n--- ✖️ Factorial Calculator ---")
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
            return
            
        result = math.factorial(num)
        print(f"✨ Result: {num}! = {result:,}")
    except ValueError:
        print("Error: Please enter a valid whole integer.")

def generate_multiplication_table():
    """Utility 4: Generates a multiplication grid up to a customizable limit."""
    print("\n--- 📋 Multiplication Table Generator ---")
    try:
        target = int(input("Enter the base number: "))
        limit = int(input("Enter the maximum range limit (e.g., 10 or 12): "))
        
        if limit <= 0:
            print("Error: The range limit must be greater than zero.")
            return
            
        print(f"\n--- Multiplication Grid for {target} ---")
        for i in range(1, limit + 1):
            print(f"{target} x {i:<2} = {target * i}")
    except ValueError:
        print("Error: Inputs must be valid whole integers.")

def analyze_password_strength():
    """Utility 5 (Custom Feature): Runs a character complexity check on a string."""
    print("\n--- 🔐 Password Security Strength Analyzer ---")
    password = input("Enter a password to evaluate: ").strip()
    
    # Tracking criteria metrics
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    is_long = len(password) >= 8
    
    score = sum([has_upper, has_lower, has_digit, has_special, is_long])
    
    print(f"\nAnalysis Summary (Length: {len(password)} characters):")
    print(f"  - Length >= 8 chars:  {'✅' if is_long else '❌'}")
    print(f"  - Capital Letters:    {'✅' if has_upper else '❌'}")
    print(f"  - Lowercase Letters:  {'✅' if has_lower else '❌'}")
    print(f"  - Numeric Digits:     {'✅' if has_digit else '❌'}")
    print(f"  - Special Characters: {'✅' if has_special else '❌'}")
    
    # Score evaluation
    if score == 5:
        print("🛡️ Security Verdict: STRONG PASSWORD")
    elif score >= 3:
        print("⚠️ Security Verdict: MEDIUM PASSWORD (Could be improved)")
    else:
        print("🚨 Security Verdict: WEAK PASSWORD (Highly vulnerable)")


# ----------------- MAIN MENU CONTROLLER -----------------

def run_utility_suite():
    """Core driver layout handling navigation flow loop loops."""
    while True:
        print("\n==========================================")
        print("        🚀 MULTI-UTILITY PLATFORM         ")
        print("==========================================")
        print("1. Palindrome Checker")
        print("2. Prime Number Checker")
        print("3. Factorial Calculator")
        print("4. Multiplication Table Generator")
        print("5. Password Security Strength Analyzer")
        print("6. Exit Program")
        print("==========================================")
        
        choice = input("Select an application option (1-6): ").strip()
        
        if choice == "1":
            check_palindrome()
        elif choice == "2":
            check_prime()
        elif choice == "3":
            calculate_factorial()
        elif choice == "4":
            generate_multiplication_table()
        elif choice == "5":
            analyze_password_strength()
        elif choice == "6":
            print("\nShutting down utilities safely. Goodbye!")
            break
        else:
            print("Invalid input! Please select a valid tracking option between 1 and 6.")

run_utility_suite()

# Submission Guidelines