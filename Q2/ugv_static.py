import heapq
import random
import time

GRID_SIZE = 70

MOVES = [(1,0),(-1,0),(0,1),(0,-1)]

DENSITY = {
    "low":0.1,
    "medium":0.2,
    "high":0.3
}


def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def generate_grid(density,start,goal):

    grid=[[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    obstacles=int(GRID_SIZE*GRID_SIZE*density)

    count=0

    while count<obstacles:

        x=random.randint(0,GRID_SIZE-1)
        y=random.randint(0,GRID_SIZE-1)

        if (x,y)!=start and (x,y)!=goal and grid[x][y]==0:

            grid[x][y]=1
            count+=1

    return grid


def valid(x,y,grid):

    return 0<=x<GRID_SIZE and 0<=y<GRID_SIZE and grid[x][y]==0


def reconstruct(parent,current):

    path=[]

    while current in parent:
        path.append(current)
        current=parent[current]

    path.append(current)

    return path[::-1]


def astar(grid,start,goal):

    pq=[]
    heapq.heappush(pq,(0,0,start))

    g_cost={start:0}

    parent={}

    visited=set()

    nodes=0

    while pq:

        f,g,current=heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        nodes+=1

        if current==goal:
            return reconstruct(parent,current),nodes

        for dx,dy in MOVES:

            nx=current[0]+dx
            ny=current[1]+dy

            neighbor=(nx,ny)

            if valid(nx,ny,grid):

                new_g=g+1

                if neighbor not in g_cost or new_g<g_cost[neighbor]:

                    g_cost[neighbor]=new_g

                    parent[neighbor]=current

                    f_cost=new_g+heuristic(neighbor,goal)

                    heapq.heappush(pq,(f_cost,new_g,neighbor))

    return None,nodes


def main():

    print("Grid Size = 70 x 70 km")

    sx=int(input("Start X: "))
    sy=int(input("Start Y: "))

    gx=int(input("Goal X: "))
    gy=int(input("Goal Y: "))

    start=(sx,sy)
    goal=(gx,gy)

    level=input("Obstacle density (low/medium/high): ").lower()

    grid=generate_grid(DENSITY[level],start,goal)

    t1=time.time()

    path,nodes=astar(grid,start,goal)

    t2=time.time()

    print("\n----- RESULTS -----")

    if path:

        print("Path found")

        print("Path length:",len(path)-1)

    else:

        print("No path found")

    print("Nodes expanded:",nodes)

    print("Execution time:",round(t2-t1,5),"seconds")

    print("\nPath:")

    print(path)


if __name__=="__main__":
    main()
