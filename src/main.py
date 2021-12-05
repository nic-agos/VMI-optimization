from Graph import *
from json import dumps
import sys

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
edgeTypes = ["supply_edge", "dispatch_edge", "holding_edge", "cycle_edge", "shortage_edge", "retailer_collection_edge", "supplier_collection_edge", "retrieval_edge"]
nodeTypes = ["dummy_supply_node", "collection_node", "supplier_node", "retailer_node"]

def printGraph(graph):
    for edge in graph:
        for w in edge.get_neighbors():
            startNodeId = edge.get_id()
            endNodeId = w.get_id()
            edgeId = edge.get_edge_to_neighbor(w).get_id()

            print("(%s , %s, %s)"  % (startNodeId, endNodeId, edgeId))

def visualize(graph):
    g = {
    "kind": {"graph": True},
    "nodes": [],
    "edges": []
    }
    for edge in graph:
        id = edge.getId()
        g["nodes"].append({"id": id, "label": id})
        json_graph = dumps(g)
    

def initialize(retailerNumber):
    g = Graph()
    g.add_dummy_supply_node(sys.maxsize)
    g.add_collection_node(0)

    #aggiungo tutti i nodi supplier
    for day in days:
        g.add_supplier_node(day, 0)

    for i in range(1, retailerNumber + 1):
        for day in days:
            g.add_retailer_node(i, day, 0, 0)

    #manca di aggiungere tutti gli archi

    return g
    
def add_data(graph):
    pass

if __name__ == '__main__':
    graph = initialize(1)
    print(graph.get_nodes_keys())
    print(graph.get_num_nodes())
    visualize(graph)