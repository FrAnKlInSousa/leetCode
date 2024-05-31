import pytest

from case_0013.case_0013 import roman_to_int


class TestRomanToInt:
    """
    Roman to Integer

    Given a roman numeral, convert it to an integer.
    """

    @pytest.mark.parametrize(
        "roman_number,expected",
        [
            ('X', 10), ('IX', 9),
            ('III', 3),
            ('LVIII', 58),
            ("MCMXCIV", 1994),
            ('MMMXLV', 3045)
        ],
    )
    def test_roman_to_int(self, roman_number, expected):
        result = roman_to_int(roman_number)
        assert result == expected
