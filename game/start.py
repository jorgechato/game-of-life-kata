from utils.main import LIVE_CELL, DEAD_CELL
from utils.main import set, get, parse


def count_alive_neighbours(x, y, matrix):
    upperNeighbours = [ get(x - 1, y - 1, matrix), get(x, y - 1, matrix), get(x + 1, y - 1, matrix) ]
    middleNeighbours = [ get(x - 1, y, matrix), get(x + 1, y, matrix) ]
    lowerNeighbours = [ get(x - 1, y + 1, matrix), get(x, y + 1, matrix), get(x + 1, y + 1, matrix) ]

    allNeighbours = upperNeighbours + middleNeighbours + lowerNeighbours

    return len(
        list(
            filter(lambda j: j == LIVE_CELL, allNeighbours)
        ))


def next_cell(cell, neighbours):
    return (
            DEAD_CELL if neighbours < 2 or neighbours > 3 else cell
        ) if cell == LIVE_CELL else (
            LIVE_CELL if neighbours == 3 else cell
        )


def calculate_next(start):
    next_board = [x[:] for x in start]

    for y, row in enumerate(start):
        for x in range(len(row)):
            count = count_alive_neighbours(x, y, start)
            cell = get(x, y, start)
            value = next_cell(cell, count)

            set(x, y, value, next_board)

    return next_board


if __name__ == '__main__':
    start = parse(4, 8, '''
                      ........
                      ...**...
                      ...*.*..
                      ....*...
                ''')
    print(start)
    print(calculate_next(start))