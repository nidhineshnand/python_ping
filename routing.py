# -*- coding: utf-8 -*-

def forwarding(predecessor, source):
    """ 
    Compute a forwarding table from a predecessor list. 
    """
    # TODO


def dijkstra_generalized(graph, source, weight='weight',
                         infinity=None,
                         plus=None,
                         less=None,
                         min=None):
    """
    Least-cost or widest paths via Dijkstra's algorithm.
    """
    # TODO: Please work from Lab 1 code

    import math
    # Definitions consistent with Kurose & Ross
    u = source

    def c(x, y):
        return graph[x][y][weight]

    N = frozenset(graph.nodes())
    NPrime = {u}  # i.e. "set([u])"
    D = dict.fromkeys(N, math.inf)
    P = dict.fromkeys(N, math.inf)

    # Initialization
    for v in N:
        if graph.has_edge(u, v):
            D[v] = c(u, v)
    D[u] = 0  # over-write inf entry for source

    # Loop
    while NPrime != N:
        candidates = {w: D[w] for w in N if w not in NPrime}
        w, Dw = min(candidates.items(), key=lambda item: item[1])
        NPrime.add(w)
        for v in graph[w]:
            if v not in NPrime:
                DvNew = D[w] + c(w, v)
                if DvNew < D[v]:
                    D[v] = DvNew
                    P[v] = v

    return P, D
