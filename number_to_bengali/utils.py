import math


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
