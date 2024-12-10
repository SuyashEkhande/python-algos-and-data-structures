from Database import Database
import uuid

class Wallet:
    """Represents a crypto wallet associated with a User."""

    def __init__(self, wallet_id, user_id, coin_type="Bitcoin", balance=0):
        self.wallet_id = wallet_id
        self.user_id = user_id
        self.coin_type = coin_type
        self.balance = balance
    
    @classmethod
    def create_wallet(cls, user_id, coin_type="Bitcoin"):
        """Create a new wallet for a user."""
        data = Database.load_data()
        wallet_id = str(uuid.uuid4())  # Generate a unique UUID for the wallet
        wallet = cls(wallet_id, user_id, coin_type)
        data["wallets"].append(wallet.to_dict())
        Database.save_data(data)
        return wallet
    
    @classmethod
    def get_wallet_by_user_id(cls, user_id, coin_type):
            """Fetch wallet for a user from the saved data."""
            data = Database.load_data()
            for wallet in data["wallets"]:
                if wallet["user_id"] == user_id and wallet["coin_type"] == coin_type:
                    return Wallet(wallet["wallet_id"], wallet["user_id"], wallet["coin_type"], wallet["balance"])
            return None

    def to_dict(self):
        """Convert Wallet object to dictionary"""
        return {
            "wallet_id": self.wallet_id,
            "user_id": self.user_id,
            "coin_type": self.coin_type,
            "balance": self.balance
        }
    
    def check_balance(self):
        """Check the current balance of the wallet."""
        return self.balance
    
    def deposit(self, amount):
        """Deposit an amount into the wallet."""
        if amount > 0:
            self.balance += amount
            # Save updated wallet data to the JSON file
            self._save_wallet_data()
            return True
        return False

    def withdraw(self, amount):
        """Withdraw an amount from the wallet."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            # Save updated wallet data to the JSON file
            self._save_wallet_data()
            return True
        return False
    
    def _save_wallet_data(self):
        """Helper function to save the updated wallet data to the JSON file."""
        data = Database.load_data()
        # Find the wallet by wallet_id and update its balance
        for wallet_data in data["wallets"]:
            if wallet_data["wallet_id"] == self.wallet_id:
                wallet_data["balance"] = self.balance
        Database.save_data(data)
    