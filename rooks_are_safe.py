def rooks_are_safe(chessboard):
    n = len(chessboard)
    for row_i in range(n):
        row_count = 0
        for col_i in range(n):
            row_count += chessboard[row_i][col_i]
        if row_count > 1:
            return False
        
        for col_i in range(n):
            col_count = 0
            for row_i in range(n):
                col_count += chessboard[row_i][col_i]
            if col_i > 1:
                return False
        return True
    return True

def main():
    # test cases
    print("""
    Are rooks safe in this board? (Should be True.)
    [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 1],
     [0, 0, 0, 0]]
    """)

    rooks_are_safe(
        [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 1],
         [0, 0, 0, 0]])

    print("""
    Are rooks safe in this board? (Should be True.)
    [[1]]
    """)

    rooks_are_safe([[1]])

    print("""
    Are rooks safe in this board? (Should be False.)
    [[1, 0],
     [1, 0]]
    """)

    rooks_are_safe(
        [[1, 0],
         [1, 0]])

    print("""
    Are rooks safe in this board? (Should be False.)
    [[0, 0, 0],
     [1, 0, 1],
     [0, 0, 0]]
    """)

    rooks_are_safe(
        [[0, 0, 0],
         [1, 0, 1],
         [0, 0, 0]])

if __name__ == "__main__":
    main()