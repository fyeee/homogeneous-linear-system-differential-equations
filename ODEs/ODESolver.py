from functools import reduce
import numpy as np
import scipy.linalg
import math
from fractions import Fraction
from Constants import *
from ODEs.SolutionModel import SolutionModel



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
    def __init__(self):
        self.system = self.eigenvalues = self.eigenvectors = None

    def set_matrix(self, values):
        self.system = np.array(values).reshape(2, 2)
        self.eigenvalues = self.eigenvectors = None

    def solve_eigen(self):
        self.eigenvalues, self.eigenvectors = scipy.linalg.eig(self.system)
        self.eigenvectors = self.eigenvectors.T
        for i in range(len(self.eigenvectors)):
            smallest_mult = get_k([val.real for val in self.eigenvectors[i]])
            self.eigenvectors[i] = self.eigenvectors[i] * smallest_mult

    def classify_equilibrium(self):
        pass

    def solve_ODE(self):
        if self.system is None:
            return
        self.solve_eigen()
        if round(self.eigenvalues[0].imag, 2) == 0:
            if round(self.eigenvalues[0].real, 2) != round(self.eigenvalues[1].real, 2):
                model = SolutionModel(self.eigenvalues, self.eigenvectors, DISTINCT_REAL_EIGENVALUES,
                                      LINEARLY_INDEPENDENT)
                return model.get_solution()
        else:
            model = SolutionModel(self.eigenvalues, self.eigenvectors, COMPLEX_CONJUGATE_EIGENVALUES,
                                  LINEARLY_INDEPENDENT)
            return model.get_solution()


if __name__ == "__main__":
    m = np.array([[5, -7], [5, 9]])
    # m = np.array([[2, -5], [1, -2]])
    # m = np.array([[2, 0], [0, -3]])
    solver = ODESolver()
    solver.set_matrix(m)
    # print(solver.eigenvectors)
    solver.solve_ODE()