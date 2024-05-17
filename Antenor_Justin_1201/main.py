import os
import sys
from user_manager import UserManager
from user import User
from dice_game import DiceGame
from score_manager import ScoreManager

def main():
    user_manager = UserManager()
    score_manager = ScoreManager()
    dice_game = DiceGame(user_manager, score_manager)

    while True:
        print("\nWelcome to the Dice Game!")
        print("1. Register")
        print("2. Login")
        print("3. Play Game")
        print("4. Show Top Scores")
        print("5. Logout")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if choice == 1:
            username = input("Enter a username (at least 4 characters): ")
            password = input("Enter a password (at least 8 characters): ")
            user_manager.register(username, password)
        elif choice == 2:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = user_manager.login(username, password)
            if user:
                dice_game.current_user = user
                print(f"Welcome, {user.username}!")
            else:
                print("Invalid username or password.")
        elif choice == 3:
            if dice_game.current_user:
                dice_game.play_game()
            else:
                print("Please log in to play a game.")
        elif choice == 4:
            dice_game.view_scores()
        elif choice == 5:
            dice_game.current_user = None
            print("Logged out.")
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()