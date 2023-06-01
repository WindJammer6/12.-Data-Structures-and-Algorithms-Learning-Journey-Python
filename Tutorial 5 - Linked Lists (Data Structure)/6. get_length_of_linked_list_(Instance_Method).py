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

    def insert_at_end(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return
        
        else:
            iterator = self.head
            while iterator.next is not None:
                iterator = iterator.next
            
        iterator.next = Node(new_data, None)

    #What this Instance Method does is that counts the number of Nodes in the Linked List. Fairly simple
    #to understand. As we use the iterator to traverse through the Linked List, every Node that we land
    #on, we increment the counter by 1 and return the counter value
    def get_length_of_linked_list(self):
        count = 0
        iterating_nodes = self.head
        while iterating_nodes:
            count += 1
            iterating_nodes = iterating_nodes.next
        return count

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

    print(samplelinkedlist.get_length_of_linked_list())