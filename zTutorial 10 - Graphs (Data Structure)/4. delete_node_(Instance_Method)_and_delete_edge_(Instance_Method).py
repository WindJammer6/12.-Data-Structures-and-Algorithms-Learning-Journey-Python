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

    def add_node(self, node):
        if node in self.graph_dictionary:
            print(node, "is already present in the Graph Data Structure")

        else:
            self.graph_dictionary[node] = []

    def add_edge(self, startnode, endnode):
        if startnode not in self.graph_dictionary:
            print(startnode, "is not present in the Graph Data Structure")
        elif endnode not in self.graph_dictionary:
            print(endnode, "is not present in the Graph Data Structure")

        else:
            self.graph_dictionary[startnode].append(endnode)

    #What this Instance Method does is that it deletes a node from the Adjacency List Directed Graph Data Structure. 
    #As mentioned from the section 'Explaining how Deletion operation works in Adjacency List Graph' in 
    #'1. What_is_a_Graph.txt', there is 2 steps during deletion of a node from a Graph, 

    #a. Deletion of the node itself
    #b. Deletion of the edges connecting to the node to be deleted

    #In the first step, in order to delete the node itself, we simply have to delete the key-value pair of the node 
    #we want to delete (which will be the key of this key-value pair) in the 'self.graph_dictionary' of our 
    #'AdjacencyListDirectedGraph' object.

    #(Just for Adjacency List Directed Graphs) In the second step, since the first step only deletes the node itself
    #and any edges pointing in the direction from it to other adjacent nodes. To delete all the edges connecting to
    #the node to be deleted (regardless of direction the edges are pointing to, we will delete them as long as they 
    #are connected to the node to be deleted), we need to check if the value Lists of other key-value pairs in the 
    #'self.graph_dictionary' of our 'AdjacencyListDirectedGraph' object still conatins the node to be deleted and
    #removethe node to be deleted from the value Lists of other key-value pairs. 

    #After these 2 steps, the node to be deleted should no longer exist in the 'self.graph_dictionary' of our 
    #'AdjacencyListDirectedGraph' object, both in the keys and value Lists, effectively deleting the node to be 
    #deleted.
    def delete_node(self, node):

        #Before we make any changes to the 'self.graph_dictionary' of the 'AdjacencyListDirectedGraph' object when
        #we delete the node to be deleted, we need to first check if the node to be deleted exists in the first place. 
        if node not in self.graph_dictionary:
            print(node, "is not present in the Graph Data Structure")

        #Once we have checked that the node to be deleted exists, we can carry on to modify the 'self.graph_dictionary'
        #of the 'AdjacencyListDirectedGraph' object.
        else:
            #For the first step, to delete the node itself, we just have to remove the whole key-value pair with the
            #node to be deleted as the key in the 'self.graph_dictionary' of the 'AdjacencyListDirectedGraph' object.
            #(Apparently Python's 'pop()' function works on Dictionaries too, which removes the whole key-value pair
            #in the Dictionary, taking the key of the key-value pair to be removed as the parameter)
            self.graph_dictionary.pop(node)
            
            #For the second step, to delete the remaining edges connecting to the node to be deleted, we will need 
            #to search the value Lists of the remaining key-value pairs if they contain the node to be deleted in
            #them and removing it from the value Lists
            for i in self.graph_dictionary:
                value_list = self.graph_dictionary[i]
                if node in value_list:
                    value_list.remove(node)


    #What this Instance Method does is that it deletes an edge from the Adjacency List Directed Graph Data Structure.

    #It takes in 2 parameters/arguments, 'startnode' and 'endnode', with the 'startnode' parameter representing 
    #the node where the newly added edge will be pointing in the direction from, and the 'endnode' parameter
    #representing the node where the newy added edge will be pointing in the direction towards
    def delete_edge(self, startnode, endnode):

        #Before we make any changes to the 'self.graph_dictionary' of the 'AdjacencyListDirectedGraph' object when
        #we delete an edge, we need to first check if the 2 parameter nodes ('startnode' and 'endnode') exists 
        #in the first place. 
        if startnode not in self.graph_dictionary:
            print(startnode, "is not present in the Graph Data Structure")
        elif endnode not in self.graph_dictionary:
            print(endnode, "is not present in the Graph Data Structure")

        #Once we have checked that the 2 parameter nodes ('startnode' and 'endnode') exists, we can carry on to 
        #modify the 'self.graph_dictionary' of the 'AdjacencyListDirectedGraph' object. To delete an edge pointing
        #in the direction from the 'startnode' to 'endnode', we just have to remove the 'endnode' from the value 
        #List of the key-value pair of the 'startnode' (which will be the key of that key-value pair)
        else:
            #The first and second if statements checks the existance of the 2 nodes, but there is one more case 
            #to check, which is if there is an edge poinitng in the particular direction, connecting between the 
            #'startnode' and 'endnode' that we can delete. So, this if statement checks that.
            if endnode in self.graph_dictionary[startnode]:
                self.graph_dictionary[startnode].remove(endnode)
            else:
                print("No such edge exists that is pointing in the direction from", startnode, "to", endnode)

    def __repr__(self):
        return '{}'.format(self.graph_dictionary)
    

if __name__ == '__main__':
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

    routes_graph.delete_node("Singapore")
    print(routes_graph)

    routes_graph.delete_edge("Mumbai", "Dubai")
    print(routes_graph)
