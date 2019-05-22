import time
import sys

"""
Real world Examples
1. linter in your text editor which is able to tell you if you're missing an opening or closing symbol
2. Reversing a character in a string
* recursive data structure
"""

class Stack:

    def __init__(self):
        """
        Initializes a list as stack
        Top : Right
        Bottom : Left
        """
        self.items = []

    def push(self,item):
        """
        Runtime : O(1)
        :param item:
        :return: None
        """
        self.items.append(item)

    def pop(self):
        """
        Removes the last item from list
        Runtime : O(1)
        :return: last item
        """
        if self.items:
            return self.items.pop()

    def peek(self): # check stack content
        pass

    def size(self):
        pass

    def is_empty(self):
        pass

def main():
    stack_1 = Stack()
    stack_1.push("orange")
    stack_1.push("apple")
    print(stack_1.items)
    stack_1.pop()
    print(stack_1.items)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(" ")
    print("Total Execution Time : {:.2f} sec".format(end - start))
    sys.exit(0)
