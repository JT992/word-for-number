first_digit = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teen_digit = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
              'nineteen']
second_digit = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
million_words = ['', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion',
                 'octillion', 'nonillion']
# noinspection SpellCheckingInspection
bigger_units = ['', 'un', 'duo', 'tre', 'quattuor', 'quinqua', 'se', 'septe', 'octo', 'nove']
# noinspection SpellCheckingInspection
bigger_tens = ['', 'deci', 'viginti', 'triginta', 'quadraginta', 'quinquaginta', 'sexaginta', 'septuaginta',
               'octoginta', 'nonaginta']
# noinspection SpellCheckingInspection
bigger_hundreds = ['', 'centi', 'ducenti', 'trecenti', 'quadringenti', 'quingenti', 'sescenti', 'septingenti',
                   'octingenti', 'nongenti']


def word_for(number: int):
    """
    Finds the ordinal number word for the number put in.

    :param number: Integer to find.
    :return str:
    """
    if not isinstance(number, int):
        raise TypeError('Only integers are accepted.')
    if number < 0:
        return f'minus {word_for(-number)}'
    number = split_int(number)
    match len(number):
        case 1:
            return first_digit[number[0]]
        case 2:
            if number[0] == 1:
                return teen_digit[number[1]]
            if number[1] == 0:
                return second_digit[number[0]]
            return f'{second_digit[number[0]]} {first_digit[number[1]]}'
        case 3:
            build = f'{first_digit[number[0]]} hundred'
            if remaining_digits_zeroes(number):
                return build
            build += ' and '
            return build + word_for(cat_int(number))
        case 4:
            build = f'{first_digit[number[0]]} thousand'
            if remaining_digits_zeroes(number):
                return build
            if number[0] == 0:
                return build + f' and {word_for(cat_int(number))}'
            return build + f' {word_for(cat_int(number))}'
        case 5:
            if number[0] == 1:
                build = f'{teen_digit[number[1]]} thousand'
            else:
                top_number = [number[0], number[1]]
                top_number = word_for(cat_int(top_number))
                build = f'{top_number} thousand'
            del number[1]
            if remaining_digits_zeroes(number):
                return build
            if number[0] == 0:
                return build + f' and {word_for(cat_int(number))}'
            return build + f' {word_for(cat_int(number))}'
        case 6:
            build = f'{first_digit[number[0]]} hundred'
            if remaining_digits_zeroes(number):
                return build + ' thousand'
            if zeroes_at_pos(number, 0, 1, 2):
                return build + f' thousand and {(word_for(cat_int(number)))}'
            if zeroes_at_pos(number, 0, 1):
                return build + f' thousand {(word_for(cat_int(number)))}'
            return build + f' and {(word_for(cat_int(number)))}'
        case x if x % 3 == 1:
            build = f'{first_digit[number[0]]} {large_number(len(number) - 1)}'
            if remaining_digits_zeroes(number):
                return build
            if zeroes_at_pos(number, 0, 1, 2, 3):
                return build + f' and {word_for(cat_int(number))}'
            return build + f' {word_for(cat_int(number))}'
        case x if x % 3 == 2:
            build = f'{word_for(cat_int([number[0], number[1]]))} {large_number(len(number) - 1)}'
            del number[0]  # eleven million and one million? no
            if remaining_digits_zeroes(number):
                return build
            if zeroes_at_pos(number, 0, 1, 2, 3):
                return build + f' and {word_for(cat_int(number))}'
            return build + f' {word_for(cat_int(number))}'
        case x if x % 3 == 0:
            build = f'{word_for(cat_int([number[0], number[1], number[2]]))} {large_number(len(number) - 1)}'
            del number[0], number[1]
            if remaining_digits_zeroes(number):
                return build
            if zeroes_at_pos(number, 0, 1, 2, 3):
                return build + f' and {word_for(cat_int(number))}'
            return build + f' {word_for(cat_int(number))}'


# noinspection SpellCheckingInspection
def large_number(power: int):
    """Constructs the name for a large number. (Credit for conversions: http://home.kpn.nl/vanadovv/BignumEN.html)"""
    if power < 6:
        raise ValueError('Power too low for a large number, must be at least 6')
    serial = split_int((power - 3) // 3)
    if len(serial) == 1:
        return million_words[serial[0]]
    build = ['llion']
    if len(serial) == 3:
        build.insert(0, bigger_hundreds[serial[0]])
        build.insert(0, bigger_tens[serial[1]])
        del serial[0], serial[1]
    elif len(serial) == 2:
        build.insert(0, bigger_tens[serial[0]])
        del serial[0]
    else:
        raise OverflowError('Power was too large to be represented, must be less than 1000.')
    check = build[0][0]
    match (serial[0], check):
        case (0 | 1 | 2 | 4 | 5 | 8, _):
            build.insert(0, bigger_units[serial[0]])

        case (3, 'c' | 'o' | 'q' | 't' | 'v'):
            build.insert(0, 'tres')
        case (3, _):
            build.insert(0, 'tre')

        case (6, 'q' | 't' | 'v'):
            build.insert(0, 'ses')
        case (6, 'c' | 'o'):
            build.insert(0, 'sex')
        case (6, _):
            build.insert(0, 'se')

        case (7, 'c' | 'd' | 'q' | 's' | 't'):
            build.insert(0, 'septen')
        case (7, 'o' | 'v'):
            build.insert(0, 'septem')
        case (7, _):
            build.insert(0, 'septe')

        case (9, 'c' | 'd' | 'q' | 's' | 't'):
            build.insert(0, 'noven')
        case (9, 'o' | 'v'):
            build.insert(0, 'noven')
        case (9, _):
            build.insert(0, 'nove')

    if build[len(build) - 2][len(build[len(build) - 2]) - 1] not in ['a', 'e', 'i', 'o', 'u']:
        build.insert(len(build) - 2, 'i')  # ^ that's the final character of the second-to-last element

    return ''.join(build)


def split_int(number: int):
    """
    Splits an integer into a list of single-digit integers.

    :param number: Integer to split.
    """
    return [int(x) for x in str(number)]


def cat_int(number: list):
    """
    Concatenates a list of integers into one integer.

    :param number: List to concatenate.
    """
    return int(''.join(map(str, number)))


def remaining_digits_zeroes(number: list):
    """``number.count(0) == len(number)`` when the first element is excluded.
    Prefer ``zeroes_at_pos()`` for objects passed by reference."""
    del number[0]
    return number.count(0) == len(number)


def zeroes_at_pos(number: list, *args: int):
    """``all(number[i] == 0 for i in args)``"""
    return all(number[i] == 0 for i in args)
