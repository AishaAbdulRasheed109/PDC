## Using Pipes with multiprocessing – Matrix Multiplication
import multiprocessing
import random

def create_matrices(pipe):
    output_pipe, _ = pipe
    N = 3  
    A = [[random.randint(1, 1000) for _ in range(N)] for _ in range(N)]
    B = [[random.randint(1, 1000) for _ in range(N)] for _ in range(N)]
    output_pipe.send((A, B))
    output_pipe.close()

def multiply_matrices(pipe_1, pipe_2):
    close_pipe, input_pipe = pipe_1
    close_pipe.close() 
    output_pipe, _ = pipe_2

    try:
        while True:
            A, B = input_pipe.recv()
            N = len(A)
            C = [[0 for _ in range(N)] for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        C[i][j] += A[i][k] * B[k][j]
            output_pipe.send(C)
    except EOFError:
        output_pipe.close()

if __name__ == '__main__':
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = multiprocessing.Process(target=create_matrices, args=(pipe_1,))
    process_pipe_1.start()

    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = multiprocessing.Process(target=multiply_matrices, args=(pipe_1, pipe_2))
    process_pipe_2.start()

    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            result = pipe_2[1].recv()
            print("Matrix multiplication result:")
            for row in result:
                print(row)
    except EOFError:
        print("End")