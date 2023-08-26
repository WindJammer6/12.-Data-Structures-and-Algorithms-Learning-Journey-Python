#Question 2:

#Modify the 'delete_node()' method in class BinarySearchTreeNode class to use max element from left subtree instead of 
#using the min element from right subtree. You will remove lines marked with ---> and use max value from left subtree

#    def delete(self, val):
#        if val < self.data:
#            if self.left:
#                self.left = self.left.delete(val)
#        elif val > self.data:
#            if self.right:
#                self.right = self.right.delete(val)
#        else:
#            if self.left is None and self.right is None:
#                return None
#            elif self.left is None:
#                return self.right
#            elif self.right is None:
#                return self.right

#          --->  min_val = self.right.find_min()
#          --->  self.data = min_val
#          --->  self.right = self.right.delete(min_val)

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

    def delete_node_via_right_subtree(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete_node_via_right_subtree(data) 
        elif data > self.data:
            if self.right:
                self.right = self.right.delete_node_via_right_subtree(data)

        else:                                                           #'elif data == self.data:' works too
            #For the first scenario
            if self.left is None and self.right is None:
                self = None
                return self
            

            #For the second scenario
            #Only child node/sub-tree is a right child node/sub-tree (no left child node/sub-tree)
            if self.left is None:
                self = self.right
                return self
            #Only child node/sub-tree is a right child node/sub-tree (no left child node/sub-tree)
            if self.right is None:
                self = self.left
                return self
            

            #For the third scenario
            if self.left is not None and self.right is not None:
                minimum_value_in_right_child_sub_tree = self.right.find_min()
                self.data = minimum_value_in_right_child_sub_tree

                self.right = self.right.delete_node_via_right_subtree(minimum_value_in_right_child_sub_tree)
                return self

        return self 


    #My answer:
    def delete_node_via_left_subtree(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete_node_via_left_subtree(data) 
        elif data > self.data:
            if self.right:
                self.right = self.right.delete_node_via_left_subtree(data)

        else:                                                           #'elif data == self.data:' works too
            #For the first scenario
            if self.left is None and self.right is None:
                self = None
                return self
            

            #For the second scenario
            #Only child node/sub-tree is a right child node/sub-tree (no left child node/sub-tree)
            if self.left is None:
                self = self.right
                return self
            #Only child node/sub-tree is a right child node/sub-tree (no left child node/sub-tree)
            if self.right is None:
                self = self.left
                return self
            

            #For the third scenario
            if self.left is not None and self.right is not None:
                maximum_value_in_left_child_sub_tree = self.left.find_max()
                self.data = maximum_value_in_left_child_sub_tree

                self.left = self.left.delete_node_via_left_subtree(maximum_value_in_left_child_sub_tree)
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

    #Testing my answer, the 'delete_node_via_left_subtree()' Instance Method for various Nodes in the BST
    numbers_binary_search_tree.delete_node_via_left_subtree(27)
    numbers_binary_search_tree.print_binary_search_tree()
    print(numbers_binary_search_tree.depth_first_search_in_order_traversal())

    numbers_binary_search_tree.delete_node_via_left_subtree(14)
    numbers_binary_search_tree.print_binary_search_tree()
    print(numbers_binary_search_tree.depth_first_search_in_order_traversal())

    numbers_binary_search_tree.delete_node_via_left_subtree(15)
    numbers_binary_search_tree.print_binary_search_tree()
    print(numbers_binary_search_tree.depth_first_search_in_order_traversal())

    numbers_binary_search_tree.delete_node_via_left_subtree(88)
    numbers_binary_search_tree.print_binary_search_tree()
    print(numbers_binary_search_tree.depth_first_search_in_order_traversal())
    
    
    #All works well, my answer looks correct, Solution is the same so won't be uploading Solution
