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
