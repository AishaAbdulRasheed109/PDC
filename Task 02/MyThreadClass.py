import time
import os
import random
from threading import Thread

class MyThreadClass(Thread):
    def __init__(self, name, row, A, B, result):
        Thread.__init__(self)
        self.name = name
        self.row = row
        self.A = A
        self.B = B
        self.result = result

    def run(self):
        print(f"---> {self.name} running, process ID {os.getpid()}")
        for j in range(len(self.B[0])):
            total = 0
            for k in range(len(self.B)):
                total += self.A[self.row][k] * self.B[k][j]
            self.result[self.row][j] = total
        print(f"---> {self.name} completed row {self.row}")


def main():
    start_time = time.time()

    N = 3

    A = [[random.randint(0, 10) for _ in range(N)] for _ in range(N)]
    B = [[random.randint(0, 10) for _ in range(N)] for _ in range(N)]
    print(f'Matrix A: {A}')
    print(f'Matrix B : {B}')
    print()

    result = [[0 for _ in range(N)] for _ in range(N)]

    print(f"Matrix size: {N}x{N}")
    print(f"Process ID: {os.getpid()}")
    print("Starting matrix multiplication...\n")

    threads = []
    for i in range(N):
        t = MyThreadClass(f"Thread#{i+1}", i, A, B, result)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()

    print("\nMatrix multiplication complete.")
    print(f"Execution time: {end_time - start_time:.4f} seconds")
    print("\nResult Matrix (A x B):")
    for row in result:
        print(row)

if __name__ == "__main__":
    main()