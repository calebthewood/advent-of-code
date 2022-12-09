from utils import file_to_list
import math
# Day 7: No Space Left On Device

def build_file_system(text):
    """ Build a dict mapping out a directory from lines of shell commands"""
    file_system = {"root": 0}
    path = []
    for line in text:
        data = line.split(" ")
        # if $, either view, move in, or move out
        if data[0] == "$" and data[1] == "cd":
            if data[2] == "/":
                path.clear()
                path.append("root")
            elif data[2] == "..":
                if len(path) > 1:
                    path.pop()
            else:
                path.append(data[2])
        # if dir, add new directory to {}
        elif data[0] == "dir":
            dir = data[1]
            new_path = f"{'/'.join(path)}/{dir}"
            if new_path not in file_system:
                file_system[new_path] = 0
        # if numeric, add value to all values in path
        elif data[0].isdigit():
            size = int(data[0])
            path_copy = path.copy()
            while len(path_copy) > 0:
                temp_path = "/".join(path_copy)
                file_system[temp_path] += size
                path_copy.pop()
    return file_system


def part_one(text):
    file_system = build_file_system(text)
    total = 0
    for value in file_system.values():
        if int(value) <= 100000:
            total += int(value)
    return total

def part_two(text):
    file_system = build_file_system(text)
    target = 2536714
    min_size = 70000000
    min_dir = ""
    for path in file_system:
        size = file_system[path]
        diff = size - target
        if diff > 0 and size < min_size:
            min_size = size
            min_dir = path
            print(f"{min_dir}: {min_size}")

    return f"{min_dir}: {min_size}"

def parse_file_name(file_name):
    """
    Accepts a file name with or without extension, and returns
    just the base text of the file name
    foobar.txt >> foobar
    """
    output = ""
    for char in file_name:
        if char == ".": return output
        output += char
    return output


with open("day_7_data.txt", "r") as f:
    text = [line.strip() for line in f]
    print("Part Two ", part_two(text))

# total: 70,000,000
# taken: 42,536,714
# needed: 30,000,000
# remaining: 27,463,286
# delete min of: 2,536,714
# 4,669,509
# 2,940,614