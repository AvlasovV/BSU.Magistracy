""" Модель Боллобаша–Риордана """

import networkx as nx
import random as r


def generateNewNode(n, a=0.3):
    g = nx.MultiGraph()
    # g.add_node(1)
    # g.add_edge(1,1)
    for i in range(1, n + 1):
        getNodeForConnect(g, i)
    return g


def getNodeForConnect(g, n):
    degrees = g.degree()
    g.add_node(n)
    pos = r.randint(1, 2 * n - 1)
    if pos == 2 * n - 1:
        g.add_edge(n, n)
    else:
        sum = 0
        for i in degrees:
            if sum < pos <= sum + i[1]:
                g.add_edge(n, i)
                break
            sum += i[1]


if __name__ == "__main__":
    for k in range(10):
        g = generateNewNode(k)
        print(g.nodes, '\n', g.edges)

