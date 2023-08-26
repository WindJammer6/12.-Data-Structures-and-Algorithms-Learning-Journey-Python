#Question 1:

#Add the following methods to BinarySearchTreeNode class created in main video tutorial:
#1. find_min(): finds minimum element in entire binary search tree
#2. find_max(): finds maximum element in entire binary search tree
#3. calculate_sum(): calcualtes sum of all elements
#4. depth_first_search_pre_order_traversal(): performs post order traversal of a binary search tree
#5. depth_first_search_post_order_traversal(): performs pre order traversal of a binary search tree

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

    #My answers:
    #1. find_min(): finds minimum element in entire binary search tree 
    #Since the most left node in the BST (you can visualise it as the bottom left node of a BST) has the smallest
    #value/data/element in the BST, in order to find the minimum/smallest element in the BST, we just have to 
    #traverse to that most left node and obtain it
    def find_min(self):
        if self.data:
            if self.left:
                return self.left.find_min()
            else:
                return self.data

    #2. find_max(): finds maximum element in entire binary search tree
    #Since the most right node in the BST (you can visualise it as the bottom right node of a BST) has the smallest
    #value/data/element in the BST, in order to find the maximum/largest element in the BST, we just have to 
    #traverse to that most right node and obtain it
    def find_max(self):
        if self.data:
            if self.right:
                return self.right.find_max()
            else:
                return self.data
                
    #3. calculate_sum(): calcualtes sum of all elements 
    #For this Instance Method I just used DFS: In Order traversal to traverse through all the elements, and added
    #each individual Node's number to the variable 'total' and return that 'total' after traversing through the
    #BST (any type of traversal method should work, but I just used the one that we created in the tutorial, 
    #DFS: In Order traversal for convenience sake)
    def calculate_sum(self):
        total = 0

        for i in self.depth_first_search_in_order_traversal():
            total += i
        
        return total

        
    #4. depth_first_search_pre_order_traversal(): performs pre order traversal of a binary search tree
    #From '1. What_is_a_Binary_Tree_and_Binary_Search_Tree.txt', the formula for DFS: Pre order traversal is
    #'Root-Left-Right'. Hence, all I had to do was take the code for DFS: In Order traversal, but instead of
    #printing the root/base/current node after printing the left child node/sub-tree, we do that first, then
    #we go and print the left then right child nodes/sub-trees
    def depth_first_search_pre_order_traversal(self):
        elements = []

        #visiting root/base/current node 
        elements.append(self.data)

        #visiting left node
        if self.left:
            elements += self.left.depth_first_search_pre_order_traversal()

        #visiting right node
        if self.right:
            elements += self.right.depth_first_search_pre_order_traversal()

        return elements

    #5. depth_first_search_post_order_traversal(): performs post order traversal of a binary search tree
    #From '1. What_is_a_Binary_Tree_and_Binary_Search_Tree.txt', the formula for DFS: Post order traversal is
    #'Left-Right-Root'. Hence, all I had to do was take the code for DFS: In Order traversal, but instead of
    #printing the root/base/current node after printing the left child node/sub-tree, we do that only after
    #we printed both the left then right child nodes/sub-trees
    def depth_first_search_post_order_traversal(self):
        elements = []

        #visiting left node
        if self.left:
            elements += self.left.depth_first_search_post_order_traversal()

        #visiting right node
        if self.right:
            elements += self.right.depth_first_search_post_order_traversal()

        #visiting root/base/current node 
        elements.append(self.data)

        return elements
    

    #Solutions:
    #1. find_min(): finds minimum element in entire binary search tree
    #Quite similar to mine, except it dosen't check for empty BST's being passed in. Otherwise looks exactly 
    #similar
        # def find_min(self):
        #     if self.left is None:
        #         return self.data
        #     return self.left.find_min()
    
    #2. find_max(): finds maximum element in entire binary search tree
    #Quite similar to mine, except it dosen't check for empty BST's being passed in. Otherwise looks exactly 
    #similar
        # def find_max(self):
        #     if self.right is None:
        #         return self.data
        #     return self.right.find_max()
    
    #3. calculate_sum(): calcualtes sum of all elements
    #Slightly different from mine. Mine traverses through the entire BST (using DFS: In Order traversal) and 
    #adding each Node's number to the total individually and returning the total. The Solution makes use of 
    #recursion to add the left child node/sub-tree, the root/current/base node, and the right child mode/sub-tree
    #together to get the total of the whole BST (it works as BST is a recursive Data Structure)
        # def calculate_sum(self):
        #     left_sum = self.left.calculate_sum() if self.left else 0
        #     right_sum = self.right.calculate_sum() if self.right else 0
        #     return self.data + left_sum + right_sum
    
    #For 4 and 5 the Solution is exactly the same as mine so I won't be adding those in

def build_binary_search_tree(elements):
    root_node = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root_node.add_child_node(elements[i])

    return root_node


if __name__ == '__main__':
    numbers = [15, 27, 12, 14, 20, 7, 88, 23]
    numbers_binary_search_tree = build_binary_search_tree(numbers)
    numbers_binary_search_tree.print_binary_search_tree()
 
    #Testing the 5 Instance Methods here
    print("Min:", numbers_binary_search_tree.find_min())
    print("Max:", numbers_binary_search_tree.find_max())
    print("Total sum:", numbers_binary_search_tree.calculate_sum())
    print("DFS: In Order traversal:", numbers_binary_search_tree.depth_first_search_in_order_traversal())
    print("DFS: Pre Order traversal:", numbers_binary_search_tree.depth_first_search_pre_order_traversal())
    print("DFS: Post Order traversal:", numbers_binary_search_tree.depth_first_search_post_order_traversal())

    #All works well, my answer looks correct, with slight differences in implementing the 'calculate_sum()'
    #Instance Method.