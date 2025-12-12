#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.

    Args:
        sentence: The input string to analyze

    Returns:
        tuple: (length of sentence, first character)
              If sentence is empty, returns (0, None)
    """
    if not sentence:  # This checks if sentence is empty
        return (0, None)

    return (len(sentence), sentence[0])
