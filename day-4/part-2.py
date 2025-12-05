rolls_accessible = 0

with open("input.txt", "r") as f:
    diagram = [list(line) for line in f.read().split("\n")]

rows = len(diagram)
cols = len(diagram[0])

while True:
    to_remove = []
    for x in range(rows):
        for i in range(cols):
            if diagram[x][i] == "@":
                neighbors = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        nx, ny = x + dx, i + dy
                        if 0 <= nx < rows and 0 <= ny < cols and diagram[nx][ny] == "@":
                            neighbors += 1
                if neighbors < 4:
                    to_remove.append((x, i))

    if not to_remove:
        break


    for x, i in to_remove:
        diagram[x][i] = "."
        rolls_accessible += 1

print(rolls_accessible)
