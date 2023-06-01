#Question 2:
#Implement doubly linked list. The only difference with regular linked list is that double linked has 
#prev node reference as well. That way you can iterate in forward and backward direction. Your node 
#class will look this this,

#Visual representation of Doubly Linked List:
#null|298|pointer <-> pointer|305|pointer <-> pointer|320|pointer <-> pointer|301|null

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

#Bulk of the code copied from CodeBasics's Github profile so that I can implement the 2 methods:

#Implement all other methods in regular linked list class and make necessary changes for doubly linked 
#list (you need to populate node.prev in all those methods)
#(Most of the necessary changes for doubly linked list here I copied from the Solution since I found it 
#quite challenging to do myself. I marked out the differences in code between Singly and Doubly Linked 
#Lists)

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' <--> ' if itr.next else str(itr.data)  #(Difference)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, self.head, None)                    #(Difference)
            self.head = node
        else:
            node = Node(data, self.head, None)                    #(Difference)
            self.head.prev = node                                 #(Difference)
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)                    #(Difference)
            return
        
        else:
            itr = self.head

            while itr.next:
                itr = itr.next

            itr.next = Node(data, None, itr)                      #(Key Difference)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)                  #(Difference)
                if node.next is not None:                         #(Difference)
                    node.next.prev = node                         #(Difference)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None                                 #(Difference)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                if itr.next is not None:                          #(Difference)
                    itr.next.prev = itr.prev                      #(Difference)
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    #My implementation of the 2 methods, 'def print_forward(self)' and 'def print_backward(self)'.

    #My answer quite similar to Solution, so I wont be copying the Solution over.

    def print_forward(self):                        #Basically the same as 'def print(self)'
        # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr.next is not None:
            llstr += str(itr.data)+' --> '
            itr = itr.next
        llstr += str(itr.data)
        print(llstr)

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        iterator = self.head
        while iterator.next is not None:
            iterator = iterator.next

        llstr = ''
        while iterator.prev is not None:
            llstr += str(iterator.data)+' --> '
            iterator = iterator.prev
        llstr += str(iterator.data)
        print(llstr)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.print_backward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()
