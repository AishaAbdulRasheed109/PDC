import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

A = []
B = []
C = []
event = threading.Event()

class Consumer(threading.Thread):
    def run(self):
        while True:
            logging.info("Consumer waiting for matrices")
            event.wait()
            logging.info("Consumer started matrix multiplication")

            global C
            n = len(A)
            C = [[0 for _ in range(n)] for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        C[i][j] += A[i][k] * B[k][j]

            logging.info(f"Result matrix C: {C}")
            event.clear()
            break 

class Producer(threading.Thread):
    def run(self):
        global A, B
        n = 3
        A = [[random.randint(1, 9) for _ in range(n)] for _ in range(n)]
        B = [[random.randint(1, 9) for _ in range(n)] for _ in range(n)]

        logging.info(f"Matrix A: {A}")
        logging.info(f"Matrix B: {B}")

        time.sleep(2)
        logging.info("Producer setting event — matrices ready for multiplication")
        event.set()

if __name__ == "__main__":
    producer = Producer(name="ProducerThread")
    consumer = Consumer(name="ConsumerThread")

    consumer.start()
    producer.start()

    producer.join()
    consumer.join()

    logging.info("Matrix multiplication completed successfully.")
