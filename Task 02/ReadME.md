# Parallel and Concurrent Matrix Multiplication Examples

This repository contains multiple Python implementations of **matrix multiplication** using various threading and synchronization mechanisms. These examples demonstrate different concurrency concepts in Python, such as **Barrier, Condition, Event, Lock, RLock, Semaphore**, and **Queue-based producer-consumer patterns**.

## Repository Structure

The repository contains the following Python scripts:

### 1. `barrier.py`

* **Concept:** `threading.Barrier`
* **Description:**
  Uses a Barrier to synchronize multiple threads performing row-wise multiplication of matrices. Threads wait at the barrier until all threads complete their assigned row computations.
* **Key Points:**

  * Randomly generates matrices `A` and `B`.
  * Each thread computes one row of the result matrix `C`.
  * Barrier ensures all threads complete before printing the final matrix.

---

### 2. `condition.py`

* **Concept:** `threading.Condition`
* **Description:**
  Demonstrates the **Producer-Consumer pattern** using a condition variable. The producer generates two matrices, and the consumer waits until the matrices are available before multiplying them.
* **Key Points:**

  * Condition variable used for signaling between threads.
  * Matrix multiplication happens **after notification**.

---

### 3. `event.py`

* **Concept:** `threading.Event`
* **Description:**
  Uses an event object to signal the consumer that matrices are ready for multiplication.
* **Key Points:**

  * Producer generates matrices and sets the event.
  * Consumer waits for the event, performs multiplication, then clears the event.

---

### 4. `Mythreadclasslock2.py` and `Mythreadclasslock.py`

* **Concept:** `threading.Lock`
* **Description:**
  Demonstrates row-wise matrix multiplication using threads and a **Lock** to synchronize print statements and logging.
* **Key Points:**

  * Protects critical sections with `Lock` to avoid concurrent print statements interfering.
  * Computes rows independently, but ensures orderly logging.

---

### 5. `mythreadclass.py`

* **Concept:** Custom `Thread` subclass
* **Description:**
  Implements matrix multiplication by creating a `MyThreadClass` for each row.
* **Key Points:**

  * Shows passing matrices and result storage to thread instances.
  * Prints execution info including process ID and thread status.

---

### 6. `rlock.py`

* **Concept:** `threading.RLock` (Reentrant Lock)
* **Description:**
  Uses `RLock` to allow the same thread to acquire the lock multiple times safely.
* **Key Points:**

  * Protects row-wise multiplication and logging.
  * Multiple threads safely compute rows concurrently.

---

### 7. `semaphore.py`

* **Concept:** `threading.Semaphore`
* **Description:**
  Implements a **Producer-Consumer model** with a semaphore controlling when the consumer can access the result.
* **Key Points:**

  * Producer computes the matrix multiplication.
  * Consumer waits on the semaphore until the result is ready.

---

### 8. `threading_with_queue.py`

* **Concept:** `threading` + `queue.Queue`
* **Description:**
  Demonstrates a **multi-producer, multi-consumer** scenario using a thread-safe queue.
* **Key Points:**

  * Producer generates multiple matrix pairs and puts them in a queue.
  * Consumers take matrix pairs from the queue and perform multiplication concurrently.
  * `Queue` ensures safe access without explicit locks.

---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

2. Run any script with Python 3:

```bash
python barrier.py
python condition.py
python event.py
python lock.py
python thread_class.py
python rlock.py
python semaphore.py
python thread_queue.py
```

3. Observe console outputs to see synchronization and concurrent computation in action.

---

## Key Concepts Demonstrated

* **Barrier:** Synchronize multiple threads until all have reached a point.
* **Condition:** Thread signaling for producer-consumer workflows.
* **Event:** Simple thread signaling mechanism for a one-time signal.
* **Lock / RLock:** Protect critical sections and avoid race conditions.
* **Semaphore:** Control access to shared resources.
* **Queue:** Thread-safe data exchange between producers and consumers.

---

## Notes

* All scripts use **row-wise matrix multiplication** with randomly generated matrices.
* Matrix size is mostly `3x3` or `4x4` for simplicity.
* Execution times vary due to random delays and concurrency scheduling.

---

This repository is intended for **learning and experimenting** with Python concurrency primitives in multi-threaded scenarios.

---
