from lib import Graph, deikstra

if __name__ == '__main__':
    # task 1
    g = Graph()
    g.add_vertexes(10)

    g.add_relation(1, 2, 5)
    g.add_relation(1, 8, 3)

    g.add_relation(2, 3, 2)
    g.add_relation(2, 7, 3)

    g.add_relation(3, 5, 5)

    g.add_relation(4, 3, 2)

    g.add_relation(5, 4, 1)
    g.add_relation(5, 10, 2)

    g.add_relation(6, 3, 4)
    g.add_relation(6, 5, 1)
    g.add_relation(6, 8, 6)
    g.add_relation(6, 9, 2)

    g.add_relation(7, 1, 2)
    g.add_relation(7, 3, 2)
    g.add_relation(7, 6, 5)

    g.add_relation(8, 2, 1)
    g.add_relation(8, 7, 4)
    g.add_relation(8, 9, 1)

    g.add_relation(9, 10, 5)

    g.add_relation(10, 4, 6)
    g.add_relation(10, 6, 3)

    print('Task 1')
    print(deikstra(g, 1))
    print('\n')