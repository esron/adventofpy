from collections import deque
import os

def run():
    with open(os.getcwd() + '/year_2022/day06/input.txt') as f:
        input = f.read().rstrip()
        quartet = deque(input[:4])
        for i in range(4, len(input)):
            if len(set(quartet)) == 4:
                print(i)
                exit(0)
            quartet.popleft()
            quartet.append(input[i])
if __name__ == "__main__":
    run()
