import re


class Solution:
    def __init__(self, input_file: str = "input.in") -> None:
        with open(input_file, "r") as f:
            self.data = f.readlines()

    def one(self) -> None:
        total = 0
        for position, line in enumerate(self.data):
            sl = SchematicLine(self.data, position, line)
            total += sl.sum_part_numbers
        print(f"The total of the valid part numbers is: {total}")

    def two(self) -> None:
        pass


class SchematicLine:
    def __init__(self, dataframe, position, row):
        self.df = dataframe
        self.position = position
        self.row = row.strip()
        self._search_row_for_numbers()
        self._find_get_number_positions()
        self._get_number_adjacent_values()
        self._valid_part_numbers()
        self._sum_part_numbers()

    def _search_row_for_numbers(self):
        self.numbers = re.findall(r"\d+", self.row)

    def _find_get_number_positions(self):
        self.number_positions = {}
        for number in self.numbers:
            start = self.row.find(number)
            end = start + len(number)
            self.number_positions[number] = [x for x in range(start, end)]

    def _valid_part_numbers(self):
        self.valid_part_numbers = []
        for number in self.number_adjacent_values:
            value_string = "".join(self.number_adjacent_values[number])
            if len(value_string.replace(".", "")) > 0:
                self.valid_part_numbers.append(number)

    def _sum_part_numbers(self):
        self.sum_part_numbers = sum(self.valid_part_numbers)

    def _get_number_adjacent_values(self):
        self.number_adjacent_values = {}
        for number_position in self.number_positions:
            top = []
            bottom = []
            left = []
            right = []
            top_left = []
            top_right = []
            bottom_left = []
            bottom_right = []
            if self.position == 0:
                pass
            else:
                top = [
                    self.df[self.position - 1][x]
                    for x in self.number_positions[number_position]
                ]

            if self.position == len(self.df) - 1:
                pass
            else:
                bottom = [
                    self.df[self.position + 1][x]
                    for x in self.number_positions[number_position]
                ]

            if self.number_positions[number_position][0] == 0:
                pass
            else:
                left = [self.row[self.number_positions[number_position][0] - 1]]

            if self.number_positions[number_position][-1] == len(self.row) - 1:
                pass
            else:
                right = [self.row[self.number_positions[number_position][-1] + 1]]

            if len(top) > 0:
                if len(left) > 0:
                    top_left = [
                        self.df[self.position - 1][
                            self.number_positions[number_position][0] - 1
                        ]
                    ]
                else:
                    pass
                if len(right) > 0:
                    top_right = [
                        self.df[self.position - 1][
                            self.number_positions[number_position][-1] + 1
                        ]
                    ]
                else:
                    pass

            if len(bottom) > 0:
                if len(left) > 0:
                    bottom_left = [
                        self.df[self.position + 1][
                            self.number_positions[number_position][0] - 1
                        ]
                    ]
                else:
                    pass
                if len(right) > 0:
                    bottom_right = [
                        self.df[self.position + 1][
                            self.number_positions[number_position][-1] + 1
                        ]
                    ]
                else:
                    pass
            self.number_adjacent_values[int(number_position)] = (
                top
                + bottom
                + left
                + right
                + top_left
                + top_right
                + bottom_left
                + bottom_right
            )


if __name__ == "__main__":
    s = Solution()
    s.one()
    s.two()
