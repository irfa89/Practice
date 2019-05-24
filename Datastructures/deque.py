import time
import sys

class Deque:

    def __init__(self):
        self.items = []

    def add_front(self,item):
        self.items.insert(0,item)

    def add_rear(self,item):
        self.items.append(item)

    def remove_front(self):
        if self.items:
            return self.items.pop(0)
        else:
            return None

    def remove_rear(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek_front(self):
        if self.items:
            return self.items[0]
        return None


    def peek_rear(self):
        if self.items:
            return self.items[-1]
        return None


    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


def main():
    d = Deque()
    d.add_front('1')
    d.add_front('2')
    print(d.items)
    d.add_rear('3')
    d.add_rear('4')
    print(d.items)
    d.remove_front()
    d.remove_rear()
    print(d.items)
    print(d.peek_front())
    print(d.peek_rear())
    print(d.is_empty())
    print(d.size())

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(" ")
    print("Total Execution Time : {:.2f} sec".format(end - start))
    sys.exit(0)

