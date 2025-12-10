import os

timers = {'addx': 2, 'noop': 1}
def run():
    x = 1
    clock = 0
    signal_strenght_sum = 0
    with open(os.getcwd() + '/year_2022/day10/input.txt') as f:
        instruction = f.readline().rstrip().split(' ')
        timer = timers[instruction[0]]
        while(clock < 220):
            clock += 1
            timer -= 1
            if clock == 20 or (clock - 20) % 40 == 0:
                signal_strenght_sum += clock * x
            if timer == 0:
                if instruction[0] == 'addx':
                    x += int(instruction[1])
                instruction = f.readline().rstrip().split(' ')
                timer = timers[instruction[0]]

    print(signal_strenght_sum)
if __name__ == "__main__":
    run()
