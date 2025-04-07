import math


class UnitClass:
    def __init__(self, one_symbol: str, half_symbol: str, ten_symbol: str):
        self.one_symbol = one_symbol
        self.half_symbol = half_symbol
        self.ten_symbol = ten_symbol

    def number_to_roman(self, number: int)-> str:
        if number == 0:
            return ""
        elif number <= 3:
            return self.one_symbol * number
        elif number == 4:
            return self.one_symbol + self.half_symbol
        elif number == 5:
            return self.half_symbol
        elif number <= 8:
            diff = number - 5
            return self.half_symbol + self.one_symbol * diff
        elif number == 9:
            return self.one_symbol + self.ten_symbol
        else:
            return "Error"
        


Unit = UnitClass("I", "V", "X")
Ten = UnitClass("X", "L", "C")
Hundred = UnitClass("C", "D", "M")
Thousand = UnitClass("M", "", "")

def digit_to_roman(digit, number)-> str:
    if digit == 1:
        return Unit.number_to_roman(number)
    if digit == 2:
        return Ten.number_to_roman(number)
    if digit == 3:
        return Hundred.number_to_roman(number)
    if digit == 4:
        return Thousand.number_to_roman(number)


def decimal_to_roman(total_number: int)-> str:
    if total_number>3999:
        return "Error number out of range"

    number_as_string = str(total_number)
    roman = ""
    inverted_string = number_as_string[::-1]
    for digit, number in enumerate(inverted_string, 1):
        roman = digit_to_roman(digit, int(number)) + roman

    return roman


