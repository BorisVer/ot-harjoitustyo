import os

class TopScore:
    def __init__(self):
        self.data_dir = os.path.join("src", "data")
        self.top_score_file = os.path.join(self.data_dir, "top_score.txt")

    def file_exists(self):
        os.makedirs(self.data_dir, exist_ok=True)

        if not os.path.exists(self.top_score_file):
            with open(self.top_score_file, "w", encoding="utf-8") as f:
                f.write("0")

    def load_top_score(self):
        with open(self.top_score_file, "r", encoding="utf-8") as f:
            return int(f.read().strip())

    def save_top_score(self, score):
        with open(self.top_score_file, "w", encoding="utf-8") as f:
            f.write(str(score))
