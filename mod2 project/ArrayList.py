import numpy as np
from Interfaces import List


class ArrayList(List):
    """
    ArrayList: Implementation of a List interface using Arrays.
    """

    def __init__(self):
        """
        constructor creates an empty ArrayList object
        """
        self.n = 0
        self.j = 0
        self.a = np.zeros(self.n, object)

    def resize(self):
        """
        helper method; creates a new array that maintains the
        array size invariant and copies the old values.
        """
        new_capacity = 2 * len(self.array)  
        new_array = [None] * new_capacity
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array

    def get(self, i: int) -> object:
        """
        returns the element at position i
        :param i: int type; integer index of the element to access
        :raise IndexError: raises IndexError if i is negative or greater than or
        equal to the number of existing elements
        """
        if i < 0 or i >= len(self.array):
            raise IndexError('Index out of bounds')
        return self.array[i]

    def set(self, i: int, x: object) -> object:
        """
        sets the value at index i to be x.
        :param i: int type; index of the element that will be replaced
        :param x: object type; i.e., any object
        :raise IndexError: raises IndexError if i is negative or greater than or
        equal to the number of existing elements
        :return object; returns the element that was replaced at index i
        """
        if i < 0 or i >= len(self.array):
            raise IndexError('Index out of bounds')
        
        old_value = self.array[i]
        self.array[i] = x
        return old_value

    def append(self, x: object):
        """
        adds a new element to the end of this list
        :param x: Object type; the new element to add
        :return: None
        """
        self.add(self.n, x)

    def add(self, i: int, x: object):
        """
        inserts a new element x at the given index i by shifting elements
        left or right depending on whether the new element is being inserted to
        the first-half or the second-half of the list.
        :param i: int type; index of the position where new element will be inserted
        :param x: object type; i.e., any object
        :raise IndexError: raises IndexError if i is negative or greater than or
        equal to the number of existing elements
        """
        if i < 0 or i > len(self.array):
                raise IndexError('Index out of bounds')
            
            self.array = self.array[:i] + [x] + self.array[i:]

    def remove(self, i: int) -> object:
        """
        removes the element at index i by shifting elements
        left or right depending on whether the element to be removed is in
        the first-half or the second-half of the array.
        returns the removed element
        :param i: int type; the index of the element to be removed
        :return: Object type; the element at index i
        :raise IndexError: raises IndexError if i is negative or greater than or
        equal to the number of existing elements
        """
        if i < 0 or i >= len(self.array):
            raise IndexError('Index out of bounds')
        
        removed_element = self.array[i]
        self.array = self.array[:i] + self.array[i+1:]
        return removed_element
   
    def size(self) -> int:
        """
        returns the size of this list
        :return: int type; the number of elements in this list
        """
        return self.n

    def __str__(self):
        """
        returns the contents of this ArrayList in a string
        :return: str type;
        """
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        """
        makes this ArrayList an iterable object
        """
        self.iterator = 0
        return self

    def __next__(self):
        """
        returns the next item in the sequence when iterating over the
        ArrayList
        """
        if self.iterator < self.n:
            x = self.a[(self.iterator + self.j) % len(self.a)]
            self.iterator += 1
        else:
            raise StopIteration()
        return x
