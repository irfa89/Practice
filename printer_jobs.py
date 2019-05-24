from Datastructures import queue
import time
import sys
import random

"""
Real world example of Queueue : Printing Jobs
"""

class PrintQueue(queue.Queue):

    def __init__(self):
        queue.Queue.__init__(self)

class Job:

    def __init__(self):
        self.pages = random.randint(1,11)

    def print_page(self):
        if self.pages > 0 :
            self.pages -= 1

    def check_complete(self):
        if self.pages == 0 :
            return True
        return False

class Printer:

    def __init__(self):
        self.current_job = None

    def get_job(self, print_queue):
        try:
            self.current_job = print_queue.dequeue()
        except IndexError:
            return "NO JOBS TO PRINT"

    def print_job(self,job):
        while job.pages > 0 :
            job.print_page()

        if job.check_complete():
            return "printing complete"
        else:
            return "ERROR"

def main():
    job1 = Job()
    print_q = PrintQueue()
    printer = Printer()

    print_q.enqueue(job1)
    printer.get_job(print_q)
    print(print_q.items)

    printer.print_job(printer.current_job)
    print(printer.print_job(printer.current_job))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(" ")
    print("Total Execution Time : {:.2f} sec".format(end - start))
    sys.exit(0)

