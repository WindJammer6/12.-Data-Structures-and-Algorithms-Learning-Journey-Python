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

    #What this Instance Method does is that it allows you to traverse the Binary Search Tree in a specific manner,
    #via Depth-First Search: In Order traversal (Formula: Left-Root-Right)(see 
    #'1. What_is_a_Binary_Tree_and_Binary_Search_Tree.txt' to understand how does DFS: In Order traversal works), 
    #and return the order of which the Nodes are traversed through in the BST in a Python's List. 
     
    #This is so you can see whats going on and how the process of DFS: In Order traversal through your BST happened,
    #when you print this Python's List created within the 'depth_first_search_in_order_traversal(self)' in the main
    #code. Printing this returned Python's List of Nodes/data/elements in the BST also allows us to see all the 
    #Nodes/data/elements in the BST in a specific order that is determined by the traversal method (in this case its
    #DFS: In Order traversal)(other traversal methods (see '1. What_is_a_Binary_Tree_and_Binary_Search_Tree.txt') 
    #will produce different order of the Nodes/data/elements in the returned Python's List)

    #In our tutorial example, due to the sorted manner of our BST, the expected output for DFS: In Order traversal
    #is the numbers in the Nodes/data/elements being traversed through in the manner of ascending number, and
    #the returned Python List will be a List of ascending numbers: [7, 12, 14, 15, 20, 23, 27, 88]

    #This traversal Instance Method may seem redundant in our example but is quite applicable in some real life 
    #contexts (different traversal methods is useful in different scenarios (can google to see the type of real
    #life BST traversal Instance Methods applications))
    def depth_first_search_in_order_traversal(self):
        elements = []

        #Visiting root/base/current node's left node/sub-tree. The '+=' operator is used to concatenate all the
        #elements of the left Node/sub-tree to the 'elements' list (it allows updating of every recursive loop's
        #(those with any alterations in their 'elements' list) element list to the original 'elements' list, and
        #using the updated 'elements' list in the next recursion loop)
        if self.left:
            elements += self.left.depth_first_search_in_order_traversal()

        #Visiting root/base/current node you are at and appending it to the 'elements' list. 
         
        #In some recursion loops where you are at the path's lowest node you may append this root/base/current node
        #as it has no more left child nodes, while in others recursion loops, the left child nodes/sub-tree has
        #already been printed hence ending the particular recursive loop and allowing the program to reach here
        #to print the root/base/current node
        elements.append(self.data)

        #Visiting root/base/current node's right node/sub-tree. The '+=' operator is used to concatenate all the
        #elements of the right Node/sub-tree to the 'elements' list (it allows updating of every recursive loop's
        #(those with any alterations in their 'elements' list) element list to the original 'elements' list, and
        #using the updated 'elements' list in the next recursion loop)
        if self.right:
            elements += self.right.depth_first_search_in_order_traversal()

        return elements
    
    #Here is a ChatGPT's attempt to explain all the crazy recursiveness step-by-step, using the BST we have built
    #below:
    #Let's go through the recursive in-order traversal step by step for the given BST.

        # 1. Initially, the `elements` list is empty.

        # 2. Starting with the root node, which contains the number 15:
        # - The `depth_first_search_in_order_traversal` method is called on the left child of the root node (12).
        
        # 3. On the left child node (12):
        # - The `depth_first_search_in_order_traversal` method is called on the left child of node 12 (7).
        
        # 4. On the left child node (7):
        # - Since there is no left child, we move to the next step.
        # - The number 7 is appended to the `elements` list.
        # - Since there is no right child, we move back to node 12.
        
        # 5. Back on node 12:
        # - The number 12 is appended to the `elements` list.
        # - The `depth_first_search_in_order_traversal` method is called on the right child of node 12 (14).
        
        # 6. On the right child node (14):
        # - Since there is no left child, we move to the next step.
        # - The number 14 is appended to the `elements` list.
        # - Since there is no right child, we move back to node 12.
        
        # 7. Back on node 12:
        # - Since both the left and right subtrees of node 12 have been traversed, we move back to the root node.

        # 8. Back on the root node (15):
        # - The number 15 is appended to the `elements` list.
        # - The `depth_first_search_in_order_traversal` method is called on the right child of the root node (27).

        # 9. On the right child node (27):
        # - The `depth_first_search_in_order_traversal` method is called on the left child of node 27 (20).

        # 10. On the left child node (20):
        #     - Since there is no left child, we move to the next step.
        #     - The number 20 is appended to the `elements` list.
        #     - Since there is no right child, we move back to node 27.

        # 11. Back on node 27:
        #     - The number 27 is appended to the `elements` list.
        #     - The `depth_first_search_in_order_traversal` method is called on the right child of node 27 (88).

        # 12. On the right child node (88):
        #     - Since there is no left child, we move to the next step.
        #     - The number 88 is appended to the `elements` list.
        #     - Since there is no right child, we move back to node 27.

        # 13. Back on node 27:
        #     - Since both the left and right subtrees of node 27 have been traversed, we move back to the root node.

        # 14. Back on the root node (15):
        #     - Since both the left and right subtrees of the root node have been traversed, the in-order traversal is complete.
        #     - The `elements` list contains the numbers in the order of an in-order traversal: [7, 12, 14, 15, 20, 27, 88].

        # That's how the in-order traversal instance method would work recursively step by step for the given BST.

def build_binary_search_tree(elements):
    root_node = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root_node.add_child_node(elements[i])

    return root_node


if __name__ == '__main__':
    numbers = [15, 27, 12, 14, 20, 7, 88, 23]

    numbers_binary_search_tree = build_binary_search_tree(numbers)

    #Printing our created BST as a Python's List, with the indexing of the elements showing the traversal order 
    #through the BST via the DFS: In Order traversal mmethod (this dosen't show the full visualisation of the BST,
    #only showing the Nodes/data/elements present in the BST, in the specific order of DFS: In Order traversal,
    #which will be the Nodes storing numbers in the BST in ascending order in the returned Python's List) 
    print(numbers_binary_search_tree.depth_first_search_in_order_traversal())


    #Here we test our 'add_child_node()' Instance Method on the part of it that prevents duplicates from being added
    #in the BST since that now we are able to somewhat print our BST using the 
    #'depth_first_search_in_order_traversal()' Instance Method. 
     
    #It is shown to work as adding duplicate numbers to our BST (by having duplicates in the Python's List that is
    #being passed through the 'build_binary_search_tree()') and somewhat printing out our BST using the 
    #'depth_first_search_in_order_traversal()' Instance Method, shows that there is an absence of any duplicates
    #in our BST. Hence it works and this proves that the 'add_child_node()' Instance Method does ignore any 
    #duplicates being added to the BST in 
    #'print(numbers_with_duplicates_binary_search_tree.depth_first_search_in_order_traversal())'
    numbers_with_duplicates = [15, 27, 12, 14, 20, 7, 88, 23, 12, 20, 88]
    numbers_with_duplicates_binary_search_tree = build_binary_search_tree(numbers)
    print(numbers_with_duplicates_binary_search_tree.depth_first_search_in_order_traversal())

