# Rock, Paper, Scissors (Best out of 3)

A robust command-line implementation of the classic Rock, Paper, Scissors game built with Python. The game tracks scores dynamically and runs until either the player or the computer wins three rounds.

## Key Features
- **Match State Management:** Implements a stateful `while` loop that handles cumulative scoring up to a "Best out of 3" threshold.
- **Graceful Exit Option:** Players can type `quit` or `q` at any prompt to terminate the session immediately.
- **Decoupled Architecture:** Core game rules are separated into a pure function (`determine_winner`), making the codebase highly maintainable and testable.
- **Automated Testing:** Covered by a suite of unit tests verifying all logical combinations (wins, losses, and ties).

## Skills Highlighted
- Python Unit Testing (`unittest`)
- Input parsing and normalization (`.lower()`, `.startswith()`)
- String formatting and logical branching

---

## How to Run the Game
```bash
python rock_paper_scissors.py
```

## How to Run the Test
Validate the game logic automatically using Python's built-in test framework:
```bash
python -m unittest test_game.py
```

