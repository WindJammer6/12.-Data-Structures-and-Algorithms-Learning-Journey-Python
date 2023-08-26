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

    #What this Instance Method does is that it removes a particular Node in the Linked List based on its
    #index. Of course, the Nodes dosent actually have an index, so it removes the Node based on its
    #positioning relative to the head Node via a counter. So if you put in an index of 3, the code will
    #traverse through the Linked List 3-1=2 times (cuz head node is of index 0) and remove the Node at
    #that positioning at the end of the while loop traversal

    #This Instance Method first considers 2 other scenarios first.
    #-> The first scenario is in the event an invalid index is given such as 'index < 0' and indexes 
    #   larger than number of Nodes in the Linked List and throws an exception
    #-> The second scenario is for removal of the head node. It does this by changing the head node of the
    #   Linked List to be the second node instead of the first node, effectively removing the first node
    #   from the Linked List

        #Visual representation for removal of head node:
        #   Before removal:
        #   298|pointer -> 305|pointer -> 320|pointer -> 301|null
        #     ^
        #     |
        #Head Node(self.head)

        #   Removal (shift of head node reference of the Linked List to the second node):
        #   298|pointer -> 305|pointer -> 320|pointer -> 301|null
        #                   ^
        #                   |
        #           Head Node(self.head)

        #   After removal:
        #   305|pointer -> 320|pointer -> 301|null
        #    ^
        #    |
        #Head Node(self.head)


    #For the 'else' part, how it does the removal of Nodes (at any point) is by manipulating the pointers
    #(for the head node it is slightly different and is explained above). 

        #Visual representation for removal of Node at any point:
        #    Before removal:
        #    298|pointer -> 305|pointer -> 320|pointer -> 301|null

        #    Removal:
        #    298|pointer -> 305|pointer -    320|pointer   -> 301|null
        #                                |                     ^
        #                                 _____________________|

        #    After removal:
        #    298|pointer -> 305|pointer -                     301|null
        #                                |                     ^
        #                                 _____________________|

    #About cleaning the data from memory: In Python, the language automatically cleans up such
    #discarded Nodes for you. But in other languages such as C and C++ you may need to manually clean
    #up these data yourself to prevent any memory spaces being wasted

    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length_of_linked_list():
            raise Exception("Invalid Index!")
        
        if index == 0:
            self.head = self.head.next
            return
        
        else:
            count = 0
            iterator = self.head
            while iterator is not None:
                if count == index - 1:
                    iterator.next = iterator.next.next
                    break
                iterator = iterator.next
                count += 1

if __name__ == '__main__':
    samplelinkedlist = LinkedList()

    samplelinkedlist.insert_node_at_beginning(5)
    samplelinkedlist.insert_node_at_beginning(89)
    samplelinkedlist.insert_node_at_beginning(86)

    samplelinkedlist.insert_at_end(7)
    samplelinkedlist.insert_at_end(90)

    samplelinkedlist.remove_at_index(2)

    samplelinkedlist.print_linked_list()

    print(samplelinkedlist.get_length_of_linked_list())
