import gameModels

from tensorforce.environments import Environment
import numpy as np # leave this to stop errors in scaffold for now


class CardEnvironment(Environment):

    def __init__(self):
        super().__init__()
        self.card_game = gameModels.SimpleGame()  # TODO: can choose other cardgames - pass as param?

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
        return self.card_game.num_turns

    # Optional additional steps to close environment
    def close(self):
        super().close()

    def reset(self):
        state = self.card_game.start_game()
        return state

    def execute(self, action):
        next_state = self.card_game.next_state(action)
        terminal = self.card_game.terminal()
        reward = self.card_game.reward()
        return next_state, terminal, reward


