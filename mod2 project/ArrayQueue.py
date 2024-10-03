import numpy as np
from Interfaces import Queue


class ArrayQueue(Queue):
    def __init__(self):
        self.n = 0
        self.j = 0
        self.a = np.zeros(self.n, dtype=object)

    def resize(self):
        """
        helper method; creates a new array that maintains the
        array size invariant and copies the old values making sure to maintain FIFO order.
        """
        new_capacity = 2 * len(self.array)  # double the current size
        new_array = [None] * new_capacity
        for i in range(len(self.array)):
            new_array[i] = self.array[(self.front + i) % len(self.array)]
        self.array = new_array
        self.front = 0

    def add(self, x: object):
        """
        adds the given element to the tail of the FIFO queue
        :param x; object type; the element that will be added to the queue
        :return bool type; returns True if the element was successfully added
        """
        if len(self.array) == self.n:  # If the array is full
            self.resize()  # Resize the array

        self.array[(self.front + self.n) % len(self.array)] = x  # Add the new element
        self.n += 1  # Increase the count of elements
        return True
    
    def remove(self) -> object:
        """
        removes the element at the head of the FIFO queue
        :return object type; returns the element that was removed
        """
        if self.n == 0:
            raise IndexError('remove from empty queue')
        
        x = self.array[self.front]
        self.array[self.front] = None  # Optional: Help garbage collector
        self.front = (self.front + 1) % len(self.array)
        self.n -= 1
        if len(self.array) >= 3 * self.n:
            self.resize()
        return x

    def size(self):
        """
        gets the current number of elements in the queue
        :return: int type; the number of elements in the queue
        """
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        """
        makes this ArrayQueue an iterable object
        """
        self.iterator = 0
        return self

    def __next__(self):
        """
        returns the next item in the sequence when iterating over the
        ArrayQueue
        """
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return x
