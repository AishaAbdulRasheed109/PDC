from threading import Thread
from queue import Queue
import time
import random

class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(5):  # produce 5 matrix pairs
            size = 3
            A = [[random.randint(1, 9) for _ in range(size)] for _ in range(size)]
            B = [[random.randint(1, 9) for _ in range(size)] for _ in range(size)]
            print("Matrix A:")
            for row in A:
                print(row)
            print("\nMatrix B:")
            for row in B:
                print(row)
            self.queue.put((A, B))
            print('Producer notify : Matrix pair %d appended to queue by %s\n' % (i + 1, self.name))
            time.sleep(1)

class Consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def multiply_matrices(self, A, B):
        rows_A, cols_A = len(A), len(A[0])
        rows_B, cols_B = len(B), len(B[0])
        result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += A[i][k] * B[k][j]
        return result

    def run(self):
        while True:
            try:
                A, B = self.queue.get(timeout=5)
            except:
                break 
            print('Consumer notify : Matrix pair popped from queue by %s' % self.name)
            result = self.multiply_matrices(A, B)
            print('Result computed by %s:\n%s\n' % (self.name, result))
            self.queue.task_done()

if __name__ == '__main__':
    queue = Queue()

    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)

    start_time = time.time()

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print(f"Total execution time: {time.time() - start_time:.2f} seconds")
