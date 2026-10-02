# Getting Started

## Prerequisites
Before running Knightly locally, ensure you have:

- **Python 3.x** installed
- `pip` available in your environment
- A local clone of the repository

> Recommended: use an isolated virtual environment per clone to avoid dependency conflicts.

## Installation

### 1) Clone the repository
```bash
git clone https://github.com/dipson-mishra/Knightly.git
cd Knightly
```

### 2) Create a virtual environment
```bash
python -m venv .venv
```

### 3) Activate the virtual environment
- **macOS / Linux**
  ```bash
  source .venv/bin/activate
  ```
- **Windows PowerShell**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

### 4) Install dependencies
```bash
pip install -r requirements.txt
```

## Local Environment Configuration

### Verify installation
Run a quick import check:

```bash
python -c "import chess, numpy, pandas, tensorflow; print('Knightly environment ready')"
```

### Keep execution context at repository root
Run scripts from the repository root so relative paths (for example `data/raw/train.csv`) resolve correctly.

```bash
python src/models/v0.1-random.py
python src/models/v0.2-material.py
```

### Optional: launch notebooks
```bash
jupyter notebook
```
Then open:
- `notebooks/v0.1-random.ipynb`
- `notebooks/v0.2-material.ipynb`

## Troubleshooting
- If dependency installation fails, upgrade pip:
  ```bash
  python -m pip install --upgrade pip
  ```
- If TensorFlow install is slow or fails, verify your Python version and platform support.
- If module import errors occur, confirm your virtual environment is active.
