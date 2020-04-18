# Game of Life

Joh Conway's Game of Life, Python+curses edition.

## The Rules
For a space that is 'populated':
- Each cell with one or no neighbors dies, as if by solitude. 
- Each cell with four or more neighbors dies, as if by overpopulation. 
- Each cell with two or three neighbors survives. 

For a space that is 'empty' or 'unpopulated':
- Each cell with three neighbors becomes populated. 


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

Simulation controls
- Move around with arrow keys
- Press `x` to toggle a cell
- Press `n` to show the next simulation state

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