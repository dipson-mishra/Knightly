# Knightly Wiki

## Project Overview
Knightly is a Python-based chess evaluation and modeling engine focused on iterative development of chess-playing agents. The project starts with simple baselines and progressively adds stronger decision logic for move selection. It uses `python-chess` for legal move generation and board state management, and evolves models through scripts and notebooks.

## Current Iterations

### v0.1 — Random Baseline Agent
- Generates all legal moves from the current board state.
- Selects one move uniformly at random.
- Establishes a control baseline for comparing future model improvements.

### v0.2 — Material-Based Evaluation Agent
- Evaluates candidate moves by resulting material balance.
- Uses classical piece weights to estimate position strength:
  - Pawn = 1
  - Knight = 3
  - Bishop = 3
  - Rook = 5
  - Queen = 9
  - King = non-capturable (no finite trade value in standard play)
- Selects the move with the best immediate material outcome, without deeper search.

## High-Level Architecture
Knightly is organized around a lightweight, iterative architecture:

1. **Position Input**
   - Board positions are represented in FEN format.
   - Datasets provide position-level records for experimentation.

2. **Move Generation Layer**
   - `python-chess` generates legal moves and validates rules (castling, en passant, promotion).

3. **Evaluation Layer**
   - v0.1: no evaluation (random choice).
   - v0.2: static, material-based scoring for candidate positions.

4. **Move Selection Layer**
   - Chooses a legal move based on the active evaluation strategy.

5. **Experimentation Interfaces**
   - Notebooks for exploratory work.
   - Modular scripts for repeatable runs.

## Repository Layout

```text
Knightly/
├── data/
│   ├── raw/
│   │   ├── train.csv
│   │   └── test.csv
│   └── processed/
├── notebooks/
│   ├── v0.1-random.ipynb
│   └── v0.2-material.ipynb
├── src/
│   ├── data/
│   ├── evaluation/
│   └── models/
│       ├── v0.1-random.py
│       └── v0.2-material.py
├── tests/
├── README.md
└── requirements.txt
```

## Related Wiki Pages
- [Getting Started](Getting-Started)
- [Model Iterations & Design](Model-Architecture)
- [Development & Contribution Guide](Contributing)
