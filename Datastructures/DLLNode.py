import time
import sys

class DLLNode:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return "Node data : {}".format(self.data)

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self,new_next):
        self.next = new_next

    def get_previous(self):
        return self.previous

    def set_previous(self, new_previous):
        self.previous = new_previous


def main():
     node1 = DLLNode(1)
     node2 = DLLNode(2)
     print(node1.get_previous())
     node1.set_previous(node2)
     print(node1.get_previous())

if __name__ == "__main__":

    start = time.time()
    main()
    end = time.time()

    print(" ")
    print("Total Execution Time : {:.2f} sec".format(end - start))
    sys.exit(0)