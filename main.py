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
    # Converting the list of strings into a list of lists of floats 
    # using list comprehension
    matrix = [list(map(float, row.split())) for row in input_values]

    return matrix

def sort_matrix(matrix):
    x_max, x_max_row_index = matrix[0][0], 0
    for i in range(len(matrix)):
        if matrix[i][0] > x_max:
            x_max = matrix[i][0]
            x_max_row_index = i
    # Swap the first row with the row containing the maximum element
    matrix[0], matrix[x_max_row_index] = matrix[x_max_row_index], matrix[0]

    y_max, y_max_row_index = matrix[1][1], 2
    for i in range(1, len(matrix)):
        if matrix[i][1] > y_max:
            y_max = matrix[i][1]
            y_max_row_index = i
    # Swap the second row with the row containing the maximum element
    matrix[1], matrix[y_max_row_index] = matrix[y_max_row_index], matrix[1]


    return matrix


if __name__ == "__main__":
    welcome()
    matrix = get_values()
    print(matrix)
    sorted_natrix = sort_matrix(matrix)
    for row in sorted_natrix:
        print(row)
 