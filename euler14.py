def collatz(n):
    if n == 1:
        return []

    if n % 2 == 0:
        n = n / 2
        return [n] + collatz(n)
    n = n * 3 + 1
    return [n] + collatz(n)
    


win = 0
winner = 1
for i in xrange(500000, 1000000):
    c = len(collatz(i))
    if c > win:
        win = c
        winner = i
    if i % 1000 == 0:
        print i / 1000, winner, win

print winner, collatz(winner)
