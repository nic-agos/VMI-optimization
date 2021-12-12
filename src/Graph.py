from Nodes import *
from Edges import *


class Graph:

    def __init__(self):
        self.nodes_dict = {}
        self.num_nodes = 0

    def __iter__(self):
        return iter(self.nodes_dict.values())

    def get_num_nodes(self):
        return self.num_nodes

    def add_dummy_supply_node(self, max_warehouse_size):
        self.num_nodes = self.num_nodes + 1
        newNode = DummySupplyNode(max_warehouse_size)
        id = newNode.get_id()
        self.nodes_dict[id] = newNode
        return newNode
    
    def add_collection_node(self, total_demand):
        self.num_nodes = self.num_nodes + 1
        newNode = CollectionNode(total_demand)
        id = newNode.get_id()
        self.nodes_dict[id] = newNode
        return newNode
    
    def add_supplier_node(self, day, warehouse_usage):
        self.num_nodes = self.num_nodes + 1
        newNode = SupplierNode(day, warehouse_usage)
        id = newNode.get_id()
        self.nodes_dict[id] = newNode
        return newNode

    def add_retailer_node(self, id, day, warehouse_usage, demand):
        self.num_nodes = self.num_nodes + 1
        newNode = RetailerNode(id, day, warehouse_usage, demand)
        id = newNode.get_id()
        self.nodes_dict[id] = newNode
        return newNode

    def get_nodes_keys(self):
        return self.nodes_dict.keys()
    
    def get_node(self, nodeId):
        if nodeId in self.nodes_dict:
            return self.nodes_dict[nodeId]
        else:
            return None

    # metodo per aggiungere un arco orientato già creato tra due nodi già creati
    def add_edge(self, startNode, endNode, edge):
        if startNode in self.nodes_dict and endNode in self.nodes_dict:
            self.nodes_dict[startNode].add_neighbor(self.nodes_dict[endNode], edge)
        else:
            return 0
    
    def get_edge(self, startNode, endNode):
        sNode = self.get_node(startNode)
        eNode = self.get_node(endNode)
        if startNode in self.nodes_dict and endNode in self.nodes_dict:
            for neighbor in sNode.get_neighbors():
                if endNode == neighbor.get_id():
                    edge = sNode.get_edge_to_neighbor(eNode)
                    return edge
            
            print("I due nodi inseriti non sono collegati da un'arco")
            return None
        else:
            print("Uno o entrambi i nodi inseriti per la ricerca non fanno parte del grafo")






