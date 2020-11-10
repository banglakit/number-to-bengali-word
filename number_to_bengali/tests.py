import pytest

from number_to_bengali.main import to_bn_word
from number_to_bengali.utils import (float_int_extraction, generate_segments,
                                     input_sanitizer, whole_part_word_gen)


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


def test_other_data_types_are_handled_correctly():
    """
    Testing to check if anything other than int, float or string is passed the 
    input_sanitizer returns None
    """
    isfloat, number = input_sanitizer([1, 0])
    assert isfloat == None
    assert number == None


def test_segment_generation():
    """
    Testing to check if the generation of segments as per units such as koti, 
    lokkho, hazar etc. are correct.
    """
    test_data = {
        'koti': 1,
        'lokkho': 20,
        'hazar': 33,
        'sotok': 4,
        'ekok': 20
    }

    assert generate_segments(12033420) == test_data

    test_data = {
        'koti': 100,
        'lokkho': 00,
        'hazar': 33,
        'sotok': 4,
        'ekok': 20
    }

    assert generate_segments(1000033420) == test_data


def test_float_and_int_are_correctly_extracted():
    """
    Testing if the integer and float part are extracted correctly from the input
    number
    """
    assert (10, 1) == float_int_extraction(10.10)
    assert (1, None) == float_int_extraction(1)


def test_word_generation_for_whole_part():
    """
    Testing if the part before the decimal point is generated correctly
    The input taken should be segments
    """
    test_data = {
        'koti': 0,
        'lokkho': 0,
        'hazar': 10,
        'sotok': 0,
        'ekok': 1
    }

    assert whole_part_word_gen(test_data) == "দশ হাজার এক"

    test_data = {
        'koti': 0,
        'lokkho': 0,
        'hazar': 0,
        'sotok': 0,
        'ekok': 1
    }
    assert whole_part_word_gen(test_data) == "এক"

    test_data = {
        'koti': 0,
        'lokkho': 12,
        'hazar': 77,
        'sotok': 5,
        'ekok': 48
    }
    assert whole_part_word_gen(
        test_data) == "বার লক্ষ সাতাত্তর হাজার পাঁচ শত আটচল্লিশ"
