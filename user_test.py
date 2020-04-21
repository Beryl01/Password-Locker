import unittest
from user import User
class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("James", "Muriuki", "0712345678", "james@example.com")  # create user object

    