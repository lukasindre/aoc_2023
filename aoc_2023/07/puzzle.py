from collections import Counter
import operator


class Solution:
    def __init__(self, input_file: str = "input.in") -> None:
        with open(input_file, "r") as f:
            self.data = f.readlines()
        self.card_values = {card: value for value, card in enumerate("23456789TJQKA")}
        self.part_two_card_values = {card: value for value, card in enumerate("J23456789TQKA")}

    def one(self) -> None:
        games = [
            (CardGame(cg).hand_strength,
            self.card_values[CardGame(cg).cards[0]],
            self.card_values[CardGame(cg).cards[1]],
            self.card_values[CardGame(cg).cards[2]],
            self.card_values[CardGame(cg).cards[3]],
            self.card_values[CardGame(cg).cards[4]],
            int(CardGame(cg).bid)) for cg in self.data
        ]
        games.sort(key=lambda element: (element[0], element[1], element[2], element[3], element[4], element[5]))
        winnings = 0
        for rank, game in enumerate(games):
            winnings += (rank + 1) * game[6]
        print(winnings)


    def two(self) -> None:
        games = [
            (CardGame(cg).part_two_hand_strength,
            self.card_values[CardGame(cg).cards[0]],
            self.card_values[CardGame(cg).cards[1]],
            self.card_values[CardGame(cg).cards[2]],
            self.card_values[CardGame(cg).cards[3]],
            self.card_values[CardGame(cg).cards[4]],
            int(CardGame(cg).bid)) for cg in self.data
        ]
        games.sort(key=lambda element: (element[0], element[1], element[2], element[3], element[4], element[5]))
        winnings = 0
        for rank, game in enumerate(games):
            winnings += (rank + 1) * game[6]
        print(winnings)


class CardGame:
    def __init__(self, game_string):
        self.cards = game_string[:5]
        self.bid = game_string[5:].strip()
        self._hand_strength()
        self._part_two_hand_strength()

    def _hand_strength(self):
        c = Counter(self.cards)
        counts = c.values()
        if 5 in counts:
            self.hand_strength = 7
        elif 4 in counts:
            self.hand_strength = 6
        elif 3 in counts and 2 in counts:
            self.hand_strength = 5
        elif 3 in counts:
            self.hand_strength = 4
        elif 2 == Counter(counts)[2]:
            self.hand_strength = 3
        elif 2 in counts:
            self.hand_strength = 2
        else:
            self.hand_strength = 1

    def _part_two_hand_strength(self):
        c = Counter(self.cards)
        counts = c.values()
        joker_count = c["J"]
        if 5 in counts or joker_count >= 4:
            self.part_two_hand_strength = 7
        elif 4 in counts or joker_count >= 3:
            self.part_two_hand_strength = 6
        elif (3 in counts and 2 in counts) or (joker_count == 1 and 2 == Counter(counts)[2]):
            self.part_two_hand_strength = 5
        elif 3 in counts or joker_count >= 2:
            self.part_two_hand_strength = 4
        elif (2 == Counter(counts)[2]) or (2 in counts and joker_count == 1):
            self.part_two_hand_strength = 3
        elif 2 in counts or joker_count >= 1:
            self.part_two_hand_strength = 2
        else:
            self.part_two_hand_strength = 1


if __name__ == "__main__":
    s = Solution()
    s.one()
    s.two()
