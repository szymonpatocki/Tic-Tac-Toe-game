# Tic-Tac-Toe Game ❌⭕

## Features

✅ **Two-player mode**: Players can take turns and play against each other.  
✅ **Board display**: The game board is displayed after each move.  
✅ **Winning conditions**: The game detects and announces a winner or if the game ends in a draw.  
✅ **Game loop**: The game will continue until a player wins or the board is full, leading to a draw.  

## Game Rules
- The board consists of 9 cells (3x3 grid).
- Players take turns to mark their moves as X or O.
- The first player to get 3 of their marks in a row, column, or diagonal wins.
- If the board is full and no player has won, the game ends in a draw.

## Code Structure
▶ tic_tac_toe.py: The main Python file where the game logic is implemented.  
▶ display_board(): Function to display the game board after each move.  
▶ check_winner(): Function to check for winning conditions.  
▶ take_turn(): Function that handles player moves and alternating turns.  
▶ is_board_full(): Function to check if the board is full and if the game ends in a draw.  

## Example Usage
Running the game:  
$ python tic_tac_toe.py  
Player X, enter your move (1-9): 1  
Player O, enter your move (1-9): 5  
Player X, enter your move (1-9): 9  
Player O, enter your move (1-9): 2  
Player X, enter your move (1-9): 3  
Player X wins!  
In this example, Player X wins by completing a row.  
