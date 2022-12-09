from utils import file_to_list

data = file_to_list("day_9_data.txt")

def find_bounds(data):
    north = 0
    west = 0
    south = 0
    east = 0
    x = 0
    y = 0
    for line in data:
        [dir, mvmt] = line.split(" ")
        dist = int(mvmt)
        if dir == "U":
            y -= dist
            north = min(north,y)
        elif dir == "L":
            x -= dist
            west = min(west,x)
        elif dir == "D":
            y += dist
            south = max(south,y)
        elif dir == "R":
            x += dist
            east = max(east,x)

    rows = abs(north - south)
    cols = abs(west - east)
    return [cols, rows]

print(find_bounds(data))



