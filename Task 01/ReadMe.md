# Matrix Multiplication: Multiprocessing vs Multithreading

## Overview

This project demonstrates **matrix multiplication** using **NumPy** in Python and compares the performance of **multiprocessing** and **multithreading**.

The goal is to observe how parallelism affects execution time and understand the limits of processes and threads for CPU-bound tasks.

---

## How It Works

1. **Matrix Generation**

   * Two random square matrices of size `500×500` are generated using `numpy.random.rand`.

2. **Matrix Multiplication**

   * The matrices are multiplied using `numpy.dot`.
   * The result is summarized by calculating the sum of all elements (simulating output for each task).

3. **Parallel Execution**

   * **Multiprocessing**: Each process runs independently in its own memory space. Useful for CPU-bound tasks.
   * **Multithreading**: Threads share memory and run concurrently. Subject to Python’s **Global Interpreter Lock (GIL)**, which may limit performance on CPU-bound tasks.

---

## Usage

```bash
python main.py
```

* The script runs the multiplication with a configurable number of processes or threads.
* Change the variable `procs` to **1, 5, 10, 15, 20** to observe different performances.

---

## Results

| Number of Processes/Threads | Multiprocessing Time (s) | Multithreading Time (s) |
| --------------------------- | ------------------------ | ----------------------- |
| 1                           | 0.569                    | 0.073                   |
| 5                           | 0.835                    | 0.119                   |
| 10                          | 1.333                    | 0.287                   |
| 15                          | 1.919                    | 0.586                   |
| 20                          | 4.032                    | 0.431                   |

---

## Analysis

### 1. Single Process / Thread

* **Multiprocessing (0.569s)** is slower than **multithreading (0.073s)** for a single unit because:

  * Multiprocessing has **process creation overhead**.
  * Multithreading runs in the same memory space with almost zero overhead.

### 2. 5 Processes / Threads

* Multiprocessing time **increases slightly (0.835s)**.
* Multithreading time **also increases slightly (0.119s)**.
* Explanation:

  * Each new process adds **overhead for creation and memory management**.
  * Threads share memory, so the increase is smaller, but GIL limits CPU-bound improvements.

### 3. 10 Processes / Threads

* Multiprocessing time continues to **increase (1.333s)**.
* Multithreading time **increases (0.287s)** but remains lower than multiprocessing.
* Explanation:

  * With many processes and a moderate matrix size, **process management overhead dominates computation time**.
  * Threads are still limited by the GIL.

### 4. 15 Processes / Threads

* Multiprocessing **1.919s**, multithreading **0.586s**.
* Overhead becomes more significant as the number of processes increases beyond CPU cores.
* Multithreading suffers from GIL but still faster for small tasks.

### 5. 20 Processes / Threads

* Multiprocessing jumps to **4.032s** due to extreme overhead:

  * Too many processes are created for the task size.
  * Context switching and memory copying slow down the computation.
* Multithreading **0.431s** improves slightly, likely due to scheduling fluctuations, but still better than multiprocessing.

---

## Observations & Recommendations

1. **Multiprocessing**

   * Only effective when the **task is large enough** to offset process creation overhead.
   * Increasing processes beyond the number of CPU cores can **increase execution time**.

2. **Multithreading**

   * Limited by Python’s GIL for CPU-bound tasks.
   * Low overhead makes it faster than a single process for **small to moderate tasks**.

3. **General Rule**

   * For CPU-bound tasks:

     * Use **multiprocessing** only when the workload is large.
     * Match the number of processes to the number of physical CPU cores.
   * For small tasks, **threads are more efficient** due to lower overhead.

---

## Dependencies

* Python 3.x
* NumPy

Install NumPy using pip:

```bash
pip install numpy