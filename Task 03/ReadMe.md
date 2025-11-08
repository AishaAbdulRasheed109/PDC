# Parallel and Distributed Computing - Python Multiprocessing Examples

This repository contains Python scripts demonstrating **parallel and distributed computing concepts** using the `multiprocessing` module. Each example showcases different techniques such as **process creation, communication, synchronization, process management, and background execution**. Most scripts focus on **matrix multiplication** to illustrate parallel computation.


## communication_with_pipe

**Concepts:**  
- Demonstrates **inter-process communication (IPC)** using `multiprocessing.Pipe`.  
- One process generates random matrices, another multiplies them.  
- Result is sent back via a second pipe.

**Key Points:**  
- `Pipe(True)` creates a duplex connection for communication.  
- `send()` and `recv()` allow sending/receiving data between processes.  
- Multiplication occurs in a separate process; the main process prints the final result.

---

## communication_with_queue

**Concepts:**  
- Demonstrates the **producer-consumer pattern** using `multiprocessing.Queue`.  
- `Producer` computes each row of the result matrix and puts it in the queue.  
- `Consumer` retrieves rows and assembles the final matrix.

**Key Points:**  
- Queue ensures **safe communication** between processes.  
- Sentinel value `None` signals the end of computation.  
- `queue.qsize()` shows the current number of items in the queue.  

---

## killing_processes

**Concepts:**  
- Shows how to **start, join, and terminate processes**.  
- Demonstrates **normal completion vs forced termination**.

**Key Points:**  
- `.start()` begins a process, `.join()` waits for it to finish.  
- `.terminate()` stops a running process immediately.  
- `.exitcode` shows process termination status.  

---

## myfunc

**Concepts:**  
- Defines a **matrix multiplication function** executed by multiple processes.  
- Each process computes a matrix of size `i x i` independently.

**Key Points:**  
- Demonstrates computation in isolated processes without shared state.  
- Useful for integration with other multiprocessing scripts.

---

## naming_processes

**Concepts:**  
- Demonstrates **naming processes** for easier identification.  
- Executes matrix multiplication in two processes: one with a custom name, one with the default name.

**Key Points:**  
- `multiprocessing.current_process().name` identifies processes.  
- Useful for logging and debugging in complex programs.  

---

## process_in_subclass

**Concepts:**  
- Demonstrates **subclassing `multiprocessing.Process`**.  
- Each process computes a single row of a matrix multiplication.

**Key Points:**  
- `super().__init__()` initializes the base `Process` class.  
- Uses a shared `multiprocessing.Manager().list()` to store results safely.  

---

## process_pool

**Concepts:**  
- Demonstrates **using process pools** for parallel computation.  
- `Pool.map()` distributes row computation across multiple processes.

**Key Points:**  
- Efficient for parallel tasks compared to manually creating many processes.  
- Results are sorted by row index before forming the final matrix.  

---

## process_barriers

**Concepts:**  
- Demonstrates **process synchronization** using `Barrier` and `Lock`.  
- Compares computation **with and without barrier synchronization**.

**Key Points:**  
- `Barrier` makes processes wait for each other before proceeding.  
- `Lock` ensures serialized printing to the console.  
- Shows the effect of synchronized vs unsynchronized execution.  

---

## run_background_processes_no_daemons

**Concepts:**  
- Demonstrates running multiple processes **without daemon mode**.  
- Splits matrix multiplication across processes.

**Key Points:**  
- `daemon=False` ensures processes run independently to completion.  
- Processes compute different portions of the matrix in parallel.

---

## run_background_processes

**Concepts:**  
- Shows **foreground vs background process execution**.  
- Background process runs silently, foreground process prints row-by-row computation.

**Key Points:**  
- `daemon=True` → background process will terminate if main program exits.  
- `daemon=False` → process runs normally until finished.  
- Highlights practical usage of background processes for long-running tasks.

---

## spawning_processes

**Concepts:**  
- Demonstrates **spawning multiple processes** sequentially using `myFunc`.  

**Key Points:**  
- Processes are started and joined **one by one** for sequential execution.  
- Each process computes a matrix of size `i x i`.  
- Illustrates **basic process creation and execution**.

---

## spawning

**Concepts:**  
- Another example of **process spawning** with matrix multiplication.  
- Each process independently computes its own matrix result.

**Key Points:**  
- Arguments are passed to processes using `args=(i,)`.  
- Sequential `.join()` ensures ordered output.  
- Can be modified for true parallelism by starting all processes first and joining later.

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/PDC.git
cd PDC/Task-02
Run any script using Python 3:

bash
Copy code
python communication_with_pipe.py
python communication_with_queue.py
python killing_processes.py
python myfunc.py
python naming_processes.py
python process_in_subclass.py
python process_pool.py
python process_barriers.py
python run_background_processes_no_daemons.py
python run_background_processes.py
python spawning_processes.py
python spawning.py
Requirements
Python 3.x

No external libraries required (uses standard multiprocessing module)