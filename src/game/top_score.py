import os

class TopScore:
    """
    Manages the top score of the game in a file

    Updates the file if score is broken, gets current highscore
    and creates the required directory and file if they dont exist yet
    """
    def __init__(self):
        """
        Initializes the pathes to the directory and file"""
        self.data_dir = os.path.join("src", "data")
        self.top_score_file = os.path.join(self.data_dir, "top_score.txt")

    def file_exists(self):
        """
        Checks if the directory and file exist, creates them if not

        Only run the first time the user launches game after download
        or if the file or directory is deleted
        """
        os.makedirs(self.data_dir, exist_ok=True)

        if not os.path.exists(self.top_score_file):
            with open(self.top_score_file, "w", encoding="utf-8") as f:
                f.write("0")

    def load_top_score(self):
        """
        Gets the current highscore from the file

        Returns:
            int: The current highscore
        """
        with open(self.top_score_file, "r", encoding="utf-8") as f:
            return int(f.read().strip())

    def save_top_score(self, score):
        """
        Overwrites the previous highscore with the new one

        Args:
            score: The new highscore to be saved
        """
        with open(self.top_score_file, "w", encoding="utf-8") as f:
            f.write(str(score))
