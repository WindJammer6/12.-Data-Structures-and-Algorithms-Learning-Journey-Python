class AdjacencyListUndirectedWeightedGraph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dictionary = {}

        for node1, node2, cost in self.edges:
            if node1 in self.graph_dictionary:
                self.graph_dictionary[node1].append((node2, cost))
            else:
                self.graph_dictionary[node1] = [(node2, cost)]

            if node2 in self.graph_dictionary:
                self.graph_dictionary[node2].append((node1, cost))
            else:
                self.graph_dictionary[node2] = [(node1, cost)]

    def add_node(self, node):
        if node in self.graph_dictionary:
            print(node, "is already present in the Graph Data Structure")

        else:
            self.graph_dictionary[node] = []

    def add_edge(self, node1, node2, cost):
        if node1 not in self.graph_dictionary:
            print(node1, "is not present in the Graph Data Structure")
        elif node2 not in self.graph_dictionary:
            print(node2, "is not present in the Graph Data Structure")

        else:
            tuple = (node2, cost)
            tuple2 = (node1, cost)
            self.graph_dictionary[node1].append(tuple)
            self.graph_dictionary[node2].append(tuple2)

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

    def delete_edge(self, node1, node2, cost):
        if node1 not in self.graph_dictionary:
            print(node1, "is not present in the Graph Data Structure")
        elif node2 not in self.graph_dictionary:
            print(node2, "is not present in the Graph Data Structure")

        else:
            node2_and_cost_set = (node2, cost)
            if node2_and_cost_set in self.graph_dictionary[node1]:
                self.graph_dictionary[node1].remove(node2_and_cost_set)
            else:
                print("No such edge exists that is connecting", node1, "to", node2, "with the cost", cost)

    def breadth_first_search(self, node):
 
        queue_list = []
        visited = []
 
        queue_list.append(node)
 
        while queue_list:
            s = queue_list.pop(0)
            visited.append(s)
            if s in self.graph_dictionary:
                for i in self.graph_dictionary[s]:
                    if i[0] not in visited and i[0] not in queue_list:
                        queue_list.append(i[0])

        return visited
    
    def depth_first_search(self, node):
 
        stack_list = []
        visited = []
 
        stack_list.insert(0, node)
 
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
    
    #Creating this Undirected Weighted Graph Data Structure (I know it conceptually dosen't make
    #sense but this is just for demonstration purposes):
    #                     [Nikisha]
    #                   / 7
    #           [Bhawin]
    #              | 6
    #         3    |        8
    # [David]---[Dhavel]--------[Rahul] 
    #              |
    #              | 10
    #           [Shukul]

    facebook_network = [
        ("Dhavel", "Bhawin", 6),
        ("David", "Dhavel", 3),
        ("Shukul", "Dhavel", 10),
        ("Rahul", "Dhavel", 8),
        ("Bhawin", "Nikisha", 7)
    ]

    facebook_network_graph = AdjacencyListUndirectedWeightedGraph(facebook_network)
    print(facebook_network_graph)

    facebook_network_graph.add_node("James")
    print(facebook_network_graph)

    facebook_network_graph.add_edge("James", "Nikisha", 5)
    print(facebook_network_graph)

    facebook_network_graph.delete_node("James")
    print(facebook_network_graph)

    facebook_network_graph.delete_edge("Nikisha", "Bhawin", 7)
    print(facebook_network_graph)
    
    print("Following is the Breadth-First Search")
    print(facebook_network_graph.breadth_first_search("Dhavel"))

    print("Following is the Depth-First Search")
    print(facebook_network_graph.depth_first_search("Dhavel"))


    start = "Shukul"
    end = "Nikisha"

    print(f"Paths between {start} and {end}: ", facebook_network_graph.get_all_possible_paths(start, end))

    print(f"Shortest path (in terms of distance) between {start} and {end}: ", facebook_network_graph.get_shortest_path(start, end))