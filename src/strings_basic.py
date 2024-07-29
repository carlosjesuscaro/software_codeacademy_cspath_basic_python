import logging

logger = logging.getLogger(__name__)

# Challenge 1: Count the number of unique letters in a string


class CustomError(Exception):
    pass


def count_unique_letters(data: str) -> int:
    """Counts the number of unique letters in a string regardless if they are upper or lower case
    Args:
        data (str): The string to count unique letters for
    Returns:
        int: The number of unique letters
    Raises:
        AttributeError: If data is not a string, the error is caught with a try-except block
    """

    try:
        data_lower = data.lower()
        count = 0
        tracking = []
        if len(data) != 0:
            for letter in data_lower:
                if (letter.isalpha()) & (letter not in tracking):
                    count += 1
                    tracking.append(letter)
            logger.debug(f"{data} has {count} unique letters")
            return count
        else:
            logger.warning(f"Empty string")
            return -2
    except Exception as error:
        logger.error(f'The data type is not a string, it is {type(data)}')
        logger.error(f'An exception occurred: {type(error).__name__}')
        return -1

# Challenge 2: Count the number a specific character is repeated in a string


def count_character(data: str, letter: str) -> int:
    """Counts the number of times `letter` appears in `data`
    Args:
        data (str): The string to count characters for
        letter (str): The letter to count
    Return:
        int: The number of times `letter` appears in `data`
    Raises:
        AttributeError: If data is not a string, the error is caught with a try-except block
    """

    try:
        if (len(data) != 0) & (len(letter) == 1):
            lower_data, lower_letter, count = data.lower(), letter.lower(), 0
            for char in lower_data:
                if char == lower_letter:
                    count += 1
            logger.debug(f"{letter} is {count} time(s) in {data}")
            return count
        else:
            logger.warning(f"string length: {len(data)} and character length: {len(letter)}")
            return -2
    except Exception as error:
        logger.error(f'Data type issue: string type: {type(data)} and character type: {type(letter)}')
        logger.error(f'An exception occurred: {type(error).__name__}')
        return -1
