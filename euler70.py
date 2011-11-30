def sieve(m):
    # Create a candidate list within which non-primes will be
    # marked as None; only candidates below sqrt(m) need be checked.
    candidates = range(m+1)
    fin = int(m**0.5)

    # Loop over the candidates, marking out each multiple.
    for i in xrange(2, fin+1):
        if not candidates[i]:
            continue

        candidates[2*i::i] = [None] * (m // i - 1)

    # Filter out non-primes and return the list.
    return [i for i in candidates[2:] if i]


def phi(n, primes):
    return [p for p in primes if p < n]


def main():
    pass


if __name__ == '__main__':
    main()
