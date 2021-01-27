""""define the models for the different card games we want to simulate"""

import tensorflow as tf
import numpy as np


class GenericCardModel:
    """"class that concrete card models derive from"""

    def __int__(self):
        self.num_players = None
        self.num_locations = None
        self.num_cards = None
        self.num_turns = None
        self.current_state = None
        self.is_illegal = False

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
        """"return an int giving the score for this round"""
        # if an illegal action has been made, return negative score
        if self.is_illegal:
            return -1000
        # if terminal, return overall game score
        if self.terminal():
            return self.calculate_score()
        # else return no score change for round
        else:
            return 0

    def calculate_score(self) -> int:
        """given a terminal state, return the score for the player"""
        pass


class SimpleGame(GenericCardModel):
    def __init__(self):
        self.num_players = 2
        self.num_locations = 4
        self.num_cards = 4
        self.num_turns = 2
        self.current_state = None
        self.is_illegal = False

    def start_game(self):
        """
        Set the current state to the SimpleGame hardcoded initial state and return this state.
        :return: initial state as a tensor
        """
        self.current_state = tf.constant([[False, True, False, True],
                                          [True, False, True, False],
                                          [False, False, False, False],
                                          [False, False, False, False]], dtype=tf.bool)
        self.is_illegal = False
        return self.current_state

    def next_state(self, player_action):
        """update the state given this action, and return it"""
        # if action is illegal, set is_illegal attribute to True (will apply -ve reward) and choose first card in hand
        # get legal actions for player
        hands = [tf.gather(self.current_state, player) for player in range(self.num_players)]
        legal_actions = [tf.where(hand) for hand in hands]
        if player_action not in legal_actions[0]:
            self.is_illegal = True
            player_action = int(tf.gather(tf.gather(legal_actions, 0), 0))
        else:
            self.is_illegal = False

        # get opponent's action - play first card
        opponent_action = int(tf.gather(tf.gather(legal_actions, 1), 0))

        # get next state given actions
        # combine all actions
        actions = [player_action, opponent_action]
        # work out who wins the trick
        winner = max(enumerate(actions), key=lambda x: x[1])[0]
        # apply actions
        state_copy = self.current_state.numpy()
        for player in range(self.num_players):
            # print('Player {} is playing'.format(player))
            # remove card from hand
            # print('Remove card {} from player {}'.format(actions[player], player))
            state_copy[player, actions[player]] = False
            # place card into tricks of winning player
            # print('Give card {} to player {} in location {}'.format(actions[player], winner, winner + self.num_players))
            state_copy[winner + self.num_players, actions[player]] = True

        # set as current state
        self.current_state = tf.convert_to_tensor(state_copy)

        return self.current_state

    def terminal(self) -> bool:
        """return whether the current state is terminal"""
        # state is terminal if player has no cards in player's hand
        player_hand = tf.gather(self.current_state, 0)
        are_cards_left = bool(tf.math.reduce_any(player_hand))
        return not are_cards_left

    def calculate_score(self) -> int:
        """given a terminal state, return the score for the player"""
        player_tricks = tf.gather(self.current_state, 2)
        opponent_tricks = tf.gather(self.current_state, 3)
        player_score = int(tf.math.reduce_sum(tf.cast(player_tricks, dtype='int32'))) * 10 / self.num_players
        opponent_score = int(tf.math.reduce_sum(tf.cast(opponent_tricks, dtype='int32'))) * 10 / self.num_players
        score = player_score - opponent_score
        return score
