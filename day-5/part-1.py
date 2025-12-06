counter = 0
usednums = []


with open("input.txt") as f:
    content = f.read().split("\n\n")
    ranges = content[0].split("\n")
    numbers = content[1].split("\n")

nums = []
for i in range(len(numbers)):
        nums.append(int(numbers[i]))

for x in range (len(ranges)):
    num1, num2 = map(int, ranges[x].split("-"))
    for y in range(len(nums)):
         if nums[y] >= num1 and nums[y] <= num2 and nums[y] not in usednums:
            counter += 1
            usednums.append(nums[y])
print(counter)
