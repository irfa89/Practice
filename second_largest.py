# Input:
#  a: The given list/array of integers.  Example: [1, -2, 3, 4]
# Returns:
#  The second largest number in the list or None if
#  the array's length is only 1 or 2.
def second_largest(given_list):
    largest = None
    second_largest =  None

    for current_number in given_list:
        if largest == None :
            largest = current_number
        elif current_number > largest :
            second_largest = largest
            largest = current_number
        elif second_largest == None :
            second_largest = current_number
        elif current_number > second_largest :
            second_largest = current_number
    return second_largest

def main():
    # Test Cases
    print('The second largest number in [1, 3, 4, 5, 0, 2] is (should be 4):')
    print(second_largest([1, 3, 4, 5, 0, 2]))

    print('The second largest number in [-2, -1] is: (should be -2)')
    print(second_largest([-2, -1]))

    print('The second largest number in [2, 2, 1] is: (should be 2)')
    print(second_largest([2, 2, 1]))

    print('The second largest number in [2] is: (should be None)')
    print(second_largest([2]))

    print('The second largest number in [] is: (should be None)')
    print(second_largest([]))

if __name__ == "__main__":
    main()