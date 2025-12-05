rolls_accessible = 0

with open ("input.txt", "r") as f:
    diagram = f.read().split("\n")

rows = len(diagram)
cols = len(diagram[0])

for i in range(cols):
    for x in range(rows):
        if diagram[x][i] == "@":
            neighbors = 0
            # Up
            if x > 0 and diagram[x-1][i] == "@":
                neighbors += 1
            # Down
            if x < rows-1 and diagram[x+1][i] == "@":
                neighbors += 1
            # Left
            if i > 0 and diagram[x][i-1] == "@":
                neighbors += 1
            # Right
            if i < cols-1 and diagram[x][i+1] == "@":
                neighbors += 1
            # Diagonals
            if x > 0 and i > 0 and diagram[x-1][i-1] == "@":
                neighbors += 1
            if x > 0 and i < cols-1 and diagram[x-1][i+1] == "@":
                neighbors += 1
            if x < rows-1 and i > 0 and diagram[x+1][i-1] == "@":
                neighbors += 1
            if x < rows-1 and i < cols-1 and diagram[x+1][i+1] == "@":
                neighbors += 1

            if neighbors < 4:
                rolls_accessible += 1
print(rolls_accessible)