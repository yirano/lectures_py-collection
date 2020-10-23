class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'SLLNode object: {self.data}'

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


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f'SLL object: {self.head}'

    def is_empty(self):
        '''Returns True is Linked List is empty // False otherwise'''
        # if self.head == None:
        #     return True
        # else:
        #     return False
        return self.head is None

    def add_to_head(self, new_data):
        '''Add a Node whose data is the new_data argument to the front of the linked list'''
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        '''
        Traverses the Linked List and returns an integer value representing the number of nods in the Linked List.
        The time complexity is O(n) because every Node in the Linked List must be visited in order to calculate the size of the Linked List.
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
        Traverses the Linked List and returns True if the data searched for is present in one of the Nodes. Otherwise it returns False

        The time complexity is O(n) because in the worst case we have to go through every Node
        '''
        if self.head is None:
            return "Linked List is empty. No Nodes to search."

        current = self.head
        while current is not None:
            # The Node's data matches what we're looking for
            if current.get_data() == data:
                return True
            # The Node's data doesn't match
            else:
                current = current.get_next()

        return False

    def remove(self, data):
        '''
        Removes the first occurence of a Node that contains the data argument as its self.data variable. Returns nothing.

        The time complexity if O(n) because in the worst case scenario we have to visit every Node before we find the one we need to remove        
        '''
        if self.head is None:
            return "Linked List is empty. No Nodes to remove."

        current = self.head
        prev = None
        found = False
        while not found:
            # If the current node's data is equal to the data being searched, return True and break out of the while loop.
            if current.get_data() == data:
                found = True
            else:
                # If the entire list has been traversed and the next node is 'None', return a message indicating that the node can't be found.
                if current.get_next() == None:
                    return "The Node with that data value is not present."
                else:  # Otherwise, onto the next node. Set the previous node as the current and the current to the next node.
                    prev = current
                    current = current.get_next()

        if prev is None:  # If the previous is None, that means the current node is the head.
            self.head = current.get_next()
        else:
            # Else, set the pointer of the previous node to the current's next node.
            prev.set_next(current.get_next())


'''
node = SLLNode('hello')
node1 = SLLNode('bye')
node.set_next(node1)
node.get_next()
'''
