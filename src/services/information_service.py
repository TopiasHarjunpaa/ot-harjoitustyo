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

    def list_saves(self):
        """Finds 8 saves from the database sorted by highest progress.

        Returns:
            save_list (list): Returns list of save objects.
        """
        return self._save_repository.find_all_saves()
