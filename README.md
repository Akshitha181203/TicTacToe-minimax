# TicTacToe with AI

A classic Tic-Tac-Toe game where you play against a computer AI powered by the Minimax algorithm. The AI explores all possible future moves to choose the optimal play, making it very challenging to beat.

## Features

- Human vs. Computer gameplay  
- Computer AI implemented with the Minimax algorithm for perfect play  
- Simple, console-based interface  
- Single-file implementation (`main.py`)  

## How It Works

The Minimax algorithm is a recursive decision-making process that simulates every possible move (and counter-move) from the current board state. It scores terminal states—win (+1), loss (−1), or draw (0)—and back-propagates these scores to choose the move that maximizes the computer’s chance of winning while minimizing yours.

## Installation & Usage

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Akshitha181203/TicTacToe-minimax.git
   cd TicTacToe-minimax
   ```
2. **Ensure you have Python 3 installed**
   ```bash
   python3 --version
   ```
3. **Run the game**
   ```bash
   python3 main.py
   ```
4. **Play**
   1.  The board is numbered rows and columns (1–3).
   2.  When prompted, enter your move as two numbers separated by space (e.g., `2 3`).
   3.  The AI will automatically make its move.  

## File Structure
```text
TicTacToe-minimax/
├── main.py    # Game logic + Minimax algorithm
└── README.md  # Project overview & instructions
```
