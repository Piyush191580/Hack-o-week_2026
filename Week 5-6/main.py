
from vector import Vector
from matrix import Matrix
from calculus import Calculus
from gradient import Gradient


def vector_menu():

    v = Vector()

    while True:

        print("\n========== VECTOR OPERATIONS ==========")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Dot Product")
        print("4. Magnitude")
        print("5. Normalize")
        print("6. Angle Between Vectors")
        print("7. Back")

        ch = int(input("\nEnter Choice: "))

        if ch == 1:
            v.addition()

        elif ch == 2:
            v.subtraction()

        elif ch == 3:
            v.dot_product()

        elif ch == 4:
            v.magnitude()

        elif ch == 5:
            v.normalize()

        elif ch == 6:
            v.angle()

        elif ch == 7:
            break

        else:
            print("Invalid Choice")


def matrix_menu():

    m = Matrix()

    while True:

        print("\n========== MATRIX OPERATIONS ==========")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Inverse")
        print("7. Eigenvalues & Eigenvectors")
        print("8. Back")

        ch = int(input("\nEnter Choice: "))

        if ch == 1:
            m.addition()

        elif ch == 2:
            m.subtraction()

        elif ch == 3:
            m.multiplication()

        elif ch == 4:
            m.transpose()

        elif ch == 5:
            m.determinant()

        elif ch == 6:
            m.inverse()

        elif ch == 7:
            m.eigen()

        elif ch == 8:
            break

        else:
            print("Invalid Choice")


def calculus_menu():

    c = Calculus()

    while True:

        print("\n========== CALCULUS ==========")
        print("1. Plot Function")
        print("2. Derivative")
        print("3. Tangent Line")
        print("4. Back")

        ch = int(input("\nEnter Choice: "))

        if ch == 1:
            c.plot_function()

        elif ch == 2:
            c.derivative()

        elif ch == 3:
            c.tangent()

        elif ch == 4:
            break

        else:
            print("Invalid Choice")


def gradient_menu():

    g = Gradient()

    while True:

        print("\n========== GRADIENT DESCENT ==========")
        print("1. Gradient Descent Visualization")
        print("2. Back")

        ch = int(input("\nEnter Choice: "))

        if ch == 1:
            g.gradient_descent()

        elif ch == 2:
            break

        else:
            print("Invalid Choice")


def main():

    while True:

        print("\n======================================")
        print("      ML Math Visualizer")
        print("======================================")
        print("1. Vector Operations")
        print("2. Matrix Operations")
        print("3. Calculus")
        print("4. Gradient Descent")
        print("5. Exit")
        print("======================================")

        ch = int(input("\nEnter Choice: "))

        if ch == 1:
            vector_menu()

        elif ch == 2:
            matrix_menu()

        elif ch == 3:
            calculus_menu()

        elif ch == 4:
            gradient_menu()

        elif ch == 5:
            print("\nThank You!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()