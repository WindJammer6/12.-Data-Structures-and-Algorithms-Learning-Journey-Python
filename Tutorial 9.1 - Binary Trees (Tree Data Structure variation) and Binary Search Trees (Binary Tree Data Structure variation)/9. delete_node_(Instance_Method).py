class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child_node(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child_node(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:                                                   #'else data > self.data' works too
            if self.right:
                self.right.add_child_node(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def depth_first_search_in_order_traversal(self):
        elements = []

        #visiting left node
        if self.left:
            elements += self.left.depth_first_search_in_order_traversal()

        #visiting root/base/current node 
        elements.append(self.data)

        #visiting right node
        if self.right:
            elements += self.right.depth_first_search_in_order_traversal()

        return elements
    
    def search_binary_search_tree(self, value_to_find):
        if self.data == value_to_find:
            return True
        
        if value_to_find < self.data:
            #'value_to_find' might be in left sub-tree
            if self.left:
                return self.left.search_binary_search_tree(value_to_find)
            else:
                return False

        else:
            #'value_to_find' might be in right sub-tree
            if self.right:
                return self.right.search_binary_search_tree(value_to_find)
            else:
                return False
    
    def print_binary_search_tree(self, level=0):
        if self.data:
            if self.right:
                self.right.print_binary_search_tree(level + 1)

            print(' ' * 4 * level + '-> ' + str(self.data))

            if self.left:
                self.left.print_binary_search_tree(level + 1)

    #In order to implement the 'delete_node()' Instance Method below, we will need to make use of the 'find_min()'
    #or 'find_max()' Instance Method (explanation on how they work in 
    #'8. Excercise1_Binary_Seach_Tree_(Data_Structure).py') depending on which approach you are taking to 
    #implement your 'delete_node()' Instance Method.
    #-> If you are implementing the 'delete_node()' Instance Method tackling the third scenario (deleting a node 
    #   with 2 child nodes/sub-tree) via the node to delete's right child node/sub-tree's node with minimum number
    #   then you will need 'find_min()'
    #-> If you are implementing the 'delete_node()' Instance Method tackling the third scenario (deleting a node
    #   with 2 child nodes/sub-tree) via the node to delete's left child node/sub-tree's node with maximum number
    #   then you will need 'find_max()'
    def find_min(self):
        if self.data:
            if self.left:
                return self.left.find_min()
            else:
                return self.data

    def find_max(self):
        if self.data:
            if self.right:
                return self.right.find_max()
            else:
                return self.data

    #For the theory behind on how deletion operation work for BST, refer to the section 'Explaining how Deletion 
    #operation works in Binary Search Tree' in '1. What_is_a_Binary_Tree_and_Binary_Search_Tree.txt'.

    #What this Instance Method does is that it deletes a node (it can be any node, the root node, intermediate
    #node or leaf node) in the BST.
    def delete_node(self, data):

        #It does this by first accessing the node in the BST to be deleted using recursion to traverse down the BST
        #(recursive Data Structure), like how we have done in some of the previous Instance Methods implemented 
        #(such as 'add_child_node()' and 'search_binary_search_tree()').  
        if data < self.data:
            if self.left:
                #Here it is important that we assign the 'self.left.delete_node(data)' back to our node to 
                #delete/current node we are at after (if we did) make any deletions in the left child 
                #node/sub-tree in previous recursive loops
                self.left = self.left.delete_node(data) 

            #Here we will return None for the 'else' as if we reached the end of the traversal path down the BST 
            #(reached the leaf node), and we still haven't found the node we are looking for to delete in the BST, 
            #this means the node we are looking to delete must not exist in the BST, hence we will return None, and
            #exit the Instance Method without doing anything to the BST, ignoring the deletion process 

            #In Python, if you want to return None and ignore/not do anything the 'else' statement, then you actually
            #don't have to bother writing this at all since Python, by default returns None if an 'else' statemenet is
            #not written if the 'if' statement goes to the 'else' case
            # else:
            #     return None
        elif data > self.data:
            if self.right:
                self.right = self.right.delete_node(data)
            # else:
            #     return None


        #Once we have accessed the node in our BST to be deleted, by comparing the data we are looking for with the 
        #current node we are at in the BST. If the current node is contains the data we are looking for for deletion,
        #or 'data == self.data:', we will deal with the 3 possible scenarios when deleting the node as explained in 
        #'1. What_is_a_Binary_Tree_and_Binary_Search_Tree.txt'.
        else:                                                           #'elif data == self.data:' works too

            #For the first scenario, deleting a node with no child nodes/sub-trees, which we define as if the node to
            #delete/current node we are at's 'self.left' and 'self.right' attributes are both None, then we will delte
            #the node with no child nodes/sub-trees to be None, so its no longer a node, removing it from the BST.
            #We then 'return self' to allow chaining between the many recursive loops working on the same copy of 
            #the BST occuring within the Instance Method when it runs
            if self.left is None and self.right is None:
                self = None
                return self
            

            #For the second scenario, deleting a node with 1 child nodes/sub-trees, which we can split into 2 possible
            #cases, if the node to delete/current node we are at's only child node/sub-tree is a left child 
            #node/sub-tree or a right child node/sub-tree

            #Depending on which side the only child node/sub-tree is at, we will sort of shift its only child 
            #node/sub-tree up the BST by letting/overriding the node to delete to now be its only child node/sub-tree
            #instead of what it initially was, effectively deleting it 

            #Only child node/sub-tree is a right child node/sub-tree (no left child node/sub-tree)
            if self.left is None:
                self = self.right
                return self
            #Only child node/sub-tree is a right child node/sub-tree (no left child node/sub-tree)
            if self.right is None:
                self = self.left
                return self
            

            #For the third scenario, deleting a node with 2 child nodes/sub-trees (via the right child node/sub-tree), 
            #which we define as if the node to delete/current node we are at's 'self.left' and 'self.right' attributes 
            #are both not None.
            if self.left is not None and self.right is not None:

                #Since we want to tackle the third scenario via the right child node/sub-tree, we will first copy and 
                #replace the node to delete's 'self.data' with the node with smallest number from node to delete's right 
                #child sub-tree
                minimum_value_in_right_child_sub_tree = self.right.find_min()
                self.data = minimum_value_in_right_child_sub_tree

                #We will then delete the duplicate original copy of the node with smallest number from node to delete's 
                #right child sub-tree by recursively calling the 'delete_node()' Instance Method here, but for the node
                #to delete's (now replaced with the node with smallest number's 'self.data' from its's right child 
                #sub-tree) right child node/sub-tree instead, and inserting the duplicate original copy's 'self.data' as
                #the 'delete_node()''s parameter instead
                self.right = self.right.delete_node(minimum_value_in_right_child_sub_tree)
                return self

        return self

def build_binary_search_tree(elements):
    root_node = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root_node.add_child_node(elements[i])

    return root_node


if __name__ == '__main__':
    #Cleaned up the main code to make things look cleaner.

    numbers = [15, 27, 12, 14, 20, 7, 88, 23]
    numbers_binary_search_tree = build_binary_search_tree(numbers)
    print(numbers_binary_search_tree.depth_first_search_in_order_traversal())
    numbers_binary_search_tree.print_binary_search_tree()

    #Testing a number that does not exist in our BST (output should return False)
    print(numbers_binary_search_tree.search_binary_search_tree(24))
    #Testing a number that does exist in our BST (output should return True)
    print(numbers_binary_search_tree.search_binary_search_tree(23))

    #Testing the 'delete_node()' Instance Method for various Nodes in the BST
    numbers_binary_search_tree.delete_node(27)
    numbers_binary_search_tree.print_binary_search_tree()
    print(numbers_binary_search_tree.depth_first_search_in_order_traversal())

    numbers_binary_search_tree.delete_node(14)
    numbers_binary_search_tree.print_binary_search_tree()
    print(numbers_binary_search_tree.depth_first_search_in_order_traversal())

    numbers_binary_search_tree.delete_node(15)
    numbers_binary_search_tree.print_binary_search_tree()
    print(numbers_binary_search_tree.depth_first_search_in_order_traversal())

    numbers_binary_search_tree.delete_node(88)
    numbers_binary_search_tree.print_binary_search_tree()
    print(numbers_binary_search_tree.depth_first_search_in_order_traversal())
    

    #Testing the 'delete_node()' Instance Method on a smaller BST
    test = [1,2]
    test_bst = build_binary_search_tree(test)
    print(test_bst.depth_first_search_in_order_traversal())
    test_bst.print_binary_search_tree()

    #Something to point out is that for the 'delete_node()' Instance Method, for smaller BSTs, if you want to delete
    #its root node, you need to assign the BST when deleting a node (see below's deletion code line) unlike for larger 
    #BSTs where you don't need to assign the BST again when deleting a node (see above's deletion code line)
    test_bst = test_bst.delete_node(1)
    print(test_bst.depth_first_search_in_order_traversal())
    test_bst.print_binary_search_tree()




    