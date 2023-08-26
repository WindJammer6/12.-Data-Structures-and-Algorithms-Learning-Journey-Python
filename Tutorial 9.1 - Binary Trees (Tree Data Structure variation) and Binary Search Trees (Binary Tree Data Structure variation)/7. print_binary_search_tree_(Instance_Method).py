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
    
    #Looks like its using some sort of traversal to print the full BST visually, first the right subtree,
    #root, then left sub tree (right-root-left) so that we can get a good visualisation (left-root-right dosent
    #look very nice)

    #What this Instance Method does is that it prints a visualisation of the BST created. Its code prints the
    #output BST visualisation (run the code to see the output) in a way very similar to the 
    #'depth_first_search_in_order_traversal()' Instance Method. (I am not going to explain it here again, see
    #'5. depth_first_search_in_order_traversal_(Instance_Method).py for the explanation on how it is able to 
    #print the BST visualisation starting from the top line of the visualisation, and going down the lines in
    #the terminal)

    #Usually dealing with the left child nodes/sub-tree comes before the right child nodes/sub-tree, but in this
    #printing BST visualisation Instance Method the visualisation looks more accurate to a BST when the right
    #child/sub-tree is printed first, then current node, then the left child node/sub-tree (you can try switching
    #the 'self.right' with 'self.left' in the Instance Method and see what happens to the printed visualisation
    #output)
    def print_binary_search_tree(self, level=0):
        if self.data:
            if self.right:
                self.right.print_binary_search_tree(level + 1)

            print(' ' * 4 * level + '-> ' + str(self.data))

            if self.left:
                self.left.print_binary_search_tree(level + 1)

def build_binary_search_tree(elements):
    root_node = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root_node.add_child_node(elements[i])

    return root_node


if __name__ == '__main__':
    numbers = [15, 27, 12, 14, 20, 7, 88, 23]
    numbers_binary_search_tree = build_binary_search_tree(numbers)
    print(numbers_binary_search_tree.depth_first_search_in_order_traversal())
    numbers_binary_search_tree.print_binary_search_tree()

    #Testing adding duplicates to our BST to see how it reacts (it should ignore any duplicates)
    numbers_with_duplicates = [15, 27, 12, 14, 20, 7, 88, 23, 12, 20, 88]
    numbers_with_duplicates_binary_search_tree = build_binary_search_tree(numbers)
    print(numbers_with_duplicates_binary_search_tree.depth_first_search_in_order_traversal())
    numbers_with_duplicates_binary_search_tree.print_binary_search_tree()

    #Testing a number that does not exist in our BST (output should return False)
    print(numbers_binary_search_tree.search_binary_search_tree(24))
    #Testing a number that does exist in our BST (output should return True)
    print(numbers_binary_search_tree.search_binary_search_tree(23))


    #Testing other types of Node data in a BST (strings). We will be using names of countries in our input
    #Python's List that we will be passing thorugh our 'build_binary_search_tree()' function to build another BST
    #(with duplicate elements)
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_binary_search_tree = build_binary_search_tree(countries)

    #Testing a string/country that does not exist in our BST (output should return False)
    print("Is UK in the list? ", country_binary_search_tree.search_binary_search_tree("UK"))
    #Testing a string/country that does exist in our BST (output should return True)
    print("Is Sweden in the list? ", country_binary_search_tree.search_binary_search_tree("Sweden"))


    #When you try to run these 2 lines of code, you will notice that the country strings are sorted in the 
    #BST in a particular order (its no random!) (seen from 'country_binary_search_tree.print_binary_search_tree()')
    #and returns the returned Python's List in lexicographical order (aka dictionary order, like how you'll see
    #these strings/words in a dictionary). Why is this so?

    #This is because within the BST building function, 'build_binary_search_tree()', within it the 
    #'add_child_node()' Instance Method, it organises the BST by the code 'if self.data > data' and 
    #'if self.data < data'. The effect that the '<' and '>' operators have on strings instead of number (this is an
    #example of Operator Overloading) is that it does a lexicographical comparison on the strings. This compares 
    #strings in the same way that they would be listed in dictionary order, generalized to work for strings with 
    #non-letter characters.

    #e.g. if you run these code:
        # print("a" < "b")
        # print("a" < "ab")
        # print("cat" < "caterpillar")
        # print("China" < "India")
        # print("China" < "Chinaa")
        # print("Chinaa" < "china")
        # print("C" < "HELLO")

    #The output for all of these will be True, true due to the the fact that all the strings on the right hand
    #side would be placed further down/back the dictionary than its comparing strings at the left hand side.
    #If you swap the direction of the operator or the sides of the strings, you would get False instead.
    #(However using '<' and '>' operators on strings is usually not recommended in Python programming)
    print(country_binary_search_tree.depth_first_search_in_order_traversal())
    country_binary_search_tree.print_binary_search_tree()

    