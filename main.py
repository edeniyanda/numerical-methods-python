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
    input_values = input("Enter the augmented matrix (comma-separated): ")
    # Splitting the input string into a list of strings
    input_values = input_values.split(",")
    # Converting the list of strings into a list of lists of floats 
    # using list comprehension
    matrix = [list(map(float, row.split())) for row in input_values]


if __name__ == "__main__":
    welcome()
    # # Importing the Gaussian Elimination function from the module
    # from gaussian_elimination import gaussian_elimination

    # # Example system of equations
    # # 2x + 3y + z = 1
    # # 4x + y + 2z = 2
    # # 3x + 2y + 3z = 3
    # A = [
    #     [2, 3, 1, 1],
    #     [4, 1, 2, 2],
    #     [3, 2, 3, 3]
    # ]

    # # Solve the system of equations
    # solution = gaussian_elimination(A)
    # print("The solution is:", solution)