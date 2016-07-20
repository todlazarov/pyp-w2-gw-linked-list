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
        if self is None and other is None:
            return True
        try:
            if self.elem == other.elem:
                return True
        except:
            return False

    def __ne__(self,other):
        return not (self == other)

    def __repr__(self):
        pass