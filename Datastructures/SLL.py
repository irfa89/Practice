from Datastructures import SLLNode
import time
import sys

class SLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "SLL Object - head = {}".format(self.head)

    def is_empty(self):
        return self.head is None

    def add_front(self, new_data):
        temp = SLLNode.SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """
        Runtime : O(n)
        :return: number of nodes in Linked List
        """
        size = 0
        if self.head is None:
            return size
        current = self.head
        while current is not None: # while there is node to count
            size += 1
            current = current.get_next()

        return size


    def search(self,data):
        """
        Runtime : O(n)
        :param data:
        :return: Bool
        """
        if self.head is None :
            return "No nodes"
        current = self.head
        while current is not None:
        # Node data matches
        # Node does not match
            if current.get_data() == data :
                return True
            else:
                current = current.get_next()
        return False

    def remove(self,data):
    # Case 1 : Empty LL
    # Case 2 : Target Data not found
    # Case 3 : Node to remove is First node
    # Case 4 : Non-First Nodes
        if self.head is None:
            return "linked List is Empty"
        current =self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next == None:
                    return "Node not found"
                else:
                    previous = current
                    current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())






def main():
    sll = SLL()
    print(sll.size())
    print(sll.remove(14))
    print(sll.is_empty())
    node = SLLNode.SLLNode(5)
    sll.head = node
    print(sll.is_empty())
    sll_add = SLL()
    print(sll_add.head)
    sll_add.add_front(1)
    sll_add.add_front(2)
    sll_add.add_front(3)
    print(sll_add.head)
    print(sll_add.size())
    print(sll_add.search(2))
    print(sll_add.search(0))
    print(sll_add.remove(1))

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()

    print(" ")
    print("Total Execution Time : {:.2f} sec".format(end - start))
    sys.exit(0)