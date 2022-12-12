from utils import file_to_list

input_list = file_to_list("day_12_data.txt")

def part_one(input):
    # find Start coords
    # find End coords
    # path_map = record of moves made
    # visited = list of coords visited
    # elevation = "abcde...z" - use index to determine relative elevation
    # set up a while(true) loop
        # determine NWSE based on Start
        # move based on two(?) conditions:
            # move is valid, difference <= current elevation + 1
            # greedy preference when more than 1 option, take choice closer to End
                #minimal difference btwn current x,y and end x,y
            # only allow backtracking if it's the only option

    for row in input: print(row)

print(part_one(input_list))