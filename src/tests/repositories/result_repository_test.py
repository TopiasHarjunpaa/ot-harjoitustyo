import unittest
from repositories.result_repository import result_repository
from entities.user import User
from entities.result import Result

# Useless right now. Needs to be removed.


class TestResultRepository(unittest.TestCase):
    def setUp(self):
        result_repository.delete()
        self.user_ids = [1, 2, 3]
        self.points = [50, 150, 500]

    def test_create_result(self):
        for i in range(len(self.user_ids)):
            result_repository.create(self.user_ids[i], self.points[i])
        results = result_repository.find_all_results()

        self.assertEqual(len(results), 3)
        self.assertEqual(results[0].points, self.points[0])
        self.assertEqual(sum([result.result_id for result in results]), 6)
        self.assertIsNotNone(results[0].time)

    def test_delete(self):
        for i in range(len(self.user_ids)):
            result_repository.create(self.user_ids[i], self.points[i])
        result_repository.delete()
        results = result_repository.find_all_results()

        self.assertEqual(len(results), 0)
