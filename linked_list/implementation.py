from .interface import AbstractLinkedList
from .node import Node
from copy import deepcopy

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.length = 0
        self.end = None
        self.current = None
        if elements:
            for element in elements:
                self.append(element)
                
    def __str__(self):
        ans = "["
        for elem in self:
            ans += str(elem) + ", "
        ans += "]"
        return ans.replace(', ]',']')

    def __len__(self):
        return self.length

    def __iter__(self):
        self.current = self.start
        return self

    def __getitem__(self, index):
        ans = 0
        for idx, element in enumerate(self):
            if idx == index:
                return element

    def __add__(self, other):
        if not self:
            return deepcopy(other)
        else:
            self_copy = deepcopy(self)
            other_copy = deepcopy(other)
            self_copy.length += other_copy.length
            self_copy.end.next = other_copy.start
            self_copy.end = other_copy.end
        return self_copy

    def __iadd__(self, other):
        self = self + deepcopy(other)
        return self

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i,j in zip(self,other):
            if i != j:
                return False
        return True
            
    def __ne__(self, other):
        return not (self.__eq__(other))

    def append(self, elem):
        self.length += 1
        if not self.start:
            tmp = Node(elem)
            self.start, self.end, self.current = [tmp] * 3
        else:
            tmp = self.end
            tmp.next = Node(elem)
            self.end = tmp.next

    def count(self):
        return len(self)

    def pop(self, index=None):
        if index == None:
            index = len(self) - 1
        if index > len(self) - 1 or index < 0:
            raise IndexError
            
        ans = self[index].elem
        if index == 0:
            self.start = self.start.next
            self.current = self.start
        else:
            self[index-1].next = self[index].next
            
        self.length -= 1
        return ans
    
    def next(self):
        ans = self.current
        if not ans:
            raise StopIteration
        self.current = self.current.next
        return ans
    
    __next__ = next