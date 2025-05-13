import numpy as np

def welcome():
    print("=" * 50)
    print("        GAUSSIAN ELIMINATION SOLVER")
    print("=" * 50)
    print("This script solves a system of linear equations")
    print("using the Gaussian Elimination method.")
    print("You'll see step-by-step elimination and back substitution.")
    print("=" * 50)
    print()

def print_matrix(matrix, label="Matrix"):
    print(f"\n{label}:")
    for row in matrix:
        row_str = "  ".join(f"{val:>7.2f}" for val in row[:-1])
        print(f"[ {row_str} | {matrix[matrix.tolist().index(list(row))][-1]:>7.2f} ]")

def get_values():
    input_values = input("Enter the augmented matrix (comma-separated): ").strip()

    # Splitting the input string into a list of strings
    input_values = input_values.split(",")
    # Converting the list of strings into a list of lists of floats using list comprehension
    matrix = [list(map(float, row.split())) for row in input_values]

    return np.array(matrix)

def sort_matrix(matrix):
    # Sort the matrix based on the first two columns
    matrix = matrix.copy() # Create a copy to avoid modifying the original matrix
    x_max_index = np.argmax(matrix[:, 0])
    
    matrix[[0, x_max_index]] = matrix[[x_max_index, 0]]  # Swap the first row with the row of the largest first column

    y_max_index = np.argmax(matrix[1:, 1]) + 1

    matrix[[1, y_max_index]] = matrix[[y_max_index, 1]]  # Swap the second row with the row of the largest second column


    return matrix

def gaussian_elimination(matrix):
    matrix = matrix.copy()

    R1 = matrix[0]
    R2 = matrix[1]
    R3 = matrix[2]

    print("\n[Step 1] Eliminating entries in column 1")
    a1, b1 = matrix[0, 0], matrix[1, 0]
    a2, b2 = matrix[0, 0], matrix[2, 0]

    print(f"R2' = {a1:.0f}*R2 - {b1:.0f}*R1")
    print(f"R3' = {a2:.0f}*R3 - {b2:.0f}*R1")

    R2_prime = a1 * R2 - b1 * R1
    R3_prime = a2 * R3 - b2 * R1

    matrix[1] = R2_prime
    matrix[2] = R3_prime

    print_matrix(matrix, label="After Column 1 Elimination")

    print("\n[Step 2] Eliminating entry in column 2")
    a3, b3 = matrix[1, 1], matrix[2, 1]
    print(f"R3'' = {a3:.0f}*R3' - {b3:.0f}*R2'")

    R3_prime_final = a3 * matrix[2] - b3 * matrix[1]
    matrix[2] = R3_prime_final

    print_matrix(matrix, label="After Column 2 Elimination")

    return matrix


def back_substitution(matrix):
    n = matrix.shape[0]
    x = np.zeros(n)

    x[2] = matrix[2, 3] / matrix[2, 2]
    x[1] = (matrix[1, 3] - matrix[1, 2] * x[2]) / matrix[1, 1]
    x[0] = (matrix[0, 3] - matrix[0, 1] * x[1] - matrix[0, 2] * x[2]) / matrix[0, 0]

    return x

if __name__ == "__main__":
    welcome()
    while True:
        try:
            matrix = get_values()
        except Exception as e:
            print(f"Error: {e}")
            print("Please enter a valid augmented matrix.")
            continue

        print_matrix(matrix, label="Original Matrix")

        print("\nSorting the matrix based on the first two columns... for easier elimination")
        sorted_natrix = sort_matrix(matrix)


        print_matrix(sorted_natrix, label="Sorted Matrix")

        print("\nPerforming Gaussian Elimination...")
        eliminated_matrix = gaussian_elimination(sorted_natrix)

        print_matrix(eliminated_matrix, label="Eliminated Matrix")
        
        print("\nPerforming Back Substitution...")
        solution = back_substitution(eliminated_matrix)
        print("\nSolution:")
        for i, val in enumerate(solution):
            print(f"x{i+1} = {val:.4f}")
    
        print("\n" + "=" * 50)
        cont = input("Do you want to solve another system? (y/n): ").strip().lower()
        if cont != 'y':
            print("Thank you for using the Gaussian Elimination Solver!")
            break