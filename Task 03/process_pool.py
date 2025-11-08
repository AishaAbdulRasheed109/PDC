import multiprocessing
import random

def compute_row(args):
    row_index, A_row, B = args
    result_row = []
    for j in range(len(B[0])):
        sum = 0
        for k in range(len(B)):
            sum += A_row[k] * B[k][j]
        result_row.append(sum)
    return (row_index, result_row)

if __name__ == '__main__':
    N = 3

    A = [[random.randint(0, 9) for _ in range(N)] for _ in range(N)]
    B = [[random.randint(0, 9) for _ in range(N)] for _ in range(N)]

    print("Matrix A:")
    for row in A:
        print(row)

    print("\nMatrix B:")
    for row in B:
        print(row)

    args = [(i, A[i], B) for i in range(len(A))]

    pool = multiprocessing.Pool(processes=3)

    pool_results = pool.map(compute_row, args)

    pool.close()
    pool.join()


    pool_results.sort(key=lambda x: x[0])
    result_matrix = [row for index, row in pool_results]

    print("\nResultant Matrix (A x B):")
    for row in result_matrix:
        print(row)
