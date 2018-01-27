"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


# global variables:
# unit_test if false then it can be submitted, otherwise is for local debugging
unit_test = True
unit_test = False


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def get_moves_players(game, player):
    global unit_test
    if unit_test == True:
        debug = True
    else:
        debug = False

    own_player = player
    opponent_player = game.get_opponent(own_player)

    own_moves = len(game.get_legal_moves(own_player))
    opp_moves = len(game.get_legal_moves(opponent_player))

    # if debug:
    #     print ("own    player %s location %s act moves %s" % (
    #     own_player,   str(game.get_player_location(own_player)),   own_moves))
    #     print ("oppone player %s location %s opp moves %s" % (
    #     opponent_player, str(game.get_player_location(opponent_player)), opp_moves))

    return own_moves, opp_moves

def open_move_score(game, player):
    """The basic evaluation function described in lecture that outputs a score
    equal to the number of moves open for your computer player on the board.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state
    """
    # if game.is_loser(player):
    #     return float("-inf")
    #
    # if game.is_winner(player):
    #     return float("inf")

    return float(len(game.get_legal_moves(player)))


def improved_score(game, player):

    """The "Improved" evaluation function discussed in lecture that outputs a
    score equal to the difference in the number of moves available to the
    two players.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state
    """

    global unit_test
    if unit_test == True:
        debug = True
    else:
        debug = False


    # if game.is_loser(player):
    #     return float("-inf")
    #
    # if game.is_winner(player):
    #     return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))


    # if debug: print("improved_score ")
    # if debug: print("\t own_moves %s" % own_moves)
    # if debug: print("\t opp_moves %s" % opp_moves)
    # if debug: print("\t own_moves %s - opp_moves %s = %s"  % (own_moves, opp_moves, own_moves - opp_moves))
    return float(own_moves - opp_moves)


def center_score(game, player):
    """Outputs a score equal to square of the distance from the center of the
    board to the position of the player.

    This heuristic is only used by the autograder for testing.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state
    """
    # if game.is_loser(player):
    #     return float("-inf")
    #
    # if game.is_winner(player):
    #     return float("inf")

    w, h = game.width / 2., game.height / 2.
    y, x = game.get_player_location(player)
    #y, x = game.get_player_location(game.get_opponent(player))
    return float((h - y)**2 + (w - x)**2)


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    global unit_test
    if unit_test == True:
        debug = True
    else:
        debug = False

    # TODO: finish this function!
    # if game.is_loser(player):
    #     return float("-inf")
    # if game.is_winner(player):
    #     return float("inf")



    _open_move_score = open_move_score(game, player)
    _improved_score = improved_score(game, player)
    _center_distance = center_score(game, player)

    #return max(open_move_score*0.2, improved_score*0.4, center_distance*0.4)
    # if debug: print("_open_move_score %s" % _open_move_score)
    # if debug: print("_improved_score %s" % _improved_score)
    # if debug: print("_center_distance %s" % _center_distance)
    # if debug: print("_open_move_score + _improved_score + _center_distance %s" % (_open_move_score + _improved_score + _center_distance ))
    return (_open_move_score + _improved_score + _center_distance )






    #raise NotImplementedError


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")
    if game.is_winner(player):
        return float("inf")

    global unit_test
    if unit_test == True:
        debug = True
    else:
        debug = False

    _open_move_score = open_move_score(game, player)
    #if debug: print("open_move_score %s" % _open_move_score)

    _improved_score = improved_score(game, player)
    #if debug: print("improved_score %s" % _improved_score)

    _center_distance = center_score(game, player)
    #if debug: print("center_distance %s" % _center_distance)
    # return max(open_move_score*0.2, improved_score*0.4, center_distance*0.4)
    return (game.utility(player) + _open_move_score*0.2 + _improved_score*0.3 + _center_distance*0.5)


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    global unit_test
    if unit_test == True:
        debug = True
    else:
        debug = False

    if game.is_loser(player):
        return float("-inf")
    if game.is_winner(player):
        return float("inf")

    _open_move_score = open_move_score(game, player)
    #if debug: print("open_move_score %s" % _open_move_score)

    _improved_score = improved_score(game, player)
    #if debug: print("improved_score %s" % _improved_score)

    _center_distance = center_score(game, player)
    #if debug: print("center_distance %s" % _center_distance)
    # return max(open_move_score*0.2, improved_score*0.4, center_distance*0.4)
    return (_open_move_score*2 + _improved_score*2 + _center_distance*3)


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout








class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """
    global unit_test
    if unit_test == True:
        debug = True
    else:
        debug = False


    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    # def score(self, gameState):
    #     return len(gameState.get_legal_moves())

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """

        global unit_test
        if unit_test == True:
            debug = True
        else:
            debug = False

        self.search_depth = depth


        # if debug: print ("game.active_player %s" %game.active_player)
        # if debug: print("player_location %s" % str(game.get_player_location(game.active_player)))
        # if debug: print("board state %s" % (game._board_state))
        # if debug: print ("self.search_depth %s" %self.search_depth)

        if unit_test == False:
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()



        # TODO: finish this function!
        #raise NotImplementedError


        gameState = game
        player_turn = game.active_player
        best_score = float("-inf")
        best_move = None #gameState.get_legal_moves()[0]#None
        aux_depth = 1

        first = True

        legal_moves = gameState.get_legal_moves()
        if not legal_moves:
            if debug: print ("NO legal Moves")
            return (-1, -1)

        # legal_moves = len(gameState.get_legal_moves())
        # if legal_moves == 0:
        #     if debug: print ("NO legal Moves")
        #     return (-1,-1)
        else:
            #if debug: print ("THERE ARE legal Moves")
            #get_moves_players(game, player_turn)
            for move in gameState.get_legal_moves():

                #if debug: print ("\nEvaluating move %s" %str(move))
                if debug: print ("\nEvaluating move %s aux_depth %s" % (str(move), aux_depth))
                if first == True:
                    best_move = move
                    first = False

                #aux_depth = 0
                value = self.min_value(gameState.forecast_move(move), aux_depth, player_turn)#, depth, aux_depth)
                #if debug: print ("%s move %s value %s" % (gameState.active_player, str(move), value))
                #if debug: print ("value:", value)
                if value > best_score:
                    best_score = value
                    best_move = move

            #if debug: print ("%s best_move %s best_score %s" % (gameState.active_player, str(best_move), best_score))


            return best_move


    def min_value(self, gameState, aux_depth, player_turn):#, depth, aux_depth):

        global unit_test
        if unit_test == True:
            debug = True
        else:
            debug = False

        if unit_test == False:
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
        """Return the value for a win (+1) if the game is over, otherwise return the minimun value over  all legas child nodes"""

        aux_depth += 1
        left_places = len(gameState.get_legal_moves())
        if left_places <= 0 or aux_depth > self.search_depth:
            value = self.score(gameState, player_turn)  # len(gameState.get_legal_moves())
            return value
        value =  float("inf")
        for legal_move in gameState.get_legal_moves():
            if debug: print ("\nmin_value Evaluating move %s aux_depth %s" % (str(legal_move), aux_depth))
            value =  min(value, self.max_value(gameState.forecast_move(legal_move), aux_depth, player_turn))#, depth, aux_depth))

        return value

    def max_value(self, gameState, aux_depth, player_turn):#, depth,  ):
        global unit_test
        if unit_test == True:
            debug = True
        else:
            debug = False

        if unit_test == False:
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
        """Return the value for a loss (+1) if the game is over, otherwise return the maximun value over  all legal child nodes"""

        aux_depth += 1
        left_places = len(gameState.get_legal_moves())
        if left_places <= 0 or aux_depth > self.search_depth:
            value = self.score(gameState, player_turn)  # len(gameState.get_legal_moves())
            return value
        value =  float("-inf")
        for legal_move in gameState.get_legal_moves():
            if debug: print ("\nmax_value Evaluating move %s aux_depth %s" % (str(legal_move), aux_depth))
            value = max(value, self.min_value(gameState.forecast_move(legal_move), aux_depth, player_turn))#, depth, aux_depth))
            #if debug: print ("max_value %s move %s" %(value,str(legal_move)))
        return value

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.
        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.
        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************
        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).
        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.
        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        self.time_left = time_left

        global unit_test
        if unit_test == True:
            debug = True
        else:
            debug = False

        if unit_test == False:
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

        # TODO: finish this function!
        # raise NotImplementedError

        gameState = game
        aux_depth = 0

        if len(gameState.get_legal_moves(self)) > 0:
            best_move = gameState.get_legal_moves(self)[0]
        else:
            best_move = (-1, -1)

        try:
            while True:
                aux_depth += 1
                move = self.alphabeta(gameState, aux_depth)
                if move == (-1, -1):
                    break
                else:
                    best_move = move

        finally:
            return best_move

    def min_value(self, game, aux_depth, alpha, beta):

        global unit_test
        if unit_test == True:
            debug = True
        else:
            debug = False

        if unit_test == False:
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

        best_move = (-1, -1)

        left_places = len(game.get_legal_moves())

        if left_places <= 0 or aux_depth <= 0:  # end reached
            value = self.score(game, self)
            return value, best_move

        value = float("inf")

        aux_depth += -1

        for move in game.get_legal_moves():
            value_aux = self.max_value(game.forecast_move(move), aux_depth, alpha, beta)
            if value_aux[0] < value:
                value, _ = value_aux
                best_move = move
            if value <= alpha:
                return (value, best_move)
            beta = min(beta, value)
        return (value, best_move)

    def max_value(self, game, aux_depth, alpha, beta):

        global unit_test
        if unit_test == True:
            debug = True
        else:
            debug = False

        if unit_test == False:
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

        best_move = (-1, -1)

        left_places = len(game.get_legal_moves())
        if left_places <= 0 or aux_depth <= 0:  # end reached
            value = self.score(game, self)
            return value, best_move

        value = float("-inf")

        aux_depth += -1

        for move in game.get_legal_moves():
            value_aux = self.min_value(game.forecast_move(move), aux_depth, alpha, beta)
            if value_aux[0] > value:
                value, _ = value_aux
                best_move = move
            if value >= beta:
                return (value, best_move)
            alpha = max(alpha, value)
        return (value, best_move)


    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.
        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md
        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************
        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state
        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting
        alpha : float
            Alpha limits the lower bound of search on minimizing layers
        beta : float
            Beta limits the upper bound of search on maximizing layers
        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves
        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.
            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        global unit_test
        if unit_test == True:
            debug = True
        else:
            debug = False

        if unit_test == False:
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

        return self.max_value(game, depth, alpha, beta)[1]
