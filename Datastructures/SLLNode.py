import time
import sys

class SLLNode:

    def __init__(self,data):
        self.data = data
        self.next = None

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


def main():
     node = SLLNode('1')
     print(node.get_data())
     node.set_data('7')
     print(node.get_data())
     node2 = SLLNode('2')
     node.set_next(node2)
     print(node.get_next())

if __name__ == "__main__":

    start = time.time()
    main()
    end = time.time()

    print(" ")
    print("Total Execution Time : {:.2f} sec".format(end - start))
    sys.exit(0)