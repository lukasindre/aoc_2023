class Solution:
    def __init__(self, input_file: str = "input.in") -> None:
        with open(input_file, "r") as f:
            self.data = f.readlines()

    def one(self) -> None:
        total = 0
        for line in self.data:
            cl = CalibrationLine(line.strip())
            total += int(cl.calibration_value)
        print(f"One answer: {total}")

    def two(self) -> None:
        total = 0
        for line in self.data:
            cl = CalibrationLine(line.strip())
            total += int(cl.more_calibration_value)
        print(f"Two answer: {total}")


class CalibrationLine:
    DIGITS = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    def __init__(self, line_string: str) -> None:
        self.line_string = line_string
        self.first_digit()
        self.second_digit()
        self.calibration_value()
        self.more_digits_one()
        self.more_digits_two()
        self.more_calibration_value()

    def first_digit(self):
        for char in self.line_string:
            try:
                self.first_digit = str(int(char))
                break
            except ValueError:
                continue

    def second_digit(self):
        for char in self.line_string[::-1]:
            try:
                self.second_digit = str(int(char))
                break
            except ValueError:
                continue

    def more_digits_one(self):
        for pos, char in enumerate(self.line_string):
            try:
                first_int = str(int(char))
                break
            except ValueError:
                continue
        my_string = self.line_string.split(first_int)[0]
        digit_positions = {}
        for digit in self.DIGITS:
            if digit in my_string:
                digit_positions.update({digit: my_string.find(digit)})
        if len(digit_positions) == 0:
            self.first_digit_two = first_int
        else:
            self.first_digit_two = self.DIGITS[
                min(digit_positions, key=digit_positions.get)
            ]

    def more_digits_two(self):
        for pos, char in enumerate(self.line_string[::-1]):
            try:
                first_int = str(int(char))
                break
            except ValueError:
                continue
        my_string = self.line_string[::-1].split(first_int)[0]
        digit_positions = {}
        for digit in self.DIGITS:
            if digit[::-1] in my_string:
                digit_positions.update({digit: my_string.find(digit[::-1])})
        if len(digit_positions) == 0:
            self.second_digit_two = first_int
        else:
            self.second_digit_two = self.DIGITS[
                min(digit_positions, key=digit_positions.get)
            ]

    def calibration_value(self):
        self.calibration_value = self.first_digit + self.second_digit

    def more_calibration_value(self):
        self.more_calibration_value = self.first_digit_two + self.second_digit_two


if __name__ == "__main__":
    s = Solution()
    s.one()
    s.two()
