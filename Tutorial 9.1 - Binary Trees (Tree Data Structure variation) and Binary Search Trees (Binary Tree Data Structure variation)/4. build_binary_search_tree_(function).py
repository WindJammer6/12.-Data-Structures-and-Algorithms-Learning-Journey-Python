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


#What this function is doing is that it builds the Binary Search Tree Data Structure, using data from the example 
#given in '1. What_is_a_Binary_Tree_and_Binary_Search_Tree.txt'

#This function takes in a Python's List of elements and adds them to the BST (in order, like index 1's element will
#be inserted first, then index's 2 element), it then returns the BST, with the Root Node (the first element from
#the Python's List inserted) as the starting point.
def build_binary_search_tree(elements):

    #We start by creating our Root Node, storing the first element from the Python's List inserted
    root_node = BinarySearchTreeNode(elements[0])

    #We will then use a for loop to iterate through the Python's List, starting from the second element to the last
    #element in the Python's List (since the first element has already been added as the Root Node of the BST)
    for i in range(1, len(elements)):
        
        #Here we use the 'add_child_node()' Instance Method to add each element to the BST as we iterate
        #through the 'elements' Python's List in order of each element's indexing in the 'elements' Python's List 
        root_node.add_child_node(elements[i])

    #Now our completed Binary Search Tree Data Structure is stored in the 'root_node' variable with starting point 
    #of our BST being at the Root Node (since 'root_node' variable is initially set as only just containing one 
    #Node (the Root Node) in 'root_node = BinarySearchTreeNode(elements[0])'), which is storing the first element in 
    #the Python's List.
    return root_node


if __name__ == '__main__':
    #This is the Python's List we will be passing through our 'build_binary_search_tree()' function which will build
    #our BST using the elements in this Python's List (elements in the Python's List will be added to the BST in 
    #order of indexing). Currently we are unable to view our Binary Search Tree Data Structure, hence we will 
    #creating 2 other Instance Methods later in '5. depth_first_search_in_order_traversal_(Instance_Method).py' and
    #'7. print_binary_search_tree_(Instance_Method)' which will allow us to view our BST in different ways
    numbers = [15, 27, 12, 14, 20, 7, 88, 23]
    numbers_binary_search_tree = build_binary_search_tree(numbers)

