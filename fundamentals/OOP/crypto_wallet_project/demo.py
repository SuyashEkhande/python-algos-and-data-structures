import json
import os

project_dir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(project_dir, "data.json")

# Check if the file exists and create it if not
if not os.path.exists(db_file):
    print(f"File {db_file} not found. Creating it now...")
    with open(db_file, "w") as file:
        # Initialize with an empty dictionary
        json.dump({"users": []}, file, indent=4)
    print(f"{db_file} created successfully.")
else:
    print(f"File {db_file} already exists.")

# Sample data to write into the file
data_to_write = {
    "users": [
        {"user_id": 1, "username": "Alice", "email": "alice@example.com"},
        {"user_id": 2, "username": "Bob", "email": "bob@example.com"}
    ]
}

# Writing data to the JSON file
try:
    with open(db_file, "w") as file:
        json.dump(data_to_write, file, indent=4)
    print(f"Data successfully written to {db_file}")
except Exception as e:
    print(f"Error writing to file: {e}")
