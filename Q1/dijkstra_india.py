import csv
import heapq
from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def load_graph(self, filename):

        with open(filename, "r") as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:

                city1 = row[0].strip()
                city2 = row[1].strip()
                distance = float(row[2].strip())

                self.add_edge(city1, city2, distance)

    def dijkstra(self, source):

        distance = {node: float('inf') for node in self.graph}

        parent = {node: None for node in self.graph}

        distance[source] = 0

        pq = [(0, source)]

        while pq:

            current_distance, current_city = heapq.heappop(pq)

            if current_distance > distance[current_city]:
                continue

            for neighbor, weight in self.graph[current_city]:

                new_distance = current_distance + weight

                if new_distance < distance[neighbor]:

                    distance[neighbor] = new_distance

                    parent[neighbor] = current_city

                    heapq.heappush(pq, (new_distance, neighbor))

        return distance, parent

    def get_path(self, parent, city):

        path = []

        while city is not None:

            path.append(city)

            city = parent[city]

        path.reverse()

        return path


def main():

    g = Graph()

    g.load_graph("india_roads.csv")

    source = input("Enter source city: ").strip().title()

    if source not in g.graph:

        print("City not found in graph")

        return

    distance, parent = g.dijkstra(source)

    print("\nShortest distances from", source, "\n")

    for city in distance:

        if distance[city] == float('inf'):

            print(city, ": Not reachable")

        else:

            path = g.get_path(parent, city)

            print(city, ":", distance[city], "km | Path ->", " -> ".join(path))


if __name__ == "__main__":
    main()


