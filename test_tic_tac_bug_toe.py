import unittest
from tic_tac_bug_toe import Main

class TestTicTacBugToe(unittest.TestCase):
    def setUp(self) -> None:
        self.test_game = Main()
    
    def test_is_win(self):
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
        results = [True, True, False, True, False]
        self.assertEqual(self.test_game.tally_wins(results), 3)

if __name__ == "__main__":
    unittest.main()