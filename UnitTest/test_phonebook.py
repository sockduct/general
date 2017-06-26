####################################################################################################
# Unit Testing with Python - Module 1
####################################################################################################

from phonebook import Phonebook

import unittest

class PhonebookTest(unittest.TestCase):

    # Test Fixture
    # Setup (half of fixture) - run before each test method
    def setUp(self):
        self.phonebook = Phonebook()
    
    def test_lookup_entry_by_name(self):
        self.phonebook.add('Bob', '12345')
        self.assertEqual('12345',self.phonebook.lookup('Bob'))

    def test_missing_entry_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')
    
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
    
    # Example of what not to do - split up into workable tests following this function
    @unittest.skip('poor example')
    def test_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add('Bob', '12345')
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add('Mary', '012345')
        self.assertTrue(self.phonebook.is_consistent())
        # Not a good way to write test cases
        # Once assertion fails, rest of test case is abandoned
        self.phonebook.add('Sue', '12345')  # identical to Bob
        self.assertFalse(self.phonebook.is_consistent())
        self.phonebook.add('Sue', '123')  # prefix of Bob
        self.assertFalse(self.phonebook.is_consistent())
    
    # These test cases have much better names - each name is descriptive of the test
    # Each of these test cases are structured - arrange, act, assert
    # Arrange - put entries into phonebook
    # Act - call is_consistent()
    # Assert - assertTrue|assertFalse about results
    def test_phonebook_with_normal_entires_is_consistent(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Mary', '012345')
        self.assertTrue(self.phonebook.is_consistent())
        
    def test_phonebook_with_duplicate_entries_is_inconsistent(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Mary', '12345')
        self.assertFalse(self.phonebook.is_consistent())
    
    def test_phonebook_with_numbers_that_prefix_one_another_is_inconsistent(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Mary', '123')
        self.assertFalse(self.phonebook.is_consistent())
    
    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add('Sue', '12345')
        self.assertIn('Sue', self.phonebook.get_names())
        self.assertIn('12345', self.phonebook.get_numbers())

if __name__ == '__main__':
    unittest.main()

