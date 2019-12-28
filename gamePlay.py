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
    def __init__(self):
        raise NotImplementedError


class BiddingRound:
    def __init__(self):
        raise NotImplementedError

    def addBid(self, bid):
        raise NotImplementedError

    def getTrumpsFromBids(self):
        raise NotImplementedError

    def getWinnerFromBids(self):
        raise NotImplementedError


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





