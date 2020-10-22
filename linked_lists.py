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


'''
node = SLLNode('hello')
node1 = SLLNode('bye')
node.set_next(node1)
node.get_next()
'''
