# polynomial.py

class Polynomial:

    def __init__(self, *args):
        self.coefficients = dict()
        self.calculated_degree = 0
        if not args:
            arg = [0]
        elif len(args) == 1:
            arg = args[0]
        else:
            arg = list(args)
        if isinstance(arg, list):
            self.coefficients = dict()
            for i in range(len(arg)):
                self.coefficients[i] = arg[i]
        elif isinstance(arg, dict):
            self.coefficients = arg
        elif isinstance(arg, Polynomial):
            self.coefficients = arg.coefficients
        else:
            self.coefficients = {0: arg}
        self.strip_zeros()
        self.calculate_degree()

    def strip_zeros(self):
        for power, coefficient in list(self.coefficients.items()):
            if not coefficient:
                self.coefficients.pop(power)
        if not self.coefficients:
            self.coefficients = {0: 0}

    def __repr__(self):
        coefficients = [str(self.coefficients.get(power, 0)) for power in range(self.degree() + 1)]
        answer = 'Polynomial ['
        answer += ', '.join(coefficients)
        answer += ']'
        return answer

    def str_terms(self):
        for power in sorted(self.coefficients.keys(), reverse=True):
            coefficient = self.coefficients[power]
            term = "-" if coefficient < 0 else ("+" if self.degree() != power else "")
            term += " " if self.degree() != power else ""
            term += str(abs(coefficient)) if abs(coefficient) != 1 or not power else ""
            term += "x" if power != 0 else ""
            term += f"^{power}" if power >= 2 else ""
            yield term
        if self.coefficients == [0]:
            yield "0"

    def __str__(self):
        return " ".join(self.str_terms())

    def __eq__(self, other):
        other = Polynomial(other)
        return self.coefficients == other.coefficients

    def __add__(self, other):
        add_coefficients = dict()
        other = Polynomial(other)
        for power in self.coefficients:
            add_coefficients[power] = self.coefficients[power] + other.coefficients.get(power, 0)
        for power in other.coefficients:
            if power not in self.coefficients:
                add_coefficients[power] = other.coefficients[power]
        return Polynomial(add_coefficients)

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        other = Polynomial(other)
        return self + other * -1

    def __rsub__(self, other):
        other = Polynomial(other)
        return (self - other) * -1

    def __call__(self, x):
        return sum([coefficient * x ** power for power, coefficient in self.coefficients.items()])

    def calculate_degree(self):
        self.calculated_degree = max(self.coefficients.keys())

    def degree(self):
        return self.calculated_degree

    def der(self, d=1):
        pass

    def __mul__(self, other):
        other = Polynomial(other)
        mul_coefficient = dict()
        for p1 in self.coefficients:
            for p2 in other.coefficients:
                coefficient1 = self.coefficients[p1]
                coefficient2 = other.coefficients[p2]
                mul_coefficient[p1 + p2] = mul_coefficient.get(p1 + p2, 0) + coefficient1 * coefficient2
        return Polynomial(mul_coefficient)

    def __rmul__(self, other):
        return self * other

    def __iter__(self):
        for _ in range(self.degree()):
            self.coefficients.items()

    def __next__(self):
        pass


class RealPolynomial(Polynomial):
    def find_root(self):
        pass


class QuadraticPolynomial(Polynomial):
    def solve(self):
        pass


if __name__ == "__main__":
    print(Polynomial(0))
    print(Polynomial())
