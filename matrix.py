import threading
import time
import random

def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        raise ValueError("Matrix dimensions not compatible for multiplication")

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def multiply_row(A, B, result, row):
    cols_B = len(B[0])
    for j in range(cols_B):
        total = 0
        for k in range(len(A[0])):
            total += A[row][k] * B[k][j]
        result[row][j] = total

def matrix_multiply_threaded(A, B):
    rows_A = len(A)
    result = [[0 for _ in range(len(B[0]))] for _ in range(rows_A)]
    threads = []

    for i in range(rows_A):
        t = threading.Thread(target=multiply_row, args=(A, B, result, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    return result

def generate_matrix(rows, cols):
    return [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]

if __name__ == "__main__":
    A = generate_matrix(50, 50)
    B = generate_matrix(50, 50)

    start = time.time()
    matrix_multiply(A, B)
    end = time.time()
    print("Single-threaded time:", round(end - start, 4), "seconds")

    start = time.time()
    matrix_multiply_threaded(A, B)
    end = time.time()
    print("Multithreaded (per row) time:", round(end - start, 4), "seconds")
