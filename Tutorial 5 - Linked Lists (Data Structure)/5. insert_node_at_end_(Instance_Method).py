class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node_at_beginning(self, new_data):
        node = Node(new_data, self.head)
        self.head = node

    #This Instance Method has an 'if' statement. The 'if' part considers the possibility that a Linked 
    #List is empty (where 'self.head' is None) and print out that the Linked List is empty.
    
    #The 'else' part is a little trickier. Basically the 'iterator = self.head' (which sets the beginning
    #of the iteration with the head node (or self.head) btw) and the while loop will loop through each 
    #'Node' in the Linked List (starting with head node, then the second node, third, fourth, etc). The 
    #while loop will traverse through the Linked List and only terminate when self.next/iterator.next is 
    #None (theres no more Nodes after that Node (which means that that Node is the last node).

    #The last line 'iterator.next = Node(data, None)' then creates a Node and inserts that Node behind
    #the last Node (which by then 'iterator.next' would be the '.next'/pointer for the last Node (and
    #that 'iterator' will be referencing to the last Node of the Linked List) after the Linked List have 
    #looped through the while loop)
    def insert_at_end(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return
        
        else:
            iterator = self.head
            while iterator.next is not None:
                iterator = iterator.next
            
        iterator.next = Node(new_data, None)
                
    def print_linked_list(self):
        if self.head == None:
            print("Linked List is empty!")
            return
        else:
            iterating_nodes = self.head
            linked_list_string = ""

            while iterating_nodes:
                linked_list_string += str(iterating_nodes.data) + '-->'
                iterating_nodes = iterating_nodes.next

        print(linked_list_string)

if __name__ == '__main__':
    samplelinkedlist = LinkedList()

    samplelinkedlist.insert_node_at_beginning(5)
    samplelinkedlist.insert_node_at_beginning(89)
    samplelinkedlist.insert_node_at_beginning(86)

    samplelinkedlist.insert_at_end(7)
    samplelinkedlist.insert_at_end(90)

    samplelinkedlist.print_linked_list()
