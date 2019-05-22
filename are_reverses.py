

def are_reverses(string_1, string_2):
    for i in range(len(string_1)):
        if string_1[i] != string_2[(len(string_2)-i-1)] :
            return False
    return True


def main():
    # Test Cases
    print('Are "ABC" and "CBA" reverses of each other? (Should be True.)')
    print(are_reverses("ABC", "CBA"))

    print('Are "CBA" and "AAA" reverses of each other? (Should be False.)')
    print(are_reverses("CBA", "AAA"))


if __name__ == "__main__":
    main()