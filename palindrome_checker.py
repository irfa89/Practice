from Datastructures import deque
import sys
import time

def check_palindrome(input_str):
    d = deque.Deque()
    for char in input_str:
        d.add_rear(char)

    while d.size() >= 2:
        front_item = d.remove_front()
        rear_item = d.remove_rear()

        if front_item != rear_item:
            return False

    return True

def main():

    n = str(input("Enter a string to check palindrome : "))
    print(check_palindrome(n.lower()))

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(" ")
    print("Total Execution Time : {:.2f} sec".format(end - start))
    sys.exit(0)