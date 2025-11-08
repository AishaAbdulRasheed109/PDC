import threading
import time
import os
from threading import Thread
import random

threadLock = threading.Lock()

N = 3

A = [[random.randint(0, 1000000) for _ in range(N)] for _ in range(N)]
B = [[random.randint(0, 1000000) for _ in range(N)] for _ in range(N)]
print(f'Matrix A: {A}')
print(f'Matrix B : {B}')
print()
result = [[0 for _ in range(N)] for _ in range(N)]

class MyThreadClass(Thread):
    def __init__(self, row):
        Thread.__init__(self)
        self.row = row

    def run(self):
        threadLock.acquire()
        print(f"---> Thread for row {self.row} running, belonging to process ID {os.getpid()}\n")
        for j in range(N):
            total = 0
            for k in range(N):
                total += A[self.row][k] * B[k][j]
            result[self.row][j] = total
        threadLock.release()

        threadLock.acquire()
        print(f"---> Thread for row {self.row} finished. Result Row: {result[self.row]}\n")
        threadLock.release()

def main():
    start_time = time.time()

    threads = []

    for i in range(N):
        thread = MyThreadClass(i)
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()

    print("Final Resultant Matrix (A x B):")
    for row in result:
        print(row)

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()