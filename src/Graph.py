from Nodes import *
from Edges import *

class Graph:

    def __init__(self):
        self.nodes_dict = {}
        self.num_nodes = 0

    def __iter__(self):
        return iter(self.nodes_dict.values())

    def get_num_vertices(self):
        return self.num_nodes

    def add_dummy_supply_node(self, nodeId, max_warehouse_size):
        self.num_nodes = self.num_nodes + 1
        new_vertex = DummySupplyNode(nodeId, max_warehouse_size, "dummy_supply_node")
        self.nodes_dict[nodeId] = new_vertex
        return new_vertex
    
    def add_collection_node(self, nodeId):
        self.num_nodes = self.num_nodes + 1
        new_vertex = CollectionNode(nodeId, "collection_node")
        self.nodes_dict[nodeId] = new_vertex
        return new_vertex

    def get_nodes_keys(self):
        return self.nodes_dict.keys()
    
    def get_node(self, nodeId):
        if nodeId in self.nodes_dict:
            return self.nodes_dict[nodeId]
        else:
            return None

    # metodo per aggiungere un arco orientato già creato tra due nodi già creati
    def add_edge(self, startNode, endNode, edge):
        self.nodes_dict[startNode].add_neighbor(self.nodes_dict[endNode], edge)
        self.nodes_dict[endNode].add_neighbor(self.nodes_dict[startNode], edge)


if __name__ == '__main__':
    g = Graph()

    print("\ndummy supply node data test:")
    g.add_dummy_supply_node("dummy_supply_node_example", 20)
    print(g.get_node("dummy_supply_node_example"))
    v1 = g.get_node("dummy_supply_node_example")
    print(v1.get_id())
    print(v1.get_neighbors())
    print(v1.get_max_warehouse_size())
    print(v1.get_type())

    print("\ncollection node data test:")
    g.add_collection_node("collection_node_example")
    print(g.get_node("collection_node_example"))
    v2 = g.get_node("collection_node_example")
    print(v2.get_id())
    print(v2.get_neighbors())
    print(v2.get_type())

    print(g.get_nodes_keys())
    print(g.get_num_vertices())

    print("\ninsert edge test")
    e = SupplyEdge("supply_edge_example", "supply_edge")
    g.add_edge(v1.get_id(), v2.get_id(), e)
    for n in g:
        for w in n.get_neighbors():
            nid = n.get_id()
            wid = w.get_id()

            print ("( %s , %s, %s)"  % ( nid, wid, n.get_edge_id(w).get_type()))



