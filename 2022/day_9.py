from utils import file_to_list
import math
# Grid will be 231 wide by 187 long
# Guess #1: 8872 is too high
data = file_to_list("day_9_data.txt")
# data = [
#     "R 4",
#     "U 4",
#     "L 3",
#     "D 1",
#     "R 4",
#     "D 1",
#     "L 5",
#     "R 2"
# ]

def board_size(data):
    instructions = []
    top = 0
    bottom = 0
    left = 0
    right = 0
    y = 0 # 4,-2,2,-3,-1
    x = 0 # 4,3,2

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

    print("YBound: ", y_bound)
    print("XBound: ", x_bound)
    print("top: ",top)
    print("bottom: ",bottom)
    print("left: ",left)
    print("right: ",right)
    print("test x y: ",x,y)
    start = [left, top]
    return [y_bound, x_bound, instructions, start]

def show_grid(temp_grid,s,h,t):
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
    S = [x, y]
    H = [x, y]
    T = [x, y]

    for [dir, dist] in instructions:
        while dist > 0:
            print("HEAD - dir: ", dir, "dist: ", dist)
            # print(show_grid(grid.copy(),S,H,T))
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
            # needs
            x_diff = abs(H[0] - T[0])
            y_diff = abs(H[1] - T[1])
            if x_diff > 1 or y_diff > 1:
                print("TAIL - dir: ", dir, "dist: ", dist)
                # print(show_grid(grid.copy(),S,H,T))
                print("Head: ", H[1], H[0],"  Tail: ", T[1], T[0])


                # Move along x-axis
                if x_diff == 2 and y_diff == 0:
                    if H[0] > T[0]:
                        T[0] += 1
                    else:
                        T[0] -= 1
                # Move along y-axis
                elif y_diff == 2 and x_diff == 0:
                    if H[1] > T[1]:
                        T[1] += 1
                    else:
                        T[1] -= 1
                 # Move diagonally
                else:
                    # if x-axis diff is greater
                    if x_diff > y_diff:
                        # move x
                        if H[0] > T[0]:
                            T[0] += 1
                        else:
                            T[0] -= 1
                        # move y
                        if H[1] > T[1]:
                            T[1] += 1
                        else:
                            T[1] -= 1
                    #if y-axis diff is greater
                    else:
                        #move y
                        if H[1] > T[1]:
                            T[1] += 1
                        else:
                            T[1] -= 1
                        # move x
                        if H[0] > T[0]:
                            T[0] += 1
                        else:
                            T[0] -= 1
            # Update Grid & Count
            if grid[(T[1])][(T[0])] != "#":
                grid[(T[1])][(T[0])] = "#"
                first_time_visits += 1

    print("Head: ", H)
    print("Tail: ", T)
    print("Start: ", S)
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
