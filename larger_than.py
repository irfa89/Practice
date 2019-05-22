
def larger_than(a,b):
    if len(a) > len(b):
        return True
    elif len(a) < len(b):
        return False

    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        elif a[i] > b[i]:
            return True
        else:
            return False

    return False


def main():
    # Test Cases
    print('Is "112" larger than "111"? (Should be True.)')
    print(larger_than("112", "111"))

    print('Is "525" larger than "1111"? (Should be False.)')
    print(larger_than("525", "1111"))

    print('Is "11" larger than "0"? (Should be True.)')
    print(larger_than("11", "0"))

    print('Is "1" larger than "1"? (Should be False.)')
    print(larger_than("1", "1"))

if __name__ == "__main__":
    main()