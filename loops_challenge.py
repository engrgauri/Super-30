transactions = [1200, 450, 800, 1500, 2300, 700, 100]

# calculate total transaction value without using sum().
sum = 0
for i in transactions:
    sum = sum + i
print(sum)
# From the same list, find the highest and lowest transaction without max() and min().
highest = transactions[0]
lowest = transactions[0] 
for i in transactions:
    if lowest > i :
        lowest = i
    if highest < i :
        highest = i
print(lowest , highest)        

temperatures = [32, 35, 28, 40, 38, 31, 42]

# find the average temperature.
len_list = 0
sum = 0
for i in temperatures:
    sum = sum + i 
    len_list = len_list + 1
avg = sum /len_list
print(avg)

marks = [78, 92, 45, 67, 88, 53, 99]
count_90 = 0
count_75_90 = 0
count_50_74 = 0
count_50 = 0
# count how many students scored
for i in marks:
    # 90+
    if i > 90 :
        count_90 = count_90 + 1
    # 75–89
    elif i >= 75 and i <= 89:
        count_75_90 = count_75_90 + 1
    # 50–74
    elif i >= 50 and i <= 74:
        count_50_74 = count_50_74 + 1
    # below 50
    elif i < 50 :
        count_50 = count_50 + 1
print(count_90,count_75_90,count_50_74,count_50)
# Create a simple login system with a maximum of 3 password attempts.

products = {"Laptop": 55000,"Phone": 30000,"Headphones": 2000,"Mouse": 700,"Keyboard": 1500}

# print only products costing more than ₹2,000.
for i in products.keys():
    if products[i] > 2000:
        print(products)

# Accept 10 numbers from the user and store them in a list using a loop.
num_list = []
for i in range(0,10):
    num = input("Enter the number..")
    num_list.append(num)
print(num_list)
# Count the frequency of every character in a string without using Counter.
# banana
# b -> 1
# a -> 3
# n -> 2

string = "banana"
count_dict = {}
for char in string:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1

print(count_dict)

# Find the second-largest number in a list without using sort().
lst = [2, 4, 1, 4, 2, 3, 36, 7]

# Initialize to negative infinity to handle any number scale safely
largest = float('-inf')
second_largest = float('-inf')

for num in lst:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("Second Largest Number:", second_largest)

# Check whether a string is a palindrome using loops.
string = "radar"

cleaned_string = string.lower()

is_palindrome = True
length = len(cleaned_string)

for i in range(length // 2):
    if cleaned_string[i] != cleaned_string[length - 1 - i]:
        is_palindrome = False
        break  

if is_palindrome:
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
# Create this number pattern

# 1
# 12
# 123
# 1234
# 12345
for i in range (1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
# Create a basic ATM simulation where a user can repeatedly
# Check balance
# Deposit money
# Withdraw money
# Exit

# 1. Initialize the starting balance
balance = 1000.0

print("=== Welcome to the Python ATM ===")

# 2. Run an infinite loop to keep the simulation going
while True:
    print("\n--- Main Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    # Accept the user's choice
    choice = input("Please choose an option (1-4): ")
    
    # Option 1: Check Balance
    if choice == "1":
        print(f"\nYour current balance is: ${balance:,.2f}")
        
    # Option 2: Deposit Money
    elif choice == "2":
        amount = float(input("\nEnter the amount to deposit: $"))
        if amount > 0:
            balance += amount
            print(f"Successfully deposited ${amount:,.2f}. New balance: ${balance:,.2f}")
        else:
            print("Invalid amount. You must deposit more than $0.")
            
    # Option 3: Withdraw Money
    elif choice == "3":
        amount = float(input("\nEnter the amount to withdraw: $"))
        if amount > balance:
            print(f"Transaction Declined! Insufficient funds. Your balance is ${balance:,.2f}")
        elif amount <= 0:
            print("Invalid amount. You must withdraw more than $0.")
        else:
            balance -= amount
            print(f"Successfully withdrew ${amount:,.2f}. Remaining balance: ${balance:,.2f}")
            
    # Option 4: Exit the ATM
    elif choice == "4":
        print("\nThank you for using our ATM. Goodbye!")
        break  # Breaks the loop to exit the program
        
    # Handle invalid menu inputs
    else:
        print("Invalid choice. Please select a valid option from the menu (1-4).")



