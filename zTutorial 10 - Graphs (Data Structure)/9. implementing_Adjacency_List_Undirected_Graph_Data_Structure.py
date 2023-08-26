class AdjacencyListUndirectedGraph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dictionary = {}

        for node1, node2 in self.edges:
            if node1 in self.graph_dictionary:
                self.graph_dictionary[node1].append(node2)
            else:
                self.graph_dictionary[node1] = [node2]

            if node2 in self.graph_dictionary:
                self.graph_dictionary[node2].append(node1)
            else:
                self.graph_dictionary[node2] = [node1]

    def add_node(self, node):
        if node in self.graph_dictionary:
            print(node, "is already present in the Graph Data Structure")

        else:
            self.graph_dictionary[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.graph_dictionary:
            print(node1, "is not present in the Graph Data Structure")
        elif node2 not in self.graph_dictionary:
            print(node2, "is not present in the Graph Data Structure")

        else:
            self.graph_dictionary[node1].append(node2)
            self.graph_dictionary[node2].append(node1)

    def delete_node(self, node):
        if node not in self.graph_dictionary:
            print(node, "is not present in the Graph Data Structure")

        else:
            self.graph_dictionary.pop(node)
            
            for i in self.graph_dictionary:
                value_list = self.graph_dictionary[i]
                if node in value_list:
                    value_list.remove(node)

    def delete_edge(self, node1, node2):
        if node1 not in self.graph_dictionary:
            print(node1, "is not present in the Graph Data Structure")
        elif node2 not in self.graph_dictionary:
            print(node2, "is not present in the Graph Data Structure")

        else:
            if node2 in self.graph_dictionary[node1]:
                self.graph_dictionary[node1].remove(node2)
                self.graph_dictionary[node2].remove(node1)
            else:
                print("No such edge exists that is connecting", node1, "to", node2)

    def breadth_first_search(self, node):
 
        queue_list = []
        visited = []
 
        queue_list.append(node)
 
        while queue_list:
            s = queue_list.pop(0)
            visited.append(s)
            if s in self.graph_dictionary:
                for i in self.graph_dictionary[s]:
                    if i not in visited and i not in queue_list:
                        queue_list.append(i)

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

    def get_shortest_path(self, startnode, endnode, path=[]):
        
        path = path + [startnode]

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

    def __repr__(self):
        return '{}'.format(self.graph_dictionary)
    

if __name__ == '__main__':

    #Creating this Undirected Graph Data Structure:
    #                     [Nikisha]
    #                   /
    #           [Bhawin]
    #              |
    #              |
    # [David]---[Dhavel]--------[Rahul] 
    #              |
    #              |
    #           [Shukul]

    facebook_network = [
        ("Dhavel", "Bhawin"),
        ("David", "Dhavel"),
        ("Shukul", "Dhavel"),
        ("Rahul", "Dhavel"),
        ("Bhawin", "Nikisha")
    ]

    facebook_network_graph = AdjacencyListUndirectedGraph(facebook_network)
    print(facebook_network_graph)

    facebook_network_graph.add_node("James")
    print(facebook_network_graph)

    facebook_network_graph.add_edge("James", "Nikisha")
    print(facebook_network_graph)

    facebook_network_graph.delete_node("James")
    print(facebook_network_graph)

    # facebook_network_graph.delete_edge("Nikisha", "Bhawin")
    # print(facebook_network_graph)
    
    print("Following is the Breadth-First Search")
    print(facebook_network_graph.breadth_first_search('Dhavel'))

    print("Following is the Depth-First Search")
    print(facebook_network_graph.depth_first_search('Dhavel'))


    start = "Shukul"
    end = "Nikisha"

    print(f"Paths between {start} and {end}: ", facebook_network_graph.get_all_possible_paths(start, end))

    print(f"Shortest path (in terms of number of stops) between {start} and {end}: ", facebook_network_graph.get_shortest_path(start, end))