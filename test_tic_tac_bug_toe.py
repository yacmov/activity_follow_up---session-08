import unittest
from tic_tac_bug_toe import Main

class TestTicTacBugToe(unittest.TestCase):
    def setUp(self) -> None:
        """
        Purpose
        =======
        Initialise Testing class 

        Return
        ------
        None

        """
        self.test_game = Main()
    
    def test_is_win(self):
        """
        Purpose
        =======
        Testing winning valid condition and invalid condition
        """
        board_X = [['X', 'O', 'O'],
                       [' ', 'X', ' '],
                       [' ', ' ', 'X']]
        self.test_game.board = board_X
        self.assertTrue(self.test_game.is_win("X"))

        board_O = [['X', 'O', 'O'],
                       ['X', 'O', ' '],
                       ['O', 'X', ' ']]
        self.test_game.board = board_O
        self.assertTrue(self.test_game.is_win("O"))

        board_none = [['X', 'O', 'O'],
                        [' ', ' ', ' '],
                        [' ', 'X', ' ']]
        self.test_game.board = board_none
        self.assertFalse(self.test_game.is_win("O"))
        self.assertFalse(self.test_game.is_win("X"))

    def test_tally_wins(self):
        """
        Purpose
        =======
        Check counting of winning condition(True) from results list

        Examples
        --------
        .. code-block:: python
        
            results = [True, True, False, True, False]
            >>> 3
            results = [False, True, False, True, False]
            >>> 2

        """
        results = [True, True, False, True, False]
        self.assertEqual(self.test_game.tally_wins(results), 3)

if __name__ == "__main__":
    unittest.main()