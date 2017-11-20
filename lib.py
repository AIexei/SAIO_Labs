import collections


class Graph:
    def __init__(self):
        self.vertexes = set()
        self.relations = collections.defaultdict(list)
        self.weights = {}

    @property
    def n(self):
        return len(self.vertexes)

    def add_vertex(self, value):
        self.vertexes.add(value - 1)

    def add_vertexes(self, count):
        for i in range(count):
            self.add_vertex(i)

    def add_relation(self, from_vertex, to_vertex, distance):
        if from_vertex == to_vertex:
            return

        self.relations[from_vertex-1].append(to_vertex-1)
        self.weights[(from_vertex-1, to_vertex-1)] = distance

    def __str__(self):
        string = "Vertexes: " + str(self.vertexes) + "\n"
        string += "Relations: " + str(self.relations) + "\n"
        string += "Weights: " + str(self.weights)
        return string


def deikstra(graph, start):
    used = set()

    distances = [float('inf')] * graph.n
    distances[start-1] = 0

    for i in range(graph.n):
        minimum = float('inf')
        position = 0

        for j in range(graph.n):
            if distances[j] < minimum and j not in used:
                minimum = distances[j]
                position = j

        used.add(position)
        for vertex in graph.relations[position]:
            distances[vertex] = min(distances[vertex], distances[position]+graph.weights[(position, vertex)])

    return distances