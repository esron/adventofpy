import os

from math import sqrt
def distance(A: list[int], B: list[int]) -> float:
    """Calculates the Euclidian distance between A and B.
       A and B are two dimention points.
    """
    if A == B:
        return 0
    return sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
def move_tail(previous_head: list[int], head: list[int],
              tail: list[int], track: set[tuple[int]]) -> list[int]:
    if distance(head, tail) >= 2.0:
        track.add(tuple(previous_head))
        return previous_head
    return tail
def run():
    head_position = [0, 0]
    head_previous_position = [0, 0]
    tail_position = [0, 0]
    tail_track = {tuple(tail_position)}
    with open(os.getcwd() + '/year_2022/day09/input.txt') as f:
        for line in f:
            movement, length = line.rstrip().split(' ')
            if movement == 'R':
                for _ in range(int(length)):
                    head_previous_position = head_position.copy()
                    head_position[0] += 1
                    tail_position = move_tail(head_previous_position,
                                              head_position,
                                              tail_position,
                                              tail_track)
            elif movement == 'L':
                for _ in range(int(length)):
                    head_previous_position = head_position.copy()
                    head_position[0] -= 1
                    tail_position = move_tail(head_previous_position,
                                              head_position,
                                              tail_position,
                                              tail_track)
            elif movement == 'U':
                for _ in range(int(length)):
                    head_previous_position = head_position.copy()
                    head_position[1] += 1
                    tail_position = move_tail(head_previous_position,
                                              head_position,
                                              tail_position,
                                              tail_track)
            elif movement == 'D':
                for _ in range(int(length)):
                    head_previous_position = head_position.copy()
                    head_position[1] -= 1
                    tail_position = move_tail(head_previous_position,
                                              head_position,
                                              tail_position,
                                              tail_track)
    print(len(tail_track))
if __name__ == "__main__":
    run()
