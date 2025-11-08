import multiprocessing
import time
import random

def Matrix_Multiplication():
    name = multiprocessing.current_process().name
    print("Starting %s \n" % name)

    n = 4
    A = [[random.randint(1, 5) for _ in range(n)] for _ in range(n)]
    B = [[random.randint(1, 5) for _ in range(n)] for _ in range(n)]
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

        if name != 'background_process':
            print(f'---> Row {i}: {result[i]}')

    time.sleep(1)
    print("\nExiting %s \n" % name)


    print(f"Final Result from {name}:")
    for row in result:
        print(row)


if __name__ == '__main__':
    background_process = multiprocessing.Process(
        name='background_process',
        target=Matrix_Multiplication
    )
    background_process.daemon = True

    NO_background_process = multiprocessing.Process(
        name='NO_background_process',
        target=Matrix_Multiplication
    )
    NO_background_process.daemon = False

    background_process.start()
    NO_background_process.start()

    NO_background_process.join()
