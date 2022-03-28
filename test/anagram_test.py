import unittest
from app.anagram import AnagramService

class TestAnagram(unittest.TestCase):

    def setUp(self):
        self.service = AnagramService()
        self.valid_words = self.service.load_dictionary('test_list.txt')

    def test_get_anagrams(self):
        expected = ['finder', 'friend', 'redfin', 'refind']
        actual = self.service.get_anagrams('friend')
        
        self.assertEqual(len(expected), len(actual))
        for word in actual:
            self.assertTrue(word in expected)
