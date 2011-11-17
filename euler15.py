def pascals_triangle(n):
    x = [[1]]
    for i in range(n - 1):
        x.append(list(map(sum, zip([0] + x[-1], x[-1] + [0]))))
    return x


print max(pascals_triangle(41)[-1])
