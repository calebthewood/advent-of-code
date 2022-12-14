# Treetop Tree House
from utils import file_to_list

test_forest = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390",
]

forest = file_to_list("day_8_data.txt")
X_BOUND = len(forest[0])
Y_BOUND = len(forest)


def check_x(x, y):
    """Traverses the forest along the x axis from a given coord.
    Returns True if tree is visible or false if tree obscured"""
    visible = True
    tree = int(forest[y][x])
    delta_x = 0
    while delta_x < x:
        if tree <= int(forest[y][delta_x]):
            visible = False
        delta_x += 1

    if visible:
        return True
    delta_x = x + 1
    visible = True

    while delta_x < X_BOUND:
        if tree <= int(forest[y][delta_x]):
            visible = False
        delta_x += 1
    return visible


def check_y(x, y):
    """Traverses the forest along the y axis from a given coord.
    Returns False if tree is visible or false if tree obscured"""
    visible = True
    tree = int(forest[y][x])
    delta_y = 0
    # check north of the tree
    while delta_y < y:
        if tree <= int(forest[delta_y][x]):
            visible = False
        delta_y += 1

    if visible:
        return True
    delta_y = y + 1
    visible = True
    # if north side not visible, check south side of tree
    while delta_y < Y_BOUND:
        if tree <= int(forest[delta_y][x]):
            visible = False
        delta_y += 1
    return visible


def scan_nsew(x, y, forest):
    tree = int(forest[y][x])
    nsew = [0, 0, 0, 0]

    # North
    delta = y - 1
    while delta >= 0:
        target = int(forest[delta][x])
        nsew[0] += 1
        if tree <= target:
            break
        delta -= 1

    # South
    delta = y + 1
    while delta < Y_BOUND:
        target = int(forest[delta][x])
        nsew[1] += 1
        if tree <= target:
            break
        delta += 1

    # East
    delta = x + 1
    while delta < X_BOUND:
        target = int(forest[y][delta])
        nsew[2] += 1
        if tree <= target:
            break
        delta += 1

    # West
    delta = x - 1
    while delta >= 0:
        target = int(forest[y][delta])
        nsew[3] += 1
        if tree <= target:
            break
        delta -= 1
    return nsew


def scenic_score(forest):
    score = 0
    for y in range(0, Y_BOUND):
        for x in range(0, X_BOUND):
            [n, s, e, w] = scan_nsew(x, y, forest)
            # print("score: ", n * s * e * w, " coords: ", x," ",y, " nwse: ",n,w,s,e)
            score = max(n * s * e * w, score)
    return score


def tree_is_visible(x, y):
    return check_x(x, y) or check_y(x, y)


def count_trees():
    visible_count = ((Y_BOUND + X_BOUND) * 2) - 4
    for y in range(1, Y_BOUND-1):
        for x in range(1, X_BOUND-1):
            print("tree: ", forest[y][x])
            if x != 0 and y != 0:
                if tree_is_visible(x, y):
                    visible_count += 1
    return visible_count


print("Scenic Score: ", scenic_score(forest))
