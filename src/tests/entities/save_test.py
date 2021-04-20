import unittest
from repositories.save_repository import save_repository
from entities.save import Save


class TestSave(unittest.TestCase):
    def setUp(self):
        save_repository.delete()
        self.save1 = save_repository.create("TEST")
        self.save2 = save_repository.create("AAAA")
        self.save3 = save_repository.create("BBBB")

    def test_get_start_information(self):
        progress = self.save1.get_information()

        self.assertEqual(progress["id"], 1)
        self.assertEqual(progress["nickname"], "TEST")
        self.assertEqual(progress["progress"], 0)
        self.assertTrue(progress["unlocked1"])
        self.assertFalse(progress["unlocked2"])
        self.assertEqual(progress["level1"], 0)
        self.assertEqual(progress["level2"], 0)

    def test_get_information_after_update(self):
        save_repository.update(100, 2)
        self.save2 = save_repository.find_by_id(2)
        progress = self.save2.get_information()

        self.assertEqual(progress["id"], 2)
        self.assertEqual(progress["nickname"], "AAAA")
        self.assertEqual(progress["progress"], 100)
        self.assertTrue(progress["unlocked1"])
        self.assertTrue(progress["unlocked2"])
        self.assertFalse(progress["unlocked3"])
        self.assertEqual(progress["level1"], 100)
        self.assertEqual(progress["level2"], 0)

    def test_get_information_with_max_points(self):
        save_repository.update(400, 3)
        self.save3 = save_repository.find_by_id(3)
        progress = self.save3.get_information()

        self.assertEqual(progress["id"], 3)
        self.assertEqual(progress["nickname"], "BBBB")
        self.assertEqual(progress["progress"], 400)
        self.assertTrue(progress["unlocked1"])
        self.assertTrue(progress["unlocked2"])
        self.assertTrue(progress["unlocked3"])
        self.assertTrue(progress["unlocked4"])
        self.assertEqual(progress["level1"], 100)
        self.assertEqual(progress["level2"], 100)
        self.assertEqual(progress["level3"], 100)
        self.assertEqual(progress["level4"], 100)
