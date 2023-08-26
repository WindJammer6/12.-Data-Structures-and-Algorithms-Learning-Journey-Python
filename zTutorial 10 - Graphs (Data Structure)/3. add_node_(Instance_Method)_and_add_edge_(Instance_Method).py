class AdjacencyListDirectedGraph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dictionary = {}

        for start, end in self.edges:
            if start in self.graph_dictionary:
                self.graph_dictionary[start].append(end)
            else:
                self.graph_dictionary[start] = [end]
            
        for start, end in self.edges:
            if end not in self.graph_dictionary:
                self.graph_dictionary[end] = []

    #What this Instance Method does is that it adds a node to the Adjacency List Directed Graph Data Structure. 
    #This newly added node will be disconnected from the rest of the Adjacency List Directed Graph Data Structure, 
    #without any edges pointing in the direction to it or from it.

    #This Instance Method does this by adding a new key-value pair to the 'self.graph_dictionary' of our 
    #'AdjacencyListDirectedGraph' object, with the data the new node is storing as the key, and an empty List as 
    #the value (indicating there is no edges pointing in the direction to the new node or from it, showing that
    #the new node will be currently disconnected from the rest of Adjacency List Directed Graph Data Structure). 
    def add_node(self, node):

        #Our Adjacency List Directed Graph Data Structure doesn't take duplicates, hence we will need to check 
        #if our Adjacency List Directed Graph Data Structure dosen't already contain another node storing 
        #duplicate data as the data our new node is storing. Ways to get the Adjacency List Directed Graph Data 
        #Structure to handle duplicates is discussed in the section 'A Problem on the Graph Data Structure 
        #implemented in this tutorial' in '1. What_is_a_Graph.txt', but we will not be implementing our Adjacency
        #List Directed Graph Data Structure to handle duplicates in this tutorial
        if node in self.graph_dictionary:
            print(node, "is already present in the Graph Data Structure")

        #When adding the new disconnected node as a new key-value pair in our 'self.graph_dictionary' in the
        #'AdjacencyListDirectedGraph' object, while its key will be the data the new node is storing, we will 
        #set its value as an empty List to show its 'disconnectedness'
        else:
            self.graph_dictionary[node] = []

    #What this Instance Method does is that it adds an edge to the Adjacency List Directed Graph Data Structure.

    #It takes in 2 parameters/arguments, 'startnode' and 'endnode', with the 'startnode' parameter representing 
    #the node where the newly added edge will be pointing in the direction from, and the 'endnode' parameter
    #representing the node where the newly added edge will be pointing in the direction towards
    def add_edge(self, startnode, endnode):

        #Before we make any changes to the 'self.graph_dictionary' of the 'AdjacencyListDirectedGraph' object when
        #we add our new edge, we need to first check if the 2 parameter nodes ('startnode' and 'endnode') exists 
        #in the first place. 
        if startnode not in self.graph_dictionary:
            print(startnode, "is not present in the Graph Data Structure")
        elif endnode not in self.graph_dictionary:
            print(endnode, "is not present in the Graph Data Structure")

        #Once we have checked that the 2 parameter nodes ('startnode' and 'endnode') exists, we can carry on to 
        #modify the 'self.graph_dictionary' of the 'AdjacencyListDirectedGraph' object. To add a new edge pointing
        #in the direction from the 'startnode' to 'endnode', we just have to append the 'endnode' to the value List
        #of the key-value pair of the 'startnode' (which will be the key of that key-value pair)
        else:
            self.graph_dictionary[startnode].append(endnode)

    def __repr__(self):
        return '{}'.format(self.graph_dictionary)


if __name__ == '__main__':
    #Hence, after creating the 'add_node' and 'add_edge' Instance Methods, we can see that there is 2 ways to create
    #our Adjacency List Directed Graph Data Structure. 
     
    #1. The first way is by creating a List of Tuples in the main code and then passing it through our 
    #'AdjacencyListDirectedGraph' class. 

    #2. The second way is by using the 'add_node' and 'add_edge' Instance Methods to manually add individual nodes 
    #and edges to our Adjacency List Directed Graph Data Structure.
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    routes_graph = AdjacencyListDirectedGraph(routes)
    print(routes_graph)

    routes_graph.add_node("Singapore")
    print(routes_graph)

    routes_graph.add_edge("Singapore", "Toronto")
    print(routes_graph)
