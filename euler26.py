from decimal import Decimal, getcontext


if __name__ == '__main__':
    getcontext().prec = 2000

    results = []

    for i in xrange(1, 1001):
        s = str(Decimal(1) / Decimal(i))

        while s[0] in ('0', '.'):
            s = s[1:]

        r = s.find(s[:50], 1)

        if r is -1:
            continue

        if r > 100:
            results.append((r, i, s))

    for r, i, s in sorted(results):
        print i, r, s[:r]
