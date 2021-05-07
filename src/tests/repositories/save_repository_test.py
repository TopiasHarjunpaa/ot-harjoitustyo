import unittest
from repositories.save_repository import save_repository
from entities.save import Save


class TestSaveRepository(unittest.TestCase):
    def setUp(self):
        save_repository.delete()
        self.nicknames = ["TOTO", "ASWD", "TEST"]
        self.updates = [400, 100, 10]
        self.mixed_updates = [100, 10, 400]

    def test_create_save(self):
        for i in range(len(self.nicknames)):
            save_repository.create(self.nicknames[i])
        saves = save_repository.find_and_sort_saves()

        self.assertEqual(len(saves), 3)
        self.assertEqual(saves[0].nickname, self.nicknames[0])
        self.assertEqual(saves[0].progress, 0)
        self.assertEqual(sum([save.save_id for save in saves]), 6)

    def test_update_save(self):
        for i in range(len(self.nicknames)):
            save_repository.create(self.nicknames[i])
        saves = save_repository.find_and_sort_saves()
        for i, save in enumerate(saves):
            save_repository.update(self.updates[i], save.save_id)
        saves = save_repository.find_and_sort_saves()

        self.assertEqual(saves[0].progress, self.updates[0])
        self.assertNotEqual(saves[1].progress, 0)

    def test_find_by_id(self):
        for i in range(len(self.nicknames)):
            save_repository.create(self.nicknames[i])

        right_nickname = save_repository.find_by_id(1)
        wrong_nickname = save_repository.find_by_id(10)

        self.assertEqual(right_nickname.nickname, self.nicknames[0])
        self.assertEqual(wrong_nickname, None)

    def test_find_saves_by_id(self):
        for i in range(len(self.nicknames)):
            save_repository.create(self.nicknames[i])

        user_one = save_repository.find_by_id(1)
        user_none = save_repository.find_by_id(10)

        self.assertEqual(user_one.nickname, self.nicknames[0])
        self.assertEqual(user_none, None)

    def test_find_saves_by_id_limits(self):
        for i in range(100):
            save_repository.create("TEST")
        saves = save_repository.find_and_sort_saves(8)
        saves2 = save_repository.find_and_sort_saves()
        saves3 = save_repository.find_and_sort_saves(3)

        self.assertEqual(len(saves), 8)
        self.assertEqual(len(saves2), 100)
        self.assertEqual(len(saves3), 3)

    def test_find_saves_by_id_orders_by_progress(self):
        for i in range(len(self.nicknames)):
            save_repository.create(self.nicknames[i])
        saves = save_repository.find_and_sort_saves()
        for i, save in enumerate(saves):
            save_repository.update(self.mixed_updates[i], save.save_id)
        saves = save_repository.find_and_sort_saves()

        self.assertEqual(saves[0].progress, self.updates[0])
        self.assertEqual(saves[1].progress, self.updates[1])
        self.assertEqual(saves[2].progress, self.updates[2])
        self.assertNotEqual(saves[0].progress, self.mixed_updates[0])

    def test_delete(self):
        for i in range(len(self.nicknames)):
            save_repository.create(self.nicknames[i])
        save_repository.delete()
        saves = save_repository.find_and_sort_saves()

        self.assertEqual(len(saves), 0)
