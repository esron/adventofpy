from collections import deque
from collections.abc import Iterable, Mapping
import os
from typing import IO, Deque

def read_stacks(file: IO) -> Mapping[str, Deque[str]]:
    input: Iterable[str] = []
    line = file.readline()
    while (line != '\n'):
        input.append(line)
        line = file.readline()
    input.reverse()
    stacks: Mapping[str, Deque] = {}
    for i in range(1, len(input)):
        for j, c in enumerate(input[0]):
            if c.isnumeric() and input[i][j] != ' ':
                if c in stacks:
                    stacks[c].append(input[i][j])
                else:
                    stacks[c] = deque([input[i][j]])
    return stacks
def execute_instruction(instruction: str, stacks: Mapping[str, Deque]):
    _, quantity, _, origin, _, destiny = instruction.split(' ')
    quantity = int(quantity)
    aux = []
    for _ in range(quantity):
        aux.append(stacks[origin].pop())
    aux.reverse()
    stacks[destiny].extend(aux)
def run():
    with open(os.getcwd() + '/year_2022/day05/input.txt') as f:
        stacks = read_stacks(f)
        for line in f:
            execute_instruction(line.rstrip(), stacks)
        top_of_stacks = ''
        for _, s in stacks.items():
            if len(s) != 0:
                top_of_stacks += s[-1]
        print(top_of_stacks)
if __name__ == "__main__":
    run()
