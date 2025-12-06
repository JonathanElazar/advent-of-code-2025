counter = 0
low_nums = []
corrisponding_nums = {}

with open("input.txt") as f:
    content = f.read().split("\n\n")
    raw_lines = content[0].split("\n")

for i in range(len(raw_lines)):
    line = raw_lines[i].strip()
    if not line:
        continue
    parts = line.split("-")
    if len(parts) != 2:
        continue
    low = int(parts[0].strip())
    high = int(parts[1].strip())
    if low in corrisponding_nums:
        corrisponding_nums[low] = max(corrisponding_nums[low], high)
    else:
        low_nums.append(low)
        corrisponding_nums[low] = high

low_nums.sort()

i = 0
while i < len(low_nums) - 1:
    current_low = low_nums[i]
    current_high = corrisponding_nums[current_low]

    next_low = low_nums[i + 1]
    next_high = corrisponding_nums[next_low]

    if next_low <= current_high:
        if next_high > current_high:
            corrisponding_nums[current_low] = next_high
            current_high = next_high
        del low_nums[i + 1]
    else:
        i += 1

for x in range(len(low_nums)):
    low = low_nums[x]
    high = corrisponding_nums[low]
    counter += (high - low + 1)

print(counter)
