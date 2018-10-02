""" Модель Боллобаша–Риордана """

import networkx as nx
import random as r


def creating_web_graph(n, m, a=0.3):
    g = nx.MultiGraph()
    # g.add_node(1)
    # g.add_edge(1,1)
    for i in range(1, n * m + 1):
        add_node_edge(g, i)
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


if __name__ == "__main__":
    # for k in range(10):
    #     g = generateNewNode(k)
    #     print("Graph " + str(k) + ": ", g.nodes)
    #     print(g.edges)
    import cProfile, pstats, io
    from pstats import SortKey
    pr = cProfile.Profile()
    pr.enable()

    g = creating_web_graph(4000, 16)
    # print("Graph " ": ", g.nodes)
    # print(g.edges)
    print("nodes_with_selfloops: ", [x for x in g.nodes_with_selfloops()], "\nnumber_of_selfloops^ ",
          g.number_of_selfloops())

    pr.disable()
    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
