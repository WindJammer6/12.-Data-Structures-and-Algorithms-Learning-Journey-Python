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
                
    #What this Instance Method does is that it allows us to print out our Linked List Data Structure.

    #If there are no nodes in our Linked List (which where the head node will be 'None'), it will return
    #that the Linked List is empty. Else, it will iterate through each node in the Linked List, starting
    #with the head node and adding it into the 'linked_list_string', and then going to the next node via 
    #'iterating_nodes = iterating_nodes.next' and adding the data in that node into the 
    #'linked_list_string' via the 'linked_list_string += str(iterating_nodes.data) + '-->''and it will 
    #print the overall Linked List via printing the 'linked_list_string'
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


#From this, the output should be '86-->89-->5-->', which is correct since we first added '5' to the 
#beginning of the Linked List, then '89' at the beginning afterwards, and then another '86' after. Hence 
#'86' should be infront of '89', which is in turn in front '5' which is shown to be indeed the case hence
#our 'LinkedList' object works
if __name__ == '__main__':
    samplelinkedlist = LinkedList()

    samplelinkedlist.insert_node_at_beginning(5)
    samplelinkedlist.insert_node_at_beginning(89)
    samplelinkedlist.insert_node_at_beginning(86)

    samplelinkedlist.print_linked_list()