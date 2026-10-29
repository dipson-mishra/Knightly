<h1 align="center">♞ Knightly</h1>

<p align="center">
  <i>Too many blunders, not enough brain cells, so I am building an AI to do the suffering for me.</i>
</p>

<p align="center">
  <img alt="Status" src="https://img.shields.io/badge/status-blundering-red">
  <img alt="Elo" src="https://img.shields.io/badge/Elo-still%20loading...-yellow">
  <img alt="Made with" src="https://img.shields.io/badge/made%20with-pain%20%26%20Python-blue">
</p>

> *"If I don't kill myself tonight, I'm gonna live a thousand years."*
> — **Grandmaster Ivan Sokolov**

---

## About

Knightly is a chess AI project built out of a simple, painful realization: I hang my queen far too often. Instead of getting better at chess like a normal person, I decided to teach a machine to do it for me.

## Goal

To create **Temu Magnus Carlsen**

---

## ✨ Features

- [x] Legal move generation and full rule handling via `python-chess` (castling, en passant, promotion)
- [x] Random move bot (Day 1)
- [x] Basic position evaluation using material count (Day 2)
- [x] Material evaluation with minimax and alpha-beta pruning (Day 3)
- [ ] Play against the AI interactively
- [ ] Difficulty levels, from "Temu Beginner" to "Temu Magnus"
- [ ] Game history and move logging (PGN support)
- [ ] Blunder detection, so it can tell me exactly how badly I played

---

## Tech Stack

| Area | Tools |
|------|-------|
| Language | Python |
| Chess logic | `python-chess` |
| AI / ML | Material evaluation, minimax, alpha-beta pruning; `TensorFlow` in the Day 2 experiment |
| Environment | IPython / Jupyter |
| Interface | IPython board display (for now) |

---

## Getting Started

### Prerequisites

- Python 3.x
- Dependencies listed in `requirements.txt`

### Installation

```bash
# Clone the repository
git clone https://github.com/dipson-mishra/Knightly.git
cd Knightly

# Create and activate a virtual environment
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

## Repository Structure

```text
Knightly/
├── data/
│   ├── raw/
│   │   ├── train.csv
│   │   └── test.csv
│   └── processed/
├── notebooks/
│   ├── v0.1-random.ipynb
│   ├── v0.2-material.ipynb
│   └── v0.3-minmax-eval.ipynb
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── v0.1-random.py
│   │   ├── v0.2-material.py
│   │   └── v0.3-minmax-eval.py
│   ├── data/
│   │   └── __init__.py
│   └── evaluation/
│       └── __init__.py
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Scripts

Run from the repository root so relative paths resolve correctly:

```bash
python src/models/v0.1-random.py
python src/models/v0.2-material.py
python src/models/v0.3-minmax-eval.py
```

The minimax bot plays Black against a human as White. Set the search depth with
`--depth` (default: 3):

```bash
python src/models/v0.3-minmax-eval.py --depth 4
```

## Running Notebooks

1. Start Jupyter from repository root:

```bash
jupyter notebook
```

2. Open notebooks in `notebooks/`:
   - `notebooks/v0.1-random.ipynb`
   - `notebooks/v0.2-material.ipynb`
   - `notebooks/v0.3-minmax-eval.ipynb`


| Day 1: Random bot | Day 2: Material bot | Day 3: Min-Max Evaluation bot
|:---:|:---:|:---:|
| <img width="320" alt="Day 1 board: random move bot" src="https://github.com/user-attachments/assets/0c94802a-9a44-4f19-9bb8-4ef43e560b8b"> | <img width="320" alt="Day 2 board: material evaluation bot" src="https://github.com/user-attachments/assets/15589783-2084-4f68-bc8a-d3ae87c57c22"> <img width="545" height="631" alt="image" src="https://github.com/user-attachments/assets/56ba70da-e800-46d3-9e93-146362fc08a4" />


To explore the notebooks, start Jupyter from the repository root:

```bash
jupyter notebook
```

Then open any notebook in `notebooks/`, including `notebooks/v0.3-minmax-eval.ipynb`.

---

## How It Works

1. **Board representation**: handled by `python-chess`
2. **Evaluation**: material balance from White's perspective (pawn = 100, knight = 320, bishop = 330, rook = 500, queen = 900)
3. **Search**: minimax explores possible moves to a configurable depth; alpha-beta pruning skips branches that cannot change the result
4. **Move selection**: the AI plays Black and chooses a move that minimizes White's evaluation

---

## Dev Log

| Day | Progress | Status |
|-----|----------|--------|
| 1 | Built a random-move bot using `random`, `python-chess`, and IPython. It picks any move from the legal moves list. | Significantly weak |
| 2 | Built a material-evaluation bot using `tensorflow`, `python-chess`, and IPython. It calculates material for each legal move and plays the best one. | Weak, but no longer a lottery |
| 3 | Added material-based minimax with alpha-beta pruning and a configurable search depth. | Thinking several moves ahead |

---

## Roadmap

- [x] Day 1: play legal moves (legal, but bad)
- [x] Day 2: play moves chosen by material evaluation (better than a lottery, but far from good)
- [x] Day 3: add lookahead search (minimax with alpha-beta pruning)
- [ ] Get the engine to stop hanging its own queen
- [ ] Beat a random-move bot consistently
- [ ] Beat me
- [ ] Beat a friend who "plays casually"
- [ ] Reach Temu Magnus status

---

## Contributing

Pull requests are welcome. Bug reports too, as long as they are not just "it beat me again."

1. Fork the repo
2. Create a branch (`git checkout -b feature/better-endgames`)
3. Commit your changes
4. Open a pull request

---

## ⚠️ Disclaimer

Knightly is not affiliated with Magnus Carlsen, Stockfish, or anyone's chess rating. Any resemblance to a grandmaster is purely coincidental and probably wishful thinking.

---

<p align="center"><i>Made with ❤️, ☕, and an unreasonable number of blunders.</i></p>
