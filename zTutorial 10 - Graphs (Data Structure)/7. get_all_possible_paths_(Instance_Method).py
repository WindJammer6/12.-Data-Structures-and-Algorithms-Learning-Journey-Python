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
            s = queue_list.pop(0)
            visited.append(s)
            if s in self.graph_dictionary:
                for i in self.graph_dictionary[s]:
                    if i not in visited and i not in queue_list:
                        queue_list.append(i)

        return visited
    
    def depth_first_search(self, rootnode):
 
        stack_list = []
        visited = []
 
        stack_list.insert(0, rootnode)
 
        while stack_list:
            s = stack_list.pop(0)
            visited.append(s)
            if s in self.graph_dictionary:
                for i in self.graph_dictionary[s]:
                    if i not in visited and i not in stack_list:
                        stack_list.insert(0, i)

        return visited

    #What this Instance Method does is that it finds all possible paths between 2 nodes in the Adjacency List 
    #Directed Graph Data Structure.

    #It takes in 3 parameters, 
    #'startnode' representing the starting node from which all the possible paths will originate from

    #'endnode' parameter representing the end node where which all the possible paths will end at
    
    #'path', which is set as an empty List by default, which is used to keep track of the current path being 
    #explored (see the part when this Instance Method is called recursively in the Instance Method) 

    #Since Graph Data Structures are recursive Data Structure, it makes sense for us to use recursion in this
    #Instance Method. 



    #Here is a ChatGPT's attempt to explain all the recursiveness step-by-step, in the Instance Method:

    # -This Instance Method starts by appending the start node to the path.

    # -It then checks if the 'startnode' and 'endnodes' are the same. If so, it means the path is complete, 
    #  and it returns a List containing the current path.

    # -Otherwise, it iterates through each neighbor node of the start node using for node in 
    #  'self.graph_dictionary[startnode]:'.

    # -If the neighbor node ('node') is not already in the current path, it means we can explore it further 
    #  to find more paths.

    # -It calls itself, the 'get_all_possible_paths' Instance Method, recursively with the neighbor node 
    #  ('node') as the new 'startnode', with the same end node as the 'endnode', and the updated path values. 
    #  This step explores all possible paths from the current start node to the end.

    # -The result of the recursive call is a List of paths, which are stored in the 'new_paths' variable.

    # -It then appends each path from 'new_paths' to the 'all_possible_paths' list to accumulate all possible
    #  paths from the current start node to the end.

    # -Finally, after exploring all possible paths from the current start node, the method returns the 
    #  'all_possible_paths' List, which contains all the paths found.
    
    def get_all_possible_paths(self, startnode, endnode, path=[]):

        #Appending the 'startnode' element to the 'path' List
        path = path + [startnode]

        #When we do recursion, we must always define the simplest cases first for our recursion loops to 
        #'bounce' back from, which will be if the 'startnode' also happens to be the 'endnode', then we will
        #return the path (List)(which is a List), within another List so that we can append the other path Lists 
        #into the List of path Lists (initially it only contains the first possible path List) to create a 
        #List of path Lists, which will represent the Lists of all possible paths Lists between the 'startnode'
        #and 'endnode' after all the recursion loops have completed
        if startnode == endnode:
            return [path]
        
        all_possible_paths = []

        #The main recursive looping code
        for node in self.graph_dictionary[startnode]:
            if node not in path:
                new_paths = self.get_all_possible_paths(node, endnode, path)
                for p in new_paths:
                    all_possible_paths.append(p)

        return all_possible_paths

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


    start = "Mumbai"
    end = "New York"

    print(f"Paths between {start} and {end}: ", routes_graph.get_all_possible_paths(start, end))