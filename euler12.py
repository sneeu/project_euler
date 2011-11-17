import math


def divisors(n):
    r = []
    for i in xrange(1, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            r.append(i)
    return len(r) * 2


for i in xrange(1, 50000):
    n = sum(xrange(1, i))
    if divisors(n) > 500:
        print n
        break
