import os

board = []


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
    increments = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 9:
                board[i][j] = 0
                increments.append((i, j))
    if len(increments) > 0:
        for i, j in increments:
            increases_surroundings(i, j)
        flash()


def is_sync():
    for line in board:
        for cell in line:
            if cell != 0:
                return False
    return True


def run():
    f = open(os.getcwd() + '/year_2021/day11/input.txt')
    for line in f:
        board.append(list(map(int, line.rstrip())))

    steps = 0
    while(not is_sync()):
        step()
        flash()
        steps += 1

    print(steps)


if __name__ == "__main__":
    run()
