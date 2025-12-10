import os

board = []
counter = 0


def step():
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += 1


def in_range(x, y):
    return (0 <= x < len(board)) and (0 <= y < len(board[x]))


def increases_surroundings(i, j):
    for ii in (-1, 0, 1):
        for jj in (-1, 0, 1):
            x = ii + i
            y = jj + j

            if in_range(x, y) and board[x][y] != 0:
                board[x][y] += 1


def flash():
    global counter
    increments = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 9:
                board[i][j] = 0
                counter += 1
                increments.append((i, j))
    if len(increments) > 0:
        for i, j in increments:
            increases_surroundings(i, j)
        flash()


def run():
    steps = 100

    f = open(os.getcwd() + '/year_2021/day11/input.txt')
    for line in f:
        board.append(list(map(int, line.rstrip())))

    for s in range(1, steps + 1):
        step()
        flash()

    print(counter)


if __name__ == "__main__":
    run()
