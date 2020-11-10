import math

from .bengali_words import numeric_words, units


def input_sanitizer(number):
    if isinstance(number, float) or isinstance(number, int) or isinstance(number, str):
        isfloat = isinstance(number, float)
        if isinstance(number, str):
            try:
                isfloat = "." in number
                if isfloat:
                    number = float(number)
                else:
                    number = int(number)
            except ValueError:
                return None, None
        return isfloat, number
    else:
        return None, None


def generate_segments(number):
    """
    Generating the unit segments such as koti, lokkho
    """
    segments = dict()
    segments['koti'] = math.floor(number/10000000)
    number = number % 10000000
    segments['lokkho'] = math.floor(number/100000)
    number = number % 100000
    segments['hazar'] = math.floor(number/1000)
    number = number % 1000
    segments['sotok'] = math.floor(number/100)
    number = number % 100
    segments['ekok'] = number

    return segments


def float_int_extraction(number):
    """
    Extracting the float and int part from the passed number. The first return
    is the part before the decimal point and the rest is the fraction.
    """
    _number = str(number)
    if "." in _number:
        return tuple([int(x) for x in _number.split(".")])
    else:
        return number, None


def whole_part_word_gen(segments):
    """
    Generating the bengali word for the whole part of the number
    """
    generated_words = ''
    for segment in segments:
        if segments[segment]:
            generated_words += numeric_words[str(segments[segment])] + \
                " " + units[segment] + " "

    return generated_words[:-2]
