def is_palindrome(s):
    return s == ''.join(reversed(s))


def main():
    r = [i for i in range(1, 1000000, 2) if is_palindrome(str(i)) and is_palindrome(bin(i)[2:])]
    print sum(r)


if __name__ == '__main__':
    main()
