from UI.Constants import *

unicode_superscript_dict = {'1': "\u00b9", '2': "\u00b2", '3': "\u00b3", '4': "\u2074", '5': "\u2075", '6': "\u2076",
                            '7': "\u2077", '8': "\u2078", '9': "\u2079", '0': "\u2070", 't': "\u1d57", '.': "\u22c5",
                            '-': "\u207B"}
unicode_subscript_dict = {'1': "\u2081", '2': "\u2082"}


def get_unicode_superscript(string):
    result = ""
    for char in string:
        result += unicode_superscript_dict[char]
    return result


# Storing a Solution of Homogeneous System of Two Linear
# First Order Equations in Two Unknowns
class SolutionModel:
    def __init__(self, eigenvalues, eigenvectors, eigenvalue_type, lin_ind, n=None):
        self.type = eigenvalue_type
        self.lin_ind = lin_ind
        if eigenvalue_type == DISTINCT_REAL_EIGENVALUES:
            self.r1 = round(eigenvalues[0].real, 2)
            self.r2 = round(eigenvalues[1].real, 2)
            self.k1 = eigenvectors[0]
            self.k2 = eigenvectors[1]
        elif eigenvalue_type == COMPLEX_CONJUGATE_EIGENVALUES:
            self.r1 = round(eigenvalues[0].real, 2)
            self.r2 = round(eigenvalues[0].real, 2)
            self.mu = round(eigenvalues[0].imag, 2)
            self.k1 = eigenvectors[0].real
            self.k2 = eigenvectors[0].imag

        elif eigenvalue_type == REPEATED_REAL_EIGENVALUES:
            if lin_ind == LINEARLY_INDEPENDENT:
                self.r1 = round(eigenvalues[0].real, 2)
                self.r2 = round(eigenvalues[1].real, 2)
                self.k1 = eigenvectors[0]
                self.k2 = eigenvectors[1]
            elif lin_ind == LINEARLY_DEPENDENT:
                self.r1 = round(eigenvalues[0].real, 2)
                self.r2 = round(eigenvalues[1].real, 2)
                self.k1 = eigenvectors[0]
                self.k2 = eigenvectors[1]
                self.n = n
        if self.r1 == 0:
            self.r1 = 0
        if self.r2 == 0:
            self.r2 = 0

    def get_solution(self):
        if self.type == DISTINCT_REAL_EIGENVALUES:
            sign = "+" if self.k2[0] >= 0 else ''
            solution_x1 = "X1=" + str(round(self.k1[0], 2)) + "C" + unicode_subscript_dict['1'] + "e" + \
                          get_unicode_superscript(str(self.r1) + 't') + sign + str(round(self.k2[0], 2)) + "C" + \
                          unicode_subscript_dict[
                              '2'] + "e" + get_unicode_superscript(str(self.r2) + 't')
            sign = "+" if self.k2[1] >= 0 else ''
            solution_x2 = "X2=" + str(round(self.k1[1], 2)) + "C" + unicode_subscript_dict[
                '1'] + "e" + get_unicode_superscript(
                str(self.r1) + 't') + sign + str(round(self.k2[1], 2)) + "C" + unicode_subscript_dict[
                              '2'] + "e" + get_unicode_superscript(str(self.r2) + 't')
        elif self.type == COMPLEX_CONJUGATE_EIGENVALUES:
            sign1 = "-" if self.k2[0] >= 0 else "+"
            sign2 = "+" if self.k2[0] >= 0 else "-"
            solution_x1 = "X1=C" + unicode_subscript_dict['1'] + "e" + get_unicode_superscript(str(self.r1) + 't') + \
                          "(" + str(round(self.k1[0], 2)) + "cos(" + str(self.mu) + "t)" + sign1 + \
                          str(abs(round(self.k2[0], 2))) + "sin(" + str(self.mu) + "t))+C" + \
                          unicode_subscript_dict['2'] + "e" + get_unicode_superscript(str(self.r2) + 't') + "(" + \
                          str(round(self.k1[0], 2)) + "sin(" + str(self.mu) + "t)" + sign2 + \
                          str(abs(round(self.k2[0], 2))) + "cos(" + str(self.mu) + "t))"
            sign1 = "-" if self.k2[1] >= 0 else "+"
            sign2 = "+" if self.k2[1] >= 0 else "-"
            solution_x2 = "X2=C" + unicode_subscript_dict['1'] + "e" + get_unicode_superscript(str(self.r1) + 't') \
                          + "(" + str(round(self.k1[1], 2)) + "cos(" + str(self.mu) + "t)" + sign1 + \
                          str(abs(round(self.k2[1], 2))) + "sin(" + str(self.mu) + "t))+C" + \
                          unicode_subscript_dict['2'] + "e" + get_unicode_superscript(str(self.r2) + 't') + "(" + \
                          str(round(self.k1[1], 2)) + "sin(" + str(self.mu) + "t)" + sign2 + \
                          str(abs(round(self.k2[1], 2))) + "cos(" + str(self.mu) + "t))"
        else:
            if self.lin_ind == LINEARLY_INDEPENDENT:
                sign = "+" if self.k2[0] >= 0 else ''
                solution_x1 = "X1=" + str(round(self.k1[0], 2)) + "C" + unicode_subscript_dict['1'] + "e" + \
                              get_unicode_superscript(str(self.r1) + 't') + sign + str(round(self.k2[0], 2)) + "C" + \
                              unicode_subscript_dict[
                                  '2'] + "e" + get_unicode_superscript(str(self.r2) + 't')
                sign = "+" if self.k2[1] >= 0 else ''
                solution_x2 = "X2=" + str(round(self.k1[1], 2)) + "C" + unicode_subscript_dict[
                    '1'] + "e" + get_unicode_superscript(
                    str(self.r1) + 't') + sign + str(round(self.k2[1], 2)) + "C" + unicode_subscript_dict[
                                  '2'] + "e" + get_unicode_superscript(str(self.r2) + 't')
            else:
                sign = "+" if self.n[0] >= 0 else ''
                solution_x1 = "X1=" + str(round(self.k1[0], 2)) + "C" + unicode_subscript_dict['1'] + "e" + \
                              get_unicode_superscript(str(self.r1) + 't') + "+" + "C" + unicode_subscript_dict['2'] + \
                              "e" + get_unicode_superscript(str(self.r1) + 't') + "(" + str(round(self.k1[0], 2)) + "t" \
                              + sign + str(round(self.n[0], 2)) + ')'
                sign = "+" if self.n[1] >= 0 else ''
                solution_x2 = "X2=" + str(round(self.k1[1], 2)) + "C" + unicode_subscript_dict['1'] + "e" + \
                              get_unicode_superscript(str(self.r1) + 't') + "+" + "C" + unicode_subscript_dict['2'] + \
                              "e" + get_unicode_superscript(str(self.r1) + 't') + "(" + str(round(self.k1[1], 2)) + "t" \
                              + sign + str(round(self.n[1], 2)) + ')'
        return solution_x1, solution_x2
