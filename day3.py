inputFile = open("day3.txt", "r")
lines = []

for intputLine in inputFile:
    line = []
    for i in range(0, len(intputLine)):
        if intputLine[i] == ".":
            line.append(True)
        elif intputLine[i] == "#":
            line.append(False)
    lines.append(line)

# [line,row]
rules = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
colIdxs = [0, 0, 0, 0, 0]
openAreas = [0, 0, 0, 0, 0]
trees = [0, 0, 0, 0, 0]
for rowIdx in range(1, len(lines)):
    row = lines[rowIdx]
    for ruleIdx in range(0, len(rules)):
        rows = rules[ruleIdx][0]
        cols = rules[ruleIdx][1]
        if rowIdx % rows == 0:       
            colIdxs[ruleIdx] += cols
            if colIdxs[ruleIdx] >= len(row):
                colIdxs[ruleIdx] -= len(row)

            if row[ colIdxs[ruleIdx]]:
                openAreas[ruleIdx] += 1
            else:
                trees[ruleIdx] += 1

treeSum = 1
for i in range(0,len(rules)):
    print("Rule: ", rules[i] ,"OpenAreas: ", openAreas[i], " Trees: ", trees[i])
    treeSum *= trees[i]

print("TreeSum:",treeSum)