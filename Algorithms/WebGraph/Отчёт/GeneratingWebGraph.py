""" Модель Боллобаша–Риордана """

import networkx as nx
import random as r
from math import ceil
from collections import defaultdict
import pandas as ps
import matplotlib.pyplot as plt


def creating_web_graph(n, m):
    g = nx.MultiGraph()
    # g.add_node(1)
    # g.add_edge(1,1)
    for value in range(1, n * m + 1):
        add_node_edge(g, value)
    k = 0
    # for i in g.edges:
    #     print(i, end="")
    #     k += 1
    #     if k == 10:
    #         print()
    #         k = 0

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
    g2 = nx.MultiGraph()
    for i in range(1, n + 1):
        g2.add_node(i * m)
    for edge in graph.edges:
        # difference = abs(edge[1] - edge[0])
        # is_in_one_cluster = (difference / m < 1)
        # if is_in_one_cluster:
        g2.add_edge(m * ceil(edge[1] / m), m * ceil(edge[0] / m))
    return g2


def draw_hist(g, m):
    degree_dict = defaultdict(lambda: int(0))
    for k in g.degree():
        degree_dict[k[1]] += 1

    ps.DataFrame(
        {"Count of nodes": list(degree_dict.keys()), "Node degree": list(degree_dict.values())}).plot(
        x="Count of nodes", kind="bar", color="red", figsize=(20, 12))
    plt.savefig("Histogram 4k nodes m=" + str(m) + ".png")
    plt.clf()


def get_diam_avg_path_connected_components(g):
    connected_components = list(nx.connected_component_subgraphs(g))
    diam = max([nx.diameter(i) for i in connected_components])
    count_of_nodes = []
    for i in connected_components:
        count_of_nodes.append(i.number_of_nodes())
    average_short_path = sum(
        nx.average_shortest_path_length(component) for component in connected_components) / len(
        connected_components)
    return diam, average_short_path, len(connected_components), count_of_nodes


if __name__ == "__main__":
    import cProfile, pstats, io
    from pstats import SortKey

    for i in range(10, 11):

        """Here profiling code starts"""
        pr = cProfile.Profile()
        pr.enable()

        g = creating_web_graph(100, i)

        with open("Graph 4k, m=" + str(i) + ".txt", "w") as f:

            diam, avg_shortest_path, count_of_components, count_of_nodes_in_component \
                = get_diam_avg_path_connected_components(g)
            f.write("Diameter in the biggest connected copmonent = " + str(diam) + '\n')
            f.write("Average shortest path = " + str(avg_shortest_path) + '\n')
            f.write("Count of connected components = " + str(count_of_components) + '\n')
            f.write("Power of different connected components in Graph: \n")
            for i in count_of_nodes_in_component:
                f.write(str(i) + ", ")
            f.write('\n')
            draw_hist(g, i)

            """ending profiling"""
            pr.disable()
            s = io.StringIO()
            sortby = SortKey.CUMULATIVE
            statistics = pstats.Stats(pr, stream=s).sort_stats(sortby)
            statistics.print_stats()
            f.write(s.getvalue())
