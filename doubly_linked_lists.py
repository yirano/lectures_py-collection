class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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

    def get_prev(self):
        '''Return the self.prev attribute'''
        return self.prev

    def set_prev(self, new_prev):
        '''Replace the existing value of the self.prev attribute with a new_prev parameter'''
        self.prev = new_prev


'''
python3 -i doubly_linked_lists.py
node1 = DLLNode(1)
node2 = DLLNode(2)
node1.set_prev(node2)
node1.get_prev()
'''
