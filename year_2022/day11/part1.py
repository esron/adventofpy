from collections import deque
import os
from typing import Optional, Union

class Monkey:
    def __init__(
        self,
        start_items: list[int],
        operation: tuple[str, Union[int, str]],
        test_value: int,
        monkey_to_move_when_test_true: int,
        monkey_to_move_when_test_false: int
    ) -> None:
        self.items = deque(start_items)
        self.operation = operation
        self.test_value = test_value
        self.monkey_a = monkey_to_move_when_test_true
        self.monkey_b = monkey_to_move_when_test_false
        self.inspected_items = 0

    def __operate(self, item: int) -> int:
        operator, operand = self.operation
        if type(operand) == str:
            operand = item
        if operator == '+':
            return item + int(operand)
        if operator == '-':
            return item + int(operand)
        if operator == '*':
            return item * int(operand)
        return 0

    def __test_item(self, item: int) -> int:
        if item % self.test_value == 0:
            return self.monkey_a
        else:
            return self.monkey_b

    def process_item(self) -> Union[tuple[int, int], tuple[None, None]]:
        if len(self.items) > 0:
            # Inspect item:
            item = self.items.popleft()
            item = self.__operate(item)
            self.inspected_items += 1

            # Reduce worry:
            item //= 3
            monkey_index = self.__test_item(item)
            return monkey_index, item
        return (None, None)
def get_starting_items(monkey_raw_data: str) -> list[int]:
    return [int(x) for x in monkey_raw_data.strip().split(': ')[1].split(',')]
def get_operation(monkey_raw_data: str) -> tuple[str, Union[int, str]]:
    operator, operand = monkey_raw_data.strip().split(' ')[-2:]
    operand = int(operand) if operand.isnumeric() else operand
    return operator, operand
def get_test_value(monkey_raw_data: str) -> int:
    return int(monkey_raw_data.strip().split(' ')[-1])
def monkey_to_move_when_test_true(monkey_raw_data: str) -> int:
    return int(monkey_raw_data.strip().split(' ')[-1])
def monkey_to_move_when_test_false(monkey_raw_data: str) -> int:
    return int(monkey_raw_data.strip().split(' ')[-1])
def run():
    file_lines = []
    monkeys: list[Monkey] = []
    with open(os.getcwd() + '/year_2022/day11/input.txt') as f:
        file_lines = f.readlines()
    for i in range(0, len(file_lines), 7):
        monkey_raw_data = file_lines[i:i+6]
        start_items = get_starting_items(monkey_raw_data[1])
        operation = get_operation(monkey_raw_data[2])
        test_value = get_test_value(monkey_raw_data[3])
        monkey_a = monkey_to_move_when_test_true(monkey_raw_data[4])
        monkey_b = monkey_to_move_when_test_false(monkey_raw_data[5])
        monkeys.append(Monkey(start_items,
                              operation, test_value, monkey_a, monkey_b))
    for _ in range(20):
        for monkey in monkeys:
            while(len(monkey.items) > 0):
                m_index, item = monkey.process_item()
                if m_index is not None and item is not None:
                    monkeys[m_index].items.append(item)
    monkeys = sorted(monkeys, key=lambda x: x.inspected_items, reverse=True)
    print(monkeys[0].inspected_items * monkeys[1].inspected_items)
if __name__ == "__main__":
    run()
