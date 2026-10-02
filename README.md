# Knightly

Knightly is a chess machine learning project for experimenting with chess move selection, position evaluation, and model-driven gameplay using Python.

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
│   └── v0.2-material.ipynb
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── v0.1-random.py
│   │   └── v0.2-material.py
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
```

## Running Notebooks

1. Start Jupyter from repository root:

```bash
jupyter notebook
```

2. Open notebooks in `notebooks/`:
   - `notebooks/v0.1-random.ipynb`
   - `notebooks/v0.2-material.ipynb`
