from .cards import Suit, Card, Hand


class Game:
    def __init__(self):
        raise NotImplementedError

    def initPlayers(self):
        raise NotImplementedError

    def runRound(self):
        raise NotImplementedError

    def displayResults(self):
        raise NotImplementedError


class Player:
    def __init__(self):
        raise NotImplementedError

    def addTrickToPlayer(self, trick):
        raise NotImplementedError


class Round:
    def __init__(self):
        raise NotImplementedError

    def dealCards(self):
        notrumps = Suit("NT", 5)
        hearts = Suit("H", 4)
        diamonds = Suit("D", 3)
        clubs = Suit("C", 2)
        spades = Suit("S", 1)

        raise NotImplementedError

    def runBidding(self):
        raise NotImplementedError

    def implementBiddingResults(self):
        """
        1. Assign trumps to cards.
        2. Assign roles to players.
        3. Give winner kitty and throw out cards.
        """
        raise NotImplementedError

    def runTrick(self):
        raise NotImplementedError

    def displayResults(self):
        raise NotImplementedError


class Bid:
    def __init__(self, suit, number, player):
        self.suit = suit
        self.number = number
        self.player = player
        if number == 0:
            self.bid_name = "Pass"
            self.is_pass = True
        else:
            self.bid_name = "{}{}".format(self.number, self.suit)
            self.is_pass = False

    def __repr__(self):
        """
        Define how bids are represented as strings.
        """
        return self.bid_name

    def __lt__(self, other):
        """
        Define how bids are ordered.
        """
        return self.number < other.number or \
               (self.number == other.number and self.suit < other.suit) or \
               self.is_pass


class BiddingRound:
    def __init__(self):
        self.winning_bid = Bid(None, 0, None)
        self.complete = False

    def addBid(self, bid):
        if bid > self.winning_bid:
            self.winning_bid = bid
            return 1
        elif bid.is_pass:
            return 1
        else:
            print("Bid too low, try again.")
            return 0

    def getWinningBid(self):
        return self.winning_bid


class Trick:
    """
    An object representing a trick that is either in progress or has been
    won by a particular player.
    """
    def __init__(self):
        raise NotImplementedError

    def addCardToTrick(self, card):
        raise NotImplementedError

    def findTrickWinner(self):
        raise NotImplementedError





