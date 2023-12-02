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
            if self.evaluate_game(cube):
                total_ids += cube.game_id
        print(f"Total of game ids for possible games: {total_ids}")

    def two(self) -> None:
        pass

    def evaluate_game(self, cube_game):
        for game in cube_game.aggregate:
            totals = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            for marble in game:
                totals[marble] += game[marble]
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
            marbles = cube_set.split(",")
            for marble in marbles:
                split_marble = marble.strip().split(" ")
                game_values.update({split_marble[1]: int(split_marble[0])})
            self.aggregate.append(game_values)


if __name__ == "__main__":
    s = Solution()
    s.one()
    s.two()
