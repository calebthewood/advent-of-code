from utils import file_to_list
import math
# Grid will be 231 wide by 187 long

data = file_to_list("day_9_data.txt")
# data = [
#     "R 5",
#     "U 8",
#     "L 8",
#     "D 3",
#     "R 17",
#     "D 10",
#     "L 25",
#     "U 20",
# ]


def board_size(data):
    instructions = []
    top = 0
    bottom = 0
    left = 0
    right = 0
    y = 0  # 4,-2,2,-3,-1
    x = 0  # 4,3,2

    for line in data:
        [dir, mvmt] = line.split(" ")
        dist = int(mvmt)
        instructions.append([dir, dist])

        if dir == "U":
            y += dist
            top = max(top, y)
        if dir == "D":
            y -= dist
            bottom = min(bottom, y)
        if dir == "L":
            x -= dist
            left = min(left, x)
        if dir == "R":
            x += dist
            right = max(right, x)
    y_bound = abs(top - bottom) + 1
    x_bound = abs(left - right) + 1

    # print("YBound: ", y_bound)
    # print("XBound: ", x_bound)
    # print("top: ",top)
    # print("bottom: ",bottom)
    # print("left: ",left)
    # print("right: ",right)
    # print("test x y: ",x,y)
    start = [left, top]
    return [y_bound, x_bound, instructions, start]


def show_grid(temp_grid, s, h, t):
    [sx, sy] = s
    [tx, ty] = t
    [hx, hy] = h
    temp_grid[sy][sx] = "S"
    temp_grid[ty][tx] = "T"
    temp_grid[hy][hx] = "H"
    for row in temp_grid:
        print(" ".join(row))


def model_rope(data):
    first_time_visits = 0
    [rows, cols, instructions, start] = board_size(data)
    grid = build_grid(rows, cols)
    [x, y] = start
    rope = [[x, y] for num in range(0, 10)]

    for [dir, dist] in instructions:
        while dist > 0:
            print("HEAD - dir: ", dir, "dist: ", dist)
            # Move Head
            if dir == "U":
                rope[0][1] -= 1
            elif dir == "L":
                rope[0][0] -= 1
            elif dir == "D":
                rope[0][1] += 1
            elif dir == "R":
                rope[0][0] += 1
            dist -= 1

            # Move Tail, while there's an x or y diff > 1
            for h in range(0, 9):
                t = h + 1
                x_diff = abs(rope[h][0] - rope[t][0])
                y_diff = abs(rope[h][1] - rope[t][1])
                if x_diff > 1 or y_diff > 1:
                    print("TAIL - dir: ", dir, "dist: ", dist)
                    # print(show_grid(grid.copy(),S,H,T))

                    # Move along x-axis
                    if x_diff == 2 and y_diff == 0:
                        if rope[h][0] > rope[t][0]:
                            rope[t][0] += 1
                        else:
                            rope[t][0] -= 1
                    # Move along y-axis
                    elif y_diff == 2 and x_diff == 0:
                        if rope[h][1] > rope[t][1]:
                            rope[t][1] += 1
                        else:
                            rope[t][1] -= 1
                    # Move diagonally
                    else:
                        # if x-axis diff is greater
                        if x_diff > y_diff:
                            # move x
                            if rope[h][0] > rope[t][0]:
                                rope[t][0] += 1
                            else:
                                rope[t][0] -= 1
                            # move y
                            if rope[h][1] > rope[t][1]:
                                rope[t][1] += 1
                            else:
                                rope[t][1] -= 1
                        # if y-axis diff is greater
                        else:
                            # move y
                            if rope[h][1] > rope[t][1]:
                                rope[t][1] += 1
                            else:
                                rope[t][1] -= 1
                            # move x
                            if rope[h][0] > rope[t][0]:
                                rope[t][0] += 1
                            else:
                                rope[t][0] -= 1
            # Update Grid & Count
            tail_x = rope[9][0]
            tail_y = rope[9][1]
            if grid[tail_y][tail_x] != "#":
                grid[tail_y][tail_x] = "#"
                first_time_visits += 1

    print("Grid: ")
    output = ["".join(row) for row in grid]
    for row in output:
        print("ROW:  ", row)
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
