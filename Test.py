import json
import os
from routing import dijkstra_generalized

filename = os.path.join('.', 'KuroseRoss5-15.json')  # modify as required
netjson = json.load(open(filename))

import networkx as nx  # saves typing later on

graph = nx.Graph()
graph.add_nodes_from((
    (node['id'], node['properties'])  # node-attributes
    for node in netjson['nodes']))
graph.add_edges_from((
    (link['source'], link['target'], {'cost': link['cost']})  # source-target-attributes
    for link in netjson['links']))

p, d = dijkstra_generalized(graph, "u", "cost")
print(p)
print(d)