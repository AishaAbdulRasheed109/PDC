import multiprocessing
import random

A = [[random.randint(0,5) for _ in range(3)] for _ in range(3)]
B = [[random.randint(0,5) for _ in range(3)] for _ in range(3)]

class MyProcess(multiprocessing.Process):
    def __init__(self, row_index, result):
        super().__init__()
        self.row_index = row_index
        self.result = result

    def run(self):
        print('called run method in %s' % self.name)
        row_result = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(B)):
                sum += A[self.row_index][k] * B[k][j]
            row_result.append(sum)
        self.result[self.row_index] = row_result
        print(f'Row {self.row_index} computed: {row_result}')


if __name__ == '__main__':
    print("Matrix A:")
    for row in A:
        print(row)
    print("\nMatrix B:")
    for row in B:
        print(row)

    manager = multiprocessing.Manager()
    result = manager.list([0]*len(A))

    for i in range(len(A)):
        process = MyProcess(i, result)
        process.start()
        process.join()

    print("\nResult Matrix:")
    for row in result:
        print(row)
