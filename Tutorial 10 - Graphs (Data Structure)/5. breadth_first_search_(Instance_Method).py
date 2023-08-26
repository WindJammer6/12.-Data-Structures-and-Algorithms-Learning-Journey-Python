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

    def add_edge(self, startnode, nodenode):
        if startnode not in self.graph_dictionary:
            print(startnode, "is not present in the Graph Data Structure")
        elif nodenode not in self.graph_dictionary:
            print(nodenode, "is not present in the Graph Data Structure")

        else:
            self.graph_dictionary[startnode].append(nodenode)

    def delete_node(self, node):
        if node not in self.graph_dictionary:
            print(node, "is not present in the Graph Data Structure")

        else:
            self.graph_dictionary.pop(node)
            
            for i in self.graph_dictionary:
                value_list = self.graph_dictionary[i]
                if node in value_list:
                    value_list.remove(node)

    def delete_edge(self, startnode, nodenode):
        if startnode not in self.graph_dictionary:
            print(startnode, "is not present in the Graph Data Structure")
        elif nodenode not in self.graph_dictionary:
            print(nodenode, "is not present in the Graph Data Structure")

        else:
            if nodenode in self.graph_dictionary[startnode]:
                self.graph_dictionary[startnode].remove(nodenode)
            else:
                print("No such edge exists that is pointing in the direction from", startnode, "to", nodenode)

    #What this Instance Method does is that it does Breadth-First Search (BFS) traversal operation on the Adjacency
    #List Directed Graph Data Structure.

    #For more technical explanation of how BFS is done on Adjacency List Graph Data Structures, refer to the section
    #'Explaining how Scanning/Traversal operation works in Graph' in '1. What_is_a_Graph.txt'.

    #These are the steps of BFS for Graph Data Structures:
        # 1. You can start from any node (only for Undirected Graphs, for Directed Graphs, you must start from the root
        #    node) in the Graph Data Structure. So, we will start by enqueuing any one of the Graph’s nodes at the rear
        #    of the Queue.
        # 2. Now take the front item of the Queue and append it to the 'Visited' List.
        # 3. Create a List of that node's adjacent nodes. Enqueue all those which are not within the 'Visited' List and 
        #    Queue to the rear of the Queue. The adjacent nodes can be added in any order to the rear of the Queue. We
        #    will ignore the adjacent nodes that has already been visited before since they should already either be 
        #    in the 'Visited' List or is currently in the Queue already.
        # 4. Keep repeating steps 2 and 3 till the Queue is empty.
    
    #The 'rootnode' parameter represents the root node (since we are implementing a Directed Graph Data Structure
    #instead of an Undirected Graph Data Structure)
    def breadth_first_search(self, rootnode):
 
        #This is the Queue Data Structure for the BFS operation (we will be using Python's List to represent a Queue 
        #Data Structure)
        queue_list = []
        #This is the 'Visited' List, which we will return at the end of the Instance Method
        visited = []
 
        #Enqueue the 'rootnode' from rear of the Queue
        queue_list.append(rootnode)
 

        #We are using a while loop so that the BFS operation will only stop when the Queue is empty, which is indeed when
        #we want the BFS operation to stop
        while queue_list:
            #Dequeue a node from Queue and append it to the 'Visited' List
            dequeued_node = queue_list.pop(0)
            visited.append(dequeued_node)

            #Get all adjacent nodes of the dequeued node 'dequeued_node'. For all adjacent nodes, enqueue all the adjacent 
            #nodes that has not been visited before (in 'Visited' List) and not already in Queue, into the Queue
            if dequeued_node in self.graph_dictionary:
                for i in self.graph_dictionary[dequeued_node]:
                    if i not in visited and i not in queue_list:
                        queue_list.append(i)

        return visited

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

    # routes_graph.delete_edge("Mumbai", "Dubai")
    # print(routes_graph)
    
    print("Following is the Breadth-First Search")
    print(routes_graph.breadth_first_search('Mumbai'))