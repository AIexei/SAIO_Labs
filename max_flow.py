from lib import Graph
from copy import deepcopy

class FlowNetwork:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start -1
        self.end = end - 1
        self.residual = deepcopy(self.graph.weights)
        self.max_flow = 0

        self.labels = {self.start: [float('inf'), None]}


    def find_path(self, from_vertex, labels):
        following = {}

        for i in self.graph.relations[from_vertex]:
            capacity = self.residual[(from_vertex, i)]

            if capacity > 0 and i not in labels.keys():
                following[i] = capacity

        if len(following) > 0:
            max_res_vertex = -1
            max_residual = 0

            for v, c in following.items():
                if c > max_residual:
                    max_residual = c
                    max_res_vertex = v

            labels[max_res_vertex] = [max_residual, from_vertex]

            if max_res_vertex == self.end:
                cur_flow = min(map(lambda x: x[0], labels.values()))
                self.max_flow += cur_flow

                labels.pop(self.start)

                for v, label in labels.items():
                    self.residual[(label[1], v)] -= cur_flow

                return self.find_path(self.start, deepcopy(self.labels))
            else:
                return self.find_path(max_res_vertex, labels)
        else:
            if from_vertex == self.start:
                return self.max_flow
            else:
                previous_vertex = labels[from_vertex][1]
                labels.pop(from_vertex)

                relations = self.graph.relations[previous_vertex]
                relations.remove(from_vertex)
                self.graph.relations[previous_vertex] = relations

                return self.find_path(previous_vertex, labels)


if __name__ == '__main__':
    g = Graph()
    g.add_vertexes(7)

    g.add_relation(6, 1, 4)
    g.add_relation(6, 3, 9)

    g.add_relation(1, 4, 4)
    g.add_relation(1, 3, 2)

    g.add_relation(2, 4, 1)
    g.add_relation(2, 5, 10)

    g.add_relation(3, 2, 1)
    g.add_relation(3, 5, 6)

    g.add_relation(4, 5, 1)
    g.add_relation(4, 7, 2)

    g.add_relation(5, 7, 9)

    flow_network = FlowNetwork(g, 6, 7)
    print(flow_network.find_path(flow_network.start, deepcopy(flow_network.labels)))