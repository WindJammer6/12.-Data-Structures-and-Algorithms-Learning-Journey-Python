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
    
    def get_all_possible_paths(self, startnode, endnode, path=[]):

        path = path + [startnode]

        if startnode == endnode:
            return [path]
        
        all_possible_paths = []

        for node in self.graph_dictionary[startnode]:
            if node not in path:
                new_paths = self.get_all_possible_paths(node, endnode, path)
                for p in new_paths:
                    all_possible_paths.append(p)

        return all_possible_paths

    #What this Instance Method does is that it finds the first shortest path between 2 nodes in the Adjacency 
    #List Directed Graph Data Structure (in terms of number of nodes in between the 2 nodes, instead of the
    #weighted cost of the edges since this is not a weighted Graph Data Structure)

    #It takes in 3 parameters, 
    #'startnode' representing the starting node from which the shortest path will originate from

    #'endnode' parameter representing the end node where which the shortest path will end at
    
    #'path', which is set as an empty List by default, which is used to keep track of the current path being 
    #explored (see the part when this Instance Method is called recursively in the Instance Method) 

    #Similar to the 'get_all_possible_paths' Instance Method, since Graph Data Structures are recursive Data 
    #Structure, it makes sense for us to use recursion in this Instance Method as well


    #Here is a ChatGPT's attempt to explain all the recursiveness step-by-step in the Instance Method:

    # -The Instance Method starts by appending the 'startnode' to the path.

    # -It then checks if the 'startnode' and 'endnode' are the same. If so, it means the path is complete, 
    #  and it returns the current path as the shortest path.

    # -Otherwise, it initializes 'shortest_path' to None. This variable will be used to keep track of the 
    #  shortest path found so far.

    # -It iterates through each neighbor node ('node') of the 'startnode' using 'for node in 
    #  'self.graph_dictionary[startnode]:'

    # -If the neighbor node ('node') is not already in the current path, it means we can explore it further
    #  to find more paths.

    # -It calls itself, the 'get_shortest_path' Instance Method recursively with the neighbor node ('node')
    #  as the new 'startnode', with the same end node as the 'endnode', and the updated path values.

    # -The result of the recursive call is stored in the 'sp' variable. If there is a path found, 'sp' will 
    #  contain the List representing that path. Otherwise, it will be None.

    # -If 'sp' is not None, it means a path exists from the current start node to the end.

    # -It then compares the length of the path 'sp' to the current 'shortest_path'. If 'shortest_path' is 
    #  None, (i.e., no shortest path found yet) or if the length of 'sp' is shorter than the length of 
    #  'shortest_path', it updates 'shortest_path' to 'sp'.
    
    # -After exploring all possible paths from the current start node, the method returns the 
    # 'shortest_path'.


    #(Note: A problem with this Instance Method is that if there is 2 paths that have the same number of
    #nodes between the 2 nodes ('startnode' and 'endnode'), then it will only return the first path out of
    #the 2 paths with the same shortest path (in terms of number of nodes in between the 2 nodes). Such as
    #in this case there are 2 shortest paths, '["Mumbai", "Paris", "New York"]' and 
    #'["Mumbai", "Dubai", "New York"]' but this Instance Method will only return the first path found, 
    #'["Mumbai", "Paris", "New York"]', so this is a flaw as it would be better to return both shortest paths.

    # def egt_shortest_path(self, all_paths):
    #     d = {}
    #     for i in all_paths:
    #         if len(i) in d:
    #            d[len(i)].append(i)
    #         else:
    #             d[len(i)] = [i]
    #     return d[min(d.keys())]

    #The code above is an alternative way of implementing this Instance Method that solves this problem)

    def get_shortest_path(self, startnode, endnode, path=[]):
        
        #Appending the 'startnode' element to the 'path' List
        path = path + [startnode]

        #When we do recursion, we must always define the simplest cases first for our recursion loops to 
        #'bounce' back from, which will be if the 'startnode' also happens to be the 'endnode', then we
        #will just return the path List
        if startnode == endnode:
            return path
        
        shortest_path = None

        for node in self.graph_dictionary[startnode]:
            if node not in path:
                sp = self.get_shortest_path(node, endnode, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path
    
    # def shortest_path(self, all_paths):
    #         d = {}
    #         for i in all_paths:
    #             if len(i) in d:
    #                 d[len(i)].append(i)
    #             else:
    #                 d[len(i)] = [i]
    #         return d[min(d.keys())]
    

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

    print(f"Shortest path (in terms of number of stops) between {start} and {end}: ", routes_graph.get_shortest_path(start, end))