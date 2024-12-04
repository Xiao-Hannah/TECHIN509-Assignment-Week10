class Board:
    def __init__(self):
        # Initialize a 3x3 board
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def draw_board(self):
        """
        Draw the board of Tic-Tac-Toe game
        """
        for row in range(3):
            # Access the correct attribute: self.grid
            print("|".join(self.grid[row]))
            if row < 2:
                print("-" * 9)

    def update_board(self, row: int, col: int, symbol: str) -> bool:
        """
        Update the game board based on location selected by player

        Args:
            row (int): row index of board
            col (int): column index of board
            symbol (str): symbol used by player
        """
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self) -> str:
        """
        Check the winner of the current board.

        Returns:
        str: The winning symbol ('X' or 'O') if there is a winner, else an empty string.
        """
        # Check rows and columns
        for i in range(3):
            # Check rows
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != " ":
                return self.grid[i][0]
            # Check columns
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != " ":
                return self.grid[0][i]

        # Check diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " ":
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != " ":
            return self.grid[0][2]

        # No winner
        return ""


    def is_full(self) -> bool:
        """
        Check if the current board is full or not

        Returns:
            bool: Boolean outcome indicating whether the board is full
        """
        return all(cell != " " for row in self.grid for cell in row)


# # Example Usage
# if __name__ == "__main__":
#     board = Board()

#     # Update the board with some moves
#     board.update_board(0, 0, "X")
#     board.update_board(0, 1, "O")
#     board.update_board(0, 2, "X")
#     board.update_board(1, 1, "X")
#     board.update_board(2, 0, "O")
#     board.update_board(2, 2, "X")

#     # Draw the board
#     board.draw_board()

#     # Check for a winner
#     winner = board.check_winner()
#     print(f"Winner: {winner}" if winner else "No winner yet")

#     # Check if the board is full
#     print(f"Is the board full? {'Yes' if board.is_full() else 'No'}")