def pascal_triangle(n):
    """Returns a list of lists of integers representing the
    Pascal’s triangle of n"""
    if n <= 0:
        return []
    t = [[1]]
    for i in range (1, n):
        t.append([1])
        for j in range(1, i):
            t[i].append(t[i-1][j-1] + t[i-1][j])
        t[i].append(1)
    return t
