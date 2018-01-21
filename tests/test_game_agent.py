"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)



    # def test_MinimaxPlayer_1(self):
    #
    #     minimaxPlayer = game_agent.MinimaxPlayer()
    #     self.game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 21]
    #     self.game._active_player = self.player1
    #     self.game._inactive_player = self.player2
    #     print ("location player 1 %s" % str(self.game.get_player_location(self.player1)))
    #     print ("location player 2 %s" % str(self.game.get_player_location(self.player2)))
    #     print(self.game.to_string())
    #     print (self.game._board_state)
    #     minimaxPlayer.minimax(self.game, 1)


    def test_MinimaxPlayer_center_distance(self):

        minimaxPlayer = game_agent.MinimaxPlayer()
        self.game._board_state = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 33]

        print(self.game.to_string())
        print (self.game._board_state)


        minimaxPlayer.minimax(self.game, 2)

if __name__ == '__main__':
    unittest.main()
