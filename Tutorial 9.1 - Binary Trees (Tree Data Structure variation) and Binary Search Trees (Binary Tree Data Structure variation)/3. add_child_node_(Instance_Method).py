class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #What this Instance Method does is that it allows you to add a child Node to another Node (that may or may 
    #not already be part of a BST Data Structure). Unlike for General Tree Data Structure, before we create/set 
    #that 'pointer' between the new child Node and the initial parent Node, we need to create that 'no duplicates'
    #and the 'sorted order' characteristics of our BST. Then we'll create that link/pointer between the 
    #new child node and the initial parent node as we create the 'sorted order' characteristic (see below at the 
    #second point):
    def add_child_node(self, data):

        #1. To create the 'no duplicates' characteristic, during every recursive loop, we will check if the
        #current node we are at is storing the same data as the new child node we are trying to add to our BST
        #via the line of code 'if data == self.data'. If it is, then we will return nothing, and exit the 
        #'add_child_node()' Instance Method without doing anything, effectively ignoring and not adding the
        #duplicate new child node that we are trying to add to the BST
        if data == self.data:
            return
        

        #2. In these 2 if statements ('if data < self.data' and 'if data > self.data'), we create the 'sorted order'
        #characteristic, where child nodes storing numbers smaller than the initial parent node will be stored as
        #the left child node/sub-tree, while child nodes storing numbers larger than the initial parent node will be
        #stored as the right child node/sub-tree.

        #Here we are trying to add the new child node to the left child node/sub-tree
        if data < self.data:

            #However, before we just add our child node in, we need to check that the current node we are at 
            #dosen't already have a left child node (since we want to add our new child node to the path's lowest 
            #node of our BST with no left child node (not necessarily leaf node since this node may still have a 
            #right child node but no left child node)(such that it becomes the new leaf node) and not slot it 
            #randomly at the intermediate area of our BST)

            #This if statement checks if there exists a left child node (if there exists a 'self.left' and that it is
            #not None).
            if self.left:
                #If there exists a left child node, we will repeat the recursively loop and repeat the process of
                #the 'add_child_node()' Instance Method in the current node's left child node (since it is also the
                #'BinarySearchTreeNode' class and has the 'add_child_node()' Instance Method). This will loop
                #recursively and allow you to traverse down the BST to find the path's lowest node of our BST with 
                #no left child node (not necessarily leaf node since this node may still have a right child node 
                #but no left child node) to add our new child node in
                self.left.add_child_node(data)

            #This else statement checks if there is exists no left child node (if there exists no 'self.left' and 
            #that it is None). In this case, we know that we are already at the path's lowest node of our BST with 
            #no left child node and go ahead and add that path's lowest node's left child node as our new child
            #node, effectively adding our new child node to our BST and its rightful, sorted location
            else:
                #Creating/setting the link/pointer between the new child node and the parent node with no left 
                #child node
                self.left = BinarySearchTreeNode(data)


        #This else statement deals with trying to add the new child node to right child node/sub-tree 
         
        #The code here is very similar to the code above to add the new child node to the left sub-tree (I'm not 
        #going to type out the explanation, please refer to the if statement  (to add new child node to left child
        #node/sub-tree above for the explanation. Instead of left child node its right child node in this case as 
        #we are dealing with trying to add the new child node to right child node/sub-tree)
        else:                                                   #'else data > self.data' works too
            if self.right:
                self.right.add_child_node(data)
            else:
                self.right = BinarySearchTreeNode(data)