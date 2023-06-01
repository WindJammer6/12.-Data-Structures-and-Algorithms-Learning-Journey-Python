#Question 1:
#In LinkedList class that we implemented in our tutorial add following two methods,
    # def insert_after_value(self, data_after, data_to_insert):
    #     # Search for first occurance of data_after value in linked list
    #     # Now insert data_to_insert after data_after node

    # def remove_by_value(self, data):
    #     # Remove first node that contains data

#Bulk of the code copied from CodeBasics's Github profile so that I can implement the 2 methods:
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


    #My implementation of the 2 methods, 'def insert_after_value(self, data_after, data_to_insert)' and
    #'def remove_by_value(self, data)'

    #My answer quite similar to Solution, so I wont be copying the Solution over. Only 1 error in my
    #'def remove_by_value(self, data)' Instance Method
    def insert_after_value(self, data_after, data_to_insert):
        iterator = self.head
        while iterator.next is not None:
            #Search for first occurance of data_after value in linked list
            if iterator.data == data_after:
                #Now insert data_to_insert after data_after node
                iterator.next = Node(data_to_insert, iterator.next)
                break
            iterator = iterator.next
         

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head.data == data:
            self.remove_at(0)
            return                            #My error: Forgot to add this 'return' function. Without it
                                              #I kept getting an error when the Linked List is empty
                                              #in the main code after all the Nodes are removed

        iterator = self.head
        while iterator.next is not None:
            if iterator.next.data == data:
                iterator.next = iterator.next.next
                break
            else:
                iterator = iterator.next


# Now make following calls,
ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.insert_after_value("mango","apple") # insert apple after mango
ll.print()
ll.remove_by_value("orange") # remove orange from linked list
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()