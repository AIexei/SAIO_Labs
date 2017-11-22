from lib import floyd, print_matrix, Graph

if __name__ == '__main__':
    # test task
    g = Graph()
    g.add_vertexes(3)

    g.add_relation(1, 1, 2)
    g.add_relation(1, 2, 8)
    g.add_relation(1, 3, 5)

    g.add_relation(2, 1, 3)

    g.add_relation(3, 2, 2)

    a, r = floyd(g.get_matrix())

    print('Task 1\n')

    print('Matrix D:')
    print_matrix(a)

    print('\n')
    print('Matrix R:')
    print_matrix(r)


    # sample task
    g = Graph()
    g.add_vertexes(8)

    g.add_relation(1, 2, 9)
    g.add_relation(1, 4, 3)

    g.add_relation(2, 1, 9)
    g.add_relation(2, 3, 2)
    g.add_relation(2, 5, 7)

    g.add_relation(3, 2, 2)
    g.add_relation(3, 4, 2)
    g.add_relation(3, 5, 4)
    g.add_relation(3, 6, 8)
    g.add_relation(3, 7, 6)

    g.add_relation(4, 1, 3)
    g.add_relation(4, 3, 2)
    g.add_relation(4, 7, 5)

    g.add_relation(5, 2, 7)
    g.add_relation(5, 3, 4)
    g.add_relation(5, 6, 10)

    g.add_relation(6, 3, 8)
    g.add_relation(6, 5, 10)
    g.add_relation(6, 7, 7)

    g.add_relation(7, 3, 6)
    g.add_relation(7, 4, 5)
    g.add_relation(7, 6, 7)

    g.add_relation(8, 5, 9)
    g.add_relation(8, 6, 12)
    g.add_relation(8, 7, 10)

    a, r = floyd(g.get_matrix())

    print('\nTask 2\n')

    print('Matrix D:')
    print_matrix(a)

    print('\n')
    print('Matrix R:')
    print_matrix(r)


