from utils import file_to_list

# Part 1

assignments = file_to_list("day_4_data.txt")

def part_one():
    count = 0
    for item in assignments:
        [num1, num2] = item.split(",")
        [start1, end1] = num1.split("-")
        [start2, end2] = num2.split("-")
        print(num1,num2)
        if int(start1) >= int(start2) and int(end1) <= int(end2):
            count += 1
        elif int(start1) <= int(start2) and int(end1) >= int(end2):
            count += 1
    print("Count: ",count)

def part_two():
    o_count = 0
    n_count = 0

    for item in assignments:
        [num1, num2] = item.split(",")
        [start1, end1] = num1.split("-")
        [start2, end2] = num2.split("-")

        end1 = int(end1) + 1
        end2 = int(end2) + 1

        list1 = set(range(int(start1),end1))
        list2 = set(range(int(start2),end2))

        overlap = list1.intersection(list2)
        print(len(overlap))

        if len(overlap) > 0:
            o_count += 1
        else:
            n_count += 1

    print(len(assignments))
    print(o_count + n_count)
    print("count: ", o_count)

part_two()