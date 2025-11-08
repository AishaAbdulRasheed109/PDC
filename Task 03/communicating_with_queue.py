import multiprocessing
import random
import time

class producer(multiprocessing.Process):
    def __init__(self, queue, A, B):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.A = A
        self.B = B

    def run(self):
        for i, row in enumerate(self.A):
            result_row = []
            for j in range(len(self.B[0])):
                sum_ = 0
                for k in range(len(self.B)):
                    sum_ += row[k] * self.B[k][j]
                result_row.append(sum_)
            self.queue.put((i, result_row))
            print("Process Producer: Row %d computed by %s" % (i, self.name))
            time.sleep(1)
            print("The size of queue is %s" % self.queue.qsize())
        self.queue.put(None)

class consumer(multiprocessing.Process):
    def __init__(self, queue, N):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.N = N
        self.result = [None] * N

    def run(self):
        while True:
            if self.queue.empty():
                time.sleep(0.5)
                continue
            item = self.queue.get()
            if item is None:
                break
            i, row = item
            self.result[i] = row
            print("Process Consumer: Row %d received by %s" % (i, self.name))
            time.sleep(1)
        
        print("\nResultant Matrix C:")
        for row in self.result:
            print(row)


if __name__ == '__main__':
    N = 3
    A = [[random.randint(0, 1000) for _ in range(N)] for _ in range(N)]
    B = [[random.randint(0, 1000) for _ in range(N)] for _ in range(N)]

    print("Matrix A:")
    for row in A:
        print(row)

    print("\nMatrix B:")
    for row in B:
        print(row)

    queue = multiprocessing.Queue()
    process_producer = producer(queue, A, B)
    process_consumer = consumer(queue, N)
    
    start_time = time.time()
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()
    end_time = time.time()

    print("\nMatrix multiplication completed in %.2f seconds" % (end_time - start_time))
