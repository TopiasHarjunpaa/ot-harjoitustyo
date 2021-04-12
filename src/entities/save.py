from settings import NUMBER_OF_LEVELS

# TODO: Needs some rethinking...


class Save:

    def __init__(self, nickname, progress, created_at):
        self.nickname = nickname
        self.progress = progress
        self.created_at = created_at

    def get_information(self):
        # TODO: Clean up the logic.
        progress = {}
        levels_completed = self.progress // 100
        progress["levels_completed"] = levels_completed
        level = 1
        while level <= levels_completed:
            progress[f"level{level}"] = "100%"
            progress[f"unlocked{level}"] = True
            level += 1
        if level <= NUMBER_OF_LEVELS:
            progress[f"level{level}"] = f"{self.progress - (levels_completed * 100)}%"
            progress[f"unlocked{level}"] = True
            level += 1
            while level <= NUMBER_OF_LEVELS:
                progress[f"level{level}"] = "0%"
                progress[f"unlocked{level}"] = False
                level += 1
        progress["nickname"] = self.nickname
        progress["created_at"] = self.created_at
        progress["progress"] = f"{self.progress}%"
        progress["number_of_levels"] = NUMBER_OF_LEVELS
        return progress
