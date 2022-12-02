#!/usr/bin/env python3

from enum import Enum


class WinningState(Enum):
    WIN = 6
    DRAW = 3
    LOSS = 0


class Play(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


rounds: list[list[Play, Play]] = []


def winning_value(round: list[Play, Play]) -> WinningState:

    # 1 = rock
    # 2 = paper
    # 3 = scissors

    # Paper (2) beats Rock(1) ... round[1].value > round[0].value
    # Scissors (3) beats Paper (2)  ... round[1].value > round[0].value
    # Rock (1) beats Scissors (3) ... round[1] == Play.ROCK and round[0] == play.SCISSORS

    if round[0] == round[1]:
        return WinningState.DRAW

    if round[1].value - 1 % 3 == round[0].value % 3:
        return WinningState.WIN

    return WinningState.LOSS


with open("input") as infile:
    # with open("example") as infile:
    for line in infile:
        theirs, ours = line.strip().split(" ")
        theirs = Play(ord(theirs) - ord("A") + 1)
        ours = Play(ord(ours) - ord("X") + 1)

        rounds.append([theirs, ours])

wins = [winning_value(round) for round in rounds]

for idx, win in enumerate(wins):
    print(rounds[idx], win)

wins_sum = sum([win.value for win in wins])
play_sums = sum([round[1].value for round in rounds])

print(wins_sum + play_sums)
