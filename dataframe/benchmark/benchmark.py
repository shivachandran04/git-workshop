import time
from dataframe import DataFrame

def benchmark_dataframe_operations():
    # Example dataframes
    df1 = DataFrame([[1, 2], [3, 4]], ["A", "B"])
    df2 = DataFrame([[5, 6], [7, 8]], ["C", "D"])

    start_time = time.time()
    df1.concatenate_vertically(df2)
    print(f"Dataframe Concatenate Vertically Time: {time.time() - start_time:.6f} seconds")
    
    # Add more benchmarks as necessary


if __name__ == "__main__":
    benchmark_dataframe_operations()
