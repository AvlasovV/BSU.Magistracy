""" Модель Боллобаша–Риордана """

import networkx as nx
import random as r
from math import ceil


def creating_web_graph(n, m, a=0.3):
    g = nx.MultiGraph()
    # g.add_node(1)
    # g.add_edge(1,1)
    for i in range(1, n * m + 1):
        add_node_edge(g, i)
    k = 0
    for i in g.edges:
        print(i, end="")
        k += 1
        if k == 10:
            print()
            k = 0

    g = transformation_to_web_graph(g, n, m)
    return g


def add_node_edge(graph, n):
    """Create fundamental graph with 1 edge for 1 node"""
    degrees = graph.degree()
    graph.add_node(n)
    pos = r.randint(1, 2 * n - 1)
    if pos == 2 * n - 1:
        graph.add_edge(n, n)
    else:
        sum = 0
        for i in degrees:
            if sum < pos <= sum + i[1]:
                graph.add_edge(n, i[0])
                break
            sum += i[1]


def transformation_to_web_graph(graph, n, m):
    """From fundamental graph function makes WemGraph by bollobash-riordan"""
    g2 = nx.MultiDiGraph()
    for i in range(1, n + 1):
        g2.add_node(i * m)
    for edge in graph.edges:
        # difference = abs(edge[1] - edge[0])
        # is_in_one_cluster = (difference / m < 1)
        # if is_in_one_cluster:
        g2.add_edge(m * ceil(edge[1] / m), m * ceil(edge[0] / m))
    return g2


if __name__ == "__main__":
    # for k in range(10):
    #     g = generateNewNode(k)
    #     print("Graph " + str(k) + ": ", g.nodes)
    #     print(g.edges)
    import cProfile, pstats, io
    from pstats import SortKey

    pr = cProfile.Profile()
    pr.enable()

    g = creating_web_graph(4, 2)
    # print("Graph " ": ", g.nodes)
    print('\n', g.edges, end="\n")
    print(g.nodes)
    print("nodes_with_selfloops: ", [x for x in g.nodes_with_selfloops()], "\nnumber_of_selfloops^ ",
          g.number_of_selfloops())
    diam = nx.diameter(g)
    average_short_path = nx.average_shortest_path_length(g)

    pr.disable()
    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
