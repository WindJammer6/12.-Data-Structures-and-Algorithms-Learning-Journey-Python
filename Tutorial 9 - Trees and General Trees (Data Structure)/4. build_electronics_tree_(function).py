class GeneralTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None              

    def add_child_node(self, child_node_data):
        child_node_data.parent = self
        return self.children.append(child_node_data)
        

#What this function is doing is that it builds the General Tree Data Structure, using data from the real life
#scenario described in '1. What_is_a_Tree_and_General_Tree.txt'.
def build_electronics_tree():

    #We start by creating our Root Node, storing "Electronics" as the data that it contains
    root_node = GeneralTreeNode("Electronics")

    #Then we add a child Node to the Root Node, another object of 'GeneralTreeNode' class storing "Laptop" as 
    #data. After this new child Node, of variable 'laptop' is appended to 'root_node.children''s List, we can
    #run debugging to see that the Root Node now has 1 child Node, storing "Laptop" as data. And of course, 
    #the child Node 'laptop' currently has no further children Nodes (since they havent been added)
    laptop = GeneralTreeNode("Laptop")

    #The rest of the code further down is quite repetitive and similar, by first creating the immediate child 
    #Nodes of "Electronics", and in turn, create the new child 'GeneralTreeNode' object, then appending them 
    #to these immediate child (now parent) Nodes to "Electronics", 'laptop', 'cellphone' and 'television'. 
    #Effectively, we now have 3 smaller' sub-'General Trees'
    laptop.add_child_node(GeneralTreeNode("Macbook"))
    laptop.add_child_node(GeneralTreeNode("Microsoft Surface"))
    laptop.add_child_node(GeneralTreeNode("Thinkpad"))

    #'cellphone' sub-'General Tree'
    cellphone = GeneralTreeNode("Cell Phone")
    cellphone.add_child_node(GeneralTreeNode("iPhone"))
    cellphone.add_child_node(GeneralTreeNode("Google Pixel"))
    cellphone.add_child_node(GeneralTreeNode("Vivo"))

    #'television' sub-'General Tree'
    television = GeneralTreeNode("Television")
    television.add_child_node(GeneralTreeNode("Samsung"))
    television.add_child_node(GeneralTreeNode("LG"))

    #We then combine all 3 smaller sub-'General Tree' to the Root Node by appending the sub-'General Tree''s Root
    #Nodes to our main 'root_node', storing "Electronics" as data
    root_node.add_child_node(laptop)
    root_node.add_child_node(cellphone)
    root_node.add_child_node(television)

    #Now our completed 'electronics tree' General Tree Data Structure is stored in the 'root_node' variable with 
    #starting point of our General Tree being at the Root Node (since 'root_node' variable is initially set as only
    #just containing one Node (the Root Node) in 'root_node = GeneralTreeNode("Electronics")'), storing 
    #"Electronics". We can sort of view the hirerachy of our 'electronic tree' General Data Structure by setting a 
    #breakpoint at 'return root_node' and run debugging. We then return 'root_node'.
    return root_node


if __name__ == '__main__':
    electronics_general_tree = build_electronics_tree()
        
        
