from utils import file_to_list

data = file_to_list("day_5_data.txt")

crates = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": []
}
num = 1
for i in range(0,8):
    line = data[i]
    blanks = 0
    num = 1
    for char in line:
        if char.isalpha():
            key = str(num)
            crates[key].insert(0,char)
            num += 1
            blanks = 0
        elif char != "]" and char != "[":
            blanks += 1
            if blanks == 4:
                num += 1
                blanks = 0

print("Starting From:   ")
for key in crates:
    print(key,":",crates[key])


def part_one():
    end = len(data)
    for i in range(10, end):
        [x, move, y, fro, z ,to] = data[i].split(" ")
        # print("AA", data[i].split(" "))
        count = int(move)
        while count > 0:
            popped = crates[fro].pop()
            crates[to].append(popped)
            count -= 1


def part_two():
    end = len(data)
    for i in range(10, end):
        [x, move, y, fro, z ,to] = data[i].split(" ")
        count = int(move)
        temp = []

        while count > 0:
            popped = crates[fro].pop()
            temp.append(popped)
            count -= 1

        count = int(move)
        while len(temp) > 0:
            popped = temp.pop()
            crates[to] += popped


part_two()

print("Final Result:   ")
for key in crates:
    print(key,":",crates[key])

