import os
from typing import Iterable, Mapping, Union


def run():
    f = open(os.getcwd() + '/year_2021/day14/input.txt')

    polymer_template = f.readline().rstrip()

    # Skip empty line
    f.readline()
    pairs: Mapping[str, Iterable[Union[str, int]]] = {}
    element_counts: Mapping[str, int] = {}
    for line in f:
        pair, element = line.rstrip().split(' -> ')

        # i.e. NN -> C: {'NN': ['NC', 'CN', 0]}
        pairs[pair] = [pair[0] + element, element + pair[1], 0]
        if element not in element_counts.keys():
            element_counts[element] = 0

    for i in range(len(polymer_template) - 1):
        pairs[polymer_template[i] + polymer_template[i + 1]][2] += 1

    for _ in range(1, 40):
        to_increment = []
        for key in pairs:
            to_increment.append((pairs[key][0], pairs[key][2]))
            to_increment.append((pairs[key][1], pairs[key][2]))
            pairs[key][2] -= pairs[key][2]
        for key, value in to_increment:
            pairs[key][2] += value

    for p in pairs.values():
        element_counts[p[0][0]] += p[2]
        element_counts[p[0][1]] += p[2]

    # Hack :)
    element_counts[polymer_template[-1]] += 1

    element_counts = {k: v for k, v in sorted(
        element_counts.items(), key=lambda item: item[1])}

    print(element_counts[list(element_counts.keys())[-1]] -
          element_counts[list(element_counts.keys())[0]])


if __name__ == "__main__":
    run()
