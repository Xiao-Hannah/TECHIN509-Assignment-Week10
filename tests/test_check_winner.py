import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from models.board import Board

class TestCheckWinner(unittest.TestCase):
    def setUp(self):
        # Initialize a fresh board before each test
        self.board = Board()

    def test_no_winner(self):
        # Test a game with no winners (empty board)
        self.board.grid = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.assertEqual(self.board.check_winner(), "")

        # Test a game with no winners (random placements)
        self.board.grid = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "O"]
        ]
        self.assertEqual(self.board.check_winner(), "")

    def test_row_winner(self):
        # Test a winner in a row
        self.board.grid = [
            ["X", "X", "X"],
            ["O", "O", " "],
            [" ", " ", " "]
        ]
        self.assertEqual(self.board.check_winner(), "X")

        self.board.grid = [
            ["O", "O", "O"],
            ["X", " ", "X"],
            [" ", " ", "X"]
        ]
        self.assertEqual(self.board.check_winner(), "O")

    def test_column_winner(self):
        # Test a winner in a column
        self.board.grid = [
            ["X", "O", " "],
            ["X", "O", " "],
            ["X", " ", " "]
        ]
        self.assertEqual(self.board.check_winner(), "X")

        self.board.grid = [
            ["O", "X", " "],
            ["O", "X", " "],
            ["O", " ", "X"]
        ]
        self.assertEqual(self.board.check_winner(), "O")

    def test_diagonal_winner(self):
        # Test a winner in the main diagonal
        self.board.grid = [
            ["X", "O", " "],
            ["O", "X", " "],
            [" ", " ", "X"]
        ]
        self.assertEqual(self.board.check_winner(), "X")

        # Test a winner in the anti-diagonal
        self.board.grid = [
            ["O", "X", "X"],
            ["X", "O", " "],
            ["X", " ", "O"]
        ]
        self.assertEqual(self.board.check_winner(), "O")

    def test_incomplete_game(self):
        # Test an incomplete game (no winner, spaces remaining)
        self.board.grid = [
            ["X", "O", " "],
            ["O", "X", " "],
            [" ", "O", "X"]
        ]
        self.assertEqual(self.board.check_winner(), "")

        # Another example of incomplete game
        self.board.grid = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", " "]
        ]
        self.assertEqual(self.board.check_winner(), "")

if __name__ == "__main__":
    unittest.main()
