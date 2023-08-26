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

    def delete_node(self, node):
        if node not in self.graph_dictionary:
            print(node, "is not present in the Graph Data Structure")

        else:
            self.graph_dictionary.pop(node)

            for i in self.graph_dictionary:
                value_list = self.graph_dictionary[i]
                if node in value_list:
                    value_list.remove(node)

    def delete_edge(self, startnode, endnode):
        if startnode not in self.graph_dictionary:
            print(startnode, "is not present in the Graph Data Structure")
        elif endnode not in self.graph_dictionary:
            print(endnode, "is not present in the Graph Data Structure")

        else:
            if endnode in self.graph_dictionary[startnode]:
                self.graph_dictionary[startnode].remove(endnode)
            else:
                print("No such edge exists that is pointing in the direction from", startnode, "to", endnode)

    def breadth_first_search(self, rootnode):
        queue_list = []
        visited = []

        queue_list.append(rootnode)
 
        while queue_list:
            dequeued_node = queue_list.pop(0)
            visited.append(dequeued_node)
 
            if dequeued_node in self.graph_dictionary:
                for i in self.graph_dictionary[dequeued_node]:
                    if i not in visited and i not in queue_list:
                        queue_list.append(i)

        return visited

    #What this Instance Method does is that it does Depth-First Search (DFS) traversal operation on the Adjacency
    #List Directed Graph Data Structure.

    #For more technical explanation of how DFS is done on Adjacency List Graph Data Structures, refer to the section
    #'Explaining how Scanning/Traversal operation works in Graph' in '1. What_is_a_Graph.txt'.

    #These are the steps of DFS for Graph Data Structures:
    # 1. You can start from any node (only for Undirected Graphs, for Directed Graphs, you must start from the root
    #    node) in the Graph Data Structure. So, we will start by pushing any one of the Graph's nodes on top of the 
    #    Stack.
    # 2. Now take the top item of the Stack and add it to the 'Visited' List.
    # 3. Create a List of that node's adjacent nodes. Append all the ones which aren't in the 'Visited' List and 
    #    Stack to the top of the Stack. The adjacent nodes can be pushed in any order to the top of the Stack. We 
    #    will ignore the adjacent nodes that has already been visited before since they should already either be in 
    #    the 'Visited' List or is currently in the Stack already.
    # 4. Keep repeating steps 2 and 3 until the stack is empty.
    
    #The 'rootnode' parameter represents the root node (since we are implementing a Directed Graph Data Structure
    #instead of an Undirected Graph Data Structure)
    def depth_first_search(self, node):
 
        #This is the Stack Data Structure for the DFS operation (we will be using Python's List to represent a Stack
        #Data Structure)
        stack_list = []
        #This is the 'Visited' List, which we will return at the end of the Instance Method
        visited = []
 
        #Push the 'rootnode' into the top of the Stack
        stack_list.insert(0, node)
 

        #We are using a while loop so that the DFS operation will only stop when the Stack is empty, which is indeed when
        #we want the DFS operation to stop
        while stack_list:
            #Pop a node from the top of the Stack and append it to the 'Visited' List
            popped_node = stack_list.pop(0)
            visited.append(popped_node)

            #Get all adjacent nodes of the poppeed node 'popped_node'. For all adjacent nodes, push all the adjacent 
            #nodes that has not been visited before (in 'Visited' List) and not already in Stack, into the top of the
            #Stack
            if popped_node in self.graph_dictionary:
                for i in self.graph_dictionary[popped_node]:
                    if i not in visited and i not in stack_list:
                        stack_list.insert(0, i)

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

    print("Following is the Depth-First Search")
    print(routes_graph.depth_first_search('Mumbai'))