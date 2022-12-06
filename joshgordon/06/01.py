puzzle_input = open("input").read().strip()
for x in [4, 14]:
    for i in range(len(puzzle_input) - x):
        if len(set(puzzle_input[i:i+x])) == x:
            print(i + x)
            break
