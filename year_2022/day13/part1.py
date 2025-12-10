import os
import json
from enum import Enum
class States(Enum):
    RIGHT_ORDER = 'RIGHT_ORDER',
    WRONG_ORDER = 'WRONG_ORDER',
    INCONCLUSIVE = 'INCONCLUSIVE'
def compare_pairs(left: list, right: list) -> States:
    """Returns True if pairs are in the right order."""
    for i in range(len(left)):
        if len(right) <= i:
            return States.WRONG_ORDER
        if isinstance(left[i], int) and isinstance(right[i], list):
            state = compare_pairs([left[i]], right[i])
            if state == States.INCONCLUSIVE:
                continue
            else:
                return state
        if isinstance(left[i], list) and isinstance(right[i], int):
            state = compare_pairs(left[i], [right[i]])
            if state == States.INCONCLUSIVE:
                continue
            else:
                return state
        if isinstance(left[i], list) and isinstance(right[i], list):
            state = compare_pairs(left[i], right[i])
            if state == States.INCONCLUSIVE:
                continue
            else:
                return state
        if left[i] == right[i]:
            continue
        elif left[i] < right[i]:
            return States.RIGHT_ORDER
        else:
            return States.WRONG_ORDER
    if len(right) > len(left):
        return States.RIGHT_ORDER

    return States.INCONCLUSIVE
def run():
    with open(os.getcwd() + '/year_2022/day13/input.txt') as f:
        line = '¯\\_(ツ)_/¯'
        index = 1
        index_sum = 0
        while line != '':
            pair_1 = json.loads(f.readline().rstrip())
            pair_2 = json.loads(f.readline().rstrip())

            if compare_pairs(pair_1, pair_2) == States.RIGHT_ORDER:
                index_sum += index

            line = f.readline()
            index += 1

        print(index_sum)
if __name__ == "__main__":
    run()
