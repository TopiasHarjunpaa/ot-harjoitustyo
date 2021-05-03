import unittest
from services.information_service import InformationService
from repositories.save_repository import save_repository
from entities.save import Save


class TestInformationService(unittest.TestCase):
    def setUp(self):
        save_repository.delete()
        self.info = InformationService()
        self.nick = "TEST"

    def test_save_is_not_none_after_create(self):
        self.info.create_new_save(self.nick)
        self.assertNotEqual(self.info.get_save(), None)
        self.assertEqual(self.info.get_save().nickname, self.nick)

    def test_open_save_finds_save_file_by_id(self):
        self.info.create_new_save(self.nick)
        id_number = self.info.get_save().save_id
        self.info.close_save()
        self.info.open_save(id_number)
        self.assertEqual(id_number, 1)
        self.assertEqual(self.info.get_save().nickname, self.nick)

    def test_progress_information_is_returned(self):
        self.info.create_new_save(self.nick)
        progress = self.info.get_progress_information()
        self.assertEqual(progress["id"], 1)
        self.assertEqual(progress["nickname"], "TEST")
        self.assertEqual(progress["progress"], 0)
        self.assertTrue(progress["unlocked1"])
        self.assertFalse(progress["unlocked2"])
        self.assertEqual(progress["level1"], 0)
        self.assertEqual(progress["level2"], 0)

    def test_update_save_updates_progress(self):
        self.info.create_new_save(self.nick)
        id_number = self.info.get_save().save_id
        self.info.update_save(400, id_number)
        progress = self.info.get_progress_information()
        self.assertEqual(progress["id"], 1)
        self.assertEqual(progress["nickname"], "TEST")
        self.assertEqual(progress["progress"], 400)
        self.assertTrue(progress["unlocked1"])
        self.assertTrue(progress["unlocked4"])
        self.assertEqual(progress["level1"], 100)
        self.assertEqual(progress["level4"], 100)

    def test_list_saves_returns_list_of_all_saves(self):
        self.info.create_new_save(self.nick)
        self.info.create_new_save("AAAA")
        self.info.create_new_save("BBBB")
        save_list = self.info.list_saves()
        self.assertEqual(save_list[0].nickname, self.nick)
        self.assertEqual(save_list[1].nickname, "AAAA")
        self.assertEqual(save_list[2].nickname, "BBBB")
        self.assertEqual(len(save_list), 3)
