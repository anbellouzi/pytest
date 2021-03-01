import pytest


# test_exception.py
def palindrome(word):
    if not isinstance(word, str):
        raise TypeError('Please provide a string argument')
    return word == word[::-1]

def test_palindrom():
    with pytest.raises(TypeError):
        palindrome(44)