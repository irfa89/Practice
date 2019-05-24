from Datastructures import stack
import time
import sys

def match_symbols(symbol_str):

    symbol_pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    openers = symbol_pairs.keys()
    my_stack = stack.Stack()

    index = 0
    while index < len(symbol_str):
        symbol = symbol_str[index]

        if symbol in openers:
            my_stack.push(symbol)
        else:  # The symbol is a closer

            # If the Stack is already empty, the symbols are not balanced
            if my_stack.is_empty():
                return False

            # If there are still items in the Stack, check for a mis-match.
            else:
                top_item = my_stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False

        index += 1

    if my_stack.is_empty():
        return True
    return False  # Stack is not empty so symbols were not balanced

def main(): # Test cases

    print(match_symbols('({[]})'))
    print(match_symbols('({[})'))
    print(match_symbols('([{}])'))
    print(match_symbols('(([{}]])'))

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(" ")
    print("Total Execution Time : {:.2f} sec".format(end - start))
    sys.exit(0)