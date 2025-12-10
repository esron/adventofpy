import os
from typing import Mapping


def insert(pair: tuple[str, str], map: Mapping[str, str]) -> str:
    return pair[0] + map[pair[0] + pair[1]] + pair[1]


def step(polymer: str, map: Mapping[str, str]) -> str:
    inserts = []
    for i in range(len(polymer) - 1):
        inserts.append(insert((polymer[i], polymer[i + 1]), map))

    new_polymer = inserts[0]
    for i in inserts[1:]:
        new_polymer += i[1:]

    return new_polymer


def run():
    f = open(os.getcwd() + '/year_2021/day14/input.txt')
    polymer_template = f.readline().rstrip()

    # Skip empty line
    f.readline()

    insertions_map: Mapping[str, str] = {}
    elements_counts: Mapping[str, int] = {}
    for line in f:
        pair, element = line.rstrip().split(' -> ')
        insertions_map[pair] = element
        if element not in elements_counts.keys():
            elements_counts[element] = 0

    for _ in range(10):
        polymer_template = step(polymer_template, insertions_map)

    for e in polymer_template:
        elements_counts[e] += 1

    elements_counts = {k: v for k, v in sorted(
        elements_counts.items(), key=lambda item: item[1])}

    print(elements_counts[list(elements_counts.keys())[-1]] -
          elements_counts[list(elements_counts.keys())[0]])


if __name__ == "__main__":
    run()
