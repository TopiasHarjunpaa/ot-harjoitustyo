from entities.save import Save
from repositories.save_repository import (
    save_repository as default_save_repository)

# TODO: Needs some rethinking...


class InformationService:
    def __init__(self, save_repository=default_save_repository):
        self._save = None
        self._save_repository = save_repository

    def create_new_save(self, nickname):
        self._save_repository.create(nickname)
        self.open_save(nickname)

    def open_save(self, nickname):
        self._save = self._save_repository.find_by_nickname(nickname)

    def get_save(self):
        return self._save

    def close_save(self):
        self._save = None

    def get_progress_information(self):
        return self._save.get_information()

    def list_saves(self):
        return self._save_repository.find_all_saves()
