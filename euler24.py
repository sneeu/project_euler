from itertools import permutations


if __name__ == '__main__':
    perms = permutations(range(10))
    for i in range(1, 10 ** 6):
        perms.next()
    print ''.join([str(n) for n in perms.next()])
