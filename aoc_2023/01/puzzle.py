class Solution:
    def __init__(self, input_file: str = "input.in") -> None:
        with open(input_file, "r") as f:
            self.data = f.readlines()

    def one(self) -> None:
        total = 0
        for line in self.data:
            cl = CalibrationLine(line.strip())
            total += int(cl.calibration_value(cl.first_digit, cl.second_digit))
        print(f"One answer: {total}")

    def two(self) -> None:
        total = 0
        for line in self.data:
            cl = CalibrationLine(line.strip())
            total += int(cl.calibration_value(cl.first_digit_two, cl.second_digit_two))
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
        self.first_digit = self.find_first_digit_in_string(self.line_string)
        self.second_digit = self.find_first_digit_in_string(self.line_string[::-1])
        self.first_digit_two = self.find_first_digit_in_string_for_real(
            self.line_string, self.DIGITS
        )
        self.second_digit_two = self.find_first_digit_in_string_for_real(
            self.line_string[::-1], {k[::-1]: self.DIGITS[k] for k in self.DIGITS}
        )

    def find_first_digit_in_string(self, calibration_string: str) -> str:
        for char in calibration_string:
            try:
                return str(int(char))
            except ValueError:
                continue

    def find_first_digit_in_string_for_real(
        self, calibration_string: str, digit_map: dict[str, str]
    ) -> str:
        for pos, char in enumerate(calibration_string):
            try:
                first_int = str(int(char))
                break
            except ValueError:
                continue
        search_string = calibration_string.split(first_int)[0]
        digit_positions = {}
        for digit in digit_map:
            if digit in search_string:
                digit_positions.update({digit: search_string.find(digit)})
        if len(digit_positions) == 0:
            return first_int
        else:
            return digit_map[min(digit_positions, key=digit_positions.get)]

    def calibration_value(self, first_digit, second_digit):
        return first_digit + second_digit


if __name__ == "__main__":
    s = Solution()
    s.one()
    s.two()
