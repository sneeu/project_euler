import datetime


def date_range(start, end, delta=None):
    if delta is None:
        delta = datetime.timedelta(days=1)

    while True:
        if start > end:
            raise StopIteration

        yield start
        start = start + delta


def main():
    start = datetime.date(1901, 1, 1)
    end = datetime.date(2000, 12, 31)
    delta = datetime.timedelta(days=7)

    print sum([1 for d in date_range(start, end, delta) if d.day == 1])


if __name__ == '__main__':
    main()
