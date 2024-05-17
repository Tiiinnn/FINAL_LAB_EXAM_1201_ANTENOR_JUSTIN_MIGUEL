import os
import random
from score_manager import ScoreManager

class DiceGame:
    def __init__(self, user_manager, score_manager):
        self.user_manager = user_manager
        self.score_manager = score_manager
        self.current_user = None

    def play_stage(self):
        user_rounds_won = 0
        cpu_rounds_won = 0
        while user_rounds_won < 3 and cpu_rounds_won < 3:
            user_roll = random.randint(1, 6)
            cpu_roll = random.randint(1, 6)
            print(f"You rolled a {user_roll}. CPU rolled a {cpu_roll}.")
            if user_roll > cpu_roll:
                user_rounds_won += 1
            elif cpu_roll > user_roll:
               cpu_rounds_won += 1
            else:
                print("It's a tie, rolling again.")

        return user_rounds_won, cpu_rounds_won

    def play_game(self):
        if self.current_user is None:
            print("Please log in to play a game.")
            return

        total_points = 0
        stages_won = 0

        while True:
            print(f"Starting stage {stages_won + 1}.")
            user_rounds_won, cpu_rounds_won = self.play_stage()
            if user_rounds_won == 3:
                stages_won += 1
                total_points += 6 # 1 point for each round win, 3 points for stage win
                print(f"Stage {stages_won} won. Total points: {total_points}.")
                self.score_manager.save_score(self.current_user.username, total_points, stages_won)
                while True:
                    choice = input("Do you want to proceed to the next stage? (1 for yes, 0 for no): ").strip()
                    if choice == '1':
                        break
                    elif choice == '0':
                        return  # Return to the main function
                    else:
                        print("Invalid choice. Please enter 1 to continue or 0 to stop.")
            else:
                print("Game over. You didn't win any stages.")
                return  # Return to the main function

    def view_scores(self):
        scores = self.score_manager.get_top_scores()
        print("Top 10 Scores:")
        for i, score in enumerate(scores):
            print(f"{i+1}. {score['username']} - {score['total_points']} points, {score['stages_won']} stages won")