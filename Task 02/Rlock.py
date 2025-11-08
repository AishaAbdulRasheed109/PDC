import threading
import random
import time

class Box:
    def __init__(self, size):
        self.lock = threading.RLock()
        self.size = size
        self.A = [[random.randint(1, 1000) for _ in range(size)] for _ in range(size)]
        self.B = [[random.randint(1, 1000) for _ in range(size)] for _ in range(size)]
        self.result = [[0 for _ in range(size)] for _ in range(size)]

    def multiply_row(self, row):
        with self.lock:
            print(f"Thread {threading.current_thread().name} started row {row}")
            for j in range(self.size):
                for k in range(self.size):
                    self.result[row][j] += self.A[row][k] * self.B[k][j]
            time.sleep(0.5)
            print(f"Thread {threading.current_thread().name} finished row {row}")

    def multiply(self):
        threads = []
        for i in range(self.size):
            t = threading.Thread(target=self.multiply_row, args=(i,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

def main():
    start_time = time.time()
    size = 3
    box = Box(size)

    print("Matrix A:")
    for row in box.A:
        print(row)
    print("\nMatrix B:")
    for row in box.B:
        print(row)

    box.multiply()

    print("\nResult Matrix (A × B):")
    for row in box.result:
        print(row)

    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nTotal Execution Time: {total_time:.4f} seconds")

if __name__ == "__main__":
    main()
