# Part 1 - Find the Elf Carrying the most calories
file = open("day_1_data.txt", "r")
sum = 0
elves = []
max_cal = 0
for line in file:
    if line[0].isdigit():
        sum = sum + int(line.rstrip())
    else:
        if sum > max_cal:
            max_cal = sum
        elves.append(int(sum))
        sum = 0

# Part 2 - Find the Elves carrying the top 3 number of calories then sum them

def find_top_three(nums):
    first = 0
    second = 0
    third = 0

    for num in nums:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num
    print("first: ", first)
    print("second: ", second)
    print("third: ", third)
    return first + second + third


print("Top 3 Sum: ", find_top_three(elves))
