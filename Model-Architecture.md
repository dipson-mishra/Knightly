# Model Iterations & Design

## Evolution Strategy
Knightly is designed as an iterative chess engine project: begin with a minimal legal-move baseline, then progressively improve evaluation quality and move selection strength.

## v0.1 — Random Agent (Baseline)

### Purpose
The v0.1 agent provides a strict baseline for comparison. It confirms legal move handling and game-loop integration before introducing evaluation logic.

### Core Logic
1. Parse the input FEN into a board object.
2. Enumerate all legal moves.
3. Randomly choose one legal move.
4. Return the move in UCI format.

### Design Characteristics
- **Strength**: very low
- **Determinism**: non-deterministic across runs
- **Search depth**: none
- **Evaluation function**: none

## v0.2 — Material Evaluation Agent

### Purpose
v0.2 replaces random choice with a classical static heuristic: material advantage.

### Material Scoring Model
For each candidate move, the resulting position is scored by piece material values:

- Pawn = 1
- Knight = 3
- Bishop = 3
- Rook = 5
- Queen = 9
- King = excluded from standard material trade valuation

A side’s material score is the sum of its piece values. Position quality is estimated by material difference (own material minus opponent material).

### Move Selection Process
1. Generate all legal candidate moves.
2. Apply each move on a copied board.
3. Compute material score of the resulting position.
4. Select the move with best immediate material outcome.

### Design Characteristics
- **Strength**: stronger than random baseline in many tactical positions
- **Search depth**: single-ply (no lookahead)
- **Evaluation scope**: material only (no king safety, mobility, pawn structure, or positional terms)

## Data Usage Across Experiments
Knightly includes raw datasets in `data/raw/`:

- `train.csv`
- `test.csv`

### `train.csv` structure
Columns:
- `id`: unique row identifier
- `board`: board state in FEN notation
- `black_score`: target score for black side evaluation
- `best_move`: target move label (UCI)

### `test.csv` structure
Columns:
- `id`: unique row identifier
- `board`: board state in FEN notation

### How the data is used
- **Training experiments**: `train.csv` provides position inputs and supervision targets.
- **Validation and comparison**: held-out or split subsets from training data are used to evaluate iteration behavior.
- **Inference experiments**: `test.csv` provides unlabeled board positions for move prediction/evaluation output.

## Design Limitations and Next Steps
Current iterations focus on legality and basic tactical signal. Future versions can extend evaluation quality by adding:
- Multi-ply search (minimax/alpha-beta)
- Positional heuristics beyond material
- Learned evaluation models trained on richer labels
