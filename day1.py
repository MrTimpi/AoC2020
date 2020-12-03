f = open("day1.txt", "r")
lines = []
for x in f:
    lines.append(int(x))

sumTarget = 2020


for x in range(0, len(lines)):
    for y in range(x+1, len(lines)):
        for z in range(y+1, len(lines)):
            if lines[x] + lines[y] + lines[z] == sumTarget:
                print(lines[x] * lines[y] * lines[z],
                      lines[x], lines[y], lines[z])
