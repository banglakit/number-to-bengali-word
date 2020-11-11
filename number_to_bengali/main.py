from .utils import (float_int_extraction, fraction_to_words, generate_segments,
                    input_sanitizer, whole_part_word_gen)


def to_bn_word(number):
    """
    Takes a number and outputs the word form in Bengali for that number.
    """

    generated_words = ""
    number = input_sanitizer(number)

    whole, fraction = float_int_extraction(number)

    whole_segments = generate_segments(whole)

    generated_words = whole_part_word_gen(whole_segments)

    if fraction:
        if generated_words:
            return generated_words + " দশমিক " + fraction_to_words(fraction)
        else:
            return "দশমিক " + fraction_to_words(fraction)
    else:
        return generated_words
