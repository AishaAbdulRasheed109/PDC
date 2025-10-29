import numpy as np

def multiply_matrices(size, output_list):
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)

    result = np.dot(A, B)

    # Append a summary value to output_list (just to simulate some output)
    output_list.append(np.sum(result))
