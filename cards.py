class Suit:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __repr__(self):
        return self.name


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.location = None

    def __lt__(self, other):
        return self.suit < other.suit \
               or (self.suit == other.suit and self.number < other.number)

    def __repr__(self):
        return "{} {}".format(self.number, self.suit)


class Hand:
    def __init__(self, card_list, player):
        self.card_list = []
        for card in card_list:
            card.location = player
            self.card_list.append(card)
        self.card_list.sort()

hearts = Suit("hearts", 4)
diamonds = Suit("diamonds", 3)
clubs = Suit("clubs", 2)
spades = Suit("spades", 1)

print(hearts)
print(diamonds)

spades2 = Card(spades, 2)

print(spades2)






