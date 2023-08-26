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
    
    #What this Instance Method does is that it finds/searches a particular Node/number in the BST. Pretty simple 
    #logic. This Instance Method makes use of 3 if statements (or 2 if statement and 1 else statement),
    def search_binary_search_tree(self, value_to_find):

        #1. It first checks if the current Node we are at is the particular Node we are looking for. If it is, then 
        #we will return True, that this particular Node we are looking for does exist in our BST. If the current 
        #Node is not the paricular Node we are looking for, then we will traverse down the BST via either the left 
        #or right  child node of the current Node depending if the number of looking for is smaller or larger than 
        #the current node, which is covered by the other 2 if statements.
        if self.data == value_to_find:
            return True
        
        #2. It then checks if the number we are looking for is smaller than the current Node. If it is, then before
        #we move to the current Node's left child node recursively (we are looping recursively so that this Instance
        #Method can traverse down the BST to search for the Node we are looking for (it works since Tree Data 
        #Structures are recursive Data Structures)), we need to check again if the current Node has a left child
        #node to move to.
         
        #If it does, then we recursively loop this Instance Method, shifting to the current Node' left child node,
        #this time with it being the current Node, effectively traversing one level down the BST, and recursively
        #looping this Instance Method multiple times allow us to traverse down the BST.
         
        #If it does not, then we conclude that the number that we are looking for does not exist in our BST,
        #returning False as we have already searched all the possible areas that the number that we are looking for
        #could be at in our BST but to no avail as we recursively loop this Instance Method, traversing down the BST 
        #through the path that the number we are looking for could be at in our BST
        if value_to_find < self.data:
            if self.left:
                #Sometimes you'll need a 'return' function here, sometimes you don't. So why is it so? In an
                #'if-else' statement if your 'else' statement has a 'return' function, then if you want to 
                #recursively call your last line of code you might want to have a 'return' statement as well so
                #that Python dosen't do anything funny like returning the output as None 
                return self.left.search_binary_search_tree(value_to_find)       #try figure out why if no return function output keeps showing 'None'
            else:                                                               #sth about needing to return the particular value (due to the second 'value' parapeter where to take in an argument in the function which is not an attribute of the BSTNode class?)
                return False

        #3. It lastly checks if the number we are looking for is larger than the current Node. If it is, then before
        #we move to the current Node's right child node recursively (we are looping recursively so that this 
        #Instance Method can traverse down the BST to search for the Node we are looking for (it works since Tree 
        #Data Structures are recursive Data Structures)), we need to check again if the current Node has a right 
        #child node to move to.
         
        #If it does, then we recursively loop this Instance Method, shifting to the current Node' right child node,
        #this time with it being the current Node, effectively traversing one level down the BST, and recursively
        #looping this Instance Method multiple times allow us to traverse down the BST.
         
        #If it does not, then we conclude that the number that we are looking for does not exist in our BST,
        #returning False as we have already searched all the possible areas that the number that we are looking for
        #could be at in our BST but to no avail as we recursively loop this Instance Method, traversing down the BST 
        #through the path that the number we are looking for could be at in our BST
        if value_to_find > self.data:                                           #'else' works too
            if self.right:
                return self.right.search_binary_search_tree(value_to_find)
            else:
                return False

def build_binary_search_tree(elements):
    root_node = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root_node.add_child_node(elements[i])

    return root_node


if __name__ == '__main__':
    numbers = [15, 27, 12, 14, 20, 7, 88, 23]
    numbers_binary_search_tree = build_binary_search_tree(numbers)
    print(numbers_binary_search_tree.depth_first_search_in_order_traversal())

    #Testing adding duplicates to our BST to see how it reacts (it should ignore any duplicates)
    numbers_with_duplicates = [15, 27, 12, 14, 20, 7, 88, 23, 12, 20, 88]
    numbers_with_duplicates_binary_search_tree = build_binary_search_tree(numbers)
    print(numbers_with_duplicates_binary_search_tree.depth_first_search_in_order_traversal())

    #Testing a number that does not exist in our BST (output should return False)
    print(numbers_binary_search_tree.search_binary_search_tree(24))
    #Testing a number that does exist in our BST (output should return True)
    print(numbers_binary_search_tree.search_binary_search_tree(23))