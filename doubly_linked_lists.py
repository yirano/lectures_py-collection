class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'DLLNode object: {self.data}'

    def get_data(self):
        """Return the self.data attribute"""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribute with new_data parameter"""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute"""
        return self.next

    def set_next(self, new_next):
        '''Set the next pointer'''
        self.next = new_next

    def get_prev(self):
        '''Return the self.prev attribute'''
        return self.prev

    def set_prev(self, new_prev):
        '''Replace the existing value of the self.prev attribute with a new_prev parameter'''
        self.prev = new_prev


class DLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f'DLL object: {self.head}'

    def is_empty(self):
        return self.head is None

    def size(self):
        '''
        Traverses the Doubly Linked List and returns an integer value representing the number of nods in the Doubly Linked List.
        The time complexity is O(n) because every Node in the Doubly Linked List must be visited in order to calculate the size of the Doubly Linked List.
        '''
        size = 0
        if self.head is None:
            return 0

        current = self.head
        while current is not None:  # While there are still Nodes left to count
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        '''
        Traverses the Doubly Linked List and returns True if the data searched for is present in one of the Nodes. Otherwise it returns False

        The time complexity is O(n) because in the worst case we have to go through every Node
        '''
        if self.head is None:
            return "Doubly Linked List is empty. No Nodes to search."

        current = self.head
        while current is not None:
            # The Node's data matches what we're looking for
            if current.get_data() == data:
                return True
            # The Node's data doesn't match
            else:
                current = current.get_next()

        return False

    def add_to_head(self, data):
        '''Add a Node whose data is the data argument to the front of the doubly linked list'''
        temp = DLLNode(data)
        temp.set_next(self.head)

        if self.head is not None:
            self.head.set_prev(temp)

        self.head = temp

    def remove(self, data):
        '''
        Removes the first occurence of a Node that contains the data argument as its self.data attribute. Returns nothing.

        The time complexity is O(n) because in the worst case, we have to traverse through the entire linked list"
        '''
        if self.head is None:
            return "Linked List is empty. No Nodes to remove."

        current = self.head
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "A Node with that data value is not present."
                else:
                    current = current.get_next()

        if current.prev is None:
            self.head = current.get_next()
        else:
            current.prev.set_next(current.get_next())
            current.next.set_prev(current.get_prev())


'''
python3 -i doubly_linked_lists.py
node1 = DLLNode(1)
node2 = DLLNode(2)
node1.set_prev(node2)
node1.get_prev()
'''
