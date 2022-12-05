from collections import defaultdict
import re
from tqdm import tqdm

stacks: defaultdict[list] = defaultdict(lambda: list())

move_re = re.compile(r"move (\d+) from (\d+) to (\d+)")

with open("input") as infile:
    stacknum = 0
    while True:
        obj = infile.read(4)
        stacknum += 1
        token = obj[1]
        if token.isdigit():
            break
        if token != " ":
            stacks[stacknum].insert(0, token)
        if obj[-1] == "\n":
            stacknum = 0

    infile.readline()
    infile.readline()
    for line in infile:
        move = [int(x) for x in move_re.match(line).groups()]
        for i in range(move[0]):
            stacks[move[2]].append(stacks[move[1]].pop())

for key in sorted(stacks.keys()):
    print(stacks[key][-1], end="")
print()
