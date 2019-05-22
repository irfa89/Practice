def pair10(given_list):
    numbers = {}
    for item in given_list:
        if (10 - item) in numbers:
            print(str(10-item)+'-'+ str(item))
        else:
            numbers[item] = 1
    print("There is no pair that adds up to 10.")

def main():
    # Test cases
    print("""
    Which pair adds up to 10? (Should print 1, 9)

    [3, 4, 1, 2, 9]
    """)

    print(pair10([3, 4, 1, 2, 9]))

    print("""
    Which pair adds up to 10? (Should print -20, 30)

    [-11, -20, 2, 4, 30]
    """)

    print(pair10([-11, -20, 2, 4, 30]))

if __name__ == "__main__" :
    main()

