class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        return str(self.elem)

    def __eq__(self, other):
        if other is None:
            return False
        if type(self) is not type(other):
            return False
        if type(self.elem) is not type(other.elem):
            return False
            
        return self.elem == other.elem

    def __ne__(self,other):
        return not (self == other)

    def __repr__(self):
        return str(self.elem)