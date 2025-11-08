import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

semaphore = threading.Semaphore(0)

result_matrix = None
N = 3

def generate_matrix(n):
    """Generate an n x n matrix of random integers."""
    return [[random.randint(0, 10000) for _ in range(n)] for _ in range(n)]

def multiply_matrices(A, B):
    """Multiply two matrices A and B."""
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

def consumer():
    global result_matrix
    logging.info('Consumer waiting for matrices...')
    semaphore.acquire()
    logging.info('Consumer notified: result matrix is ready')
    logging.info(f"Resultant Matrix:\n{result_matrix}\n")

def producer():
    global result_matrix
    
    logging.info('Producer generating matrices...')
    A = generate_matrix(N)
    B = generate_matrix(N)

    logging.info(f"Matrix A: {A}")
    logging.info(f"Matrix B: {B}")

    start = time.time()
    time.sleep(3)
    result_matrix = multiply_matrices(A, B)
    end = time.time()

    logging.info(f'Producer finished multiplication in {end - start:.4f} seconds')
    semaphore.release() 

def main():
    for i in range(3): 
        t1 = threading.Thread(target=consumer, name=f'Consumer-{i+1}')
        t2 = threading.Thread(target=producer, name=f'Producer-{i+1}')

        t1.start()
        t2.start()

        t1.join()
        t2.join()

if __name__ == "__main__":
    main()