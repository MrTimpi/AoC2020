import re
f = open("day2.txt", "r")
lines = []
valid1 = []
invalid1 = []
for x in f:
    lines.append(x)

rex = re.compile("([0-9]+)-([0-9]+)\s(\w):\s(\w*)")

# ------ part one
for i in range(0, len(lines)):
    matches = rex.match(lines[i])
    count = matches.group(4).count(matches.group(3))
    if count >= int(matches.group(1)) and count <= int(matches.group(2)):
        valid1.append(lines[i])
    else:
        invalid1.append(lines[i])

print("part one valid: ", len(valid1))

# ----- part two
valid2 = []
invalid2 = []
for i in range(0, len(lines)):
    matches = rex.match(lines[i])
    line = matches.group(0)
    passwd = matches.group(4)
    charcter = matches.group(3)
    pos1 = int(matches.group(1)) - 1
    charIdx1 = ""
    if len(passwd) > pos1:
        charIdx1 = passwd[int(pos1)]
    pos2 = int(matches.group(2)) - 1
    charIdx2 = ""
    if len(passwd) > pos2:
        charIdx2 = passwd[int(pos2)]

    if charIdx1 == charcter and charIdx1 != charIdx2:
        valid2.append(line)
    elif charIdx2 == charcter and charIdx1 != charIdx2:
        valid2.append(line)
    else:
        invalid2.append(line)

print("part two valid: ", len(valid2))
