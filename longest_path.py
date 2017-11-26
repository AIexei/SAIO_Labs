from lib import Graph, markup_method

if __name__ == '__main__':
    # task 1
    g = Graph()
    g.add_vertexes(6)

    g.add_relation(1, 2, 2)
    g.add_relation(1, 6, 1)

    g.add_relation(2, 3, 2)
    g.add_relation(2, 5, 7)

    g.add_relation(3, 4, 8)

    g.add_relation(5, 3, 1)
    g.add_relation(5, 4, 1)

    g.add_relation(6, 2, 4)
    g.add_relation(6, 3, 4)
    g.add_relation(6, 5, 1)

    result = markup_method(g, 1, 4)
    print('Longest path is ' + str(result[0]))
    print('Path: ' + str(result[1]))