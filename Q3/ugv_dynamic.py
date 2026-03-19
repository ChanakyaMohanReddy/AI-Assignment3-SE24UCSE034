import heapq
import random
import time

GRID_SIZE = 20

MOVES = [(1,0), (-1,0), (0,1), (0,-1)]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def valid(x, y, grid):
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and grid[x][y] == 0

def reconstruct_path(parent, node):
    path = []

    while node in parent:
        path.append(node)
        node = parent[node]

    path.append(node)

    return path[::-1]

def astar(grid, start, goal):

    pq = []
    heapq.heappush(pq, (0, 0, start))

    g_cost = {start: 0}

    parent = {}

    visited = set()

    nodes_expanded = 0

    while pq:

        f, g, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return reconstruct_path(parent, current), nodes_expanded

        for dx, dy in MOVES:

            nx = current[0] + dx
            ny = current[1] + dy

            neighbor = (nx, ny)

            if valid(nx, ny, grid):

                new_cost = g + 1

                if neighbor not in g_cost or new_cost < g_cost[neighbor]:

                    g_cost[neighbor] = new_cost
                    parent[neighbor] = current

                    heapq.heappush(
                        pq,
                        (new_cost + heuristic(neighbor, goal), new_cost, neighbor)
                    )

    return None, nodes_expanded

def add_dynamic_obstacle(grid, forbidden):

    while True:

        x = random.randint(0, GRID_SIZE-1)
        y = random.randint(0, GRID_SIZE-1)

        if (x,y) not in forbidden and grid[x][y] == 0:

            grid[x][y] = 1
            return (x,y)

def print_grid(grid, robot, goal):

    for i in range(GRID_SIZE):

        row = ""

        for j in range(GRID_SIZE):

            if (i,j) == robot:
                row += "R "
            elif (i,j) == goal:
                row += "G "
            elif grid[i][j] == 1:
                row += "# "
            else:
                row += ". "

        print(row)

    print()

def main():

    grid = [[0]*GRID_SIZE for _ in range(GRID_SIZE)]

    start = (0,0)
    goal = (19,19)

    current = start

    replans = 0
    nodes_total = 0

    print("Dynamic UGV Navigation\n")

    while current != goal:

        path, nodes = astar(grid, current, goal)

        nodes_total += nodes

        if not path:
            print("Mission Failed: No Path Available")
            return

        print("Current position:", current)

        print_grid(grid, current, goal)

        if len(path) > 1:
            current = path[1]

        if random.random() < 0.3:

            obstacle = add_dynamic_obstacle(grid, {current, goal})

            print("Dynamic obstacle detected at:", obstacle)
            print("Replanning path...\n")

            replans += 1

    print("Goal reached successfully\n")

    print("Measures of Effectiveness")
    print("-------------------------")
    print("Total replans:", replans)
    print("Total nodes expanded:", nodes_total)

if __name__ == "__main__":
    main()
