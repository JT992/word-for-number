import unittest
from assertpy import assert_that
from word_for_number import word_for


class WordForTestCase(unittest.TestCase):
    def test_one_digit(self):
        assert_that(word_for(0)).is_equal_to('zero')
        assert_that(word_for(7)).is_equal_to('seven')

    def test_two_digits(self):
        assert_that(word_for(12)).is_equal_to('twelve')
        assert_that(word_for(64)).is_equal_to('sixty four')
        assert_that(word_for(90)).is_equal_to('ninety')

    def test_three_digits(self):
        assert_that(word_for(100)).is_equal_to('one hundred')
        assert_that(word_for(214)).is_equal_to('two hundred and fourteen')
        assert_that(word_for(509)).is_equal_to('five hundred and nine')
        assert_that(word_for(888)).is_equal_to('eight hundred and eighty eight')

    def test_four_digits(self):
        assert_that(word_for(1000)).is_equal_to('one thousand')
        assert_that(word_for(2014)).is_equal_to('two thousand and fourteen')
        assert_that(word_for(5009)).is_equal_to('five thousand and nine')
        assert_that(word_for(7901)).is_equal_to('seven thousand nine hundred and one')
        assert_that(word_for(9135)).is_equal_to('nine thousand one hundred and thirty five')

    def test_five_digits(self):
        assert_that(word_for(10000)).is_equal_to('ten thousand')
        assert_that(word_for(13000)).is_equal_to('thirteen thousand')
        assert_that(word_for(20001)).is_equal_to('twenty thousand and one')
        assert_that(word_for(30015)).is_equal_to('thirty thousand and fifteen')
        assert_that(word_for(50689)).is_equal_to('fifty thousand six hundred and eighty nine')
        assert_that(word_for(93428)).is_equal_to('ninety three thousand four hundred and twenty eight')

    def test_six_digits(self):
        assert_that(word_for(100000)).is_equal_to('one hundred thousand')
        assert_that(word_for(140000)).is_equal_to('one hundred and forty thousand')
        assert_that(word_for(114000)).is_equal_to('one hundred and fourteen thousand')
        assert_that(word_for(235600)).is_equal_to('two hundred and thirty five thousand six hundred')
        assert_that(word_for(487360)).is_equal_to('four hundred and eighty seven thousand three hundred and sixty')
        assert_that(word_for(610315)).is_equal_to('six hundred and ten thousand three hundred and fifteen')
        assert_that(word_for(836527)).is_equal_to('eight hundred and thirty six thousand five hundred and twenty seven')

    def test_seven_digits(self):
        assert_that(word_for(1000000)).is_equal_to('one million')
        assert_that(word_for(1600000)).is_equal_to('one million six hundred thousand')
        assert_that(word_for(2430000)).is_equal_to('two million four hundred and thirty thousand')
        assert_that(word_for(3518000)).is_equal_to('three million five hundred and eighteen thousand')
        assert_that(word_for(4365800)).is_equal_to('four million three hundred and sixty five thousand eight hundred')
        assert_that(word_for(5832440)).is_equal_to('five million eight hundred and thirty two thousand four hundred '
                                                   'and forty')
        assert_that(word_for(7658413)).is_equal_to('seven million six hundred and fifty eight thousand four hundred '
                                                   'and thirteen')
        assert_that(word_for(9365821)).is_equal_to('nine million three hundred and sixty five thousand eight hundred '
                                                   'and twenty one')

    def test_eight_digits(self):
        assert_that(word_for(10000000)).is_equal_to('ten million')
        assert_that(word_for(13000000)).is_equal_to('thirteen million')
        assert_that(word_for(15200000)).is_equal_to('fifteen million two hundred thousand')
        assert_that(word_for(23680000)).is_equal_to('twenty three million six hundred and eighty thousand')
        assert_that(word_for(35815000)).is_equal_to('thirty five million eight hundred and fifteen thousand')
        assert_that(word_for(41365800)).is_equal_to('forty one million three hundred and sixty five thousand eight '
                                                    'hundred')
        assert_that(word_for(60189540)).is_equal_to('sixty million one hundred and eighty nine thousand five hundred '
                                                    'and forty')
        assert_that(word_for(85743261)).is_equal_to('eighty five million seven hundred and forty three thousand two '
                                                    'hundred and sixty one')

    def test_nine_digits(self):
        assert_that(word_for(100000000)).is_equal_to('one hundred million')
        assert_that(word_for(140000000)).is_equal_to('one hundred and forty million')
        assert_that(word_for(151200000)).is_equal_to('one hundred and fifty one million two hundred thousand')
        assert_that(word_for(236870000)).is_equal_to('two hundred and thirty six million eight hundred and seventy '
                                                     'thousand')
        assert_that(word_for(316281500)).is_equal_to('three hundred and sixteen million two hundred and eighty one '
                                                     'thousand five hundred')
        assert_that(word_for(413655820)).is_equal_to('four hundred and thirteen million six hundred and fifty five '
                                                     'thousand eight hundred and twenty')
        assert_that(word_for(601895414)).is_equal_to('six hundred and one million eight hundred and ninety five '
                                                     'thousand four hundred and fourteen')
        assert_that(word_for(985743261)).is_equal_to('nine hundred and eighty five million seven hundred and forty '
                                                     'three thousand two hundred and sixty one')

    def test_further_digits(self):
        assert_that(word_for(1000000000)).is_equal_to('one billion')
        assert_that(word_for(10000000000)).is_equal_to('ten billion')
        assert_that(word_for(100000000000)).is_equal_to('one hundred billion')
