import logging
import threading
import random
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

condition = threading.Condition()
matrices = {} 


def generate_matrix(n, m):
    """Generate an n x m matrix with random integers."""
    return [[random.randint(0, 9) for _ in range(m)] for _ in range(n)]


def multiply_matrices(A, B):
    """Perform matrix multiplication A x B."""
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        raise ValueError("Matrix dimensions do not match for multiplication")

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result


class Producer(threading.Thread):
    def run(self):
        with condition:
            logging.info("Producer generating matrices...")

            A = generate_matrix(4, 4)
            B = generate_matrix(4, 4)
            matrices["A"] = A
            matrices["B"] = B

            logging.info(f"Matrix A: {A}")
            logging.info(f"Matrix B: {B}")

            condition.notify()

        time.sleep(1)


class Consumer(threading.Thread):
    def run(self):
        with condition:
            while "A" not in matrices or "B" not in matrices:
                logging.info("Consumer waiting for matrices...")
                condition.wait()

            logging.info("Consumer received matrices, performing multiplication...")
            A = matrices["A"]
            B = matrices["B"]

        # Perform multiplication outside lock
        result = multiply_matrices(A, B)
        logging.info(f"Resultant Matrix: {result}")

def main():
    producer = Producer(name="Producer")
    consumer = Consumer(name="Consumer")

    consumer.start()
    producer.start()

    producer.join()
    consumer.join()

if __name__ == "__main__":
    main()
