def roman_to_int(s: str) -> int:
    roman_values = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000,
    }

    def has_next(index, lenght) -> bool:
        if index == lenght - 1:
            return False
        return True

    special_chars = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    len_roman = len(s)
    value = 0
    for index, char in enumerate(s):
        if has_next(index, len_roman):
            if char + s[index + 1] in special_chars:
                value -= roman_values[char]
            else:
                value += roman_values[char]
        else:
            value += roman_values[char]
    return value
