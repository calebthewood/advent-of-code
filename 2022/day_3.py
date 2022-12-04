
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

# sum the priorities of letters that appear 2x in each string?

LETTERS = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def file_to_list():
    file = open("day_3_data.txt", "r")
    output = []
    for line in file:
        output.append(line.strip())
    return output

rucksacks = file_to_list()

def sum_priorities():
    priority_sum = 0

    for string in rucksacks:
        chars = [*string]
        mid = int(len(chars) / 2)

        p1_list = chars[:mid]
        p2_list = chars[mid:]

        p1_set = set(p1_list)
        p2_set = set(p2_list)

        item = list(p1_set.intersection(p2_set))

        print("p1_len ", len(p1_list))
        print("p2_len ", len(p2_list))
        if (len(item) > 0):
            priority_sum += int(LETTERS.index(item[0]))

    return priority_sum

def group_priorities():
    """Part 2: Finds single common char for every 3 elements,
    and returns the sum of their 'priority'"""
    priority_sum = 0
    size = int(len(rucksacks)) - 2
    i = 0

    while i < size:
        j = i + 1
        k = i + 2
        elf_one = set([*rucksacks[i]])
        elf_two = set([*rucksacks[j]])
        elf_thr = set([*rucksacks[k]])
        badge = list(elf_one.intersection(elf_two,elf_thr))[0]
        priority_sum += int(LETTERS.index(badge))
        i += 3

    return priority_sum

print(group_priorities())