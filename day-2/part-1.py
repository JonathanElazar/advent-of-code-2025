invalid_ids = 0

with open("input.txt") as f:
    inputtxt = f.read()
ranges = inputtxt.split(",")
for i in range(len(ranges)):
    one_range = int(ranges[i].split("-")[0])
    two_range = int(ranges[i].split("-")[1])

    for x in range(one_range, two_range):
        if len(str(x)) % 2 == 0:
            digits = len(str(x)) // 2
            part1 = str(x)[0:digits]
            part2 = str(x)[digits:len(str(x))]
            if part1 == part2:
                invalid_ids += x
        else:
            pass

print(invalid_ids)