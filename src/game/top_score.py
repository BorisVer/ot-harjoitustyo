import os

class TopScore:
    def __init__(self):
        self.DATA_DIR = os.path.join("src", "data")
        self.TOP_SCORE_FILE = os.path.join(self.DATA_DIR, "top_score.txt")

    def file_exists(self):
        os.makedirs(self.DATA_DIR, exist_ok=True)

        if not os.path.exists(self.TOP_SCORE_FILE):
            with open(self.TOP_SCORE_FILE, "w") as f:
                f.write("0")

    def load_top_score(self):
        with open(self.TOP_SCORE_FILE, "r") as f:
            return int(f.read().strip())

    def save_top_score(self, score):
        with open(self.TOP_SCORE_FILE, "w") as f:
            f.write(str(score))
