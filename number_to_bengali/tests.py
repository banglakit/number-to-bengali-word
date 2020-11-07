import pytest

from number_to_bengali.main import to_bn_word
from number_to_bengali.utils import input_sanitizer


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
    isfloat, nubmer = input_sanitizer("1")
    assert isfloat == False
    assert nubmer == 1

    isfloat, nubmer = input_sanitizer("10.1")
    assert isfloat == True
    assert nubmer == 10.1


def test_can_handle_space_in_input_string():
    """
    Testing to check if the input_sanitizer() can correctly handle if the input
    string has empty space
    """

    isfloat, number = input_sanitizer("1 ")
    assert isfloat == False
    assert number == 1

    isfloat, number = input_sanitizer(" 1 ")
    assert isfloat == False
    assert number == 1


def test_raises_valueerror_if_string_has_non_numeric_chars():
    """
    Testing to check if other-non numeric char in the input is handled correctly
    """
    isfloat, number = input_sanitizer(" a1 ")
    assert isfloat == None
    assert number == None
