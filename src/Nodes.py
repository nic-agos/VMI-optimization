import sys

class DummySupplyNode:

    def __init__(self, max_warehouse_size):
        self.id = "DummySupplyNode"
        self.adjacent = {}
        self.type = "dummy_supply_node"
        self.max_warehouse_size = max_warehouse_size

    #per ottenere l'identificativo del nodo
    def get_id(self):
        return self.id

    #per impostare l'id del nodo
    def set_id(self, value):
        self.id = value
        
    # per aggiungere un nodo adiacente con il relativo arco che li collega
    def add_neighbor(self, neighbor, edgeId):
        self.adjacent[neighbor] = edgeId

    #per ottenere tutti i nodi adiacenti al nodo
    def get_neighbors(self):
        return self.adjacent.keys()

    #per ottenere l'arco che collega il nodo con neighbor
    def get_edge_to_neighbor(self, neighbor):
        return self.adjacent[neighbor]

    #per ottenere la capacità massima del magazino
    def get_max_warehouse_size(self):
        return self.max_warehouse_size

    #per impostare la capacità massima del magazino
    def set_max_warehouse_size(self, value):
        self.max_warehouse_size = value

    #per ottenere il tipo dell'arco
    def get_type(self):
        return self.type
    
    #per impostare il tipo dell'arco
    def set_type(self, type):
        self.type = type

class CollectionNode:

    def __init__(self, total_demand):
        self.id = "CollectionNode"
        self.adjacent = {}
        self.type = "collection_node"
        self.total_demand = total_demand 
    
    #per ottenere l'identificativo del nodo
    def get_id(self):
        return self.id

    #per impostare l'id del nodo
    def set_id(self, value):
        self.id = value
        
    # per aggiungere un nodo adiacente con il relativo arco che li collega
    def add_neighbor(self, neighbor, edgeId):
        self.adjacent[neighbor] = edgeId

    #per ottenere tutti i nodi adiacenti al nodo
    def get_neighbors(self):
        return self.adjacent.keys()

    #per ottenere l'arco che collega il nodo con neighbor
    def get_edge_to_neighbor(self, neighbor):
        return self.adjacent[neighbor]

    #per ottenere il tipo dell'arco
    def get_type(self):
        return self.type
    
    #per impostare il tipo dell'arco
    def set_type(self, type):
        self.type = type
    
    #per ottenere la richiesta totale di merci
    def get_total_demand(self):
        return self.total_demand

    #per impostare la richiesta totale di merci
    def set_total_domand(self, demand):
        self.total_demand = demand


class SupplierNode:

    def __init__(self, day, warehouse_usage):
        self.id = "SupplierNode" + "_" + str(day)
        self.adjacent = {}
        self.type = "supplier_node"
        self.day = day
        self.warehouse_usage = warehouse_usage
        
    #per ottenere l'identificativo del nodo
    def get_id(self):
        return self.id

    #per impostare l'id del nodo
    def set_id(self, value):
        self.id = value

    # per aggiungere un nodo adiacente con il relativo arco che li collega
    def add_neighbor(self, neighbor, edgeId):
        self.adjacent[neighbor] = edgeId

    #per ottenere tutti i nodi adiacenti al nodo
    def get_neighbors(self):
        return self.adjacent.keys()

    #per ottenere l'arco che collega il nodo con neighbor
    def get_edge_to_neighbor(self, neighbor):
        return self.adjacent[neighbor]

    #per ottenere l'utilizzo del magazzino  
    def get_warehouse_usage(self):
        return self.warehouse_usage
    
    #per impostare l'utilizzo del magazzino
    def set_warehouse_usage(self, value):
        self.warehouse_usage = value

    #per ottenere il giorno
    def get_day(self):
        return self.day

    #per impostare il giorno
    def set_day(self, value):
        self.day = value

    #per ottenere il tipo dell'arco
    def get_type(self):
        return self.type
    
    #per impostare il tipo dell'arco
    def set_type(self, type):
        self.type = type

class RetailerNode:

    def __init__(self, id, day, warehouse_usage, demand):
        self.id = "RetailerNode" + "_" + str(id) + "_" + str(day)
        self.adjacent = {}
        self.type = "retailer_node"
        self.day = day
        self.warehouse_usage = warehouse_usage
        self.demand = demand
    
    #per ottenere l'identificativo del nodo
    def get_id(self):
        return self.id
    
    #per impostare l'id del nodo
    def set_id(self, value):
        self.id = value

    # per aggiungere un nodo adiacente con il relativo arco che li collega
    def add_neighbor(self, neighbor, edgeId):
        self.adjacent[neighbor] = edgeId

    #per ottenere tutti i nodi adiacenti al nodo
    def get_neighbors(self):
        return self.adjacent.keys()

    #per ottenere l'arco che collega il nodo con neighbor
    def get_edge_to_neighbor(self, neighbor):
        return self.adjacent[neighbor]
    
    #per ottenere l'utilizzo del magazzino
    def get_warehouse_usage(self):
        return self.warehouse_usage
    
    #per impostare l'utilizzo del magazzino
    def set_warehouse_usage(self, value):
        self.warehouse_usage = value

    # per ottenere la domanda di merci
    def get_demand(self):
        return self.demand
    
    #per impostare la domanda di merci
    def set_demand(self, value):
        self.demand = value

    #per ottenere il giorno
    def get_day(self):
        return self.day

    #per impostare il giorno
    def set_day(self, value):
        self.day = value

    #per ottenere il tipo dell'arco
    def get_type(self):
        return self.type
    
    #per impostare il tipo dell'arco
    def set_type(self, type):
        self.type = type
 
    

