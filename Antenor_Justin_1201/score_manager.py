import os
import pickle

class ScoreManager:
    scores_file = "scores.pkl"

    def __init__(self):
        self.scores = self.load_scores()

    def load_scores(self):
        if not os.path.exists(self.scores_file):
            return []
        with open(self.scores_file, "rb") as f:
            return pickle.load(f)

    def save_scores(self):
        with open(self.scores_file, "wb") as f:
            pickle.dump(self.scores, f)

    def save_score(self, username, total_points, stages_won):
        new_score = {"username": username, "total_points": total_points, "stages_won": stages_won}
        self.scores.append(new_score)
        self.scores.sort(key=lambda x: x["total_points"], reverse=True)
        self.scores = self.scores[:10]  # Keep only the top 10 scores
        self.save_scores()

    def get_top_scores(self):
        return self.scores