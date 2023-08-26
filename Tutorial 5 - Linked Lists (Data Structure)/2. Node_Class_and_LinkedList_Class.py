#The 'Node' object which represents individuals node for each element in the Linked List. It has 2
#attributes, the first is 'data', the data itself for the element, the second is 'next', the pointer
#of the node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


#The 'LinkedList' object represents the overall Linked List Data Structure. It has 1 attribute, 'head',
#which points to the head/start of the Linked List
class LinkedList:
    def __init__(self):
        self.head = None

if __name__ == '__main__':
    samplelinkedlist = LinkedList()


#////////////////////////////////////////////////


#By the way, Linked Lists are a recursive Data Structure (not very important concept for its 
#implemention in this tutorial). Just something to know. Refer to 'Tutorial 9 - Trees and General 
#Trees', the Python file '2. GeneralTreeNode_Class_and_recursive_Data_Structures.py' for more info

