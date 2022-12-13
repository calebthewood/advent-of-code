from utils import file_to_list
import os
from time import sleep


class PriorityQueue:
    def __init__(self):
        self.values = []

    def enqueu(self, val, priority):
        node = {
            "val": val,
            "priority": priority
        }
        self.values.append(node)
        self.pq_sort()

    def dequeue(self):
        return self.values.pop(0)

    def pq_sort(self):
        self.values.sort(key=lambda x: x["priority"])


class WeightedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2, weight):
        if v2 not in self.adjacency_list[v1]:
            self.adjacency_list[v1].append({"node": v2, "weight": weight})

    def _initialize_dijkstra(self, start):
        nodes = PriorityQueue()
        distances = {}
        previous = {}

        for vertex in self.adjacency_list:
            previous[vertex] = 0
            if vertex == start:
                distances[vertex] = 0
                nodes.enqueu(vertex, 0)
            else:
                distances[vertex] = float('inf')
                nodes.enqueu(vertex, float('inf'))

        return [distances, nodes, previous]

    def dijkstras_path(self, start, end):
        [distances, nodes, previous] = self._initialize_dijkstra(start)
        path = []

        while len(nodes.values):
            smallest = nodes.dequeue()["val"]
            if smallest == end:
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]
                break
            if (smallest or distances[smallest]) != float('inf'):
                for neighbor in range(0, len(self.adjacency_list[smallest])):
                    next_node = self.adjacency_list[smallest][neighbor]
                    prospect = float(
                        distances[smallest]) + float(next_node["weight"])
                    next_neighbor = next_node["node"]
                    if prospect < distances[next_neighbor]:
                        distances[next_neighbor] = prospect
                        previous[next_neighbor] = smallest
                        nodes.enqueu(next_neighbor, prospect)

        if isinstance(smallest, list):
            path.extend(smallest)
        else:
            path.append(smallest)
        path.reverse()
        return path


def validate_elevation(x, y, nx, ny, grid):
    """
    Determines whether it's possible to travel between 2 cells on the grid
    with a vertical limit of 1.
        [5,5] "a", [5,6] "b" >> true
        [5,5] "a", [5,6] "g" >> false
    """
    elevation = "SabcdefghijklmnopqrstuvwxyzE"
    vertical_limit = 1
    current_elev = elevation.index(grid[y][x]) + vertical_limit
    new_elev = elevation.index(grid[ny][nx])
    # print("ELEVATION: ",new_elev <= current_elev)
    return new_elev <= current_elev


def get_adjacency_list(x, y, grid):
    """Checks NWSE move options for elevation and proximity to end"""
    nwse = [[x, y-1], [x-1, y], [x, y+1], [x+1, y]]
    adjacency_list = []
    x_bound = len(grid[0])
    y_bound = len(grid)

    for [nx, ny] in nwse:
        if (0 <= nx < x_bound) and (0 <= ny < y_bound):
            if validate_elevation(x, y, nx, ny, grid):
                vertex = f"{nx}-{ny}"
                adjacency_list.append(vertex)
    return adjacency_list


def grid_to_graph(grid):
    graph = WeightedGraph()
    x_bound = len(grid[0])
    y_bound = len(grid)
    # Add Vertices
    for y in range(0, y_bound):
        for x in range(0, x_bound):
            vertex_a = f"{x}-{y}"
            graph.add_vertex(vertex_a)
    # Add Edges
    for y in range(0, y_bound):
        for x in range(0, x_bound):
            vertex_a = f"{x}-{y}"
            adjacency_list = get_adjacency_list(x, y, grid)
            for vertex_b in adjacency_list:
                graph.add_edge(vertex_a, vertex_b, 1)

    return graph


def find_start_end(grid):
    x_bound = len(grid[0])
    y_bound = len(grid)
    for y in range(0, y_bound):
        for x in range(0, x_bound):
            if grid[y][x] == "S":
                start = f"{x}-{y}"
            if grid[y][x] == "E":
                end = f"{x}-{y}"
    return [start, end]


def print_path_map(path, grid):
    path_map = []

    for col in grid:
        row = []
        for cell in col:
            row.append(cell)
        path_map.append(row)

    for node in path:
        coords = node.split("-")
        x = int(coords[0])
        y = int(coords[1])
        path_map[y][x] = "."

        sleep(.02)
        os.system('clear')

        for row in path_map:
            print("".join(row))
        print(f"<-- Steps: {len(path)-1} -->")


def part_one(grid):
    graph = grid_to_graph(grid)
    [start, end] = find_start_end(grid)
    path = graph.dijkstras_path(start, end)

    print_path_map(path, grid)


def find_all_char_in_grid(char, grid):
    x_bound = len(grid[0])
    y_bound = len(grid)
    starts = []
    for y in range(0, y_bound):
        for x in range(0, x_bound):
            if grid[y][x] == char:
                start = f"{x}-{y}"
                starts.append(start)
            if grid[y][x] == "E":
                end = f"{x}-{y}"
    return [starts, end]



def part_two(grid):
    graph = grid_to_graph(grid)
    [start, end] = find_start_end(grid)
    path = graph.dijkstras_path(start, end)

    total_steps = len(path)

    for step in range(0,total_steps):
        coords = path[step].split("-")
        x = int(coords[0])
        y = int(coords[1])
        char = grid[y][x]
        if char == 'b':
            return total_steps - step

    return "oops"
    # 459 correct guess!
    # print_path_map(path, grid)


test_grid = ["Sabqponm","abcryxxl","accszExk","acctuvwj","abdefghi"]
grid = file_to_list("day_12_data.txt")

part_one(grid)
# print(part_two(grid))
