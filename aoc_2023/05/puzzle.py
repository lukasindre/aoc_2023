import re

import numpy as np


class Solution:
    def __init__(self, input_file: str = "input.in") -> None:
        with open(input_file, "r") as f:
            data = f.read()
            self.data = data.strip().split("\n\n")
        self.seeds = [int(x.group()) for x in re.finditer(r"\d+", self.data.pop(0))]
        self.maps = [Mapperson(x) for x in self.data]
        self.seed_ranges = np.array_split(self.seeds, len(self.seeds) / 2)

    def one(self) -> None:
        locations = []
        for seed in self.seeds:
            location = seed
            for x in self.maps:
                location = x.process_number(location)
            locations.append(location)
        print(min(locations))

    def two(self) -> None:
        locations = []
        for seed_range in self.seed_ranges:
            for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
                location = seed
                for x in self.maps:
                    location = x.process_number(location)
                locations.append(location)
        print(min(locations))


class Mapperson:
    def __init__(self, map_string):
        split_map_string = map_string.split("\n")
        self.map_name = split_map_string.pop(0)
        self.relations = split_map_string
        self._create_map()

    def _create_map(self):
        self.map = {}
        for pos, line in enumerate(self.relations):
            components = [int(x) for x in line.strip().split(" ")]
            self.map[range(components[1], components[1] + components[2])] = {
                "dest": components[0],
                "increment": components[0] - components[1],
            }

    def process_number(self, number):
        final = number
        for key in self.map.keys():
            if final in key:
                final += self.map[key]["increment"]
                break
        return final


if __name__ == "__main__":
    s = Solution()
    s.one()
    s.two()
