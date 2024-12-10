from User import User
from Wallet import Wallet
from Transaction import Transaction
from Database import Database

# Initialize by creating users
user1 = User.create("Alice", "alice@example.com")
user2 = User.create("Bob", "bob@example.com")

# Create wallets for the users
wallet1 = Wallet.create_wallet(user1.user_id, "Bitcoin")
wallet2 = Wallet.create_wallet(user2.user_id, "Bitcoin")

# Deposit some funds to wallet1 and wallet2
wallet1.deposit(100)
wallet2.deposit(100)

# Check balances before deletion
print(f"{user1.username}'s Wallet Balance: {wallet1.check_balance()} {wallet1.coin_type}")
print(f"{user2.username}'s Wallet Balance: {wallet2.check_balance()} {wallet2.coin_type}")

# Transfer between wallets
transaction = Transaction.transfer_between_wallets(user1.user_id, user2.user_id, 50)

if transaction:
    print(f"\nTransaction successful: {transaction['withdrawal'].amount} withdrawn from {user1.username}'s wallet.")
    print(f"Transaction successful: {transaction['deposit'].amount} deposited to {user2.username}'s wallet.")

# Reload wallet data from JSON to get updated balances
wallet1 = Wallet.get_wallet_by_user_id(user1.user_id, "Bitcoin")
wallet2 = Wallet.get_wallet_by_user_id(user2.user_id, "Bitcoin")

# Print the final balances after the transaction
print(f"\nFinal Balances:")
print(f"{user1.username}'s Wallet Balance: {wallet1.check_balance()} {wallet1.coin_type}")
print(f"{user2.username}'s Wallet Balance: {wallet2.check_balance()} {wallet2.coin_type}")


