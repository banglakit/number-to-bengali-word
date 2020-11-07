import pytest

from number_to_bengali.main import to_bn_word
from number_to_bengali.utils import input_sanitization


def test_single_digit():
    """
    Testing to check if single digit numbers are converted to words properly
    """
    assert to_bn_word(1) == "এক"


def test_can_take_string_input():
    """
    Testing to check if the number input can take string and convert to float 
    and int successfully
    """
    isfloat, nubmer = input_sanitization("1")
    assert isfloat == False
    assert nubmer == 1

    isfloat, nubmer = input_sanitization("10.1")
    assert isfloat == True
    assert nubmer == 10.1
