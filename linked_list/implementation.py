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
        if index > len(self) - 1:
            raise IndexError
        ans = 0
        for idx, element in enumerate(self):
            if idx == index:
                return element

    def __add__(self, other):
        # copies both lists, joins them together 
        if not self:
            return deepcopy(other)
        else:
            new_list = deepcopy(self)
            other_copy = deepcopy(other)
            new_list.length += other_copy.length
            new_list.end.next = other_copy.start
            new_list.end = other_copy.end
        return new_list

    def __iadd__(self, other):
        # same as the add method, but not copying both lists
        # self = self + other
        # return self
        if not self:
            return deepcopy(other)
        else:
            other_copy = deepcopy(other)
            self.length += other_copy.length
            self.end.next = other_copy.start
            self.end = other_copy.end
            return self

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        return all(i == j for i,j in zip(self,other))
                    
    def __ne__(self, other):
        return not self == other

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
        if len(self) == 0:
            raise IndexError
            
        if index == None:
            index = len(self) - 1
            
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