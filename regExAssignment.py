import re
handle = open("regex_sum_1920067.txt")
sum = 0
for line in handle:
    numSet = re.findall("[0-9]+", line)
    for num in numSet:
        sum = sum + int(num)
print(sum)

