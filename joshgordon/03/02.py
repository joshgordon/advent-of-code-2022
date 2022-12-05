#!/usr/bin/env python3

from functools import reduce

bags = []
sum = 0

with open("input") as infile:
    for line in infile:
        line = line.strip()
        bags.append(set(line))


for idx in range(len(bags) // 3):

    group_bags = bags[idx * 3 : idx * 3 + 3]
    print(group_bags)
    common = reduce(
        lambda x, y: x.intersection(y),
        group_bags,
    )

    item = common.pop()

    score = ord(item.upper()) - ord("A") + 1
    if item.isupper():
        score += 26

    print(item, score)
    sum += score

print(sum)
