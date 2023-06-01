class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    #What this Instance Method does is that it is taking a data value, and inserting it at the head
    #of the Linked List. 

    #How it does this is that it creates a special node using the 'Node' Class object, and since the 
    #first attribute of a 'Node' object is 'data', the data is pre-decided by the programmer, while the 
    #second attribute of the 'Node' object is 'next', the next node of the Linked List, which will be
    #the head node of the Linked List since we want to insert this new node at the beginning of the 
    #Linked List.

    def insert_node_at_beginning(self, new_data):
        node = Node(new_data, self.head)
        self.head = node        #We then assign this node added at the beginning as the new head of the 
                                #Linked List

if __name__ == '__main__':
    samplelinkedlist = LinkedList()

    samplelinkedlist.insert_node_at_beginning(5)
    samplelinkedlist.insert_node_at_beginning(89)
    samplelinkedlist.insert_node_at_beginning(86)

