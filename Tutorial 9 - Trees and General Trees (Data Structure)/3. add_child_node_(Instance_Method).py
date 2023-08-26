class GeneralTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None              

    #What this Instance Method does is that it allows you to add a child Node to another Node (that may or may 
    #not already be part of a General Tree Data Structure). To create/set that 'pointer' between the new child
    #Node and the initial parent Node, we need to do 2 things:
     
    #1. Note that the parameter 'child_node_data' must be an Instance of the 'GeneralTreeNode' object, and that
    #that is what we will be appending to the 'self.children' List of the initial Node that we want to add our 
    #new Node to

    #2. Then, to complete the link/pointer, we say that the parent of our new Node, is the initial Node we are 
    #adding the new Node to
    def add_child_node(self, child_node_data):
        child_node_data.parent = self
        return self.children.append(child_node_data)
    

        
