"""
 Encapsulation is one of the four fundamental principles of 
 object-oriented programming (OOP). It refers to the practice 
 of hiding the internal state of an object and only exposing a 
 controlled interface (methods) through which the state can be accessed 
 or modified. This helps to ensure that the internal workings of an object
 are protected from unintended modifications and that the object maintains a 
 consistent state.
"""

class CryptoWallet:
    def __init__(self, wallet_owner, initial_balance):
        # Private attributes (encapsulated) - 
        # prefix _ for "private" - access within class 
        # prefix __ for "protected - access within subclasses"
        self.__wallet_owner = wallet_owner
        self.__balance = initial_balance

    # Getter method for balance
    def get_balance(self):
        return self.__balance
    
    #Setter method for balance with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")

    # Setter method for balance with validation
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance")
    
    # Method to show account details - 
    # interface for users to access private attributes
    def wallet_details(self):
        print(f"Wallet Owner: {self.__wallet_owner}")
        print(f"Balance: {self.__balance}")


# Create a wallet object
wallet = CryptoWallet("Elon Musk", 0)

#Accessing private attributes directly (this will raise an error)
# - print(wallet.__wallet_owner)

# Accessing private attributes through Getter/Setter methods
wallet.wallet_details()
wallet.deposit(1000)
wallet.withdraw(500)
wallet.wallet_details()

print("----------")
wallet.deposit(-100)
wallet.withdraw(1000000)
# Using getter method to access the balance
print(f"Balance: {wallet.get_balance()}")

