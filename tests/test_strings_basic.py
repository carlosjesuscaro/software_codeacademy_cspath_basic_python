import logging
from unittest import TestCase
from src.strings_basic import count_unique_letters
from src.strings_basic import count_character

logger = logging.getLogger(__name__)


class TestStringsBasic(TestCase):
    # Challenge 1
    def test_count_unique_letters_basic(self):
        self.assertEqual(count_unique_letters("carlos"), 6)

    def test_count_unique_letters_complex(self):
        self.assertEqual(count_unique_letters("natalia is playing at the park"), 13)

    def test_count_unique_letters_no_int(self):
        self.assertEqual(count_unique_letters(5), -1)

    def test_count_unique_letters_empty(self):
        self.assertEqual(count_unique_letters(""), -2)

    # Challenge 2
    def test_count_character_basic(self):
        self.assertEqual(count_character('natalia', 'a'), 3)

    def test_count_character_data_not_str(self):
        self.assertEqual(count_character(23, 'a'), -1)

    def test_count_character_letter_not_str(self):
        self.assertEqual(count_character('natalia', 23), -1)

    def test_count_character_data_empty(self):
        self.assertEqual(count_character('', 'a'), -2)

    def test_count_character_letter_empty(self):
        self.assertEqual(count_character('natalia', ''), -2)

    def test_count_character_all_empty(self):
        self.assertEqual(count_character('', ''), -2)
