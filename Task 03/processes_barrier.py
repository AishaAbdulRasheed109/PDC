import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime
import random

N = 3

def multiply_row_with_barrier(row_index, A, B, C, synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    row_result = [sum(A[row_index][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
    C[row_index] = row_result
    with serializer:
        print(f"process {name} ----> {datetime.fromtimestamp(time())} | Computed row {row_index}: {row_result}")

def multiply_row_without_barrier(row_index, A, B, C, serializer):
    name = multiprocessing.current_process().name
    row_result = [sum(A[row_index][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
    C[row_index] = row_result
    with serializer:
        print(f"process {name} ----> {datetime.fromtimestamp(time())} | Computed row {row_index}: {row_result}")

if __name__ == '__main__':
    A = [[random.randint(1, 5) for _ in range(N)] for _ in range(N)]
    B = [[random.randint(1, 5) for _ in range(N)] for _ in range(N)]

    print("Matrix A:")
    for row in A: print(row)
    print("\nMatrix B:")
    for row in B: print(row)

    manager = multiprocessing.Manager()
    C = manager.list([manager.list([0]*N) for _ in range(N)])

    synchronizer = Barrier(2)
    serializer = Lock()

    p1 = Process(name='p1 - with_barrier', target=multiply_row_with_barrier, args=(0, A, B, C, synchronizer, serializer))
    p2 = Process(name='p2 - with_barrier', target=multiply_row_with_barrier, args=(1, A, B, C, synchronizer, serializer))
    p3 = Process(name='p3 - without_barrier', target=multiply_row_without_barrier, args=(2, A, B, C, serializer))

    for p in [p1, p2, p3]:
        p.start()
    for p in [p1, p2, p3]:
        p.join()

    print("\nResultant Matrix C:")
    for row in C: print(list(row))
