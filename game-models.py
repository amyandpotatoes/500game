""""define the models for the different card games we want to simulate"""

class GenericCardModel:
    """"class that concrete card models derive from"""

    def __int__(self):
        self.num_players = None
        self.num_locations = None
        self.num_cards = None
        self.current_state = None

    def start_game(self):
        """"set up the game, shuffle the cards etc and store in current state and return it"""
        pass

    def next_state(self, action):
        """"update the state given this action, and return it"""
        pass

    def terminal(self) -> bool:
        """"return whether the current state is terminal"""
        pass

    def reward(self) -> int:
        """"return an int giving the score at the end of the game"""
        score = 1
        if self.terminal():
            return self.calculate_score()
        else:
            return 0

    def calculate_score(self) -> int:
        """"given a terminal state, return the score for the player"""
        pass

class SimpleGame(GenericCardModel):
    def __init__(self):
        self.num_players = 2
        self.num_locations = 4
        self.num_cards = 10
        self.current_state = None