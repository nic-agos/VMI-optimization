#implementation of all edge's types

class SupplyEdge:

    def __init__(self, cost, upper_bound, lower_bound):
        self.id = "SupplyEdge"
        self.type = "supply_edge"
        self.cost = cost
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

    #per ottenere l'identificativo del'arco
    def get_id(self):
        return self.id

    #per impostare l'id del'arco
    def set_id(self, value):
        self.id = value

    #per ottenere il tipo dell'arco
    def get_type(self):
        return self.type
    
    #per impostare il tipo dell'arco
    def set_type(self, type):
        self.type = type

    #per impostare il costo dell'arco
    def set_cost(self, cost):
        self.cost = cost
    
    #per ottenere il costo dell'arco
    def get_cost(self):
        return self.cost

    #per impostare l'upper bound dell'arco
    def set_upper_bound(self, upper_bound):
        self.upper_bound = upper_bound

    #per ottenere l'upper bound dell'arco
    def get_upper_bound(self):
        return self.upper_bound

    #per impostare il lower bound dell'arco
    def set_lower_bound(self, lower_bound):
        self.lower_bound = lower_bound

    #per ottenere il lower bound dell'arco
    def get_lower_bound(self):
        return self.lower_bound

class DispatchEdge:

    def __init__(self, id, cost, upper_bound, lower_bound):
        self.id = "DispatchEdge" + "_" + str(id)
        self.type = "dispatch_edge"
        self.cost = cost
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        
    #per ottenere l'identificativo del'arco
    def get_id(self):
        return self.id

    #per impostare l'id del'arco
    def set_id(self, value):
        self.id = value

    #per ottenere il tipo dell'arco
    def get_type(self):
        return self.type
    
    #per impostare il tipo dell'arco
    def set_type(self, type):
        self.type = type

    #per impostare il costo dell'arco
    def set_cost(self, cost):
        self.cost = cost
    
    #per ottenere il costo dell'arco
    def get_cost(self):
        return self.cost

    #per impostare l'upper bound dell'arco
    def set_upper_bound(self, upper_bound):
        self.upper_bound = upper_bound

    #per ottenere l'upper bound dell'arco
    def get_upper_bound(self):
        return self.upper_bound

    #per impostare il lower bound dell'arco
    def set_lower_bound(self, lower_bound):
        self.lower_bound = lower_bound

    #per ottenere il lower bound dell'arco
    def get_lower_bound(self):
        return self.lower_bound

class HoldingEdge:

    def __init__(self, id, cost, upper_bound, lower_bound):
        self.id = "HoldingEdge" + "_" + str(id)
        self.type = "holding_edge"
        self.cost = cost
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
    
    #per ottenere l'identificativo del'arco
    def get_id(self):
        return self.id

    #per impostare l'id del'arco
    def set_id(self, value):
        self.id = value

    #per ottenere il tipo dell'arco
    def get_type(self):
        return self.type
    
    #per impostare il tipo dell'arco
    def set_type(self, type):
        self.type = type

    #per impostare il costo dell'arco
    def set_cost(self, cost):
        self.cost = cost
    
    #per ottenere il costo dell'arco
    def get_cost(self):
        return self.cost

    #per impostare l'upper bound dell'arco
    def set_upper_bound(self, upper_bound):
        self.upper_bound = upper_bound

    #per ottenere l'upper bound dell'arco
    def get_upper_bound(self):
        return self.upper_bound

    #per impostare il lower bound dell'arco
    def set_lower_bound(self, lower_bound):
        self.lower_bound = lower_bound

    #per ottenere il lower bound dell'arco
    def get_lower_bound(self):
        return self.lower_bound

class CycleEdge:

    def __init__(self, id, cost, upper_bound, lower_bound):
        self.id = "CycleEdge" + "_" + str(id)
        self.type = "cycle_edge"
        self.cost = cost
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

    #per ottenere l'identificativo del'arco
    def get_id(self):
        return self.id

    #per impostare l'id del'arco
    def set_id(self, value):
        self.id = value

    #per ottenere il tipo dell'arco
    def get_type(self):
        return self.type
    
    #per impostare il tipo dell'arco
    def set_type(self, type):
        self.type = type

    #per impostare il costo dell'arco
    def set_cost(self, cost):
        self.cost = cost
    
    #per ottenere il costo dell'arco
    def get_cost(self):
        return self.cost

    #per impostare l'upper bound dell'arco
    def set_upper_bound(self, upper_bound):
        self.upper_bound = upper_bound

    #per ottenere l'upper bound dell'arco
    def get_upper_bound(self):
        return self.upper_bound

    #per impostare il lower bound dell'arco
    def set_lower_bound(self, lower_bound):
        self.lower_bound = lower_bound

    #per ottenere il lower bound dell'arco
    def get_lower_bound(self):
        return self.lower_bound

class ShortageEdge:

    def __init__(self, id, cost, upper_bound, lower_bound):
        self.id = "ShortageEdge" + "_" + str(id)
        self.type = "shortage_edge"
        self.cost = cost
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

    #per ottenere l'identificativo del'arco
    def get_id(self):
        return self.id

    #per impostare l'id del'arco
    def set_id(self, value):
        self.id = value

    #per ottenere il tipo dell'arco
    def get_type(self):
        return self.type
    
    #per impostare il tipo dell'arco
    def set_type(self, type):
        self.type = type

    #per impostare il costo dell'arco
    def set_cost(self, cost):
        self.cost = cost
    
    #per ottenere il costo dell'arco
    def get_cost(self):
        return self.cost

    #per impostare l'upper bound dell'arco
    def set_upper_bound(self, upper_bound):
        self.upper_bound = upper_bound

    #per ottenere l'upper bound dell'arco
    def get_upper_bound(self):
        return self.upper_bound

    #per impostare il lower bound dell'arco
    def set_lower_bound(self, lower_bound):
        self.lower_bound = lower_bound

    #per ottenere il lower bound dell'arco
    def get_lower_bound(self):
        return self.lower_bound

class RetailerCollectionEdge:

    def __init__(self, id, cost, upper_bound, lower_bound):
        self.id = "RetailerCollectionEdge" + "_" + str(id)
        self.type = "retailer_collection_edge"
        self.cost = cost
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

    #per ottenere l'identificativo del'arco
    def get_id(self):
        return self.id

    #per impostare l'id del'arco
    def set_id(self, value):
        self.id = value

    #per ottenere il tipo dell'arco
    def get_type(self):
        return self.type
    
    #per impostare il tipo dell'arco
    def set_type(self, type):
        self.type = type

    #per impostare il costo dell'arco
    def set_cost(self, cost):
        self.cost = cost
    
    #per ottenere il costo dell'arco
    def get_cost(self):
        return self.cost

    #per impostare l'upper bound dell'arco
    def set_upper_bound(self, upper_bound):
        self.upper_bound = upper_bound

    #per ottenere l'upper bound dell'arco
    def get_upper_bound(self):
        return self.upper_bound

    #per impostare il lower bound dell'arco
    def set_lower_bound(self, lower_bound):
        self.lower_bound = lower_bound

    #per ottenere il lower bound dell'arco
    def get_lower_bound(self):
        return self.lower_bound

class SupplierCollectionEdge:

    def __init__(self, cost, upper_bound, lower_bound):
        self.id = "SupplierCollectionEdge"
        self.type = "supplier_collection_edge"
        self.cost = cost
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

    #per ottenere l'identificativo del'arco
    def get_id(self):
        return self.id

    #per impostare l'id del'arco
    def set_id(self, value):
        self.id = value

    #per ottenere il tipo dell'arco
    def get_type(self):
        return self.type
    
    #per impostare il tipo dell'arco
    def set_type(self, type):
        self.type = type

    #per impostare il costo dell'arco
    def set_cost(self, cost):
        self.cost = cost
    
    #per ottenere il costo dell'arco
    def get_cost(self):
        return self.cost

    #per impostare l'upper bound dell'arco
    def set_upper_bound(self, upper_bound):
        self.upper_bound = upper_bound

    #per ottenere l'upper bound dell'arco
    def get_upper_bound(self):
        return self.upper_bound

    #per impostare il lower bound dell'arco
    def set_lower_bound(self, lower_bound):
        self.lower_bound = lower_bound

    #per ottenere il lower bound dell'arco
    def get_lower_bound(self):
        return self.lower_bound


class RetrievalEdge:

    def __init__(self, cost, upper_bound, lower_bound):
        self.id = "RetrievalEdge"
        self.type = "retrieval_edge"
        self.cost = cost
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

    #per ottenere l'identificativo del'arco
    def get_id(self):
        return self.id

    #per impostare l'id del'arco
    def set_id(self, value):
        self.id = value

    #per ottenere il tipo dell'arco
    def get_type(self):
        return self.type
    
    #per impostare il tipo dell'arco
    def set_type(self, type):
        self.type = type

    #per impostare il costo dell'arco
    def set_cost(self, cost):
        self.cost = cost
    
    #per ottenere il costo dell'arco
    def get_cost(self):
        return self.cost

    #per impostare l'upper bound dell'arco
    def set_upper_bound(self, upper_bound):
        self.upper_bound = upper_bound

    #per ottenere l'upper bound dell'arco
    def get_upper_bound(self):
        return self.upper_bound

    #per impostare il lower bound dell'arco
    def set_lower_bound(self, lower_bound):
        self.lower_bound = lower_bound

    #per ottenere il lower bound dell'arco
    def get_lower_bound(self):
        return self.lower_bound
    

    