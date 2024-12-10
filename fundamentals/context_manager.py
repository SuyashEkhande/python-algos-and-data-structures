"""
Context managers are used to manage resources that need to be 
set up and cleaned up properly. The `__enter__` method is called 
when entering the `with` block, allowing for resource initialization, 
and the `__exit__` method handles cleanup, even if an exception 
occurs. This ensures that resources like file handles, network 
connections, or locks are reliably released after use, preventing 
resource leaks and improving error handling.
"""

class CryptoWallet:
    def __init__(self, balance):
        self.balance = balance
    
    def __enter__(self):
        print("Opening the crypto wallet")
        # Simulating some setup like connecting to the blockchain
        self.wallet_connection = "Connected to Blockchain"
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing the crypto wallet")
        # Simulating some cleanup like disconnecting from the blockchain
        self.wallet_connection = None
        if exc_type:
            print(f"""Error occurred: {exc_value}""")
        return True
    
    def check_balance(self):
        print(f"Balance: {self.balance} BTC")

    def withdraw_transaction(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Transaction successful. New balance: {self.balance} BTC")
    

# Simulating a crypto wallet transaction with context management

try:
    with CryptoWallet(5) as wallet: # Start with 5 BTC in the wallet
        wallet.check_balance() # Check the balance
        wallet.withdraw_transaction(2) # Perform a transaction of 2 BTC
        wallet.check_balance() # Check the balance
        wallet.withdraw_transaction(10) # Error
except Exception as e:
    print(f"Error: {e}")
