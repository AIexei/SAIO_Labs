class AssignTask:
    def __init__(self, matrix):
        self.matrix = matrix


    def prepare_matrix(self):
        for i in range(len(self.matrix)):
            min_value = min(self.matrix[i])
            self.matrix[i] = list(map(lambda x: x - min_value, self.matrix[i]))

        for j in range(len(self.matrix)):
            min_value = float('inf')

            for i in range(len(self.matrix)):
                if self.matrix[i][j] < min_value:
                    min_value = self.matrix[i][j]

            if min_value > 0:
                for i in range(len(self.matrix)):
                    self.matrix[i][j] -= min_value


    def print_matrix(self):
        for i in self.matrix:
            print(i)



if __name__ == '__main__':
    matrix = [
        [1, 7, 1, 3],
        [1, 6, 4, 6],
        [17, 1, 5, 1],
        [1, 6, 10, 4],
    ]

    s = AssignTask(matrix)
    s.prepare_matrix()
    s.print_matrix()