import logging

logger = logging.getLogger(__name__)

# Challenge 1: Count the number of unique letters in a string


class InvalidLetter(Exception):
    pass


def count_unique_letters(data: str) -> int:
    """Counts the number of unique letters in a string regardless if they are upper or lower case
    Args:
        data (str): The string to count unique letters for
    Returns:
        int: The number of unique letters
    Raises:
        ValueError: If data is not a string
        InvalidLetter: If a character is not a letter
    """

    if not isinstance(data, str):
        raise ValueError("Data must be string")

    lower_case = data.lower()
    base = "abcdefghijklmnopqrstuvwxyz"
    return len(set(lower_case))
