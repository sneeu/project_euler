def fib(m, n):
    yield m
    yield n
    while True:
        m, n = n, m + n
        yield n


if __name__ == '__main__':
    fibs = fib(1, 1)
    for i, t in enumerate(fib(1, 1)):
        if t > 10 ** 999:
            print t, i
            break
