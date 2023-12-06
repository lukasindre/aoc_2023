import re
from math import prod


class Solution:
    pattern = re.compile(r"\d+")

    def __init__(self, input_file: str = "input.in") -> None:
        with open(input_file, "r") as f:
            self.data = f.readlines()
        times = [x.group() for x in self.pattern.finditer(self.data[0].strip())]
        records = [x.group() for x in self.pattern.finditer(self.data[1].strip())]
        self.races = zip(times, records)
        self.long_race = "".join(times), "".join(records)

    def one(self) -> None:
        numbers = []
        for race in self.races:
            r = Race(race)
            numbers.append(r.max_distances())
        print(prod(numbers))

    def two(self) -> None:
        print(Race(self.long_race).max_distances())


class Race:
    def __init__(self, numbers):
        self.numbers = numbers
        self.time_limit = int(self.numbers[0])
        self.record = int(self.numbers[1])

    def max_distances(self):
        record_breakers = []
        for x in range(self.time_limit + 1):
            distance = x * (self.time_limit - x)
            if distance > self.record:
                record_breakers.append(x)
        return len(record_breakers)


if __name__ == "__main__":
    s = Solution()
    s.one()
    s.two()
