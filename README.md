# Game of Life TDD Kata

```
.*.
*..
***
```

Based on [Coding Dojo's Game of Life](http://codingdojo.org/kata/GameOfLife/)

## Rules

1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2. Any live cell with more than three live neighbours dies, as if by overcrowding.
3. Any live cell with two or three live neighbours lives on to the next generation.
4. Any dead cell with exactly three live neighbours becomes a live cell.

## Run

```bash
# Run game
$ python -m game.start

# Run tests
$ python -m tests.start -v
```

## Requirements

### Must have

- [python 3.x](https://www.python.org/downloads/)
- pip3

### We recommend you

- [anaconda](https://anaconda.org/anaconda/python)

#### Install dependencies

```bash
# with anaconda
$ conda env create -f environment.yml # create virtual environment
$ conda activate gol # enter VE
(gol) $ conda deactivate # exit VE
```
