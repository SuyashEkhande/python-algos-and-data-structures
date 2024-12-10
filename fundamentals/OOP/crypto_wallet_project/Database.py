import json
import os

class Database:
    # Path to the JSON file
    project_dir = os.path.abspath(os.path.dirname(__file__))
    db_file = os.path.join(project_dir, "crypto_db.json")

    @staticmethod
    def load_data():
        """Load data from the JSON file, or create an empty structure if the file doesn't exist."""
        # If the file doesn't exist, create it with initial empty structure
        if not os.path.exists(Database.db_file):
            Database.save_data({"wallets": [], "transactions": [], "users": []})
            return {"wallets": [], "transactions": [], "users": []}

        with open(Database.db_file, "r") as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                # In case of malformed JSON, return a fresh structure
                Database.save_data({"wallets": [], "transactions": [], "users": []})
                return {"wallets": [], "transactions": [], "users": []}

    @staticmethod
    def save_data(data):
        """Save data to the JSON file."""
        try:
            # print(f"Saving data: {data}")  # Debugging line to check what is being saved
            with open(Database.db_file, "w") as file:
                json.dump(data, file, indent=4)
                file.flush()  # Ensure data is written to the file
        except Exception as e:
            print(f"Error saving data: {e}") #Ensure data is written to the file
