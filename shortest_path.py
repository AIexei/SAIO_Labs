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


    # task 2
    g = Graph()
    g.add_vertexes(9)

    g.add_relation(1, 2, 6)
    g.add_relation(1, 3, 2)
    g.add_relation(1, 7, 2)

    g.add_relation(2, 3, 5)
    g.add_relation(2, 6, 6)

    g.add_relation(3, 6, 1)

    g.add_relation(4, 3, 2)
    g.add_relation(4, 5, 3)

    g.add_relation(5, 8, 4)

    g.add_relation(6, 1, 4)
    g.add_relation(6, 5, 6)
    g.add_relation(6, 7, 3)
    g.add_relation(6, 8, 7)

    g.add_relation(7, 8, 4)

    g.add_relation(8, 2, 1)
    g.add_relation(8, 9, 1)

    g.add_relation(9, 6, 2)
    g.add_relation(9, 4, 1)
    g.add_relation(9, 5, 5)

    print('Task 2')
    print(deikstra(g, 1))
    print('\n')


    # task 3
    g = Graph()
    g.add_vertexes(8)

    g.add_relation(1, 2, 3)
    g.add_relation(1, 7, 4)

    g.add_relation(2, 3, 4)
    g.add_relation(2, 6, 8)
    g.add_relation(2, 8, 6)

    g.add_relation(3, 5, 6)

    g.add_relation(4, 3, 2)

    g.add_relation(5, 2, 2)
    g.add_relation(5, 7, 2)

    g.add_relation(6, 1, 2)
    g.add_relation(6, 3, 5)
    g.add_relation(6, 4, 1)
    g.add_relation(6, 5, 4)
    g.add_relation(6, 8, 2)

    g.add_relation(7, 6, 6)
    g.add_relation(7, 4, 1)

    g.add_relation(8, 1, 1)
    g.add_relation(8, 7, 5)

    print('Task 3')
    print(deikstra(g, 1))
    print('\n')


    # task 4
    g = Graph()
    g.add_vertexes(8)

    g.add_relation(1, 2, 4)
    g.add_relation(1, 3, 3)
    g.add_relation(1, 6, 7)
    g.add_relation(1, 7, 2)
    g.add_relation(1, 8, 1)

    g.add_relation(2, 3, 5)
    g.add_relation(2, 8, 1)

    g.add_relation(3, 4, 2)

    g.add_relation(4, 5, 1)
    g.add_relation(4, 6, 3)

    g.add_relation(6, 5, 6)

    g.add_relation(7, 3, 4)
    g.add_relation(7, 5, 7)
    g.add_relation(7, 6, 2)

    g.add_relation(8, 3, 4)
    g.add_relation(8, 4, 3)
    g.add_relation(8, 7, 5)

    print('Task 4')
    print(deikstra(g, 1))
    print('\n')


    # task 5
    g = Graph()
    g.add_vertexes(7)

    g.add_relation(1, 2, 4)
    g.add_relation(1, 6, 6)

    g.add_relation(2, 3, 7)
    g.add_relation(2, 4, 1)
    g.add_relation(2, 6, 3)

    g.add_relation(3, 5, 5)
    g.add_relation(3, 4, 2)

    g.add_relation(4, 1, 2)
    g.add_relation(4, 5, 6)
    g.add_relation(4, 6, 4)

    g.add_relation(5, 7, 1)

    g.add_relation(6, 5, 2)
    g.add_relation(6, 7, 3)

    g.add_relation(7, 2, 7)
    g.add_relation(7, 3, 1)
    g.add_relation(7, 4, 3)

    print('Task 5')
    print(deikstra(g, 1))
    print('\n')


    # task 6
    g = Graph()
    g.add_vertexes(8)

    g.add_relation(1, 3, 4)
    g.add_relation(1, 6, 1)
    g.add_relation(1, 8, 4)
    g.add_relation(1, 7, 5)

    g.add_relation(2, 1, 9)
    g.add_relation(2, 3, 1)

    g.add_relation(3, 6, 5)
    g.add_relation(3, 7, 1)
    g.add_relation(3, 5, 2)
    g.add_relation(3, 4, 4)

    g.add_relation(5, 4, 3)
    g.add_relation(5, 8, 8)

    g.add_relation(6, 2, 2)
    g.add_relation(6, 5, 7)
    g.add_relation(6, 8, 3)

    g.add_relation(7, 2, 10)
    g.add_relation(7, 8, 3)

    g.add_relation(8, 4, 6)

    print('Task 6')
    print(deikstra(g, 1))
    print('\n')