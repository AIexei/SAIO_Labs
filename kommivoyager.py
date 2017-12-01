from copy import deepcopy

class Solver:
    def __init__(self, matrix):
        self.original_m = matrix
        self.m = deepcopy(self.original_m)

        self.n = len(matrix)
        self.real_n = len(matrix)

        self.marks = {}
        self.path = {}
        self.start = -1


    def solve(self):
        while self.real_n > 0:
            self.prepare_matrix()
            self.make_marks()
            self.reduction()

        return self.calculate_length()


    def calculate_length(self):
        length = 0

        for i, j in self.path.items():
            length += self.original_m[i][j]

        return length


    def prepare_matrix(self):
        for i in range(len(self.m)):
            min_value = min(self.m[i])
            self.m[i] = list(map(lambda x: x if x == float('inf') else x - min_value, self.m[i]))

        for j in range(len(self.m)):
            min_value = float('inf')

            for i in range(len(self.m)):
                if self.m[i][j] < min_value:
                    min_value = self.m[i][j]

            if min_value > 0:
                for i in range(len(self.m)):
                    if self.m[i][j] != float('inf'):
                        self.m[i][j] -= min_value


    def make_marks(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.m[i][j] == 0:
                    self.marks[(i, j)] = self._make_mark_for_vertex(i, j)


    def reduction(self):
        max_mark = max(self.marks.values())

        for c, mark in self.marks.items():
            if mark == max_mark:
                i, j = c

                for x in range(self.n):
                    self.m[x][j] = float('inf')
                    self.m[i][x] = float('inf')

                self.m[j][i] = float('inf')
                self.path[i] = j

                if len(self.path) == 1:
                    self.start = i

                break

        self.marks = {}
        self.real_n -= 1


    def print_matrix(self):
        for i in self.m:
            print(i)

        print('\n\n')


    def _make_mark_for_vertex(self, i, j):
        min_i = float('inf')
        for x in range(self.n):
            if self.m[i][x] < min_i and x != j:
                min_i = self.m[i][x]

        min_j = float('inf')
        for x in range(self.n):
            if self.m[x][j] < min_j and x != i:
                min_j = self.m[x][j]

        return min_j + min_i


if __name__ == '__main__':
    matrix = [
        [float('inf'), 5, 11, 9],
        [10, float('inf'), 8, 7],
        [7, 14, float('inf'), 8],
        [12, 6, 15, float('inf')],
    ]

    s = Solver(matrix)
    print(s.solve())



    matrix = [
        [float('inf'), 10, 25, 25, 10],
        [1, float('inf'), 10, 15, 2],
        [8, 9, float('inf'), 20, 10],
        [14, 10, 24, float('inf'), 15],
        [10, 8, 25, 27, float('inf')],
    ]

    s = Solver(matrix)
    print(s.solve())