# -*- coding: utf-8 -*-


def forwarding(predecessor, source):

    """ 
    Compute a forwarding table from a predecessor list. 
    """
    # Defining the list of nodes that will be checked
    nodes = list(predecessor.keys())
    nodes.remove(source)

    # Getting minimum node (initial node) and removing it from the list
    T = dict.fromkeys(nodes, [])

    # Looping through notes and getting the next hop node
    for n in nodes:
        nextnode = n
        while nextnode != source:
            T[n] = (source, nextnode)
            # This is presented in the from that was presented to us in the lectures
            nextnode = predecessor[nextnode][0]
    return T


def dijkstra_generalized(graph, source, weight='weight'):
    # Removed min=None
    """
    Least-cost or widest paths via Dijkstra's algorithm.
    """
    import math

    # Definitions consistent with Kurose & Ross
    u = source

    def c(x, y):
        return graph[x][y][weight]

    N = frozenset(graph.nodes())
    NPrime = {u}  # i.e. "set([u])"
    D = dict.fromkeys(N, math.inf)
    P = dict.fromkeys(N, [])

    # Initialization
    for v in N:
        if graph.has_edge(u, v):
            D[v] = c(u, v)
            P[v] = [u]
    D[u] = 0  # over-write inf entry for source

    # Loop through all nodes
    while NPrime != N:
        candidates = {w: D[w] for w in N if w not in NPrime}
        w, Dw = min(candidates.items(), key=lambda item: item[1])
        NPrime.add(w)
        for v in graph[w]:
            if v not in NPrime:
                DvNew = D[w] + c(w, v)
                if DvNew < D[v]:
                    D[v] = DvNew
                    P[v] = [w]

    return P, D
