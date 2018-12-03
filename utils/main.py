
LIVE_CELL = "*"
DEAD_CELL = "."


def set(x, y, value, matrix):
    if not matrix[y]:
        matrix[y] = []

    matrix[y][x] = value


def get(x, y, matrix):
    row = matrix[y] or []

    return row[x]


def parse(height, width, layout):
    lines = list(
        filter(
            (lambda s: len(s) > 0),
            [s.strip() for s in layout.split("\n")]
        )
    )

    if len(lines) != height or any(len(line) != width for line in lines):
        raise Exception(
            "Format is not valid, it should be {} height x {} width.".format(
                height,
                width,
            )
        )

    return [list(line) for line in lines]
