from repositories.save_repository import (
    save_repository as default_save_repository)


class InformationService:
    """A class to represent information services.

    Information service updates and gets information from active save object.
    Save object is created and updated through save repository object.

    Attributes:
        save_repository: Save repository object.
    """

    def __init__(self, save_repository=default_save_repository):
        """Constructs save repository object for information service.

        Args:
            save_repository (SaveRepository, optional): Defaults to default_save_repository.
        """

        self._save = None
        self._save_repository = save_repository

    def create_new_save(self, nickname):
        """Creates new save into database and updates save object.

        Args:
            nickname (str): Name of the save object.
        """

        self._save = self._save_repository.create(nickname)

    def open_save(self, save_id):
        """Finds save from the database according to save id and updates save object.

        Args:
            save_id (int): Unique id number.
        """

        self._save = self._save_repository.find_by_id(save_id)

    def update_save(self, progress, save_id):
        """Updates existing save at the database and updates save object.

        Args:
            progress (int): Corresponds progress level of the game.
            save_id (int): Unique id number.
        """

        self._save_repository.update(progress, save_id)
        self.open_save(save_id)

    def get_save(self):
        """Returns current save object.

        Returns:
            save (Save): Returns save object.
        """

        return self._save

    def close_save(self):
        """Closes current saves and updates current save object to None type object.
        """

        self._save = None

    def get_progress_information(self):
        """Gets progress information from the save object.

        Returns:
            progress (dict): A dictionary of all information from the save object.
        """

        return self._save.get_information()

    def list_saves(self, number_of_saves=1000):
        """Finds certain number of saves from the database sorted by highest progress.

        Args:
            number_of_saves (int, optional): Number of needed saves. Defaults to 1000.

        Returns:
            save_list (list): Returns list of save objects.
        """

        return self._save_repository.find_and_sort_saves(number_of_saves)

    def get_top_records(self, number_of_records):
        """Get top records from the database.

        Fill remaining slots with text EMPTY if there are no enough saves in the database.

        Args:
            number_of_records (int): Number of needed records

        Returns:
            list: Returns list of records with nickname and score.
        """

        saves = self.list_saves(number_of_records)
        records = []
        for save in saves:
            record_info = f"{save.nickname} - SCORE: {save.progress}%"
            records.append(record_info)
        empty_slots = number_of_records - len(records)
        while empty_slots > 0:
            records.append("EMPTY")
            empty_slots -= 1
        return records
