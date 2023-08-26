class GeneralTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None              

    def add_child_node(self, child_node_data):
        child_node_data.parent = self
        return self.children.append(child_node_data)

    #What this Instance Method does is that it allows us to print and view our General Tree Data Structure in a
    #nice and clear hirerachical format/visualisation. The first step to do this is by iterating through every
    #Node in the General Tree and printing their 'data' attribute/data that each Node is storing. Lets try this
    #and see how this Instance Method behaves:
    # def print_general_tree(self):
    #     print(self.data)
    #     for child in self.children:
    #         print(child.data)

    #Here's the output:
        #Electronics
        #Laptop
        #Cell Phone
        #Television


    #From here it does print our General Tree Data Structure, but there are 2 major issues. 

    #The first issue is that immediate children Nodes of the Root Node storing "electronics" does not have their 
    #own children Nodes being printed (such as "Macbook" and "Samsung"). So how can we print them? To solve this, 
    #we need to think about recursion. Instead of 'print(child.data)', how about we do 'child.print_general_tree()'
    #instead, re-using the function 'print_general_tree(self)', within itself:
    # def print_general_tree(self):
    #     print(self.data)
    #     #You can choose to add this if statement to check for Leaf Nodes (Nodes that have no children), by 
    #     #checking if their 'self.children' List is empty. Its not necessary, but it makes the code look tighter
    #     #and more logical/clear
    #     if self.children:                      #BTW, this is equivalent to 'if len(self.children) > 0:', to check
    #         for child in self.children:        #if there are elements inside the Array/Python List
    #             child.print_general_tree()

    #Here's the ouput (and it will work, as (General) Tree Data Structures are recursive Data Structures, where
    #children Nodes of the parent 'GeneralTreeNode' objects can also be thought as the starting Root Node for a 
    #'smaller' sub-'(General) Tree', hence this recursive Instance Method solves our problem, and be able to 
    #print out the data stored by children Nodes, of children Nodes, and so on...)
        #Electronics
        #Laptop
        #Macbook
        #Microsoft Surface
        #Thinkpad
        #Cell Phone
        #iPhone
        #Google Pixel
        #Vivo
        #Television
        #Samsung
        #LG

    #Great, now that we have all the data in the General Tree Data Structure being printed, we see the second issue, 
    #that the printed General Tree Data Structure don't show a clear hirerachy between the data. So, we need some sort
    #of indentation in front of the data printed to show its hirerachy, how can we do this? One way to do this is by 
    #adding a certain number of spaces in front of the printed data of each General Tree Node based on the Level it is
    #on in the overall General Tree Data Structure (so if that data in the General Tree Node, say "Samsung", is at 
    #Level 2, then we will add 2 spaces in front of its printed data, and since "Electronics" General Tree Root Node is
    #at Level 0, we will not add any spaces in front of its printed data). An example of the printed General Tree Data 
    #Structure that clearly shows its data hirerachy could look something like this:
        #Electronics
        # Laptop
        #  Macbook
        #  Microsoft Surface
        #  Thinkpad
        # Cell Phone
        #  iPhone
        #  Google Pixel
        #  Vivo
        # Television
        #  Samsung
        #  LG


    #So how can we find the Level of a particular General Tree Node? We can create a seperate Instance Method that does
    #that for us here (then we can use this Instance Method that does this, back into the 'print_general_tree(self)' 
    #Instance Method to help us find the number of spaces to add/print in front of a particular General Tree Node's printed
    #data in the terminal):

    #What this Instance Method does is that it returns/tells you the Level of a particular General Tree Node in a General
    #Tree Data Structure that you want to check. This Instance Method determines the Level of a particular General Tree Node
    #by counting the number of ancestors the General Tree Node has. So how do we do this in code? Making use of the 'parent'
    #attribute of the 'GeneralTreeNode' class, we will iterate up the General Tree Data Structure towards the Root
    #Node through the 'parent' attribute (like from the General Tree Node to its parent, then its parent's parent, and so 
    #on...). We do this by first initialising a 'level' variable to 0, then using a while loop, iterate up the General Tree 
    #Data Structure through the 'parent' attribute, which will break when we reach the Root Node, "Electronics" (since it 
    #has no 'parent', or its 'parent' attribute is None)
    def get_level_of_node(self):
        level = 0
        p = self.parent
        #BTW, this is equivalent of saying that, while the aforementioned General Tree Node has a 'parent' Node, keep going up
        #ancestry of the Nodes in the tree, until the while loop breaks when we reach the Root Node, since its 'parent' 
        #attribute is None (has no 'parent' Node)
        while p:
            level += 1
            p = p.parent
        return level


    #Now, we can add our 'get_level_of_node(self)' Instance Method into the 'print_general_tree(self)' Instance Method. We will
    #multiply the Level of the particular General Tree Node we are at with a spacing (' '), (taking from 'get_level_of_node(self)'
    #Instance Method) in a variable called 'number_of_spaces', and then during printing of 'self.data', add this 'number_of_spaces'
    #variable in front 'self.data'. With this, the 'print_general_tree(self)' Instance Method should print each General Tree Node's
    #data, while showing the hirerachy of each General Tree Node with respect to the overall General Tree Data Structure by printing
    #a certain number of spaces in front of its printed data based on its Level in the overall General Tree Data Structure
    def print_general_tree(self):
        number_of_spaces = ' ' * self.get_level_of_node() * 3
        #This line gives our printed General Tree Data Structure abit more nicer visualisation, but is otherwise optional. Just 
        #'print(number_of_spaces + self.data)' works too otherwise. The if-else statement just says if a General Tree Node has
        #'self.parent' as not None (has a 'parent' Node), print the prefixes and the spaces in front, else General Tree Node has 
        #'self.parent' as None (no 'parent' Node, referring to the Root Node), then don't put any prefixes nor spaces in front
        prefix = number_of_spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_general_tree()


def build_electronics_tree():
    root_node = GeneralTreeNode("Electronics")

    laptop = GeneralTreeNode("Laptop")
    laptop.add_child_node(GeneralTreeNode("Macbook"))
    laptop.add_child_node(GeneralTreeNode("Microsoft Surface"))
    laptop.add_child_node(GeneralTreeNode("Thinkpad"))

    cellphone = GeneralTreeNode("Cell Phone")
    cellphone.add_child_node(GeneralTreeNode("iPhone"))
    cellphone.add_child_node(GeneralTreeNode("Google Pixel"))
    cellphone.add_child_node(GeneralTreeNode("Vivo"))

    television = GeneralTreeNode("Television")
    television.add_child_node(GeneralTreeNode("Samsung"))
    television.add_child_node(GeneralTreeNode("LG"))

    root_node.add_child_node(laptop)
    root_node.add_child_node(cellphone)
    root_node.add_child_node(television)

    return root_node

        
if __name__ == '__main__':
    electronics_general_tree = build_electronics_tree()

    #To test our 'get_level_of_node(self):' Instance method if it works. Expected output is 0 since 'root_node' variable within
    #the 'build_electronics_tree()' function technically has its starter pointer at the Root Node 'GeneralTreeNode("Electronics")', 
    #which is at Level 0, and is in turn connected to the overall General Tree Data Structure
    print(electronics_general_tree.get_level_of_node())

    #To test our 'print_general_tree(self)' Instance Method)
    electronics_general_tree.print_general_tree()
