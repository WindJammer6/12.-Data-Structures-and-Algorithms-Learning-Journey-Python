#Question 2:
# Build below location tree using TreeNode class
    # Global
    #     |__India
    #         |__Gujarat 
    #             |__Ahmedabad
    #             |__Baroda
    #         |__Karnataka
    #             |__Bangluru
    #             |__Mysore
    #     |__USA
    #         |___New Jersey
    #             |__Princeton
    #             |__Trenton
    #         |__California
    #             |__San Francisco
    #             |__Mountain View
    #             |__Palo Alto

#Now modify print_tree method to take tree level as input. And that should print tree only upto that 
#level as shown below, using this main function:

    # if __name__ == '__main__': 
    #     root_node = build_location_tree() 
    #     root_node.print_tree(1)
    #     root_node.print_tree(2)
    #     root_node.print_tree(3)

#Your output should look like this:

    # 'root_node.print_tree(1)' should give:
    # Global
    #     |__India
    #     |_USA

    # 'root_node.print_tree(2)' should give:
    # Global
    #     |__India
    #         |__Gujarat
    #         |__Karnataka
    #     |__USA
    #         |__New Jersey
    #         |__California

    # 'root_node.print_tree(3)' should give:
    # Global
    #     |__India
    #         |__Gujarat 
    #             |__Ahmedabad
    #             |__Baroda
    #         |__Karnataka
    #             |__Bangluru
    #             |__Mysore
    #     |__USA
    #         |___New Jersey
    #             |__Princeton
    #             |__Trenton
    #         |__California
    #             |__San Francisco
    #             |__Mountain View
    #             |__Palo Alto


class GeneralTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None              

    def add_child_node(self, child_node_data):
        child_node_data.parent = self
        return self.children.append(child_node_data)
    
    def get_level_of_node(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    #My answer:
    def print_general_tree(self, up_to_node_level):
        number_of_spaces = ' ' * self.get_level_of_node() * 3
        prefix = number_of_spaces + "|__" if self.parent else ""
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                if child.get_level_of_node() <= up_to_node_level:
                    child.print_general_tree(up_to_node_level)
                else:
                    break

def build_location_tree():
    root_node = GeneralTreeNode("Global")


    #'India' sub-'General Tree'
    india = GeneralTreeNode("India")

    gujarat = GeneralTreeNode("Gujarat")
    gujarat.add_child_node(GeneralTreeNode("Ahmedabad"))
    gujarat.add_child_node(GeneralTreeNode("Baroda"))

    karnataka = GeneralTreeNode("Karnataka")
    karnataka.add_child_node(GeneralTreeNode("Bangluru"))
    karnataka.add_child_node(GeneralTreeNode("Mysore"))

    india.add_child_node(gujarat)
    india.add_child_node(karnataka)


    #'USA' sub-'General Tree'
    usa = GeneralTreeNode("USA")

    newjersey = GeneralTreeNode("New Jersey")
    newjersey.add_child_node(GeneralTreeNode("Princeton"))
    newjersey.add_child_node(GeneralTreeNode("Trenton"))

    california = GeneralTreeNode("California")
    california.add_child_node(GeneralTreeNode("San Francisco"))
    california.add_child_node(GeneralTreeNode("Mountain View"))
    california.add_child_node(GeneralTreeNode("Palo Alto"))

    usa.add_child_node(newjersey)
    usa.add_child_node(california)


    root_node.add_child_node(india)
    root_node.add_child_node(usa)

    return root_node


#Solution for the 'print_general_tree()' Instance Method (answer for the 'build_location_tree()' is very similar
#to mine so I won't be adding in the Solution for that):
# def print_general_tree(self, level):
#     if self.get_level_of_node() > level:
#         return
#     spaces = ' ' * self.get_level_of_node() * 3
#     prefix = spaces + "|__" if self.parent else ""
#     print(prefix + self.data)
#     if self.children:
#         for child in self.children:
#             child.print_general_tree(level)

if __name__ == '__main__': 
    root_node = build_location_tree() 
    root_node.print_general_tree(0)
    root_node.print_general_tree(1)
    root_node.print_general_tree(2)
    root_node.print_general_tree(3)

    #All works well, my answer looks correct with some slight differences in code in the 'print_general_tree()'
    #Instance Method between my answer and Solution.