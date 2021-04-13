from settings import NUMBER_OF_LEVELS


class Save:

    def __init__(self, id, nickname, progress, created_at):
        self.id = id
        self.nickname = nickname
        self.progress = progress
        self.created_at = created_at

    def get_information(self):
        # TODO: Clean up the logic. Maybe ditch the logic here and just pass the params.
        progress = {}
        levels_completed = self.progress // 100
        progress["levels_completed"] = levels_completed
        level = 1
        while level <= levels_completed:
            progress[f"level{level}"] = 100
            progress[f"unlocked{level}"] = True
            level += 1
        if level <= NUMBER_OF_LEVELS:
            progress[f"level{level}"] = self.progress - \
                (levels_completed * 100)
            progress[f"unlocked{level}"] = True
            level += 1
            while level <= NUMBER_OF_LEVELS:
                progress[f"level{level}"] = 0
                progress[f"unlocked{level}"] = False
                level += 1
        progress["id"] = self.id
        progress["nickname"] = self.nickname
        progress["created_at"] = self.created_at
        progress["progress"] = self.progress
        progress["number_of_levels"] = NUMBER_OF_LEVELS
        return progress
