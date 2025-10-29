import numpy as np

def inp_mat(prompt):
    print(prompt)
    rows = int(input("Enter number of rows: "))

    cols = int(input("Enter number of columns: "))
    print("Enter the values of matrix row-wise, separated by spaces:")
    mat = []
    for i in range(rows):
        row = list(map(float, input().strip().split()))
        if len(row) != cols:
            raise ValueError("Number of columns does not match the specified size.")
        mat.append(row)
    return np.array(mat)

def operations():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Exit")
        choice = input("Choose an operation (1-4): ")
        if choice == '4':
            print("Exiting the program.")
            break

        mat1 = inp_mat("Enter the first matrix:")
        mat2 = inp_mat("Enter the second matrix:")
        if choice == '1':
            if mat1.shape == mat2.shape:
                print("Result:\n", mat1 + mat2)
            else:
                print("Error: Matrices must have the same dimensions for addition.")
        elif choice == '2':
            if mat1.shape == mat2.shape:
                print("Result:\n", mat1 - mat2)
            else:
                print("Error: Matrices must have the same dimensions for subtraction.")
        elif choice == '3':
            if mat1.shape[1] == mat2.shape[0]:
                print("Result:\n", np.dot(mat1, mat2))
            else:
                print("Error: Number of columns in the first matrix must equal number of rows in the second matrix for multiplication.")
        else:
            print("Invalid choice. Please select a valid operation.")
if __name__ == "__main__":
    operations()        