names = open('sorted_names.txt').readlines()
position = 1

score = 0

for n in names:
    for c in n.strip():
        score += (ord(c) - 64) * position
    position += 1


print score