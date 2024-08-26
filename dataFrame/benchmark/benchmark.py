import time
from dataFrame import DataFrame

def benchmark_matrix_operations():
    # Example matrices
    m1 = DataFrame([[1, 2], [3, 4]])
    m2 = DataFrame([[5, 6], [7, 8]])

    start_time = time.time()
    _ = m1 + m2  # Matrix addition
    print(f"Matrix Addition Time: {time.time() - start_time:.6f} seconds")

    start_time = time.time()
    _ = m1 * m2  # Matrix multiplication
    print(f"Matrix Multiplication Time: {time.time() - start_time:.6f} seconds")

    # Add more benchmarks as necessary

if __name__ == "__main__":
    benchmark_matrix_operations()
