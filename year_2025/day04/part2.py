import os

def solve(input_path):
    with open(input_path, "r") as f:
        lines = f.read().splitlines()
        board = [list(line) for line in lines]

    global_count = 0
    can_remove = True
    while can_remove:
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
                        # Remove the roll of paper
                        board[i][j] = "."
                        can_remove = True
                        count += 1
        if count == 0:
            can_remove = False
        global_count += count
    print(global_count)

def run():
    print("Example:")
    solve(os.getcwd() + "/year_2025/day04/example.txt")
    print("Input:")
    solve(os.getcwd() + "/year_2025/day04/input.txt")

if __name__ == "__main__":
    run()
