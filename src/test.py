from Nodes import *
from Edges import *
from Main import *
from Graph import *

def testEdgesIds():    
    supplyEdge = SupplyEdge(10, 150, 0)
    dispatchEdge = DispatchEdge(1, 10, 150, 0, 10)
    holdingEdge = HoldingEdge(1, 10, 150, 0, 20)
    cycleEdge = CycleEdge(1, 10, 150, 0)
    shortageEdge = ShortageEdge(1, 10, 150, 0)
    retCollEdge = RetailerCollectionEdge(1, 10, 150, 0)
    suppCollEdge = SupplierCollectionEdge(10, 150, 0)
    retrievalEdge = RetrievalEdge(10, 150, 0)

    print(supplyEdge.get_id())
    print(dispatchEdge.get_id())
    print(holdingEdge.get_id())
    print(cycleEdge.get_id())
    print(shortageEdge.get_id())
    print(retCollEdge.get_id())
    print(suppCollEdge.get_id())
    print(retrievalEdge.get_id())

def testNodesIds():
    dummSupNode = DummySupplyNode(100)
    collNode = CollectionNode(1000)
    supNode = SupplierNode("MON", 50)
    retNode = RetailerNode(1, "MON", 50, 25)

    print(dummSupNode.get_id())
    print(collNode.get_id())
    print(supNode.get_id())
    print(retNode.get_id())

if __name__ == '__main__':
    #testEdgesIds()
    #testNodesIds()
    dispatchEdge = DispatchEdge(1, 10, 150, 0, 10)
    print(dispatchEdge.get_quantity_trasported())
    dispatchEdge.set_quantity_trasported(20)
    print(dispatchEdge.get_quantity_trasported())

    g = Graph()
    g.add_supplier_node("MON", 0)
    #id, cost, upper_bound, lower_bound, quantity_holded
    holdingEdge = HoldingEdge(1, 10, 150, 0, 30)
    g.add_supplier_node("THU", holdingEdge.get_quantity_holded())
    n = g.get_node("SupplierNode_THU")
    print(n.get_warehouse_usage())

    

