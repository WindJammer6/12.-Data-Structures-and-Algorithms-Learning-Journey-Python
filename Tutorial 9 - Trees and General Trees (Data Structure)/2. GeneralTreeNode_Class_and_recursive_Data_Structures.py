#The 'GeneralTreeNode' object represents a Node/Sub-Tree in the General Tree Data Structure.

#It has 3 attributes:
#'data', which represents the data stored in the General Tree Node. Just like that those in Linked Lists,
#the data can be of any data type: ints, floats, strings, any objects, etc.

#'children', which is where the children Nodes of said General Tree Node will be recorded/stored in an 
#Array/Python List. All elements in this List should be an Instance of the 'GeneralTreeNode' object
#class to make use of the fact that (General) Tree Data Structures are recursive Data Structures (see below), 
#and the full (General) Tree Data Structure is built from 'smaller' (General) Tree Data Structures, which the 
#'GeneralTreeNode' class serves as the 'smallest' possible '(General) Tree' (a single (General) Tree Node)
#as the foundation to build our overall (General) Tree Data Structure

#'parent', which represents the parent Node of said General Tree Node (by default it is set as None (or 
#currently, no parent Node)). Every General Tree Node will at most only can have one parent Node, but
#a parent Node can have multiple children Nodes

#In this tutorial, we are using data from the real life scenario described in 
#'1. What_is_a_Tree_and_General_Tree.txt'


#//////////////////////////////////////////////////


#So how do we build a General Tree Data Structure using this 'GeneralTreeNode' object class? 
#Before we answer this question, we need to understand that Tree Data Structures are recursive Data 
#Structures.

#What are recursive Data Structures?
#Just like how a recursive function is a function that executes itself. A recursive Data Structure contains
#itself. Some examples include: Sets, Linked Lists, Trees and Graphs

#A Linked List is a recursive Data Structure because the next variable of a Linked List Node, is also a 
#Linked List Node (or that Linked Lists can also be thought to contain 'smaller' Linked Lists within it). 
#During our implementation of Linked Lists in 'Tutorial 5 - Linked Lists', you could sort of see this (though
#its not very obvious, and wasn't a very important concept to know during its implementation) 

#Similarly to Linked Lists as recursive Data Structures, Tree Data Structures are recursive because each
#'Tree' Node is not only a reference to a Node in the Tree Data Structure, but can be interpreted also as a 
#reference to a child sub-'Tree', which is a 'smaller' versions of the whole Tree Data Structure

#Similarly to Linked Lists as recursive Data Structures, Graph Data Structures are recursive because the
#the overall Graph Data Structure can be though to be composed of smaller Graph Data Structures

class GeneralTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None              