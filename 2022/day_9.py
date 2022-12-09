from utils import file_to_list
import math
# Grid will be 231 wide by 187 long
data = file_to_list("day_9_data.txt")


def find_bounds(data):
    north = 0
    west = 0
    south = 0
    east = 0
    x = 0
    y = 0
    instructions = []
    for line in data:
        [dir, mvmt] = line.split(" ")
        dist = int(mvmt)
        instructions.append([dir, dist])
        if dir == "U":
            y -= dist
            north = min(north, y)
        elif dir == "L":
            x -= dist
            west = min(west, x)
        elif dir == "D":
            y += dist
            south = max(south, y)
        elif dir == "R":
            x += dist
            east = max(east, x)

    rows = abs(north - south) + 2
    cols = abs(west - east) + 2
    return [cols, rows, instructions]


def model_rope(data):
    first_time_visits = 1
    [rows, cols, instructions] = find_bounds(data)
    grid = build_grid(rows, cols)
    x = 0
    y = 0
    S = [x, y]
    H = [x, y]
    T = [x, y]
    for [dir, dist] in instructions:
        while dist > 0:
            # Move Head
            if dir == "U":
                H[1] -= 1
            elif dir == "L":
                H[0] -= 1
            elif dir == "D":
                H[1] += 1
            elif dir == "R":
                H[0] += 1
            dist -= 1
            # Move Tail, while there's an x or y diff > 1
            while abs(H[0] - T[0]) > 1 or abs(H[1] - T[1]) > 1:
                first_time_visits += 1
                print("Head: ", H[1], H[0])
                print("Tail: ", T[1], T[0])
                grid[T[1]][T[0]] = "#"
                # if not adjacent on x-axis, move left or right
                if abs(H[0] - T[0]) > 1:
                    if H[0] > T[0]:
                        T[0] += 1
                    else:
                        T[0] -= 1
                # if not adjacent on y-axis, move up or down
                if abs(H[1] - T[1]) > 1:
                    if H[1] > T[1]:
                        T[1] += 1
                    else:
                        T[1] -= 1

    print("Head: ", H)
    print("Tail: ", T)
    print("Start: ", S)
    print("Grid: ")
    for row in grid:
        print(row)
    return first_time_visits


def build_grid(rows, cols):
    grid = []
    for y in range(0, rows):
        row = []
        for x in range(0, cols):
            row.append(".")
        grid.append(row)
    return grid


print(model_rope(data))
