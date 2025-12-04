jolts = 0

with open("input.txt", "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    line = lines[i].strip()
    digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(len(line)):

        if digits[1] > digits[0]:
            digits[0] = digits[1]
            digits[1] = digits[2]
            digits[2] = digits[3]
            digits[3] = digits[4]
            digits[4] = digits[5]
            digits[5] = digits[6]
            digits[6] = digits[7]
            digits[7] = digits[8]
            digits[8] = digits[9]
            digits[9] = digits[10]
            digits[10] = digits[11]
            digits[11] = int(line[x])
        elif digits[2] > digits[1]:
            digits[1] = digits[2]
            digits[2] = digits[3]
            digits[3] = digits[4]
            digits[4] = digits[5]
            digits[5] = digits[6]
            digits[6] = digits[7]
            digits[7] = digits[8]
            digits[8] = digits[9]
            digits[9] = digits[10]
            digits[10] = digits[11]
            digits[11] = int(line[x])
        elif digits[3] > digits[2]:
            digits[2] = digits[3]
            digits[3] = digits[4]
            digits[4] = digits[5]
            digits[5] = digits[6]
            digits[6] = digits[7]
            digits[7] = digits[8]
            digits[8] = digits[9]
            digits[9] = digits[10]
            digits[10] = digits[11]
            digits[11] = int(line[x])
        elif digits[4] > digits[3]:
            digits[3] = digits[4]
            digits[4] = digits[5]
            digits[5] = digits[6]
            digits[6] = digits[7]
            digits[7] = digits[8]
            digits[8] = digits[9]
            digits[9] = digits[10]
            digits[10] = digits[11]
            digits[11] = int(line[x])
        elif digits[5] > digits[4]:
            digits[4] = digits[5]
            digits[5] = digits[6]
            digits[6] = digits[7]
            digits[7] = digits[8]
            digits[8] = digits[9]
            digits[9] = digits[10]
            digits[10] = digits[11]
            digits[11] = int(line[x])
        elif digits[6] > digits[5]:
            digits[5] = digits[6]
            digits[6] = digits[7]
            digits[7] = digits[8]
            digits[8] = digits[9]
            digits[9] = digits[10]
            digits[10] = digits[11]
            digits[11] = int(line[x])
        elif digits[7] > digits[6]:
            digits[6] = digits[7]
            digits[7] = digits[8]
            digits[8] = digits[9]
            digits[9] = digits[10]
            digits[10] = digits[11]
            digits[11] = int(line[x])
        elif digits[8] > digits[7]:
            digits[7] = digits[8]
            digits[8] = digits[9]
            digits[9] = digits[10]
            digits[10] = digits[11]
            digits[11] = int(line[x])
        elif digits[9] > digits[8]:
            digits[8] = digits[9]
            digits[9] = digits[10]
            digits[10] = digits[11]
            digits[11] = int(line[x])
        elif digits[10] > digits[9]:
            digits[9] = digits[10]
            digits[10] = digits[11]
            digits[11] = int(line[x])
        elif digits[11] > digits[10]:
            digits[10] = digits[11]
            digits[11] = int(line[x])
        elif digits[11] < int(line[x]):
            digits[11] = int(line[x])
    string = str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3]) + str(digits[4]) + str(digits[5]) + str(digits[6]) + str(digits[7]) + str(digits[8]) + str(digits[9]) + str(digits[10]) + str(digits[11])
    jolts += int(string)
        

print(jolts)