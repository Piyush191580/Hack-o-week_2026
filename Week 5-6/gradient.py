import numpy as np
import matplotlib.pyplot as plt


class Gradient:

    def __init__(self):
        pass

    def gradient_descent(self):

        learning_rate = float(input("Enter Learning Rate (0.1 recommended): "))
        x = float(input("Enter Starting Value of x: "))
        iterations = int(input("Enter Number of Iterations: "))

        x_points = []
        y_points = []

        for i in range(iterations):

            y = x ** 2

            x_points.append(x)
            y_points.append(y)

            gradient = 2 * x

            x = x - learning_rate * gradient

        X = np.linspace(-10, 10, 400)
        Y = X ** 2

        plt.figure(figsize=(8,5))

        plt.plot(X, Y, label="f(x)=x²")

        plt.scatter(x_points, y_points, color="red")

        plt.plot(x_points, y_points, '--')

        plt.title("Gradient Descent")

        plt.xlabel("x")

        plt.ylabel("Loss")

        plt.grid(True)

        plt.legend()

        plt.show()

        print("\nFinal x =", x)
        print("Final Loss =", x ** 2)