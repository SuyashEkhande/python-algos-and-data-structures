from Database import Database
import uuid


class User:
    """Represents a User in the crypto wallet system"""

    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
    
    @classmethod
    def create(cls, username, email):
        """Creates a new user and add to the database"""
        data = Database.load_data()
        user_id = str(uuid.uuid4())  # Generate a unique UUID for the user
        user = cls(user_id, username, email)
        data["users"].append(user.to_dict())
        Database.save_data(data)
        return user
    
    def to_dict(self):
        """Convert User object to dictionary"""
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email
        }

    @classmethod
    def get_user_by_id(cls, user_id):
        """Retrieve user by user_id"""
        data = Database.load_data()
        for user_data in data["users"]:
            if user_data["user_id"] == user_id:
                return cls(**user_data) # creates runtime object of the data
        return None
    

