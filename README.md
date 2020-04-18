# Game of Life

Joh Conway's Game of Life, Python+curses edition.

## Quickstart

Setup virtual environment

```bash
virtualenv venv -p python3
source venv/bin/activate
pip intall -r requirements.txt
```

Run

```bash
python gol.py
```

## Format

Files are formatted with [Black](https://pypi.org/project/black/)

```bash
black .
```

## Test

Files are tested with Pytest

```bash
pip install -e .
pytest
```