import game-models.py

from tensorforce.environment import Environment

import numpy as np # leave this to stop errors in scaffold for now

class CardEnvironment(Environment):

    def __init__(self):
        super().__init__()
        self.card_game = SimpleGame() # TODO: can choose other cardgames - pass as param?

    def states(self):
        # num_locations is the number of places card can be - number of players + 1
        # true if the card is in that location
        return dict(type='bool', shape=(self.card_game.num_locations, self.card_game.num_cards))

    def actions(self):
        return dict(type='int', num_values=self.card_game.num_cards)

    # Optional: should only be defined if environment has a natural fixed
    # maximum episode length; otherwise specify maximum number of training
    # timesteps via Environment.create(..., max_episode_timesteps=???)
    def max_episode_timesteps(self):
        return super().max_episode_timesteps()

    # Optional additional steps to close environment
    def close(self):
        super().close()

    def reset(self):
        state = np.random.random(size=(8,))
        return state

    def execute(self, action):
        next_state = np.random.random(size=(8,))
        terminal = np.random.random() < 0.5
        reward = np.random.random()
        return next_state, terminal, reward


