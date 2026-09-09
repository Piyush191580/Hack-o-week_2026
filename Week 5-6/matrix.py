import numpy as np


class Matrix:

    def __init__(self):
        pass

    def input_matrix(self):
        r = int(input("Enter number of rows: "))
        c = int(input("Enter number of columns: "))

        print("\nEnter matrix elements:")

        matrix = []

        for i in range(r):
            row = []
            for j in range(c):
                row.append(float(input(f"Element [{i+1}][{j+1}] : ")))
            matrix.append(row)

        return np.array(matrix)

    def addition(self):
        print("\nMatrix A")
        A = self.input_matrix()

        print("\nMatrix B")
        B = self.input_matrix()

        print("\nResult")
        print(A + B)

    def subtraction(self):
        print("\nMatrix A")
        A = self.input_matrix()

        print("\nMatrix B")
        B = self.input_matrix()

        print("\nResult")
        print(A - B)

    def multiplication(self):
        print("\nMatrix A")
        A = self.input_matrix()

        print("\nMatrix B")
        B = self.input_matrix()

        print("\nResult")
        print(np.dot(A, B))

    def transpose(self):
        A = self.input_matrix()

        print("\nTranspose")
        print(A.T)

    def determinant(self):
        A = self.input_matrix()

        print("\nDeterminant")
        print(np.linalg.det(A))

    def inverse(self):
        A = self.input_matrix()

        print("\nInverse")
        print(np.linalg.inv(A))

    def eigen(self):
        A = self.input_matrix()

        values, vectors = np.linalg.eig(A)

        print("\nEigenvalues")
        print(values)

        print("\nEigenvectors")
        print(vectors)