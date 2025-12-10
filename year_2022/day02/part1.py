import os

OP_ROCK = 'A'
OP_PAPPER = 'B'
OP_SCISSORS = 'C'
MY_ROCK = 'X'
MY_PAPPER = 'Y'
MY_SCISSORS = 'Z'
prs_map = {
    OP_ROCK: {
        MY_ROCK: 'draw',
        MY_PAPPER: 'win',
        MY_SCISSORS: 'loose',
    },
    OP_PAPPER: {
        MY_ROCK: 'loose',
        MY_PAPPER: 'draw',
        MY_SCISSORS: 'win',
    },
    OP_SCISSORS: {
        MY_ROCK: 'win',
        MY_PAPPER: 'loose',
        MY_SCISSORS: 'draw',
    },
}

points_map = {
    MY_ROCK: 1,
    MY_PAPPER: 2,
    MY_SCISSORS: 3,
}

outcome_map = {
    'loose': 0,
    'draw': 3,
    'win': 6,
}

def run():
    points = 0
    f = open(os.getcwd() + '/year_2022/day02/input.txt')
    for line in f:
        op_play, my_play = line.rstrip().split(' ')
        outcome = prs_map[op_play][my_play]
        points += (outcome_map[outcome] + points_map[my_play])
    print(points)
if __name__ == "__main__":
    run()
