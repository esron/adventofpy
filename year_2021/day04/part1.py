import os


def bingo(board):
    for i in range(0, len(board)):
        colum_count = 0
        line_count = 0
        for j in range(0, len(board[i])):
            if board[i][j] == 'X':
                line_count += 1
            if line_count == 5:
                return True
            if board[j][i] == 'X':
                colum_count += 1
            if colum_count == 5:
                return True
    return False


def score(board):
    score = 0
    for line in board:
        score += sum(map(lambda x: int(x) if x != 'X' else 0, line))
    return score


def run():
    f = open(os.getcwd() + '/year_2021/day04/input.txt')
    numbers = f.readline()
    numbers = numbers.rstrip().split(',')
    boards = []
    board = []

    f.readline()
    for line in f:
        if line == '\n':
            boards.append(board)
            board = []
            continue
        board.append(list(filter(lambda e: e != '', line.strip().split(' '))))

    boards.append(board)

    for number in numbers:
        for b in range(0, len(boards)):
            for i in range(0, len(boards[b])):
                for j in range(0, len(boards[b][i])):
                    if boards[b][i][j] == number:
                        boards[b][i][j] = 'X'

                        if bingo(boards[b]):
                            print(score(boards[b]) * int(number))
                            return


if __name__ == "__main__":
    run()
