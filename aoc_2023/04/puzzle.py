import re
from functools import lru_cache
from math import pow


class Solution:
    BASE = 2

    def __init__(self, input_file: str = "input.in") -> None:
        with open(input_file, "r") as f:
            self.data = f.readlines()
        self.total_cards = len(self.data)

    def one(self) -> None:
        total = 0
        for line in self.data:
            sc = ScratchCard(line)
            if sc.number_of_matches == 0:
                continue
            else:
                total += pow(self.BASE, sc.number_of_matches - 1)
        print(f"Total of you scratch_card matches: {int(total)}")

    @lru_cache
    def two(self) -> None:
        scratch_card_counts = {k: 1 for k in range(0, self.total_cards)}
        for scratch_card in scratch_card_counts:
            for count in range(scratch_card_counts[scratch_card]):
                sc = ScratchCard(self.data[scratch_card])
                for match in range(sc.number_of_matches):
                    scratch_card_counts[scratch_card + match + 1] += 1
        print(f"Total number of scorecards: {(sum(scratch_card_counts.values()))}")


class ScratchCard:
    def __init__(self, scratch_card):
        self.scratch_card = scratch_card
        self._get_numbers()
        self._get_number_of_matches()

    def _get_numbers(self):
        number_strings = (
            re.sub(r"Card\s+\d+:", "", self.scratch_card).strip().split(" | ")
        )
        digit_pattern = re.compile(r"\d+")
        self.winning_numbers = self._extract_numbers(number_strings[0], digit_pattern)
        self.my_numbers = self._extract_numbers(number_strings[1], digit_pattern)

    def _extract_numbers(self, number_string, pattern):
        return [x.group() for x in pattern.finditer(number_string)]

    def _get_number_of_matches(self):
        self.number_of_matches = len(
            [x for x in self.my_numbers if x in self.winning_numbers]
        )


if __name__ == "__main__":
    s = Solution()
    s.one()
    s.two()
