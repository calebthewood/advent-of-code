from utils import file_to_list


class PriorityQueue:
    def __init__(self):
        self.values = []

    def enqueu(self, val, priority):
        node = {
            "val": val,
            "priority": priority
        }
        self.values.append(node)
        self.values.sort()

    def dequeue(self):
        return self.values.pop(0)

    def sort(self):
        self.values.sort(key=lambda x: x["priority"])


class WeightedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if not self.adjacencyList[vertex]:
            self.adjacencyList[vertex] = []

    def add_edge(self, v1, v2, weight):
        self.adjacency_list[v1].append({"node": v2, "weight": weight})
        self.adjacency_list[v2].append({"node": v1, "weight": weight})

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

        while len(nodes["values"]):
            smallest = nodes.dequeue().val
            if smallest == end:
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]
                break

            if smallest or distances[smallest] != float('inf'):
                for neighbor in self.adjacency_list[smallest]:
                    next_node = self.adjacency_list[smallest][neighbor]
                    prospect = distances[smallest] + next_node["weight"]
                    next_neighbor = next_node.node
                    if prospect < distances[next_neighbor]:
                        distances[next_neighbor] = prospect
                        previous[next_neighbor] = smallest
                        nodes.enqueue(next_neighbor, prospect)

        path.extend(smallest)
        path.reverse()
        return len(path)


def validate_elevation(x, y, nx, ny, new, grid):
    """
    Determines whether it's possible to travel between 2 cells on the grid
    with a vertical limit of 1.
        [5,5] "a", [5,6] "b" >> true
        [5,5] "a", [5,6] "g" >> false
    """
    elevation = "ESabcdefghijklmnopqrstuvwxyz"
    vertical_limit = 1
    current_elev = elevation.index(grid[y][x]) + vertical_limit
    new_elev = elevation.index(grid[ny][nx])
    return new_elev <= current_elev


def get_adjacency_list(x, y):
    """Checks NWSE move options for elevation and proximity to end"""
    nwse = [[x, y-1], [x-1, y], [x, y+1], [x+1, y]]
    adjacency_list = []
    x_bound = len(grid[0])
    y_bound = len(grid)

    for [nx, ny] in nwse:
        if (0 <= nx < x_bound) and (0 <= ny < y_bound):
            if validate_elevation(x, y, nx, ny):
                vertex = f"{nx}-{ny}"
                adjacency_list.append(vertex)

    return adjacency_list


def grid_to_graph(grid):
    graph = WeightedGraph()
    x_bound = len(grid[0])
    y_bound = len(grid)

    for y in range(0, y_bound):
        for x in range(0, x_bound):
            elevation = grid[y][x]
            vertex_a = f"{x}-{y}"
            graph.add_vertex(vertex)
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


def part_one():
    grid = file_to_list("day_12_data.txt")
    graph = grid_to_graph(grid)
    [start, end] = find_start_end(grid)

    print(graph.dijkstras_path(start,end))

part_one()
