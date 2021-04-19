import unittest
from repositories.save_repository import save_repository
from entities.save import Save


class TestSaveRepository(unittest.TestCase):
    def setUp(self):
        save_repository.delete()
        self.nicknames = ["TOTO", "ASWD", "TEST"]

    def test_create_save(self):
        for i in range(len(self.nicknames)):
            save_repository.create(self.nicknames[i])
        saves = save_repository.find_all_saves()

        self.assertEqual(len(saves), 3)
        self.assertEqual(saves[0].nickname, self.nicknames[0])
        self.assertEqual(sum([save.id for save in saves]), 6)

    def test_find_saves_by_id(self):
        for i in range(len(self.nicknames)):
            save_repository.create(self.nicknames[i])

        user_one = save_repository.find_by_id(1)
        user_none = save_repository.find_by_id(10)

        self.assertEqual(user_one.nickname, self.nicknames[0])
        self.assertEqual(user_none, None)

    def test_delete(self):
        pass
