class DummySupplyNode:

    def __init__(self, id, max_warehouse_size, type):
        self.id = id
        self.adjacent = {}
        self.max_warehouse_size = max_warehouse_size
        self.type = type

    # per aggiungere un nodo adiacente con il relativo arco che li collega
    def add_neighbor(self, neighbor, edgeId):
        self.adjacent[neighbor] = edgeId

    #per ottenere tutti i nodi adiacenti al nodo
    def get_neighbors(self):
        return self.adjacent.keys()
    
    #per ottenere l'identificativo del nodo
    def get_id(self):
        return self.id

    #per impostare l'id del nodo
    def set_id(self, value):
        self.id = value

    #per ottenere l'arco che collega il nodo con neighbor
    def get_edge_id(self, neighbor):
        return self.adjacent[neighbor]

    #per ottenere la capacità massima del magazino
    def get_max_warehouse_size(self):
        return self.max_warehouse_size

    #per impostare la capacità massima del magazino
    def set_max_warehouse_size(self, value):
        self.max_warehouse_size = value

    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type

class CollectionNode:

    def __init__(self, id, type):
        self.id = id
        self.adjacent = {}
        self.type = type
    
    # per aggiungere un nodo adiacente con il relativo arco che li collega
    def add_neighbor(self, neighbor, edgeId):
        self.adjacent[neighbor] = edgeId

    #per ottenere tutti i nodi adiacenti al nodo
    def get_neighbors(self):
        return self.adjacent.keys()
    
    #per ottenere l'identificativo del nodo
    def get_id(self):
        return self.id

    #per impostare l'id del nodo
    def set_id(self, value):
        self.id = value

    #per ottenere l'id di uno specifico arco che collega il nodo con un suo vicino
    def get_edge_id(self, neighbor):
        return self.adjacent[neighbor]

    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type


class SupplierNode:

    def __init__(self, id, day, type):
        self.id = id
        self.adjacent = {}
        self.warehouse_usage = 0
        self.day = day
        self.type = type

    # per aggiungere un nodo adiacente con il relativo arco che li collega
    def add_neighbor(self, neighbor, edgeId):
        self.adjacent[neighbor] = edgeId

    #per ottenere tutti i nodi adiacenti al nodo
    def get_neighbors(self):
        return self.adjacent.keys()
    
    #per ottenere l'identificativo del nodo
    def get_id(self):
        return self.id

    #per impostare l'id del nodo
    def set_id(self, value):
        self.id = value

    #per ottenere l'id di uno specifico arco che collega il nodo con un suo vicino
    def get_edge_id(self, neighbor):
        return self.adjacent[neighbor]
    
    def add_edge(self):
        pass
        
    def get_warehouse_usage(self):
        return self.warehouse_usage
    
    def set_warehouse_usage(self, value):
        self.warehouse_usage = value

    def get_day(self):
        return self.day

    def set_day(self, value):
        self.day = value

    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type

class RetailerNode:

    def __init__(self, id, day, type):
        self.id = id
        self.adjacent = {}
        self.day = day
        self.warehouse_usage = 0
        self.demand = 0
        self.type = type
    
    #per ottenere l'identificativo del nodo
    def get_id(self):
        return self.id
    
    #per ottenere l'id di uno specifico arco che collega il nodo con un suo vicino
    def get_edge_id(self, neighbor):
        return self.adjacent[neighbor]

    # per aggiungere un nodo adiacente con il relativo arco che li collega
    def add_neighbor(self, neighbor, edgeId):
        self.adjacent[neighbor] = edgeId

    #per ottenere tutti i nodi adiacenti al nodo
    def get_neighbors(self):
        return self.adjacent.keys()
    
    def get_warehouse_usage(self):
        return self.warehouse_usage
    
    def set_warehouse_usage(self, value):
        self.warehouse_usage = value

    def get_demand(self):
        return self.demand
    
    def set_demand(self, value):
        self.demand = value

    
    


