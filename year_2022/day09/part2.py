import os

from math import copysign
def sign(x: int) -> int:
    if x == 0:
        return x
    return int(copysign(1, x))
def move_tail(head: list[int], tail: list[int]) -> list[int]:
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    if abs(dx) > 1 or abs(dy) > 1:
        return [tail[0] + sign(dx), tail[1] + sign(dy)]
    return tail
def move_rope(rope: list[list[int]],
              tail_track: set[tuple[int]], index: int, step: int) -> None:
    rope[0][index] += step
    for i in range(1, len(rope)):
        rope[i] = move_tail(rope[i - 1], rope[i])
    tail_track.add(tuple(rope[len(rope) - 1]))
def run():
    rope = []
    for _ in range(10):
        rope.append([0, 0])
    tail_track = {tuple(rope[-1])}
    with open(os.getcwd() + '/year_2022/day09/input.txt') as f:
        for line in f:
            movement, length = line.rstrip().split(' ')
            if movement == 'R':
                for _ in range(int(length)):
                    move_rope(rope, tail_track, 0, 1)
            elif movement == 'L':
                for _ in range(int(length)):
                    move_rope(rope, tail_track, 0, -1)
            elif movement == 'U':
                for _ in range(int(length)):
                    move_rope(rope, tail_track, 1, 1)
            elif movement == 'D':
                for _ in range(int(length)):
                    move_rope(rope, tail_track, 1, -1)

    print(len(tail_track))
if __name__ == "__main__":
    run()
