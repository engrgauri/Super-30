# Create a simplified banking application.
# Create a BankAccount class containing account holder name, account number, and balance. 
# Implement deposit(), withdraw(), check_balance(), and display_account_details().
# Use a class variable for the bank name and a class method that can change the bank name for every account.
# Add validation so that a user cannot withdraw more money than available.

# Bonus: Keep track of the total number of bank accounts created.
class BankAccount:

    bank_name = "French Bank"

    def __init__(self,name,acct_no,balance):
        self.name = name
        self.acct_no = acct_no
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance +amount
        print("Amount Deposited. New balance is : ",self.balance)

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Balance. Current Balance is :",self.balance)
        else:
            self.balance = self.balance -amount
            print("Amount Withdrawn. New Balance is : ",self.balance)

    def check_balance(self):
        print("Current Account Balance is :",self.balance)

    def display_account_details(self):
        print("Account holder Name : ",self.name)
        print("Account Number : ", self.acct_no)
        print("Account Balance : ",self.balance)

    @classmethod
    def change_bank_name(cls, new_bank_name):
        cls.bank_name = new_bank_name
        print(f"Bank name has been updated to: {cls.bank_name}")

# --- Demonstration ---
# Create a bank account
acc1 = BankAccount("Alice Smith", "10015520", 500.0)

# Display initial details
acc1.display_account_details()

# Deposit and withdraw funds
acc1.deposit(150.0)
acc1.withdraw(200.0)

# Attempt to withdraw more than the balance (validation test)
acc1.withdraw(1000.0)

# Check balance
acc1.check_balance()

# Change bank name using the class method
BankAccount.change_bank_name("First National Bank")

# Verify the bank name change applies to the account
acc1.display_account_details()