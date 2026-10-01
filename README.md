<h1 align="center">♞ Knightly</h1>

<p align="center">
  <i>Too many blunders, not enough brain cells, so I built an AI to do the suffering for me.</i>
</p>

<p align="center">
  <img alt="Status" src="https://img.shields.io/badge/status-blundering-red">
  <img alt="Elo" src="https://img.shields.io/badge/Elo-still%20loading...-yellow">
  <img alt="Made with" src="https://img.shields.io/badge/made%20with-pain%20%26%20Python-blue">
</p>

> *"If I don't kill myself tonight, I'm gonna live a thousand years."*
> — **Grandmaster Ivan Sokolov**

---

## 📖 About

Knightly is a chess AI project built out of a simple, painful realization: I hang my queen far too often. Instead of getting better at chess like a normal person, I decided to teach a machine to do it for me.

## 🎯 Goal

To create **Temu Magnus Carlsen**: not the real thing, but it looks similar from far away and occasionally wins games.

---

## ✨ Features

- [x] Legal move generation and full rule handling via `python-chess` (castling, en passant, promotion)
- [x] Random move bot (Day 1)
- [x] Basic position evaluation using material count (Day 2)
- [ ] Move search (minimax / alpha-beta pruning)
- [ ] Play against the AI interactively
- [ ] Difficulty levels, from "Temu Beginner" to "Temu Magnus"
- [ ] Game history and move logging (PGN support)
- [ ] Blunder detection, so it can tell me exactly how badly I played

---

## 🛠️ Tech Stack

| Area | Tools |
|------|-------|
| Language | Python |
| Chess logic | `python-chess` |
| AI / ML | `TensorFlow` |
| Environment | IPython / Jupyter |
| Interface | IPython board display (for now) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `python-chess`
- `tensorflow`
- `ipython`

### Installation

```bash
# Clone the repository
git clone https://github.com/dipson-mishra/Knightly.git
cd Knightly

# Install dependencies
pip install chess tensorflow ipython
```


## 🎮 Usage

| Day 1: Random bot | Day 2: Material bot |
|:---:|:---:|
| <img width="320" alt="Day 1 board: random move bot" src="https://github.com/user-attachments/assets/0c94802a-9a44-4f19-9bb8-4ef43e560b8b"> | <img width="320" alt="Day 2 board: material evaluation bot" src="https://github.com/user-attachments/assets/15589783-2084-4f68-bc8a-d3ae87c57c22"> |

---

## 🧠 How It Works

1. **Board representation**: handled by `python-chess`
2. **Evaluation**: material count (pawn = 1, knight/bishop = 3, rook = 5, queen = 9)
3. **Search / learning**: none yet
4. **Move selection**: scores every legal move by the resulting material balance and plays the highest

---

## 📅 Dev Log

| Day | Progress | Status |
|-----|----------|--------|
| 1 | Built a random-move bot using `random`, `python-chess`, and IPython. It picks any move from the legal moves list. | Significantly weak |
| 2 | Built a material-evaluation bot using `tensorflow`, `python-chess`, and IPython. It calculates material for each legal move and plays the best one. | Weak, but no longer a lottery |

---

## 🗺️ Roadmap

- [x] Day 1: play legal moves (legal, but bad)
- [x] Day 2: play moves chosen by material evaluation (better than a lottery, but far from good)
- [ ] Day 3: add lookahead search (minimax)
- [ ] Get the engine to stop hanging its own queen
- [ ] Beat a random-move bot consistently
- [ ] Beat me
- [ ] Beat a friend who "plays casually"
- [ ] Reach Temu Magnus status

---

## 🤝 Contributing

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
