#!/usr/bin/env python3

from enum import Enum


class WinningState(Enum):
    WIN = 6
    DRAW = 3
    LOSS = 0


class Play(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


rounds: list[list[Play, Play]] = []


with open("input") as infile:
    # with open("example") as infile:
    for line in infile:
        theirs, result = line.strip().split(" ")
        theirs = Play(ord(theirs) - ord("A"))
        if result == "X":
            result = WinningState.LOSS
        elif result == "Y":
            result = WinningState.DRAW
        elif result == "Z":
            result = WinningState.WIN

        rounds.append([theirs, result])

our_plays: list[Play] = []

for round in rounds:
    if round[1] == WinningState.DRAW:
        our_plays.append(round[0])

    elif round[1] == WinningState.LOSS:
        our_plays.append(Play((round[0].value - 1) % 3))

    elif round[1] == WinningState.WIN:
        our_plays.append(Play((round[0].value + 1) % 3))

play_sum = sum([play.value + 1 for play in our_plays])
wins_sum = sum([round[1].value for round in rounds])

print(wins_sum + play_sum)
