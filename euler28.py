def spiral(m):
    n = 1
    incr = 2
    for i in range(0, m):
        for i in range(0, 4):
            n += incr
            yield n
        incr += 2


if __name__ == '__main__':
    print sum([1] + [n for n in spiral(500)])
