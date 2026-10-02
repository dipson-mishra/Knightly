# Development & Contribution Guide

## Development Workflows
Knightly supports two parallel development modes:

## 1) Notebook Workflow (`notebooks/`)
Use notebooks for exploration, rapid prototyping, and experiment visualization.

Recommended usage:
- Validate ideas quickly (new heuristics, scoring experiments).
- Compare behavior of move-selection strategies interactively.
- Keep notebook outputs focused and reproducible.

Current notebooks:
- `notebooks/v0.1-random.ipynb`
- `notebooks/v0.2-material.ipynb`

## 2) Modular Script Workflow (`src/`)
Use scripts for reusable, versioned implementations.

Recommended usage:
- Implement stable agent logic in `src/models/`.
- Keep functions modular and composable.
- Ensure scripts run from repository root with documented commands.

Current model scripts:
- `src/models/v0.1-random.py`
- `src/models/v0.2-material.py`

## Proposing New Evaluation Metrics
When introducing a new heuristic or scoring method:

1. Define the metric objective clearly (what weakness it addresses).
2. Describe the scoring formula and expected effect on move choice.
3. Validate behavior against v0.1 and v0.2 baselines.
4. Document assumptions and known failure cases.
5. Add/update supporting notebook experiments and script implementation.

Examples of candidate metrics:
- Mobility (number/quality of legal moves)
- King safety
- Pawn structure penalties/bonuses
- Piece-square positional weighting

## Proposing New ML/DL Model Versions
For machine learning or deep learning iterations:

1. Create a new versioned model artifact (for example `v0.3-*`).
2. Document input representation, target labels, and training objective.
3. Record training/validation setup and key hyperparameters.
4. Compare outcomes with existing baselines using consistent test conditions.
5. Keep training code and inference/play loop clearly separated.

## Contribution Standards
- Keep changes scoped to a single iteration or feature.
- Preserve existing behavior unless a change is intentional and documented.
- Update docs when model behavior or project workflow changes.
- Prefer reproducible runs and explicit dependencies.

## Suggested Pull Request Content
Include in your PR:
- Objective and iteration version
- Files changed
- Behavior difference versus prior version
- Any data or environment assumptions
