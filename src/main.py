from Graph import Graph
from Edges import *
from json import dumps
from Data import *
from Nodes import *
import sys

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
edgeTypes = ["supply_edge", "dispatch_edge", "holding_edge", "cycle_edge", "shortage_edge", "retailer_collection_edge", "supplier_collection_edge", "retrieval_edge"]
nodeTypes = ["dummy_supply_node", "collection_node", "supplier_node", "retailer_node"]

#metodo per stampare le informazioni
def printGraph(graph):
    
    if graph == None:
        print("Non posso stampare i dati del grafo perchè non inizializzato")
        return

    numEdges = 0
    
    for node in graph:
        for neighbor in node.get_neighbors():
            startNodeId = node.get_id()
            endNodeId = neighbor.get_id()
            edgeId = node.get_edge_to_neighbor(neighbor).get_id()
            numEdges = numEdges + 1

            print("(startNode: %s, endNode: %s, edgeId: %s)"  % (startNodeId, endNodeId, edgeId))
    
    print("Number of edges: ", numEdges)

def printRetailerData(graph):
    
    if graph == None:
        print("Non posso stampare i dati dei retailer, grafo non inizializzato")
        return
    
    for node in graph:
        if node.get_type() == "retailer_node":
            nodeId = node.get_id()
            nodeCapacity = node.get_warehouse_usage()
            nodeDemand = node.get_demand()
            print("(id: %s, capacity: %s, demand: %s)"  % (nodeId, nodeCapacity, nodeDemand))

def printSupplierData(graph):

    if graph == None:
        print("Non posso stampare i dati del supplier, grafo non inizializzato")
        return
    
    for node in graph:
        if node.get_type() == "supplier_node":
            nodeId = node.get_id()
            nodeUsage = node.get_warehouse_usage()
            print("(id: %s, warehouse_usage: %s)"  % (nodeId, nodeUsage))


def visualize(graph):

    g = {
    "kind": {"graph": True},
    "nodes": [],
    "edges": []
    }

    #aggiungo tutti gli archi
    for node in graph:
        startNodeId = node.get_id()
        g["nodes"].append({"id": startNodeId, "label": startNodeId, "key" : startNodeId})
        json_graph = dumps(g)
        for neighbor in node.get_neighbors():
            endNodeId = neighbor.get_id()
            g["nodes"].append({"id": endNodeId, "label": endNodeId, "key" : endNodeId})
            json_graph = dumps(g)
            g["edges"].append({"from": startNodeId, "to": endNodeId})
            json_graph = dumps(g)

    #impostare il breakpoint alla riga di seguito ed eseguire in modalità debug per  
    #visualizzare la struttura del grafo con Debug Visualizer
    print("Insert here a breakpoint to visualize all the graph")        

#metodo per inizializzare il grafo, richiede in inputi il numero di nodi retailer
def initialize(retailerNumber):
    
    if retailerNumber > 50 or retailerNumber < 0:
        print("Inserire un numero di nodi retailer compreso tra 1 e 50")
        return None

    #imposto la disponibilità totale del supplier
    totalAvailability = 447
    
    g = Graph()
    g.add_dummy_supply_node(totalAvailability)
    g.add_collection_node(0)  #da calcolare?


    #aggiungo tutti i nodi supplier
    for i in range (1,8):
            day = days[i-1]
            if day == "MON":
                g.add_supplier_node(day, totalAvailability)
            else:
                sum = 0
                for j in range(1, retailerNumber+1):
                    for k in range(1, i):
                        sum = sum + demand_matrix[k-1][j-1]
                usage = totalAvailability - sum
                g.add_supplier_node(day, usage)

                
    #aggiungo tutti i nodi retailer
    for i in range(1, retailerNumber + 1):
        for j in range (1, 8):
            day = days[j-1]
            if day == "MON":
                g.add_retailer_node(i, day, 0, demand_matrix[j-1][i-1])
            else:
                g.add_retailer_node(i, day, 0, demand_matrix[j-1][i-1])

    #aggiungo gli archi tra i nodi del supplier
    for i in range (1, 7):
        startNodeId = "SupplierNode_" + days[i-1]
        endNodeId = "SupplierNode_" + days[i]
        edgeId = startNodeId + "_to_" + endNodeId
        hEdge = HoldingEdge(edgeId, 0, 150, 0, 0)
        g.add_edge(startNodeId, endNodeId, hEdge)

    #aggiungo gli archi tra i nodi dello stesso retailer
    for i in range(1, retailerNumber + 1):
        for j in range(1, 7):
            startNodeId = "RetailerNode_" + str(i) + "_" + days[j-1]
            endNodeId = "RetailerNode_" + str(i) + "_" + days[j]
            edgeId = startNodeId + "_to_" + endNodeId
            hEdge = HoldingEdge(edgeId, 0, 150, 0, 0)
            g.add_edge(startNodeId, endNodeId, hEdge)

    #aggiungo gli archi giornalieri tra il supplier e tutti i retailer 
    for i in range(1, 8):
        for j in range(1, retailerNumber + 1):
            startNodeId = "SupplierNode_" + days[i-1]
            endNodeId = "RetailerNode_" + str(j) + "_" + days[i-1]
            edgeId = startNodeId + "_to_" + endNodeId
            dEdge = DispatchEdge(edgeId, 0, 150, 0, 0)
            g.add_edge(startNodeId, endNodeId, dEdge)

    #aggiungo gli archi di ritorno
    endNodeId = "SupplierNode_SUN"
    for i in range(1, retailerNumber + 1):
        startNodeId = "RetailerNode_" + str(i) + "_" + "SUN"
        edgeId = startNodeId + "_to_" + endNodeId
        rEdge = RetailerCollectionEdge(edgeId, 0, 150, 0)
        g.add_edge(startNodeId, endNodeId, rEdge)


    #chiedere quanto deve essere la domanda sul supplyeEdge 
    sEdge = SupplyEdge(100000, 150, 0)

    #chiedere cosa va inserito nel SupplierCollectionEdge
    sCEdge = SupplierCollectionEdge(0, 150, 0)
    
    rEdge = RetrievalEdge(1000, 150, 0)

    g.add_edge("SupplierNode_SUN", "CollectionNode", sCEdge)
    g.add_edge("CollectionNode", "DummySupplyNode", rEdge)
    g.add_edge("DummySupplyNode", "SupplierNode_MON", sEdge)
    
    #manca di aggiungere tutti gli archi

    return g


if __name__ == '__main__':

    #inizializzo il grafo
    graph = initialize(2)
    #printSupplierData(graph)

    #stampo il grafo creato
    #printGraph(graph)

    #invoco la funzione per la visualizzazione grafica del grafo con Debug Visualizer
    #visualize(graph)

    #stampo i dati dei nodi retailer
    #printRetailerData(graph)

    #stampo i dati di tutti i nodi supplier
    printSupplierData(graph)

    #provo a cercare un arco specifico
    '''edge = graph.get_edge("RetailerNode_1_MON", "RetailerNode_1_TUE")
    if edge != None:
        print(edge.get_id())
        print(edge.get_type())
        print(edge.get_quantity_holded())
    else:
        print("Arco non trovato")
    '''


