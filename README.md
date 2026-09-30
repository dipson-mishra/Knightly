# ♞ Knightly
> Project Philosophy:<br>
> <em> " If I don't kill myself tonight, I'm gonna live a thousand years." — Grandmaster Ivan Sokolov</em>



![Status](https://img.shields.io/badge/status-blundering-red)
![Elo](https://img.shields.io/badge/Elo-still%20loading...-yellow)
![Made with](https://img.shields.io/badge/made%20with-pain%20%26%20Python-blue)

---

## 📖 About

Knightly is a chess AI project built out of a simple, painful realization: I hang my queen far too often. Instead of getting better at chess like a normal person, I decided to teach a machine to do it for me.

## 🎯 Goal

To create **temu Magnus Carlsen**.

---

## ✨ Features

- [x] Legal move generation and full rule handling via `python-chess` (castling, en passant, promotion)
- [x] Random move bot: picks a move from the legal moves list (Day 1)
- [ ] Play against the AI in a chess game
- [ ] Position evaluation
- [ ] Move search and decision-making
- [ ] Difficulty levels, from "Temu Beginner" to "Temu Magnus"
- [ ] Game history and move logging (PGN support)
- [ ] Blunder detection, so it can tell me exactly how badly I played


---

## 🛠️ Tech Stack

| Area | Tools |
|------|-------|
| Language | Python |
| Chess logic | `python-chess` |
| Move selection | `random` (for now) |
| Environment | IPython / Jupyter |
| AI / ML | `TODO` |
| Interface | IPython board display (for now) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `python-chess`
- `ipython`

### Installation

```bash
# Clone the repository
git clone https://github.com/dipson-mishra/Knightly.git
cd Knightly

# Install dependencies
pip install chess ipython
```

### Run it

```bash
python main.py
```

---

## 🎮 Usage
**Day 1 :**

<img width="512" height="556" alt="image" src="https://github.com/user-attachments/assets/0c94802a-9a44-4f19-9bb8-4ef43e560b8b" />


---

## 🧠 How It Works

1. **Board representation**: handled by `python-chess`
2. **Evaluation**: none yet (the bot has no opinions)
3. **Search / learning**: none yet
4. **Move selection**: `random.choice()` over the list of legal moves

---

## 📅 Dev Log

| Day | Progress | Status |
|-----|----------|--------|
| 1 | Built a random-move bot using `random`, `python-chess`, and IPython. Picks a random move from the legal moves list. | Significantly weak |

---

## 🗺️ Roadmap

- [x] Day 1: make the bot play legal moves (it does, badly)
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

## 📄 License

`TODO`: MIT is a safe default.

---

<p align="center"><i>Made with ❤️, ☕, and an unreasonable number of blunders.</i></p>
