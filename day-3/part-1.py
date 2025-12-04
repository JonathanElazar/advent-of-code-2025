jolts = 0

with open("input.txt", "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    line = lines[i].strip()
    first_digit = 0
    second_digit = 0
    for x in range(len(line)):

        if second_digit > first_digit:
            first_digit = second_digit
            second_digit = int(line[x])
        elif second_digit < int(line[x]):
            second_digit = int(line[x])
    string = str(first_digit) + str(second_digit)
    jolts += int(string)
        

print(jolts)