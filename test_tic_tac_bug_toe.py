import unittest
from tic_tac_bug_toe import *

class TestTicTacBugToe(unittest.TestCase):
    
    
    def test_is_win(self):
        board_X = [['X', 'O', 'O'],
                       [' ', 'X', ' '],
                       [' ', ' ', 'X']]
        self.assertTrue(self.is_win('X', board_X))

        board_O = [['X', 'O', 'O'],
                       ['X', 'O', ' '],
                       ['O', 'X', ' ']]
        self.assertTrue(self.is_win('O', board_O))

        board_none = [['X', 'O', 'O'],
                        [' ', ' ', ' '],
                        [' ', 'X', ' ']]
        self.assertFalse(self.is_win('X', board_none))
        self.assertFalse(self.is_win('O', board_none))

if __name__ == "__main__":
    unittest.main()