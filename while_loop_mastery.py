# Understand condition-controlled iteration and learn where while is more appropriate than for.

# Questions

# Print numbers from 1 to 100 using while.
i = 1
num = 100
while i <= num:
    print(i)
    i = i+1
# Print numbers from 100 to 1.
i = 1
num = 100
while num >= i:
    print(num)
    num = num-1
# Print all even numbers between 1 and 100.
i = 0 
num = 100
while i <= num:
    if i % 2 == 0:
        print(i)
    i = i+1
# Calculate the sum of digits of a number.

# Example

number= 5832
digit_sum = 0
    
    # Loop continues until the number becomes 0
while number > 0:
        last_digit = number % 10    # Get the last digit (e.g., 123 % 10 = 3)
        digit_sum += last_digit     # Add it to the total sum
        number = number // 10       # Remove the last digit (e.g., 123 // 10 = 12)
        
print(digit_sum)
# Output: 18

# Reverse an integer using a while loop.

# Example
#Input: 12345

# Output: 54321

number= 12345
reversed_num = 0
while number > 0:
        last_digit = number % 10          # Get the last digit
        reversed_num = (reversed_num * 10) + last_digit  # Shift total left and add digit
        number = number // 10 
print(reversed_num)            

# Count the number of digits in an integer.
num = 23213
count = 0
while num > 0 :
    last_digit = num % 10    # Get the last digit (e.g., 123 % 10 = 3)
    count = count +1
    num = num // 10
print(num)         
# Calculate factorial using while.
n = 5
result = 1
while n > 1:
        result *= n
        n -= 1
print(result)
# Create a program that repeatedly asks for numbers and stops only when the user enters 0. Display the sum of all previously entered numbers.
sum = 0
while True:
    user_input = float(input("Enter a number: "))
    if user_input == 0:
        break
    sum = sum + user_input
print(sum)
# Create a password checker that keeps asking for the password until the correct password is entered.
while True:
    user_input = input("Enter the Password: ")
    if user_input == "Passwd@123":
         break
    
# Create a guessing game where the secret number is predefined and the user keeps guessing until correct.
predefined_no = 45
while True:
    guess = int(input("Enter the Guessing No.: "))
    if guess == predefined_no :
         print("You have guessed Correct Number!!!!!")
         break
# Build a menu-driven calculator

# 1
# Add

# 2
# Subtract

# 3
# Multiply

# 4
# Divide

# 5
# Exit

# The menu should continue until the user chooses Exit.
def menu_calculator():
    while True:
        # Display the Menu
        print("\n=== Menu-Driven Calculator ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        # Check for the exit condition first
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
            
        # Verify if the choice is valid before asking for numbers
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a number from 1 to 5.")
            continue
            
        try:
            # Get numbers from the user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform operations based on selection
            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                # Handle division by zero error safely
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
                    
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

# Run the calculator
menu_calculator()

# Create an ATM menu using while where the application continues running until the user explicitly chooses Exit.
def atm_system():
    # Initial account balance
    balance = 1000.0
    
    print("Welcome to the Secure ATM System!")

    while True:
        # Display ATM Menu
        print("\n=== ATM Main Menu ===")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        # 1. Check Balance
        if choice == '1':
            print(f"\n💰 Your current balance is: ${balance:,.2f}")
            
        # 2. Deposit Money
        elif choice == '2':
            try:
                deposit_amount = float(input("\nEnter the amount to deposit: $"))
                if deposit_amount <= 0:
                    print("❌ Error: Deposit amount must be greater than zero.")
                else:
                    balance += deposit_amount
                    print(f"✅ Successfully deposited ${deposit_amount:,.2f}")
                    print(f"New balance: ${balance:,.2f}")
            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
                
        # 3. Withdraw Money
        elif choice == '3':
            try:
                withdraw_amount = float(input("\nEnter the amount to withdraw: $"))
                if withdraw_amount <= 0:
                    print("❌ Error: Withdrawal amount must be greater than zero.")
                elif withdraw_amount > balance:
                    print("❌ Error: Insufficient funds. Transaction cancelled.")
                else:
                    balance -= withdraw_amount
                    print(f"✅ Successfully withdrew ${withdraw_amount:,.2f}")
                    print(f"Remaining balance: ${balance:,.2f}")
            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
                
        # 4. Exit Application
        elif choice == '4':
            print("\nThank you for using our ATM services. Goodbye!")
            break
            
        # Handle invalid menu selections
        else:
            print("❌ Invalid selection. Please choose a number from 1 to 4.")

# Run the ATM simulation
atm_system()
