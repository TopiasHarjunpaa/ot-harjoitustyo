from config import NUMBER_OF_LEVELS


class Save:
    """A class to represent save object and hold the information.

    Attributes:
        save_id: Unique id number.
        nickname: Name of the save object.
        progress: Corresponds progress level of the game.
        created_at: Timestamp when save has been created.
    """

    def __init__(self, save_id, nickname, progress, created_at):
        """Constructs all the necessary attributes for the save object.

        Args:
            save_id (int): Unique id number.
            nickname (str): Name of the save object.
            progress (int): Corresponds progress level of the game.
            created_at (date): Timestamp when save has been created.
        """

        self.save_id = save_id
        self.nickname = nickname
        self.progress = progress
        self.created_at = created_at

    def get_information(self):
        """Calculates and wraps all necessary information from the save object.

        Returns:
            progress (dict): A dictionary of all information from the save object.
        """

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
        progress["id"] = self.save_id
        progress["nickname"] = self.nickname
        progress["created_at"] = self.created_at
        progress["progress"] = self.progress
        progress["number_of_levels"] = NUMBER_OF_LEVELS
        return progress
