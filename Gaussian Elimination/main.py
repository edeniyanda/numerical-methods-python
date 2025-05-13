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
    R2_prime = matrix[0][0] * np.array(matrix[1]) - matrix[1][0] * np.array(matrix[0])
    R3_prime = matrix[0][0] * np.array(matrix[2]) - matrix[2][0] * np.array(matrix[0])

    # Update the matrix with the new rows
    matrix[1] = R2_prime
    matrix[2] = R3_prime

    # Perform elimination for the third row
    R3_prime = matrix[1][1] * np.array(matrix[2]) - matrix[2][1] * np.array(matrix[1])

    # Update the matrix with the new row
    matrix[2] = R3_prime

    return matrix

def back_substitution(matrix):
    # Assuming the matrix is in row echelon form
    n = len(matrix)
    x = [0] * n

    # Back substitution
    x[n-1] = matrix[n-1][n] / matrix[n-1][n-1]

    x[n-2] = (matrix[n-2][n] - matrix[n-2][n-1] * x[n-1]) / matrix[n-2][n-2]

    x[n-3] = (matrix[n-3][n] - matrix[n-3][n-2] * x[n-2] - matrix[n-3][n-1] * x[n-1]) / matrix[n-3][n-3]

    return x

if __name__ == "__main__":
    welcome()
    matrix = get_values()
    print("Original Matrix:")
    for row in matrix:
        print(row)

    print("\nSorting the matrix based on the first two columns... for easier elimination")
    sorted_natrix = sort_matrix(matrix)
    print("\nSorted Matrix:")
    ##############
    for row in sorted_natrix:
        print(row)

    # print("\nPerforming Gaussian Elimination...")
    # eliminated_matrix = gaussian_elimination(sorted_natrix)
    # print("\nEliminated Matrix:")
    # for row in eliminated_matrix:
    #     print(row)
    
    # print("\nPerforming Back Substitution...")
    # solution = back_substitution(eliminated_matrix)
    # print("\nSolution:")
    # for i, val in enumerate(solution):
    #     print(f"x{i+1} = {val:.2f}")
 