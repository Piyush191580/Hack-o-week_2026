import numpy as np
import matplotlib.pyplot as plt


class Calculus:

    def __init__(self):
        pass

    def choose_function(self):

        print("\nSelect Function")
        print("1. x²")
        print("2. x³")
        print("3. sin(x)")
        print("4. cos(x)")
        print("5. eˣ")

        ch = int(input("Choice: "))

        if ch == 1:
            return lambda x: x**2, "x²"

        elif ch == 2:
            return lambda x: x**3, "x³"

        elif ch == 3:
            return np.sin, "sin(x)"

        elif ch == 4:
            return np.cos, "cos(x)"

        elif ch == 5:
            return np.exp, "eˣ"

        else:
            print("Invalid Choice")
            return None, None

    def plot_function(self):

        func, name = self.choose_function()

        if func is None:
            return

        x = np.linspace(-10, 10, 400)
        y = func(x)

        plt.figure(figsize=(8,5))
        plt.plot(x, y)

        plt.title(name)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)

        plt.show()

    def derivative(self):

        func, name = self.choose_function()

        if func is None:
            return

        point = float(input("Enter x value: "))

        h = 0.0001

        slope = (func(point + h) - func(point)) / h

        print("\nApproximate Derivative =", slope)

    def tangent(self):

        func, name = self.choose_function()

        if func is None:
            return

        point = float(input("Enter x value: "))

        h = 0.0001

        slope = (func(point + h) - func(point)) / h

        x = np.linspace(point - 5, point + 5, 300)

        y = func(x)

        tangent = func(point) + slope * (x - point)

        plt.figure(figsize=(8,5))

        plt.plot(x, y, label=name)

        plt.plot(x, tangent, '--', label="Tangent")

        plt.scatter(point, func(point), s=100)

        plt.title("Tangent Line")

        plt.legend()

        plt.grid(True)

        plt.show()