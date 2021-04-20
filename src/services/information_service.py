from repositories.save_repository import (
    save_repository as default_save_repository)


class InformationService:
    def __init__(self, save_repository=default_save_repository):
        self._save = None
        self._save_repository = save_repository

    def create_new_save(self, nickname):
        self._save = self._save_repository.create(nickname)

    def open_save(self, save_id):
        self._save = self._save_repository.find_by_id(save_id)

    def update_save(self, progress, save_id):
        self._save_repository.update(progress, save_id)
        self.open_save(save_id)

    def get_save(self):
        return self._save

    def close_save(self):
        self._save = None

    def get_progress_information(self):
        return self._save.get_information()

    def list_saves(self):
        return self._save_repository.find_all_saves()
