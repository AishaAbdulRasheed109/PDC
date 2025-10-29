from matrix_multiplication import multiply_matrices
import time
import multiprocessing
import threading

if __name__ == "__main__":
    size = 500      
    procs = 20  
    jobs = []

    # --- MULTIPROCESSING ---
    start_time = time.time()
    for i in range(procs):
        out_list = []
        process = multiprocessing.Process(target=multiply_matrices, args=(size, out_list))
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("Matrix multiplication completed using multiprocessing.")
    end_time = time.time()
    print("Multiprocessing time =", round(end_time - start_time, 3), "seconds")

    # --- MULTITHREADING ---
    jobs = []
    threads = procs
    start_time = time.time()
    for i in range(threads):
        out_list = []
        thread = threading.Thread(target=multiply_matrices, args=(size, out_list))
        jobs.append(thread)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("Matrix multiplication completed using multithreading.")
    end_time = time.time()
    print("Multithreading time =", round(end_time - start_time, 3), "seconds")
