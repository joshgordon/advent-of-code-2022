#!/usr/bin/env python3

ranges: list[list[set[int]]] = []

with open("input") as infile:
    for line in infile:
        line = line.strip()
        line_range: list[set[int]] = []
        for side in line.split(","):
            range0, range1 = map(lambda x: int(x), side.split("-"))
            line_range.append(set(range(range0, range1 + 1)))

        ranges.append(line_range)

total = 0

for line in ranges:
    if line[0] <= line[1] or line[1] <= line[0]:
        total += 1
print(total)


total = 0

for line in ranges:
    if line[0].intersection(line[1]):
        total += 1
print(total)
