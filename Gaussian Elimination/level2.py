import numpy as np

def welcome():
    print("=" * 50)
    print("        GAUSSIAN ELIMINATION SOLVER")
    print("=" * 50)
    print("This script solves a system of linear equations")
    print("using the Gaussian Elimination method.")
    print("Handles unique, inconsistent, and dependent systems.")
    print("=" * 50)
    print()

def get_values():
    input_values = input("Enter the augmented matrix (comma-separated rows): ").strip()
    input_values = input_values.split(",")
    matrix = [list(map(float, row.split())) for row in input_values]
    return matrix

def sort_matrix(matrix):
    for col in range(min(len(matrix), len(matrix[0]) - 1)):
        max_row = max(range(col, len(matrix)), key=lambda r: abs(matrix[r][col]))
        matrix[col], matrix[max_row] = matrix[max_row], matrix[col]
    return matrix

def gaussian_elimination_with_checks(matrix):
    n = len(matrix)
    for i in range(n):
        # Pivot: swap with row that has largest absolute value in column i
        max_row = max(range(i, n), key=lambda r: abs(matrix[r][i]))
        if abs(matrix[max_row][i]) < 1e-12:
            continue
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Eliminate below
        for j in range(i + 1, n):
            if abs(matrix[j][i]) < 1e-12:
                continue
            factor = matrix[j][i] / matrix[i][i]
            matrix[j] = [matrix[j][k] - factor * matrix[i][k] for k in range(n + 1)]
    return matrix

def check_consistency(matrix):
    for row in matrix:
        if all(abs(x) < 1e-10 for x in row[:-1]) and abs(row[-1]) > 1e-10:
            return "inconsistent"
        if all(abs(x) < 1e-10 for x in row):
            return "dependent"
    return "unique"

def back_substitution_safe(matrix):
    n = len(matrix)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        if abs(matrix[i][i]) < 1e-12:
            return None
        x[i] = (matrix[i][-1] - sum(matrix[i][j] * x[j] for j in range(i + 1, n))) / matrix[i][i]
    return x

if __name__ == "__main__":
    welcome()
    matrix = get_values()
    print("\nOriginal Matrix:")
    for row in matrix:
        print(row)

    matrix = sort_matrix(matrix)
    print("\nSorted Matrix (for stability):")
    for row in matrix:
        print(row)

    matrix = gaussian_elimination_with_checks(matrix)
    print("\nMatrix After Elimination:")
    for row in matrix:
        print(row)

    status = check_consistency(matrix)
    print(f"\nSystem Status: {status.upper()}")

    if status == "unique":
        solution = back_substitution_safe(matrix)
        print("\nSolution:")
        for i, val in enumerate(solution):
            print(f"x{i+1} = {val:.4f}")
    elif status == "inconsistent":
        print("The system has no solution.")
    elif status == "dependent":
        print("The system has infinitely many solutions.")
