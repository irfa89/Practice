def diagonal_sum(given_2d):
    total = 0
    for i in range(len(given_2d)):
        total += given_2d[i][i]

    return total

def main():
    # test cases.

    print("""
    The diagonal sum of [[1, 0],
                         [0, 1]] is: (Should be 2)""")
    diagonal_sum([[1, 0],
                  [0, 1]])

    print("""
    The diagonal sum of [[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]] is: (Should be 15)""")
    diagonal_sum([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

if __name__ == "__main___":
    main()