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

    #What this Instance Method does is that it inserts a particular Node in the Linked List based on its
    #index. It is quite similar ot how the 'remove_at_index' Instance Method works.

    #Conisderation of its 2 other scenarios is similar as the 'remove_at_index' Instance Method.
    #-> The first scenario is in the event an invalid index is given such as 'index < 0' and indexes 
    #   larger than number of Nodes in the Linked List and throws an exception
    #-> The second scenario is for insertion of a node in front of the head node ('index == 0'). We 
    #   leverage on another Instance Method we have created, 'insert_at_beginning' to take care of this
    #   scenario

    #For the 'else' part, how it does the insertion of Nodes (at any point) is by manipulating the 
    #pointers (for the head node it is slightly different and is explained above). 

        #Visual representation for removal of Node at any point (inserting new node '400'):
        #    Before insertion:
        #    298|pointer -> 305|pointer -> 320|pointer -> 301|null

        #                            400|pointer (New node created)

        #    Insertion:
        #    298|pointer -> 305|pointer -                  -> 320|pointer -> 301|null
        #                                |                |           
        #                                 -> 400|pointer -

        #    After Insertion:
        #    298|pointer -> 305|pointer -> 400|pointer -> 320|pointer -> 301|null
                
    def insert_at_index(self, index, new_data):
        if index < 0 or index >= self.get_length_of_linked_list():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_node_at_beginning(new_data)

            #OR
            #self.head = Node(new_data, self.head)
            #return
        
        else:
            count = 0
            iterator = self.head
            while iterator.next is not None:
                #We put 'index - 1' because we want to insert the new element in front of the 
                #'index - 1'th element so the inserted element will be at the sepcified index of 
                #by the user
                if count == index - 1:
                    iterator.next = Node(new_data, iterator.next)
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

    samplelinkedlist.insert_at_index(2, 99)
    samplelinkedlist.insert_at_index(2, 39)
    samplelinkedlist.insert_at_index(0, 56)

    samplelinkedlist.print_linked_list()

    print(samplelinkedlist.get_length_of_linked_list())
