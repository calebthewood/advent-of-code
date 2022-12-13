from utils import file_to_list
import os
from time import sleep

GRID = file_to_list("day_12_data.txt")
X_BOUND = len(GRID[0])
Y_BOUND = len(GRID)


def find_char(char):
    """
    Searches 2D grid for element containing the specified value,
    and returns [x,y] coordinates.
        "S" >> [3,14]
    """
    for y in range(0, Y_BOUND):
        for x in range(0, X_BOUND):
            if GRID[y][x] == char:
                return [x, y, 120]


def validate_coordinates(coords):
    """ Ensure coordinates are within grid """
    x = coords[0]
    y = coords[1]
    return (0 <= x < X_BOUND) and (0 <= y < Y_BOUND)


def validate_elevation(current, new):
    """
    Determines whether it's possible to travel between 2 cells on the grid
    with a vertical limit of 1.
        [5,5] "a", [5,6] "b" >> true
        [5,5] "a", [5,6] "g" >> false
    """
    elevation = "ESabcdefghijklmnopqrstuvwxyz"
    vertical_limit = 1
    [cx, cy] = current
    [nx, ny] = new
    cur_elev = elevation.index(GRID[cy][cx])
    new_elev = elevation.index(GRID[ny][nx])
    return new_elev <= (cur_elev + vertical_limit)


def calculate_proximity(new, end):
    """
    Calculates the distance between current coords and end coords to
    assist in determining which direction to choose when more than
    one valid NWSE directional choice exists.
    """
    y_diff = abs(new[1] - end[1])
    x_diff = abs(new[0]  - end[0])
    return y_diff + x_diff


def survey_move_options(current, end):
    """Checks NWSE move options for elevation and proximity to end"""
    [x, y, p] = current
    nwse = [[x, y-1], [x-1, y], [x, y+1], [x+1, y]]
    move_options = []

    for coords in nwse:
        if validate_coordinates(coords):
            if validate_elevation([x,y], coords):
                prox = calculate_proximity(coords, end)
                [nx, ny] = coords
                move_options.append([nx, ny, prox])


    return move_options

#function like this one has a lot of room for improvement.
def order_by_priority(moves):
    """
    Orders the valid moves list in terms of priority from lowest to highest
        [12,5,14,7] >> [14,12,7,5]
    """
    ordered_moves = []
    # orders mvoes according to priority
    while len(moves) > 0:
        max = 0
        for i in range(0, len(moves)):
            if moves[i][2] > moves[min][2]:
                max = i
        move = moves.pop(max)
        ordered_moves.append(move)
    return


def reached_destination(coords):
    [x, y, p] = coords
    return GRID[y][x] == "E"


def print_path_map(visited, steps):
    path_map = []
    for col in GRID:
        row = []
        for cell in col:
            row.append(cell)
        path_map.append(row)

    for coords in visited:
        list_coords = list(coords)
        x = int(list_coords[0])
        y = int(list_coords[1])
        path_map[y][x] = "."
    sleep(.01)
    os.system('clear')
    # print("<-- Path Map -->")
    for row in path_map:
        print("".join(row))
    # print(f"<-- Steps: {steps} -->")
    # print(f"<-- Cells Visited: {len(visited)} -->")
    # print(visited)


def part_one():
    steps = 0
    coords = find_char("S")
    start = [coords[0],coords[1],-1]
    end = find_char("E")
    visited = []
    to_visit = [start]
    # while not reached_destination(coords):

    while len(to_visit) > 0:
        steps += 1
        coords = to_visit.pop()
        visited.append(coords)
        valid_moves = survey_move_options(coords, end)
        for move in valid_moves:
            if move not in visited:
                to_visit.append(move)
        print_path_map(visited, steps)
        if GRID[coords[1]][coords[0]] == "E":
            print(f"<-- Steps: {steps} -->")
            print(f"<-- Cells Visited: {len(visited)} -->")
            return "fin!"

    return "Looks like I'm lost!"

print(part_one())
