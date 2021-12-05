from Graph import *
from json import dumps
from Data import *
import sys

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
edgeTypes = ["supply_edge", "dispatch_edge", "holding_edge", "cycle_edge", "shortage_edge", "retailer_collection_edge", "supplier_collection_edge", "retrieval_edge"]
nodeTypes = ["dummy_supply_node", "collection_node", "supplier_node", "retailer_node"]

def printGraph(graph):
    for node in graph:
        for neighbor in node.get_neighbors():
            startNodeId = node.get_id()
            endNodeId = neighbor.get_id()
            edgeId = node.get_edge_to_neighbor(neighbor).get_id()

            print("(%s , %s, %s)"  % (startNodeId, endNodeId, edgeId))

def visualize(graph):
    g = {
    "kind": {"graph": True},
    "nodes": [],
    "edges": []
    }
    for node in graph:
        id = node.get_id()
        g["nodes"].append({"id": id, "label": id, "key" : id})
        json_graph = dumps(g)

    #manca di aggiungere gli archi
    

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
    #manca di inserire i dati nei nodi/archi
    pass

if __name__ == '__main__':
    graph = initialize(1)
    print(graph.get_nodes_keys())
    print(graph.get_num_nodes())
    visualize(graph)