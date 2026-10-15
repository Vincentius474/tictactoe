# Tic-Tac-Toe AI

A Tic-Tac-Toe game where you play against an unbeatable computer opponent. The AI uses the **Minimax algorithm** to pick the optimal move every turn, and the game runs in a simple **Pygame** window.

<img width="1918" height="1075" alt="screenshotA" src="https://github.com/user-attachments/assets/c1ea76d2-af56-4f40-984a-7a98e58461e7" />


## Features

- Choose to play as **X** or **O**
- Computer opponent that plays optimally (the best you can do is draw)
- Clickable graphical board
- Win/tie detection with a "Play Again" button

## Project Structure

```
.
├── tictactoe.py        # Game logic and Minimax AI
├── runner.py           # Pygame graphical interface
└── OpenSans-Regular.ttf  # Font used by the UI (you must supply this)
```

## Requirements

- Python 3.6+
- [Pygame](https://www.pygame.org/)
- The `OpenSans-Regular.ttf` font file, placed in the same directory as `runner.py`

Install Pygame with:

```bash
pip install pygame
```

## How to Run

```bash
python runner.py
```

1. Click **Play as X** or **Play as O**.
2. Click an empty square to make your move. X always goes first.
3. When the game ends, click **Play Again** to start a new game.

## How It Works

### Board representation

The board is a 3×3 list of lists. Each cell holds `"X"`, `"O"`, or `None` (empty).

### Functions in `tictactoe.py`

| Function | Description |
| --- | --- |
| `initial_state()` | Returns an empty board |
| `player(board)` | Returns whose turn it is (X moves first; X if counts are equal, otherwise O) |
| `actions(board)` | Returns the set of empty cells `(i, j)` available to play |
| `result(board, action)` | Returns a new board after the move, leaving the original untouched. Raises `ValueError` if the cell is already taken |
| `winner(board)` | Returns `"X"` or `"O"` if there is a three-in-a-row (rows, columns, diagonals), otherwise `None` |
| `terminal(board)` | Returns `True` if someone has won or the board is full |
| `utility(board)` | Returns `1` if X won, `-1` if O won, `0` for a tie |
| `minimax(board)` | Returns the optimal move for the current player, or `None` if the game is over |

### Minimax

The AI searches the full game tree recursively:

- **X** is the maximising player and picks the move leading to the highest value.
- **O** is the minimising player and picks the move leading to the lowest value.
- `max_value` and `min_value` alternate down the tree until a terminal board is reached, where `utility` gives the score.

Because Tic-Tac-Toe is small, the search covers every possible game without pruning. The first move of the game is the slowest, as the AI evaluates the whole tree.

## Notes

- The AI never loses, so the best outcome against it is a tie.
- `runner.py` will crash on startup if `OpenSans-Regular.ttf` is missing from the working directory.
- The interface handles input by polling mouse state each frame and uses short `time.sleep` pauses for button debouncing and the AI's "thinking" delay.

## Possible Improvements

- Add alpha-beta pruning to speed up the search.
- Add difficulty levels (e.g. random or limited-depth moves).
- Highlight the winning line when the game ends.
- Add unit tests for `winner`, `actions`, and `minimax`.

## License

MIT
