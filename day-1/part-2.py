pointer = 50
password = 0
with open("input.txt", "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    currentspin = lines[i].strip()
    direction = currentspin[0]
    if direction == "L":
        number = int(currentspin[1:])
        for x in range(number):
            pointer = (pointer - 1) % 100
            if pointer == 0:
                password += 1
        

    elif direction == "R":
        number = int(currentspin[1:])
        for x in range(number):
            pointer = (pointer + 1) % 100
            if pointer == 0:
                password += 1

print(password)