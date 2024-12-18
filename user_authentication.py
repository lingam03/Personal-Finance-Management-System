# user_authentication.py

import json
import os

USER_DATA_FILE = "user_data.json"

# Load user data from a file
def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Save user data to a file
def save_users(users):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file)

# Load users at the start of the program
users = load_users()

# Sign-up function
def sign_up(username, password):
    if username in users:
        print("Username already exists.")
    else:
        users[username] = password
        save_users(users)  # Save updated users
        print("User signed up successfully.")

# Log-in function
def log_in(username, password):
    if username in users and users[username] == password:
        print("Logged in successfully.")
        return True
    else:
        print("Invalid username or password.")
        return False
