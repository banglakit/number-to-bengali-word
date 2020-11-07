def input_sanitizer(number):
    isfloat = isinstance(number, float)
    if isinstance(number, str):
        isfloat = "." in number
        if isfloat:
            number = float(number)
        else:
            number = int(number)
    return isfloat, number
