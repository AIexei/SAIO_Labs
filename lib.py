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


    def get_matrix(self):
        matrix = [[float('inf') for _ in range(self.n)] for _ in range(self.n)]

        for i in self.relations.keys():
            for j in self.relations[i]:
                matrix[i][j] = self.weights[(i, j)]

        for i in range(self.n):
            matrix[i][i] = 0

        return matrix


    def __str__(self):
        string = "Vertexes: " + str(self.vertexes) + "\n"
        string += "Relations: " + str(self.relations) + "\n"
        string += "Weights: " + str(self.weights)
        return string


def print_matrix(matrix):
    for row in matrix:
        print(row)


def floyd(matrix):
    n = len(matrix)
    gaps = [list(range(1, n+1)) for _ in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    gaps[i][j] = k + 1

    return (matrix, gaps)


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