import unittest
from user import User
class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("Beryl", "Negesa", "0712345678", "beryl@example.com")  

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        User.users_array = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.first_name, "Beryl")
        self.assertEqual(self.new_user.last_name, "Negesa")
        self.assertEqual(self.new_user.phone_number, "0712345678")
        self.assertEqual(self.new_user.email, "beryl@example.com")

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into
        the users array
        """
        self.new_user.save_user_details()  
        self.assertEqual(len(User.users_array), 1)

    def test_save_multiple_users(self):
        """
        test_save_multiple_users to check if we can save multiple users
        to our users_array
        """
        self.new_user.save_user_details()
        test_user = User("Test", "user", "0712345678", "user@user.com")  
        test_user.save_user_details()
        self.assertEqual(len(User.users_array), 2)

   

    