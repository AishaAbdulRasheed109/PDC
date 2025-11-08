import multiprocessing
import time
import random

N = 3

def multiply_matrices(A, B):
    print("Starting matrix multiplication...")
    result = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
            print(f"result[{i}][{j}] = {result[i][j]}")
            time.sleep(0.5)
    print("Finished matrix multiplication")
    print("Result:")
    for row in result:
        print(row)

if __name__ == '__main__':
    A = [[random.randint(1, 10) for _ in range(N)] for _ in range(N)]
    B = [[random.randint(1, 10) for _ in range(N)] for _ in range(N)]

    print("Matrix A:")
    for row in A:
        print(row)

    print("Matrix B:")
    for row in B:
        print(row)

    print("\nProcess 01 started the multiplication: ")
    p1 = multiprocessing.Process(target=multiply_matrices, args=(A, B))
    print('Process before execution:', p1, p1.is_alive())
    p1.start()
    print('Process running:', p1, p1.is_alive())
    p1.join()
    print('Process joined:', p1, p1.is_alive())
    print('Process exit code:', p1.exitcode)

    print("\nProcess 02 started the multiplication: ")
    p2 = multiprocessing.Process(target=multiply_matrices, args=(A, B))
    print('Process before execution:', p2, p2.is_alive())
    p2.start()
    print('Process running:', p2, p2.is_alive())
    time.sleep(2)
    print("Terminating Process 2...")
    p2.terminate()
    p2.join()
    print('Process joined:', p2, p2.is_alive())
    print('Process exit code:', p2.exitcode)