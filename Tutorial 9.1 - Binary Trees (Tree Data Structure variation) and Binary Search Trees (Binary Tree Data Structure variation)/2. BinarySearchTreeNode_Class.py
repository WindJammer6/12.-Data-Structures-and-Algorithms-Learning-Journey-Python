#The 'BinarySearchTreeNode' object represents a Node/Sub-Tree in the General Tree Data Structure.

#A General Tree can have any number of child nodes, a Binary Tree can only up to 2 child nodes (left or right
#child node), and a Binary Search Tree is a Binary Tree but sorted in a certain manner (in this tutorial
#we will sort it as child nodes of a smaller value to be stored as the left child node and child nodes of a
#larger value to be stored as the right child node)

#It has 3 attributes:
#'data', which represents the data stored in the Binary Search Tree Node. Just like that those in Linked Lists,
#the data can be of any data type: ints, floats, strings, any objects, etc.

#'left', which represents the left child node/sub-tree of the current 'BinarySearchTreeNode' we are at (by default 
#it is set as None (or no left child node/sub-tree at first, but we'll change the None to be another 
#'BinarySearchTreeNode' when we are building our Binary Search Tree Data Structure))

#'right', which represents the right child node/sub-tree of the current 'BinarySearchTreeNode' we are at (by default 
#it is set as None (or no right child node/sub-tree at first, but we'll change the None to be another 
#'BinarySearchTreeNode' when we are building our Binary Search Tree Data Structure))

#In this tutorial, we are using data from the example given in '1. What_is_a_Binary_Tree_and_Binary_Search_Tree.txt'


#//////////////////////////////////////////////////


#So how do we build a Binary Search Tree Data Structure using this 'BinarySearchTreeNode' object class? 
#Similar to the General Tree Data Structure's Python implementation, Binary Search Tree Data Structures are 
#recursive Data Structures, which answers this question (see 
#'2. GeneralTreeNode_Class_and_recursive_Data_Structures.py' in 
#'Tutorial 9 - Trees and General Trees (Data Structure)' for about recursive Data Structures).


#//////////////////////////////////////////////////


#Note: Compared to General Tree Data Structure's Python implementation, Binary Search Tree Data Structure's Python 
#implementation has heavier implementation of recursion in the 'BinarySearchTreeNode' class's Instance Methods 
#(so you'll need to know your concept of recursion well)

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None