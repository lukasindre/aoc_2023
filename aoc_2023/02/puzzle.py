import math
import re


class Solution:
    LIMITS = {"red": 12, "green": 13, "blue": 14}

    def __init__(self, input_file: str = "input.in") -> None:
        with open(input_file, "r") as f:
            self.data = f.readlines()

    def one(self) -> None:
        total_ids = 0
        for line in self.data:
            cube = CubeGame(line.strip())
            if self.is_possible(cube):
                total_ids += cube.game_id
        print(f"Total of game ids for possible games: {total_ids}")

    def two(self) -> None:
        total_power = 0
        for line in self.data:
            cube = CubeGame(line.strip())
            max_values = self.get_max_values(cube.aggregate)
            total_power += math.prod(max_values.values())
        print(f"Total power of sets: {total_power}")

    def get_max_values(self, cube_game):
        return {
            "red": max(x.get("red", 0) for x in cube_game),
            "green": max(x.get("green", 0) for x in cube_game),
            "blue": max(x.get("blue", 0) for x in cube_game),
        }

    def is_possible(self, cube_game):
        for game in cube_game.aggregate:
            totals = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            for cube in game:
                totals[cube] += game[cube]
            if (
                totals["red"] <= self.LIMITS["red"]
                and totals["green"] <= self.LIMITS["green"]
                and totals["blue"] <= self.LIMITS["blue"]
            ):
                continue
            else:
                return False
        return True


class CubeGame:
    def __init__(self, game_results):
        self.game_results = game_results
        self.game_id()
        self.cube_sets()
        self.aggregate = []
        self.game_values()

    def game_id(self):
        self.game_match = re.search(r"Game\s\d.*:", self.game_results).group(0)
        game_id_match = re.search(r"\d+", self.game_match).group(0)
        self.game_id = int(game_id_match)

    def cube_sets(self):
        self.cube_sets = (
            self.game_results.replace(self.game_match, "").strip().split(";")
        )

    def game_values(self):
        for cube_set in self.cube_sets:
            game_values = {}
            cubes = cube_set.split(",")
            for cube in cubes:
                split_cube = cube.strip().split(" ")
                game_values.update({split_cube[1]: int(split_cube[0])})
            self.aggregate.append(game_values)


if __name__ == "__main__":
    s = Solution()
    s.one()
    s.two()
