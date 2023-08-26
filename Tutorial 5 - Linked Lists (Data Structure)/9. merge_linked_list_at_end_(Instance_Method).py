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
                
    def insert_at_index(self, index, new_data):
        if index < 0 or index >= self.get_length_of_linked_list():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_node_at_beginning(new_data)
        
        else:
            count = 0
            iterator = self.head
            while iterator.next is not None:
                if count == index - 1:
                    iterator.next = Node(new_data, iterator.next)
                    break
                iterator = iterator.next
                count += 1

#This is how it looks like. Tried to link the Linked Lists at a specified index but couldn't get it to
#work...
def merge_linked_list_at_end(linkedlist1, linkedlist2):
    dummylinkedlist = LinkedList()

    dummylinkedlist.head = linkedlist1.head

    iterator = dummylinkedlist.head
    while iterator.next is not None:
        iterator = iterator.next

    iterator.next = linkedlist2.head
    
    return dummylinkedlist


if __name__ == '__main__':
    samplelinkedlist = LinkedList()
    samplelinkedlist2 = LinkedList()

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

    samplelinkedlist2.insert_node_at_beginning(70)
    samplelinkedlist2.insert_node_at_beginning(71)
    samplelinkedlist2.insert_node_at_beginning(72)
    samplelinkedlist2.insert_node_at_beginning(73)

    samplelinkedlist2.print_linked_list()

    mergedlinkedlist = merge_linked_list_at_end(samplelinkedlist, samplelinkedlist2)
    mergedlinkedlist.print_linked_list()