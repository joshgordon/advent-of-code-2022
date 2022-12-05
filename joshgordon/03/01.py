#!/usr/bin/env python3

bags = []
sum = 0

with open("input") as infile:
    for line in infile:
        line = line.strip()
        halfway = len(line) // 2
        bag = [list(line[:halfway]), list(line[halfway:])]
        bags.append(bag)


for bag in bags:
    union = set(bag[0]).intersection(set(bag[1]))
    item = union.pop()
    score = ord(item.upper()) - ord("A") + 1
    if item.isupper():
        score += 26

    print(item, score)
    sum += score

print(sum)
