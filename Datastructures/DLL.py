from Datastructures import DLLNode
import time
import sys

class DLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "DLL Object : head => {}".format(self.head)

    def is_empty(self):
        return self.head is None

    def size(self):
        size = 0
        if self.head is None:
            return size
        current = self.head
        while current is not None:  # while there is node to count
            size += 1
            current = current.get_next()

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

    def add_front(self, new_data):
        temp = DLLNode.DLLNode(new_data)
        temp.set_next(self.head)
        if self.head is not None:
            self.head.set_previous(temp)
        self.head = temp

    def remove(self, data):
    # Case 1 : Empty LL
    # Case 2 : Target Data not found
    # Case 3 : Node to remove is First node
    # Case 4 : Non-First Nodes
        if self.head is None:
            return "linked List is Empty"
        current = self.head
        found = False
        while not found:
            if current.get_data == data:
                found = True
            else:
                if current.get_next() is None :
                    return "Node not found"
                else:
                    current = current.get_next()

        if current.previous is None:
            self.head = current.get_next()
        else:
            current.previous.set_next(current.get_next())
            current.next.set_previous(current.get_previous())


def main():
     dll1 = DLL()
     print(dll1.size())
     print(dll1.remove(1))
     dll1.add_front(1)
     print(dll1.head)
     print(dll1.head.previous)
     print(dll1.head.next)
     dll1.add_front(2)
     dll1.add_front(3)
     dll1.add_front(4)
     dll1.add_front(5)
     print(dll1.head.previous)
     print(dll1.head.next)
     print(dll1.remove(7))
     dll1.remove(2)
     print(dll1.head)

if __name__ == "__main__":

    start = time.time()
    main()
    end = time.time()

    print(" ")
    print("Total Execution Time : {:.2f} sec".format(end - start))
    sys.exit(0)