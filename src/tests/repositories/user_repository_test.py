import unittest
from repositories.user_repository import user_repository
from entities.user import User

# Useless right now. Needs to be removed.


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete()
        self.names = ["Hannu Huuru", "Topias", "Testaaja"]
        self.passwords = ["password1234", "admin", "secret1"]

    def test_create_user(self):
        for i in range(len(self.names)):
            user_repository.create(self.names[i], self.passwords[i])
        users = user_repository.find_all_users()

        self.assertEqual(len(users), 3)
        self.assertEqual(users[0].username, self.names[0])
        self.assertEqual(sum([user.user_id for user in users]), 6)

    def test_find_users_by_username(self):
        for i in range(len(self.names)):
            user_repository.create(self.names[i], self.passwords[i])

        user_one = user_repository.find_user_by_username(self.names[0])
        user_none = user_repository.find_user_by_username("Hannu Kuuru")

        self.assertEqual(user_one.username, self.names[0])
        self.assertEqual(user_none, None)

    def test_delete(self):
        for i in range(len(self.names)):
            user_repository.create(self.names[i], self.passwords[i])
        user_repository.delete()
        users = user_repository.find_all_users()

        self.assertEqual(len(users), 0)
