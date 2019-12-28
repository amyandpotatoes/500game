from cards import Suit, Card, Hand

from itertools import chain
from random import shuffle


class Game:
    def __init__(self, type="500", player_count=4, teams={}):
        # type can be "single" or "500"
        if type == "500" or type == "single":
            self.type = type
        else:
            raise Exception("invald type parameter for game")
        # player_count can be 3, 4, 5 or 6
        self.player_count = player_count
        # teams is a dictionary of teams and their members
        self.teams = teams
        # players is a list of players in the order they play
        if not teams:
            teams[0] = [0,2]
            teams[1] = [1,3]
        self.players = range(player_count)
        self.players = []
        # deck is a list of cards, decided by the number of players
        self.deck = []

    def initGame(self):
        raise NotImplementedError

    def initPlayers(self):
        raise NotImplementedError

    def initDeck(self):
        # first fill deck

        # 16 picture cards + joker, number cards have card values 2-13, picture
        # cards have card values 14-17, joker has card value 18

        red_cards = None
        black_cards = None

        while not red_cards or not black_cards:
            if self.player_count == 3:
                # need 33 cards total, so 16 number cards, red 7-10, black 7-10
                red_cards = list(chain(range(7, 11), range(14, 18)))
                black_cards = list(chain(range(7, 11), range(14, 18)))
            elif self.player_count == 4:
                # need 43 cards in total, so 26 number cards, red 4-10, black 5-10
                red_cards = list(chain(range(4, 11), range(14, 18)))
                black_cards = list(chain(range(5, 11), range(14, 18)))
            elif self.player_count == 5:
                # need 53 cards in total, full regular deck (2-10)
                red_cards = list(chain(range(2, 11), range(14, 18)))
                black_cards = list(chain(range(2, 11), range(14, 18)))
            elif self.player_count == 6:
                # need 63 cards in total, so 46 number cards, red 2-13, black 3-13
                red_cards = list(range(2, 18))
                black_cards = list(range(3, 18))
            else:
                raise Exception("Please choose a number of players between 3 and 6.")

        # create notrumps suit and cards (joker and no-trumps bids)
        notrumps = Suit("NT", 5)
        self.deck.append(Card(notrumps, 18))

        # create suits and cards and add to deck
        hearts = Suit("H", 4)
        self.deck.extend([Card(hearts, val) for val in red_cards])
        diamonds = Suit("D", 3)
        self.deck.extend([Card(diamonds, val) for val in red_cards])
        clubs = Suit("C", 2)
        self.deck.extend([Card(clubs, val) for val in black_cards])
        spades = Suit("S", 1)
        self.deck.extend([Card(spades, val) for val in black_cards])

    def runRound(self):
        raise NotImplementedError

    def displayResults(self):
        raise NotImplementedError


class Player:
    def __init__(self, name):
        self.name = name

    def addTrickToPlayer(self, trick):
        raise NotImplementedError


class Round:
    def __init__(self, players, player_count, teams, deck):
        self.players = players
        self.player_count = player_count
        self.teams = teams
        self.hands = []
        self.kitty = None
        self.deck = deck.deepcopy()

    def dealCards(self):
        # shuffle deck
        shuffle(self.deck)

        # next, create hands
        for player in self.players:
            dealt_cards = self.deck[-10:]
            del self.deck[-10:]
            self.hands.append(Hand(dealt_cards, player))
        self.kitty = Hand(self.deck, Player("kitty"))

        for hand in self.hands:
            hand.printFullHand()

        self.kitty.printFullHand()

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


a = Player("A")
b = Player("B")
c = Player("C")
d = Player("D")

round1 = Round([a, b, c, d], 4, {"team1": [a, c], "team2": [b, d]})

round1.dealCards()



