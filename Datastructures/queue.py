import time
import sys


class Queue:

    def __init__(self):
        """
        Initializing an empty list
        """
        self.items = []

    def enqueue(self,item):
        """
        Inserting an item in first
        Runtime : O(n) # inserting at 0 index moves other elements to right
        :param item:
        :return: None
        """
        self.items.insert(0,item)

    def dequeue(self):
        """
        Runtime : O(n)
        :return: if list is empty return None
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """
        look at last item in the list.
        Runtime : O(1) # indexing to last item to list
        :return: front most item
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
        Runtime : O(1)
        :return: length of list
        """
        return len(self.items)

    def is_empty(self):
        """
        Runtime : O(1)
        :return: Bool
        """
        return self.items == []


def main():
    my_Queue = Queue()
    my_Queue.enqueue('1')
    my_Queue.enqueue('2')
    print(my_Queue.items)
    my_Queue.dequeue()
    print(my_Queue.items)
    print(my_Queue.peek())
    print(my_Queue.size())
    print(my_Queue.is_empty())

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(" ")
    print("Total Execution Time : {:.2f} sec".format(end - start))
    sys.exit(0)