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
        pass

    def search(self, data):
        pass

    def remove(self, data):
        pass


'''
node = SLLNode('hello')
node1 = SLLNode('bye')
node.set_next(node1)
node.get_next()
'''
