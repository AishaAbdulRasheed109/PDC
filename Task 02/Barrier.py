from random import randint, randrange
from threading import Barrier, Thread
from time import sleep, ctime

# Matrix size
N = 3

# Barrier for all threads (each for one row)
result = Barrier(N)

# Random matrices A and B
A = [[randint(0, 500000) for _ in range(N)] for _ in range(N)]
B = [[randint(0, 500000) for _ in range(N)] for _ in range(N)]
C = [[0 for _ in range(N)] for _ in range(N)]

def multiply_row(row):
    sleep(randrange(1, 4))  # simulate work time
    for j in range(N):
        for k in range(N):
            C[row][j] += A[row][k] * B[k][j]
    print(f"Thread-{row+1} finished row {row} at: {ctime()}")
    result.wait()  # wait for others at the barrier

def main():
    print("Matrix A:")
    for r in A:
        print(r)
    print("\nMatrix B:")
    for r in B:
        print(r)

    print("\nSTART MULTIPLICATION!\n")

    threads = []
    for i in range(N):
        t = Thread(target=multiply_row, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nAll threads reached the barrier — multiplication complete!\n")
    print("Result Matrix C:")
    for r in C:
        print(r)

if __name__ == "__main__":
    main()
