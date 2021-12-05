from Nodes import *
from Edges import *
from Main import *


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


if __name__ == '__main__':
    g = Graph()

    print("\ndummy supply node data test:")
    g.add_dummy_supply_node(100)
    print("nodes keys: ", g.get_nodes_keys())
    v1 = g.get_node("DummySupplyNode")
    print(v1)
    print(v1.get_id())
    print(v1.get_neighbors())
    print(v1.get_max_warehouse_size())
    print("boolean:", v1.get_type() == "dummy_supply_node")

    print("\ncollection node data test:")
    g.add_collection_node(100)
    v2 = g.get_node("CollectionNode")
    print(v2)
    print(v2.get_id())
    print(v2.get_neighbors())
    print(v2.get_type())

    print("\nsupplier node data test:")
    g.add_supplier_node("MON", 50)
    v3 = g.get_node("SupplierNode_MON")
    print(v3)
    print(v3.get_id())
    print(v3.get_neighbors())
    print(v3.get_type())

    print("Nodes id: " , g.get_nodes_keys())
    print("Number of nodes: ", g.get_num_nodes())

    print("\ninsert edge test")
    suppEdge = SupplyEdge(10, 150, 0)

    if g.add_edge(v1.get_id(), v2.get_id(), suppEdge) != 0:
        print("stampo il grafo: ")
        printGraph(g)
    



