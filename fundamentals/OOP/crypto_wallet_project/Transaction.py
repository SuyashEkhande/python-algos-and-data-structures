import uuid
from Database import Database
import datetime as dt
from Wallet import Wallet

class Transaction:
    """Represents a Transaction made on the wallet.""" 
    def __init__(self, transaction_id, wallet_id, amount, transaction_type, date):
        self.transaction_id = transaction_id
        self.wallet_id = wallet_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = date

    @classmethod
    def create_transaction(cls, wallet_id, amount, transaction_type):
        """Create a new transaction (deposit or withdrawal)"""
        data = Database.load_data()
        transaction_id = str(uuid.uuid4())  # Generate a unique UUID for the user
        date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = cls(transaction_id, wallet_id, amount, transaction_type, date)
        data["transactions"].append(transaction.to_dict())
        Database.save_data(data)
        return transaction
    
    @classmethod
    def transfer_between_wallets(cls, from_wallet_id, to_wallet_id, amount):
        """Transfer coins between two wallets."""
        # Retrieve wallet instances using wallet_id
        from_wallet = Wallet.get_wallet_by_user_id(from_wallet_id, "Bitcoin")
        to_wallet = Wallet.get_wallet_by_user_id(to_wallet_id, "Bitcoin")

        if from_wallet is None or to_wallet is None:
            print("One or both wallets not found.")
            return None
        
        if from_wallet.check_balance() < amount:
            print(f"from wallet id: {from_wallet.wallet_id} with balance: {from_wallet.balance}")
            print("Insufficient balance in the sender's wallet.")
            return None
        
        # Create withdrawal transaction from sender's wallet
        withdrawal_transaction = cls.create_transaction(from_wallet.wallet_id, amount, "Withdrawal")
        from_wallet.withdraw(amount)

        # Create deposit transaction in receiver's wallet
        deposit_transaction = cls.create_transaction(to_wallet.wallet_id, amount, "Deposit")
        to_wallet.deposit(amount)

        return {"withdrawal": withdrawal_transaction, "deposit": deposit_transaction}

    def to_dict(self):
        """Convert Transaction object to dictionary."""
        return {
            "transaction_id": self.transaction_id,
            "wallet_id": self.wallet_id,
            "amount": self.amount,
            "transaction_type": self.transaction_type,
            "date": self.date
        }