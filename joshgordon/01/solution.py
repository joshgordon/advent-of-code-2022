#!/usr/bin/env python3


elves = []

with open("input") as infile:
    elf = []
    for line in infile:
        line = line.strip()
        if not line:
            elves.append(elf)
            elf = list()
            continue

        elf.append(int(line))

    elves.append(elf)

elven_sums = sorted([sum(elf) for elf in elves])

print(f"Part 1: {elven_sums[-1]}")

print(f"Part 2: {sum(elven_sums[-3:])}")
