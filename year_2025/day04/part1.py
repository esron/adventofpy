import os

def solve(input_path):
    with open(input_path, "r") as f:
        board = f.read().splitlines()

    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "@":
                neighbors = 0
                # Check up-left
                if i > 0 and j > 0 and board[i-1][j-1] == "@":
                    neighbors += 1
                # Check up-right
                if i > 0 and j < len(board[i]) - 1 and board[i-1][j+1] == "@":
                    neighbors += 1
                # Check up
                if i > 0 and board[i-1][j] == "@":
                    neighbors += 1
                # Check down-left
                if i < len(board) - 1 and j > 0 and board[i+1][j-1] == "@":
                    neighbors += 1
                # Check down-right
                if i < len(board) - 1 and j < len(board[i]) - 1 and board[i+1][j+1] == "@":
                    neighbors += 1
                # Check down
                if i < len(board) - 1 and board[i+1][j] == "@":
                    neighbors += 1
                # Check left
                if j > 0 and board[i][j-1] == "@":
                    neighbors += 1
                # Check right
                if j < len(board[i]) - 1 and board[i][j+1] == "@":
                    neighbors += 1
                if neighbors < 4:
                    count += 1
    print(count)

def run():
    print("Example:")
    solve(os.getcwd() + "/year_2025/day04/example.txt")
    print("Input:")
    solve(os.getcwd() + "/year_2025/day04/input.txt")

if __name__ == "__main__":
    run()
