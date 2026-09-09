import numpy as np


class Vector:

    def __init__(self):
        pass

    def input_vector(self):
        n = int(input("Enter vector size: "))
        print("Enter elements:")
        arr = []

        for i in range(n):
            arr.append(float(input()))

        return np.array(arr)

    def addition(self):
        print("\nVector A")
        a = self.input_vector()

        print("\nVector B")
        b = self.input_vector()

        print("\nResult")
        print(a + b)

    def subtraction(self):
        print("\nVector A")
        a = self.input_vector()

        print("\nVector B")
        b = self.input_vector()

        print("\nResult")
        print(a - b)

    def dot_product(self):
        print("\nVector A")
        a = self.input_vector()

        print("\nVector B")
        b = self.input_vector()

        print("\nDot Product =", np.dot(a, b))

    def magnitude(self):
        a = self.input_vector()

        print("\nMagnitude =", np.linalg.norm(a))

    def normalize(self):
        a = self.input_vector()

        print("\nNormalized Vector")

        print(a / np.linalg.norm(a))

    def angle(self):
        print("\nVector A")
        a = self.input_vector()

        print("\nVector B")
        b = self.input_vector()

        angle = np.degrees(
            np.arccos(
                np.dot(a, b) /
                (np.linalg.norm(a) * np.linalg.norm(b))
            )
        )

        print("\nAngle =", angle, "degrees")