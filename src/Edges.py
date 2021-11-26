class SupplyEdge:

    def __init__(self, id, type):
        self.id = id
        self.type = type

    #per ottenere l'identificativo del'arco
    def get_id(self):
        return self.id

    #per impostare l'id del'arco
    def set_id(self, value):
        self.id = value
    
    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type

class DispatchEdge:

    def __init__(self, id):
        self.id = id

class HoldingEdge:

    def __init__(self, id):
        self.id = id

class CycleEdge:

    def __init__(self, id):
        self.id = id

class ShortageEdge:

    def __init__(self, id):
        self.id = id

class RetailerCollectionEdge:

    def __init__(self, id):
        self.id = id

class SupplierCollectionEdge:

    def __init__(self, id):
        self.id = id


class RetrievalEdge:

    def __init__(self, id):
        self.id = id