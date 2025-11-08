import multiprocessing
import time
import random

N = 3 

A = [[random.randint(1, 10) for _ in range(N)] for _ in range(N)]
B = [[random.randint(1, 10) for _ in range(N)] for _ in range(N)]

def myFunc():
    name = multiprocessing.current_process().name
    print(f"Starting process name = {name}\n")

    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]

    print(f"Result in process {name}:")
    for row in result:
        print(row)
    print(f"Exiting process name = {name}\n")
    time.sleep(1)

if __name__ == '__main__':
    process_with_name = multiprocessing.Process(
        name='Matrix Multiplication process',
        target=myFunc
    )

    process_with_default_name = multiprocessing.Process(
        target=myFunc
    )

    process_with_name.start()
    process_with_default_name.start()

    process_with_name.join()
    process_with_default_name.join()
