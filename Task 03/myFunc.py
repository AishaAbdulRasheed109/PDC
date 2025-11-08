def myFunc(i):
    print('Calling myFunc from process n°: %s' % i)

    A = [[j + 1 for j in range(i)] for _ in range(i)]
    B = [[j + 1 for j in range(i)] for _ in range(i)]

    C = [[0 for _ in range(i)] for _ in range(i)]

    for row in range(i):
        for col in range(i):
            for k in range(i):
                C[row][col] += A[row][k] * B[k][col]
            print('Output C[%s][%s] = %s' % (row, col, C[row][col]))
    
    print('Finished myFunc for process n°: %s' % i)
    return C