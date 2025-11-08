import multiprocessing
import random

def Matrix_Multiplication(A, B, result):
    name = multiprocessing.current_process().name
    N = len(A)
    P = len(B[0])

    if name == 'background_process':
        start_row = 0
        end_row = N // 2
    else:
        start_row = N // 2
        end_row = N

    print(f"Starting {name} computing rows {start_row} to {end_row - 1}")

    for i in range(start_row, end_row):
        for j in range(P):
            sum_val = 0
            for k in range(len(B)):
                sum_val += A[i][k] * B[k][j]
            result[i][j] = sum_val

    print(f"Exiting {name}")

if __name__ == '__main__':
    N= 4
    A = [[random.randint(1,5) for _ in range(N)] for _ in range(N)]
    B = [[random.randint(1,5) for _ in range(N)] for _ in range(N)]

    manager = multiprocessing.Manager()
    result = manager.list([manager.list([0]*N) for _ in range(N)])

    print("Matrix A:")
    for row in A:
        print(row)
    print("Matrix B:")
    for row in B:
        print(row)

    background_process = multiprocessing.Process(
        name='background_process', target=Matrix_Multiplication, args=(A, B, result))
    background_process.daemon = False
    NO_background_process = multiprocessing.Process(
        name='NO_background_process', target=Matrix_Multiplication, args=(A, B, result))
    NO_background_process.daemon = False

    background_process.start()
    NO_background_process.start()

    background_process.join()
    NO_background_process.join()

    print("Resultant Matrix:")
    for row in result:
        print(list(row))