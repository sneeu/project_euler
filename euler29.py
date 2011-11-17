def atob(arange, brange):
    return set([a ** b for a in arange for b in brange])


if __name__ == '__main__':
    print len(atob(xrange(2, 101), xrange(2, 101)))
