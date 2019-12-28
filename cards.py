
class Suit:
    """
    Object representing one of the 4 suits or no trumps.

    rank is used only for ordering suits as
    spades < clubs < diamonds < hearts < no trumps.

    The only card that should have the suit of no trumps is the joker before
    trumps is called.
    """
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def __repr__(self):
        if self.name == "H":
            return "♥"
        elif self.name == "C":
            return "♣"
        elif self.name == "S":
            return "♠"
        elif self.name == "D":
            return "♦"
        else:
            return ""

    def __lt__(self, other):
        return self.rank < other.rank


class Card:
    """
    Object representing one of 52 cards.

    card_suit is the suit that would appear on a card, while bower_suit is
    the effective suit of the card in play, which is only different for the
    bower and the joker after trumps is called.

    card_val is a value from 2 to 18 that represents the ordering of
    cards as 2-13, J, Q, K, A, Jok.

    trump_val is a value from 2 to 19 that is the same as the card_val if the
    card is not in the trumps suit, or represents the ordering of
    2-13, Q, K, A, J_other, J, Jok, if the card is in the trumps suit
    (using bower_suit) after trumps is called.

    is_trumps is updated to true when trumps is decided if the card is a
    member of the trumps suit

    val_string is a string representing the value (number) of the card.
    """
    def __init__(self, suit, card_val):
        self.card_suit = suit
        self.bower_suit = suit
        self.card_val = card_val
        self.trump_val = card_val
        self.is_trumps = False
        self.location = None

        # determine printable name of value
        if self.card_val < 2 or self.card_val > 19:
            raise Exception("invalid card value")
        if self.card_val <= 13:
            self.val_name = str(self.card_val)
        elif self.card_val == 14:
            self.val_name = "J"
        elif self.card_val == 15:
            self.val_name = "Q"
        elif self.card_val == 16:
            self.val_name = "K"
        elif self.card_val == 17:
            self.val_name = "A"
        elif self.card_val == 18:
            self.val_name = "JOKER"

        # determine printable name of card
        if self.card_val == 18:
            self.card_name = "JOK"
        else:
            self.card_name = "{}{}".format(self.val_name, self.card_suit)

    def changeToTrumps(self, trump_suit):
        """
        When trumps is decided, use this function to update trump_val for cards
        in the trump suit to allow easy ordering of cards, and bower_suit and
        trump_val for the bower and joker.
        """
        self.is_trumps = True
        if self.card_val == 14:
            self.trump_val = 18
            self.bower_suit = trump_suit
        elif 15 <= self.card_val <= 17:
            self.trump_val = self.card_val - 1
        elif self.card_val == 18:
            self.trump_val = 19
            self.bower_suit = trump_suit

    def moveCard(self, location):
        self.location = location

    def __repr__(self):
        """
        Define how cards are represented as strings.
        """
        return self.card_name

    def __lt__(self, other):
        """
        Define how cards are ordered, mostly for display. (Not game play).
        """
        return self.bower_suit < other.bower_suit or \
               (self.bower_suit == other.bower_suit and self.trump_val < other.trump_val)


class Hand:
    """
    Object representing a player's hand of cards.
    """
    def __init__(self, card_list, player):
        self.player_name = player.name
        self.card_list = []
        for card in card_list:
            card.location = player
            self.card_list.append(card)
        self.card_list.sort()

    def addCard(self, card):
        self.card_list.append(card)
        self.card_list.sort()

    def removeCard(self, card):
        self.card_list.remove(card)

    def __repr__(self):
        """
        Define how hands are printed.
        """
        return " ".join(["| {:>3} |".format(str(card)) for card in self.card_list])

    def printFullHand(self):
        """
        Prints hand neatly with large cards.
        """
        print("{}:".format(self.player_name))
        print(" ".join(["-------".format(card) for card in self.card_list]))
        print(" ".join(["|{:<5}|".format(str(card.val_name)) for card in self.card_list]))
        print(" ".join(["|{:^5}|".format(str(card.card_suit)) for card in self.card_list]))
        print(" ".join(["|{:>5}|".format(str(card.val_name)) for card in self.card_list]))
        print(" ".join(["-------".format(card) for card in self.card_list]))


notrumps = Suit("NT", 5)
hearts = Suit("H", 4)
diamonds = Suit("D", 3)
clubs = Suit("C", 2)
spades = Suit("S", 1)


# TESTING

# spades2 = Card(spades, 2)
# spades12 = Card(spades, 12)
# jok = Card(notrumps, 18)
#
# print(spades2)
# print(spades12)
# print(jok)




