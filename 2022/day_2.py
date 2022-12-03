# Part 1 -
# Scores:
# A Rock      1
# B Paper     2
# C Scissors  3
# X Loss - 0
# Y Draw - 3
# Z Win - 6

# STEP 1 What would your total score be if everything goes
# exactly according to your strategy guide?

file = open("day_2_data.txt", "r")

def parse_rps_guide():
    score = 0
    for line in file:
        [them, space, me] = line.rstrip()

        if me == "X":
            score += 1
            if them == "A":
                score += 3
            elif them == "C":
                score += 6
        elif me == "Y":
            score += 2
            if them == "A":
                score += 6
            elif them == "B":
                score += 3
        elif me == "Z":
            score += 3
            if them == "B":
                score += 6
            elif them == "C":
                score += 3

    return score

# print(parse_rps_guide())

# Step 2 Revised Guide

def resolve_guide():
    score = 0
    for line in file:
        [them, space, me] = line.rstrip()

        if them == "A":
            if me == "X":
                score += 3
            elif me == "Y":
                score += 4
            elif me == "Z":
                score += 8
        elif them == "B":
            if me == "X":
                score += 1
            elif me == "Y":
                score += 5
            elif me == "Z":
                score += 9
        elif them == "C":
            if me == "X":
                score += 2
            elif me == "Y":
                score += 6
            elif me == "Z":
                score += 7
    return score

print(resolve_guide())