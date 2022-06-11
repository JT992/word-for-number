units = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
teens = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
tens = ('', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')

million_words = ('', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion',
                 'octillion', 'nonillion')
bigger_units = ('', 'un', 'duo', 'tre', 'quattuor', 'quinqua', 'se', 'septe', 'octo', 'nove')
bigger_tens = ('', 'deci', 'viginti', 'triginta', 'quadraginta', 'quinquaginta', 'sexaginta', 'septuaginta',
               'octoginta', 'nonaginta')
bigger_hundreds = ('', 'centi', 'ducenti', 'trecenti', 'quadringenti', 'quingenti', 'sescenti', 'septingenti',
                   'octingenti', 'nongenti')


def word_for(number: int):
    """Returns the word for a number."""
    if number < 0:
        return f'minus {word_for(-number)}'
    if number == 0:
        return 'zero'
    if number < 10:
        return units[number]
    if number < 100:
        return two_digit(number)
    if number < 1000:
        return three_digit(number)
    chunked = chunk(number)
    chunked_words = list(reversed([word_for(number) for number in chunked]))
    finished_words = list(reversed([f'{word} {calculate_big_number_word(chunked_words.index(word) - 1)} ' if word != 'zero' else '' for word in chunked_words]))
    stripped_words = [word.strip() for word in finished_words]
    return ''.join(stripped_words)

def two_digit(number: int):
    if number % 10 == 0:
        return tens[number // 10]
    if number < 20:
        return teens[number - 10]
    return f'{tens[number // 10]} {units[number - ((number // 10) * 10)]}'


def three_digit(number: int):
    build = f'{units[number // 100]} hundred'
    if number % 100 == 0:
        return build
    build += ' and '
    remaining = number - ((number // 100) * 100)
    return build + two_digit(remaining) if remaining >= 10 else build + units[remaining]


def calculate_big_number_word(bigness: int):
    """Returns the big number word for a given bigness.
    (uses American system, negative is no bigness and 0 is 'thousand' bigness. 
    credit: https://home.kpn.nl/vanadovv/BignumEN.html)"""
    assert bigness < 1000, 'bigness is too big'
    if bigness < 1:
        return 'thousand' if bigness == 0 else ''
    if bigness < 10:
        return million_words[bigness]
    build = ['llion']
    if bigness >= 100:
        build.insert(0, bigger_hundreds[(bigness // 100)])
        bigness -= (bigness // 100) * 100
    build.insert(0, bigger_tens[(bigness // 10)])
    bigness -= (bigness // 10) * 10
    build = [x for x in build if x]  # strip empty strings from list
    build.insert(0, calculate_big_unit(bigness, build[0][0]))
    return ''.join(build)


def calculate_big_unit(remaining_bigness: int, next_letter: str):
    if remaining_bigness in (0, 1, 2, 4, 5, 8):
        return bigger_units[remaining_bigness]
    if remaining_bigness == 3:
        if next_letter in ('c', 'o', 'q', 't', 'v'):
            return 'tres'
        return 'tre'
    if remaining_bigness == 6:
        if next_letter in ('q', 't', 'v'):
            return 'ses'
        if next_letter in ('c', 'o'):
            return 'sex'  # heheh.
        return 'se'
    if remaining_bigness == 7:
        if next_letter in ('c', 'd', 'q', 's', 't'):
            return 'septen'
        if next_letter in ('o', 'v'):
            return 'septem'
        return 'septe'
    if remaining_bigness == 9:
        if next_letter in ('c', 'd', 'q', 's', 't'):
            return 'noven'
        if next_letter in ('o', 'v'):
            return 'novem'
        return 'nove'



def chunk(number: int):
    result = ['']
    for digit in reversed(str(number)):
        if len(result[0]) == 3:
            result[0] = int(result[0])
            result.insert(0, '')
        result[0] = f'{digit}{result[0]}'
    result[0] = int(result[0])
    return tuple(result)


def word_for_float(number: float | int):
    """Returns the word for a number using `word_for()`. Supports floats."""
    word = word_for(int(number))
    if isinstance(number, int):
        return word
    list_number = str(number).split('.')  # splits the float at the decimal point
    digits = [units[int(digit)] for digit in list_number[1]]  # compute the word for each digit
    return f'{word} point {" ".join(digits)}'


def main():
    print(calculate_big_number_word(1))


if __name__ == '__main__':
    main()
