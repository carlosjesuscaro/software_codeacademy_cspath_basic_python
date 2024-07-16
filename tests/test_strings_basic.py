import logging
from unittest import TestCase
from src.strings_basic import count_unique_letters

logger = logging.getLogger(__name__)


class TestStringsBasic(TestCase):
    def test_count_unique_letters_basic(self):
        self.assertEqual(count_unique_letters("carlos"), 6)

    def test_count_unique_letters_complex(self):
        self.assertEqual(count_unique_letters("natalia is playing at the park"), 13)

    def test_count_unique_letters_no_int(self):
        self.assertEqual(count_unique_letters(5), -1)

    def test_count_unique_letters_empty(self):
        self.assertEqual(count_unique_letters(""), -2)
