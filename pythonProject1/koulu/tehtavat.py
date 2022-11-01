def laske_alkiot(matrix: list, element: int):
    k = 0
    for i in matrix:
        for j in i:
            if j == element:
                k += 1
    print(k)



m = [[1, 2, 1],
     [0, 3, 4],
    [0, 3, 4],
[0, 3, 4],
     [1, 0, 0]]

print(laske_alkiot(m, 2))

