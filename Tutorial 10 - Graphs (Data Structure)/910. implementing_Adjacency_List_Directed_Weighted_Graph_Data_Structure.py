class AdjacencyListDirectedWeightedGraph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dictionary = {}

        for start, end, cost in self.edges:
            if start in self.graph_dictionary:
                self.graph_dictionary[start].append((end, cost))
            else:
                self.graph_dictionary[start] = [(end, cost)]
            
        for start, end, cost in self.edges:
            if end not in self.graph_dictionary:
                self.graph_dictionary[end] = []

    def add_node(self, node):
        if node in self.graph_dictionary:
            print(node, "is already present in the Graph Data Structure")

        else:
            self.graph_dictionary[node] = []

    def add_edge(self, startnode, endnode, cost):
        if startnode not in self.graph_dictionary:
            print(startnode, "is not present in the Graph Data Structure")
        elif endnode not in self.graph_dictionary:
            print(endnode, "is not present in the Graph Data Structure")

        else:
            tuple = (endnode, cost)
            self.graph_dictionary[startnode].append(tuple)

    def delete_node(self, node):
        if node not in self.graph_dictionary:
            print(node, "is not present in the Graph Data Structure")

        else:
            self.graph_dictionary.pop(node)
            
            for i in self.graph_dictionary:
                value_list = self.graph_dictionary[i]

                #To find the node to deleted in an Adjacency List Directed Weighted Graph Data Structure, we will 
                #compare the first element ('j[0]') of the Tuple with the data the node is storing to determine which 
                #Tuple we need to delete in each key-value pair's value list in the 'self.graph_dictionary'
                for j in value_list:
                    if node == j[0]:
                        value_list.remove(j)

    def delete_edge(self, startnode, endnode, cost):
        if startnode not in self.graph_dictionary:
            print(startnode, "is not present in the Graph Data Structure")
        elif endnode not in self.graph_dictionary:
            print(endnode, "is not present in the Graph Data Structure")

        else:
            endnode_and_cost_set = (endnode, cost)
            if endnode_and_cost_set in self.graph_dictionary[startnode]:
                self.graph_dictionary[startnode].remove(endnode_and_cost_set)
            else:
                print("No such edge exists that is pointing in the direction from", startnode, "to", endnode, "with the cost", cost)

    def breadth_first_search(self, rootnode):
 
        queue_list = []
        visited = []
 
        queue_list.append(rootnode)
 
        while queue_list:
            s = queue_list.pop(0)
            visited.append(s)
            if s in self.graph_dictionary:
                for i in self.graph_dictionary[s]:
                    if i[0] not in visited and i[0] not in queue_list:
                        queue_list.append(i[0])

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
                    if i[0] not in visited and i[0] not in stack_list:
                        stack_list.insert(0, i[0])

        return visited
    
    def get_all_possible_paths(self, startnode, endnode, path=[]):

        path = path + [startnode]

        if startnode == endnode:
            return [path]
        
        all_possible_paths = []

        for node, cost in self.graph_dictionary[startnode]:
            if node not in path:
                new_paths = self.get_all_possible_paths(node, endnode, path)
                for p in new_paths:
                    all_possible_paths.append(p)

        return all_possible_paths
    
    #For Adjacency List Weighted (Directed and Undirected) Graph Data Structure this Instance Method returns
    #shortest path in terms of distance/total cost or weight of the edges of that path instead of the number
    #of stops in between the 'startnode' and 'endnode'
    def get_shortest_path(self, startnode, endnode):
        
        list_of_paths = self.get_all_possible_paths(startnode, endnode)

        cost_list = []

        for path in list_of_paths:
            total_cost = 0

            for i in range(len(path)-1):
                for j in self.graph_dictionary[path[i]]:
                    if j[0] == path[i+1]:
                        total_cost += j[1]

            cost_list.append(total_cost)
            total_cost = 0

        index_of_lowest_cost = cost_list.index(min(cost_list))

        return list_of_paths[index_of_lowest_cost]

    def __repr__(self):
        return '{}'.format(self.graph_dictionary)


if __name__ == '__main__':
    
    #Creating this Directed Weighted Graph Data Structure:
    #       2000           8000
    #     ------->[Paris]--------
    #     |          |          |
    #     |          | 2000    \ /      400
    # [Mumbai]       |      [New York]------
    #     |          |          ^          |
    #     |         \ /         |         \ /
    #     ------->[Dubai]--------      [Toronto]
    #       5000           3000

    routes = [
        ["Mumbai", "Paris", 2000],
        ["Mumbai", "Dubai", 5000],
        ["Paris", "Dubai", 2000],
        ["Paris", "New York", 8000],
        ["Dubai", "New York", 3000],
        ["New York", "Toronto", 400]
    ]

    routes_graph = AdjacencyListDirectedWeightedGraph(routes)
    print(routes_graph)

    routes_graph.add_node("Singapore")
    print(routes_graph)

    routes_graph.add_edge("Singapore", "Toronto", 7000)
    print(routes_graph)

    routes_graph.delete_node("Singapore")
    print(routes_graph)

    # routes_graph.delete_edge("Mumbai", "Dubai", 5000)
    # print(routes_graph)
    
    print("Following is the Breadth-First Search")
    print(routes_graph.breadth_first_search('Mumbai'))

    print("Following is the Depth-First Search")
    print(routes_graph.depth_first_search('Mumbai'))


    start = "Mumbai"
    end = "New York"

    print(f"Paths between {start} and {end}: ", routes_graph.get_all_possible_paths(start, end))

    print(f"Shortest path (in terms of distance) between {start} and {end}: ", routes_graph.get_shortest_path(start, end))