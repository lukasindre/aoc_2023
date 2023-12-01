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
            cl = CalibrationLine(line)
        print(f"Two answer: {total}")


class CalibrationLine:
    DIGITS = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    def __init__(self, line_string: str) -> None:
        self.line_string = line_string
        self.first_digit()
        self.second_digit()
        self.calibration_value()

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

    def calibration_value(self):
        self.calibration_value = self.first_digit + self.second_digit


if __name__ == "__main__":
    s = Solution()
    s.one()
    s.two()
