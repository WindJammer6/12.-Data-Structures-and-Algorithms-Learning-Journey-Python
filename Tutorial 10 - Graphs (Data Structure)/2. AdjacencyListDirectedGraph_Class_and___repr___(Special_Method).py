#In this tutorial we will be implementing Adjacency List Directed Graph Data Structure

#So how can we represent a Graph Data Structure? As we have learnt in '1. What_is_a_Graph.txt', there are 2 ways
#represent/implement a Graph Data Structure, either as an Adjacency Matrix or an Adjacency List. In this tutorial
#we will be implementing our Directed Graph Data Structure using an Adjacency List. An Adjacency List represents
#a Directed Graph Data Structure as something like this, which we will be able to work with to behave as a 
#Directed Graph Data Structure,

    #Adjacency List Directed Graph Data Structure:
    #{A : [B, C],
    # B : [E],
    # C : [D],
    # D : [B, E],
    # E : []}

    #Visualisation of the Adjacency List Directed Graph Data Structure above:
    #[A]----->[B]------>[E]
    # |        ^         ^ 
    # |        |         |
    #\ /       |         |
    #[C]----->[D]--------- 

#The Adjacency List is essentially a Dictionary (storing key-value pairs) with keys representing the individual
#node entities themselves present in the Directed Graph Data Structure, and the values storing a List of adjacent
#nodes of the individual node entity (key) itself that has an edge being pointed at them from the individual node
#entity (key)(there is a direction for the edges since this is a Directed Graph)


#////////////////////////////////////////////////////


#Implementation of code for the 'AdjacencyListDirectedGraph' class:

#To implement an Adjacency List Graph Data Structure (any kind), you can imagine it as being made up of just many
#pairs of 2 nodes,

#Visualisation of a Directed Graph Data Structure:
#[A]----->[B]------>[E]
# |        ^         ^ 
# |        |         |
#\ /       |         |
#[C]----->[D]--------- 

#where the nodes "A" and "B" are a pair, nodes "A" and "C" are a pair, nodes "B" and "D" as a pair and so on.
#Hence, in code implementation of an Adjacency List, using the 'AdjacencyListDirectedGraph' class, we can pass 
#through the pairs as a Tuple, and then compile all these pairs/Tuples in a List, and passing the full List of 
#Tuples through the 'AdjacencyListDirectedGraph' class to create the Adjacency List Directed Graph Data Structure 
#Dictionary. So to do this, we will need to define our 'AdjacencyListDirectedGraph' class by defining its 
#attributes.


#The 'AdjacencyListDirectedGraph' class has 2 attributes:
#'edges', which represents the List of Tuples of 2 elements, representing 2 nodes, the first node being where 
#the edge is being pointed from (start node), and the second node being where the edge is being pointed at. 
#(end node) This List of Tuples will be passed through the 'AdjacencyListDirectedGraph' object from the main code
#to create our Adjacency List Directed Graph Data Structure. For example,

    #list_of_tuples = [("A", "B"),
    #                  ("B", "C")]

    #Visualisation of the first tuple in a Directed Graph Data Structure:
    #Start node     End node
    #   [A]----------->[B]

    #Visualisation of the second tuple in a Directed Graph Data Structure:
    #Start node     End node
    #   [B]----------->[C]

    #Visualisation of the Directed Graph Data Structure after the 'list_of_tuples' is passed through the 
    #'AdjacencyListDirectedGraph' class:
    #   [A]----------->[B]----------->[C]

#'graph_dictionary', which represents the Adjacency List Directed Graph Data Structure itself (since Adjacency
#List Graph Data Structure (any kind) is essentially just a dictionary)


class AdjacencyListDirectedGraph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dictionary = {}

        #Here's the code to sort of 'unpack' the List of Tuples provided in the main code to create the Adjacency 
        #List Directed Graph Data Structure (see above), and store it in the 'self.graph_dictionary' attribute of 
        #our 'AdjacencyListDirectedGraph' object, using the 'edges' attribute to take in the List of Tuples 
        #provided in the main code into our 'AdjacencyListDirectedGraph' object. 

        #The 'edges' attribute represents the List of Tuples provided in our main code, since each Tuple will
        #only contain 2 elements, the start node, represented by the 'start' variable (node where the edge is 
        #pointing from) and end node, represented by the 'end' variable (node where the edge is pointing at)), we
        #can reference to the start node and end node of each Tuple in the List like so, and using a for loop.
        for start, end in self.edges:

            #If the start node, 'start' of the particular Tuple we are looking at in the for loop already exist
            #as a key in the 'self.graph_dictionary' attribute Dictionary, then we will append the end node 'end'
            #of that Tuple into the value List (which will be a List for all the values in the key-value pairs in 
            #the 'self.graph_dictionary' Dictionary) List.
            if start in self.graph_dictionary:
                self.graph_dictionary[start].append(end)

            #Otherwise, if the start node, 'start' of the particular Tuple we are looking at in the for loop 
            #dosen't yet exists as a key in the 'self.graph_dictionary' attribute Dictionary, then we will create
            #a new key-value pair in the 'self.graph_dictionary' attribute Dictionary, with the start node, 'start'
            #of the Tuple as the key and assign a List as the value while immediately appending the end node 'end' 
            #of the Tuple to the value List
            else:
                self.graph_dictionary[start] = [end]
        

        #Taking reference from the data provided in the List of Tuples in the main code, as of now the 
        #'self.graph_dictionary' attribute Dictionary looks like this:
        
            #{'Mumbai': ['Paris', 'Dubai'], 
            # 'Paris': ['Dubai', 'New York'], 
            # 'Dubai': ['New York'], 
            # 'New York': ['Toronto']}

        #However, later in the Instance Method 'add_edge()' 
        #(see '3. add_node_(Instance_Method)_and_add_edge_(Instance_Method).py'), for it to work, it needs every 
        #individual node entity present in the Adjacency List Directed Graph Data Structure to exist in the 
        #'self.graph_dictionary' attribute Dictionary as a key, regardless if it has any elements in its value List
        #or not (empty List)(indicating existance of edges pointing in the direction from the node (key) to other 
        #adjacency nodes). It should look something like this,

            #{'Mumbai': ['Paris', 'Dubai'], 
            # 'Paris': ['Dubai', 'New York'], 
            # 'Dubai': ['New York'], 
            # 'New York': ['Toronto']
            # 'Toronto': []}
        
        #Currently the node storing the city 'Toronto' does exist in the 'self.graph_dictionary' attribute Dictionary,
        #but not as key in a key-value pair, but rather as one of the elements in the value List of other key-value 
        #pairs ('New York': ['Toronto'])

        #Hence, in order to create the key-value pair for cases such as 'Toronto', where it has an empty value List
        #in its key-value pair, we need to run another for loop through the List of Tuples to check for these cases
        for start, end in self.edges:

            #If there is a node without an edge pointing in the direction from it to anywhere like "Toronto", create
            #a key-value pair for it still, but with its value just being an empty list
            if end not in self.graph_dictionary:
                self.graph_dictionary[end] = []


    #So I can use the 'print()' function on my 'AdjacencyListDirectedGraph' class to look at my 
    #'AdjacencyListDirectedGraph' object
    def __repr__(self):
        return '{}'.format(self.graph_dictionary)


if __name__ == '__main__':
    #This is the List of Tuples that we will be passing through the 'AdjacencyListDirectedGraph' 
    #class to create our Adjacency List Directed Graph Data Structure
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
