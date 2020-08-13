class Node:
    def __init__(self, value, next_node=None):
        #The value that the node is holding
        self.value = value
        #Reference to the next node in the linked list
        self.next_node = next_node

    #method to get the value of the node
    def get_value(self):
        return self.value

    #method to get next node
    def get_next(self):
        return self.next_node

    #method to update the node's 'next_node' to the input node
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None
        
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        else:
            val = self.tail.get_value()
            current = self.head

            while current.get_next() != self.tail:
                current = current.get_next()

            self.tail = current
            self.tail.set_next(None)
            return val

    def remove_head(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            val = self.head.get_value()
            self.head = self.head.get_next()
            return val



# ll = LinkedList()
# ll.add_to_tail(5)

# ll.set_next(Node(7))
# ll.next_node.set_next(Node(18))
# ll.next_node.next_node.set_next(Node(22))
# ll.next_node.next_node.next_node.set_next(Node(3))
