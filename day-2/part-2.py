invalid_ids = 0

with open("input.txt") as f:
    inputtxt = f.read()
ranges = inputtxt.split(",")
for i in range(len(ranges)):
    one_range = int(ranges[i].split("-")[0])
    two_range = int(ranges[i].split("-")[1])

    for x in range(one_range, two_range):
        length = len(str(x))
        for y in range(1, length):
            if length % (y) == 0:
                string = str(x)[:(y)]
                string = string * (length // (y))
                if string == str(x):
                    invalid_ids += x
                    break
print(invalid_ids)