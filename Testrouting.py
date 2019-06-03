import json
import os
from routing import dijkstra_generalized
from routing import forwarding
import networkx as nx

if __name__ == '__main__':
    # load test graph
    filename = os.path.join('.', 'KuroseRoss5-15.json')
    netjson = json.load(open(filename))

    # construct networkx graph
    graph = nx.Graph()
    graph.add_nodes_from(
        ((node['id'], node['properties']) for node in netjson['nodes']))
    graph.add_edges_from(
        ((link['source'], link['target'], {'cost': link['cost']}) for link in netjson['links']))

    # apply networkx function
    P, D = nx.dijkstra_predecessor_and_distance(graph, 'u', weight='cost')

    # apply our function
    P1, D1 = dijkstra_generalized(graph, 'u', weight='cost')

    # assert outputs
    assert D == D1
    assert P == P1
    print('Dijkstra\'s algorithm test passed.')

    # test forwarding tables
    table = forwarding(P1, 'u')
    expected_table = {'y': ('u', 'w'), 'z': ('u', 'w'), 'v': (
        'u', 'w'), 'x': ('u', 'x'), 'w': ('u', 'w')}
    assert table == expected_table
    print('Forwarding table test passed.')