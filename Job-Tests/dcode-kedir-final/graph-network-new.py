import sys

# Constraits include:
#   Vertex can have no more than 100 edges 
#   Each vertex can hold a payload no larger than 100 bytes
#   Each edge can hold a weight of up to 1000
#   Must find the shortest path between two vertices in the graph network (Specifically using breadth-first search)

#This will be holding all of the data that gets generated as a nested dictionary (easily converted to a json or dataframe to be passed into programs that utilize the data to build a visual representation of graph network)
data = {}

# Function: Add Vertex (node) to graph network
def add_vertex(vertex = str, payload = any):
    payload_size = int(sys.getsizeof(payload))
    if payload_size <= 100:
        data_structure = {
            'payload': payload,
            'edges': {
                'edge_vertex': [],
                'weight': []
                }
            }
        data[vertex] = data_structure
        print("Node " + vertex + " Creation Successfull - Payload is " + str(payload_size) + " bytes, under the maximum threshold of 100 bytes.")
    else:
        print("Node " + vertex + " Creation Failed - Payload is " + str(payload_size) + " bytes, greater than the 100 bytes threshold")

# Function: Add an Edge (or link) between vertices to graph network
def add_edge(origin_vertex = str, ending_vertex = str, weight = int):
    #Dont need conditional if elif line cause if vertex doesnt exist, it will throw an error immediately

    initial_origin_edge_vertexes = data[origin_vertex]['edges']['edge_vertex']
    initial_ending_edge_vertexes = data[ending_vertex]['edges']['edge_vertex']

    if len(initial_origin_edge_vertexes) < 100 and weight <= 1000:
        #Adding edge to the origin vertex after counting the number to ensure less than 100
        data[origin_vertex]['edges']['edge_vertex'].append(ending_vertex)
        data[origin_vertex]['edges']['weight'].append(weight)
        print("Number of edges below maximumum, edge and weight between Vertex '" + origin_vertex + "' and Vertex '" + ending_vertex + "'  created successfully")
    elif len(initial_origin_edge_vertexes) >= 100 or weight > 1000:
        print("Number of edges exceeds maximum capacity of 100, edge creation between Vertex '" + origin_vertex + "' and Vertex '" + ending_vertex + "' failed")
    else:
        print("Error in fuction, review inputs/code")

    #Adding inverse edge to ending vertex

    if len(initial_ending_edge_vertexes) < 100 and weight <= 1000:
        data[ending_vertex]['edges']['edge_vertex'].append(origin_vertex)
        data[ending_vertex]['edges']['weight'].append(weight)
        print("Number of edges below maximumum, edge and weight between Vertex '" + origin_vertex + "' and Vertex '" + ending_vertex + "'  created successfully")
    elif len(initial_ending_edge_vertexes) >= 100 or weight > 1000:
        print("Number of edges exceeds maximum capacity of 100, edge creation between Vertex '" + origin_vertex + "' and Vertex '" + ending_vertex + "' failed")
    else:
        print("Error in fuction, review inputs/code")

# Function: Remove Vertex (node) to graph network
def remove_vertex(vertex = str):
    edge_list = data[vertex]['edges']['edge_vertex']
    for i in edge_list:
        index_of_edge = data[i]['edges']['edge_vertex'].index(vertex)
        data[i]['edges']['edge_vertex'].remove(vertex)
        data[i]['edges']['weight'].pop(index_of_edge)
        print("Vertex and weight removal from " + i + " edges complete")
    print("Edge list removals complete")
    data.pop(vertex)
    print("Vertex '" + vertex + "' and all relevent data removal complete")

# Function: Remove an Edge (or link) between vertices to graph network
def remove_edge(origin_vertex = str, ending_vertex = str):
    #This finds where each value is, so we know which weight to splice out as well, ending edge index finds where the ending edge is in the origin edge vertex list
    ending_edge_index = data[origin_vertex]['edges']['edge_vertex'].index(ending_vertex)
    origin_edge_index = data[ending_vertex]['edges']['edge_vertex'].index(origin_vertex)
    data[origin_vertex]['edges']['edge_vertex'].remove(ending_vertex)
    data[ending_vertex]['edges']['edge_vertex'].remove(origin_vertex)
    data[origin_vertex]['edges']['weight'].pop(ending_edge_index)
    data[ending_vertex]['edges']['weight'].pop(origin_edge_index)
    print("Edge from Vertex '" + origin_vertex + "' to Vertex '" + ending_vertex + "' removal successful")


#Function: Find the shortest path between two vertices in the graph network (Specifically using breadth-first search)
#BFS Shortest Path Function will take the dataset (preferably dictionary with key-value pairs of nodes and edges, generated above by the for x function)
def shortest_path(data, startpoint = str, endpoint = str):
    #A list to manage paths that have already been checked
    explored = []
    #A queue to manage paths left to check
    queue = [[startpoint]]
    #This is a fail safe if someone selects a startpoint that is the same as the endpoint
    if startpoint == endpoint:
        return "The shortest path start point is the same as the endpoint"
    #While loop will continue until all of the items in the queue have been checked
    while queue:
        #Removes the first node from the queue as it is the startpoint, needed something in it to start the while loop
        path = queue.pop(0)
        #This will check the last index in the path
        node = path[-1]
        if node not in explored:
            adjacent_nodes = data[node]
            #For each vertex, it will filter through each vetrtex's edges, generating a new path and and adding this path to the queue
            for i in adjacent_nodes:
                shortest_path = list(path)
                shortest_path.append(i)
                queue.append(shortest_path)
                #Once we have acheived the path (i = endpoint), it stops the function there (regardless if there are other paths because this one will automatically be the shortest), indicating that it has found the shortest path, and then return the path
                if i == endpoint:
                    print("From Vertex '" + str(startpoint) + "' to Vertex '" + endpoint + "',the shortest path using unweighted Breadth-First Search is " + str(shortest_path))
                    return shortest_path
            #This will add eached explored path to the explored node
            explored.append(node)
    #A print function if the path does not exist
    return print("There is no existing path from Vertex '" + startpoint + "' and Vertex '" + endpoint + "'")
 

#Creating/Removing all the nodes and edges
add_vertex('A', 45)
add_vertex('B', 55)
add_vertex('C', 65)
add_vertex('D', 75)
add_vertex('E', 85)
add_vertex('F', 95)
add_vertex('G', 5)
add_vertex('H', 10)
add_vertex('I', 15)
add_edge('A','B',15)
add_edge('A','C',10)
add_edge('B','C',10)
add_edge('C','D', 20)
add_edge('D','E', 10)
add_edge('F','C', 10)
add_edge('F','E', 10)
add_edge('F','B', 10)
add_edge('G','E', 10)
add_edge('G','C', 10)
add_edge('H','A', 10)
remove_vertex('I')
remove_edge('H', 'A')

#Pulling the key values from the nested dictionary storing all values and creating separate lists for the edge data -- to be passed throught the shortest path function
#THIS HAS HAS TO BE AFTER THE ALL OF THE NODE AND EDGE CREATIONS AND ANY REMOVALS MUST BE BEFORE THIS POINT
new_data_list = list(data.keys())
edge_data = dict.fromkeys(new_data_list, {})

for x in edge_data:
    edge_data[x]=data[x]['edges']['edge_vertex']

shortest_path(edge_data, 'A', 'F')