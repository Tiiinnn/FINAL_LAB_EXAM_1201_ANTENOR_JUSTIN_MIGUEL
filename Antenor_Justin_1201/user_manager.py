import os
import pickle
import re 
from user import User

class UserManager:
    data_folder = "data"
    users_file = os.path.join(data_folder, "users.pkl")

    def __init__(self):
        self.load_users()
        
    def load_users(self):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
        if not os.path.exists(self.users_file):
            self.users = []
        else:
            with open(self.users_file, "rb") as f:
                self.users = pickle.load(f)

    def save_users(self):
        with open(self.users_file, "wb") as f:
            pickle.dump(self.users, f)

    def validate_username(self, username):
        if not re.match(r"^[a-zA-Z0-9_]{4,}$", username):
            raise ValueError("Username must be at least 4 characters long and contain only letters, numbers, and underscores.")
        if any(user.username == username for user in self.users):
            raise ValueError("Username already exists.")
        return True

    def validate_password(self, password):
        if not re.match(r"^[a-zA-Z0-9_]{8,}$", password):
            raise ValueError("Password must be at least 8 characters long and contain only letters, numbers, and underscores.")
        return True

    def register(self, username, password):
        try:
            if self.validate_username(username) and self.validate_password(password):
                self.users.append(User(username, password))
                self.save_users()
                return True
            else:
                return False
        except ValueError as e:
            print(f"Registration failed: {e}")
            return False

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None