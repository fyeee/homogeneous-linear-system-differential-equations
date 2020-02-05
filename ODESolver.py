from functools import reduce

import numpy as np
import scipy.linalg
import math
from fractions import Fraction
from Constants import *



# least common multiple
def lcm(a, b):
    return a * b / math.gcd(a, b)


# returns the denominator of the square of a number
def get_square_denominator(x):
    return Fraction(x ** 2).limit_denominator(MAX_DENOMINATOR).denominator


# returns the smallest multiplier, k, that can be used to scale a vector to
# have integer coefficients. Assumes vector has the property that it can be
# expressed as [x**0.5, y**0.5, ...] where x, y, ... are rational with
# denominators <= MAX_DENOMINATOR
def get_k(v):
    denominators = [get_square_denominator(i.item()) for i in v]
    return reduce(lcm, denominators) ** 0.5


class ODESolver:
    def __init__(self, matrix):
        self.matrix = matrix
        self.eigenvalues = self.eigenvectors = None

    def solve_eigen(self):
        self.eigenvalues, self.eigenvectors = scipy.linalg.eig(self.matrix)
        self.eigenvectors = self.eigenvectors.T
        for i in range(len(self.eigenvectors)):
            smallest_mult = get_k([val.real for val in self.eigenvectors[i]])
            self.eigenvectors[i] = self.eigenvectors[i] * smallest_mult

    def classify_equilibrium(self):
        pass
#
# import tkinter as tk
# class SampleApp(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         l = tk.Text(self, width=5, height=2, borderwidth=0,
#                     background=self.cget("background"))
#         l.tag_configure("subscript", offset=-4)
#         l.insert("insert", "H", "", "2", "subscript", "O")
#         l.configure(state="disabled")
#         l.pack(side="top")
#


if __name__ == "__main__":
    # m = np.array([[-0.5, 1], [-1, -0.5]])
    m = np.array([[-0.5, 1], [-1, -0.5]])
    solver = ODESolver(m)
    solver.solve_eigen()
    print(solver.eigenvalues)
    print(solver.eigenvectors)
    print("\n")
    print(solver.eigenvalues[0].imag)
