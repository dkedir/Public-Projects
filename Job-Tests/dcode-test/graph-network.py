import pandas as pd
import numpy as np
import networkx as nx
import matplotlib
import json
import os
import sys



# Constraits include:
#   Vertex can have no more than 100 edges 
#   Each vertex can hold a payload no larger than 100 bytes
#   Each edge can hold a weight of up to 1000
#   Must find the shortest path between two vertices in the graph network (Specifically using breadth-first search)

# Necessary variables, empty lists/graphs, and generic functions
G = nx.Graph()
Edge_qty_pass_fail = []


# Function: Add/Remove Vertex (node(s)/vertices) to graph network
#Since byte is = 1 number
def add_vertex(Node_A, Payload, Endpoint_Edge_Node=None, Edge_Weight=None):
    if len(os.path.getsize(Payload)) >= 1000:
        G.add_node(Node_A)
        G.set_node_attributes(Node_A, Payload, "Payload")
        print("Vertex creation successful")
        if len(G.edges(Node_A)) <= 100 and len(G.edgs(Endpoint_Edge_Node)) <= 100 and weight <= 1000:
            G.add_edge(Node, Endpoint_Edge_Node, weight=Edge_Weight)
            print("Initial edge creations successful")
        else:
            print("Edge creation failed, Node(s) have more than 100 edges or weight is greater than 1000")
    else:
        print("Node Creation Failed - Payload greater than 1000 bytes")


def remove_vertex(Node):
    G.remove_node(Node)
    Print("Node " + Node + " removed successfully")

def remove_vertexes(Node_List):
    G.remove_nodes_from(Nodes_List)
    Print("Node " + Node_list + " removed successfully")

# Function: Add/Remove an Edge(s) (or link(s)) between vertices to graph network

def add_edge(Node_A, Node_B, weight):
    if len(G.edges(Node_A)) <= 100 and len(G.edgs(Node_B)) <= 100 and weight <= 1000:
        G.add_edge(Node_A, Node_B, weight=weight)
    else:
        print("Edge creation failed, Node(s) have more than 100 edges or weight is greater than 1000")

def remove_edge(Node_A, Node_B):
    try:
        G.remove_node(Node_A, Node_B)
        Print("Edge between " + Node_A + Node_B + " removed successfully")
    except Exception as e:
        print(e)
        print("Error raised when deleting edge, likely that this edge does not exist.")

#Special formatting required to pass this function successfully [(Node_A,Node_B), (Node_C,Node_D), (Node_E,Node_F)]
def remove_edges(Edge_List):
    try:
        G.remove_nodes_from(Edge_List)
        Print("Node list of " + Node_list + " removed successfully")
    except Exception as e:
        print(e)
        print("Error raised when deleting edge, likely that this edge does not exist.")

#Function: Find the shortest path between two vertices in the graph network (Specifically using breadth-first search)

#def shortest_path(Node_A, Node_B):


# Input (supposed to be a list of operations (i.e. add vertex, add edge, remove vertex, remove edge, or find shortest path):

Edges = ("A", 1)
Weight = (5,6)

#add_vertex()
#remove_vertex()
#remove_vertexes()
#add_edge()
#remove_edge()
#remove_edges()





# def add_links(Nodes_Link, weight):
#     list_of_nodes_passed = []
#     list_of_nodes_passed_weights = []
#     list_of_nodes_failed = []
#     for i in Nodes_Link, weight:
#         if len(G.edges(Nodes_Link)) <= 100:
#             list_of_nodes_passed.append(Nodes_Link)
#             list_of_nodes_passed_weights.append(weight)
#             print("Add link/edge successgful, edges printed below.")
#             print(G.edges(Nodes_Link))
#         elif len(G.edges(Nodes_Link)) > 100:
#             list_of_nodes_failed.append(Nodes_Link[i])
#             print("Add link/edge function failed: Number of edges for Node" + x + "has exceeded limit of 100.")
#             print(G.edges(Nodes_Link))
#         else:
#             print("Error in node edge quantity validation - check code")
#     #G.add_edges_from(list_of_nodes_passed)
#     Nodes_Weight_Pairs = np.array(list_of_nodes_passed, list_of_nodes_passed_weights)
#     print(Nodes_Weight_Pairs)
#     G.from_numpy_array(Nodes_Weight_Pairs)