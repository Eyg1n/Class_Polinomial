# test_polynomial.py

import pytest
import random

from cl import Polynomial, RealPolynomial, QuadraticPolynomial


def test_coefficients():
    p1 = Polynomial([1, 2, 3, 4])
    assert p1.coefficients == {0: 1, 1: 2, 2: 3, 3: 4}
    assert str(p1) == "4x^3 + 3x^2 + 2x + 1"

    p2 = Polynomial([1, 0, 0, 4, 0])
    assert p2.coefficients == {0: 1, 3: 4}
    assert str(p2) == "4x^3 + 1"

    p3 = Polynomial({0: 1, 3: 4, 10: 0})
    assert p3.coefficients == {3: 4, 0: 1}
    assert str(p3) == "4x^3 + 1"

    p4 = Polynomial([1, 3, 4, 6, 0, 1])
    assert p4.coefficients == {0: 1, 1: 3, 2: 4, 3: 6, 5: 1}

    p5 = Polynomial(5)
    assert p5.coefficients == {0: 5}

    p6 = Polynomial()
    assert p6.coefficients == {0: 0}
    assert str(p6) == '0'

    p7 = Polynomial(0)
    assert p7.coefficients == {0: 0}
    assert str(p7) == '0'

    p8 = Polynomial(-1)
    assert p8.coefficients == {0: -1}
    assert str(p8) == '-1'


def test_init():
    poly_list = Polynomial([0, 1, 0, -2, 3, 0])
    assert str(poly_list) == '3x^4 - 2x^3 + x'
    assert repr(poly_list) == 'Polynomial [0, 1, 0, -2, 3]'

    poly_copy = Polynomial(poly_list)
    assert str(poly_copy) == '3x^4 - 2x^3 + x'
    assert repr(poly_copy) == 'Polynomial [0, 1, 0, -2, 3]'

    poly_dict = Polynomial({5: 3, 0: -1, 10: 7, 2: -4})
    assert str(poly_dict) == '7x^10 + 3x^5 - 4x^2 - 1'
    assert repr(poly_dict) == 'Polynomial [-1, 0, -4, 0, 0, 3, 0, 0, 0, 0, 7]'

    poly_args = Polynomial(1, 2, -3, 0, 5)
    assert str(poly_args) == '5x^4 - 3x^2 + 2x + 1'
    assert repr(poly_args) == 'Polynomial [1, 2, -3, 0, 5]'

    poly_const = Polynomial(10)
    assert str(poly_const) == '10'
    assert repr(poly_const) == 'Polynomial [10]'


def test_eq():
    poly_zero = Polynomial([0] * 100)
    assert poly_zero == Polynomial(0)

    poly_zero_tail = Polynomial([1, 2, 0, -3, 0, 0, 0, 0, 0])
    assert poly_zero_tail == Polynomial([1, 2, 0, -3])


def test_add():
    poly_lhs = Polynomial([2, 5, 0, 3, 2])
    poly_rhs = Polynomial(1, 3, 5, 0, 1, 0, 3)

    assert poly_lhs + poly_rhs == poly_rhs + poly_lhs
    assert str(poly_lhs + poly_rhs) == '3x^6 + 3x^4 + 3x^3 + 5x^2 + 8x + 3'
    assert str(14 + poly_lhs + 5) == '2x^4 + 3x^3 + 5x + 21'

    poly_lhs = Polynomial([2, 1, 2, 1])
    poly_rhs = Polynomial({3: 1, 1: 1, 0: 2, 2: 2})
    assert str(1 + poly_rhs + 2 + poly_lhs + 3) == '2x^3 + 4x^2 + 2x + 10'
    poly_3 = Polynomial([2, 1, 2, 1])
    poly_2 = Polynomial(poly_3)
    poly_4 = Polynomial({1: 3, 100: 100})
    poly_3 += poly_4
    assert poly_3 == poly_2 + poly_4

    poly_lhs += poly_rhs
    assert str(poly_lhs) == '2x^3 + 4x^2 + 2x + 4'


def test_der():
    poly = Polynomial([0, 4, 2, 2, 2, 1, 5])
    print(poly)
    assert str(poly.der(0)) == str(poly)
    print(poly.der())
    assert str(poly.der()) == '30x^5 + 5x^4 + 8x^3 + 6x^2 + 4x + 4'
    assert str(poly.der(5)) == '3600x + 120'


def test_deg():
    poly_list = Polynomial([0, 1, 0, -2, 3, 0, 0])
    assert poly_list.degree() == 4

    poly_dict = Polynomial({5: 3, 0: -1, 10: 7, 2: -4})
    assert poly_dict.degree() == 10

    poly_const = Polynomial(10)
    assert poly_const.degree() == 0


def test_sub():
    poly_lhs = Polynomial([1, 4, 1, 3])
    poly_rhs = Polynomial([4, 5, 5, 3])

    assert str(poly_lhs - poly_rhs) == '-4x^2 - x - 3'
    assert str(50 - poly_lhs - 4) == '-3x^3 - x^2 - 4x + 45'

    poly_lhs = Polynomial([1, 4, 1, 3])
    poly_rhs = Polynomial([4, 5, 5, 3])

    assert (poly_lhs - poly_rhs).coefficients == {0: -3, 1: -1, 2: -4}
    assert str(poly_lhs - poly_rhs) == '-4x^2 - x - 3'
    assert str(50 - poly_lhs - 4) == '-3x^3 - x^2 - 4x + 45'


def test_call():
    poly = Polynomial([2, 1, 4, 1, 2, 5, 0])
    assert poly(0) == 2
    assert poly(1) == 15
    assert poly(2) == 220


def test_mul():
    poly_lhs = Polynomial([9, 6, 1, 1, 9, 9, 8])
    poly_rhs = Polynomial([7, 5, 1, 0, 6])
    assert poly_lhs * poly_rhs == poly_rhs * poly_lhs
    assert str(
        poly_lhs * poly_rhs) == '48x^10 + 54x^9 + 62x^8 + 55x^7 + 116x^6 + 145x^5 + 123x^4 + 18x^3 + 46x^2 + 87x + 63'


def test_iter():
    poly = Polynomial([1, 1, 5, 3, 9])
    print(poly, poly.degree())
    pairs = [i for i in poly]
    print(pairs)
    true_pairs = [(0, 1), (1, 1), (2, 5), (3, 3), (4, 9)]
    for i in range(len(true_pairs)):
        assert pairs[i] == true_pairs[i]


def test_real_poly():
    poly = RealPolynomial([2, 2, 9, 9, 7, 1, 8, 8])
    eps = 1e-6
    root = poly.find_root()
    assert abs(poly(root)) < eps


def test_quadratic():
    poly = QuadraticPolynomial([-15, 7, 2])
    assert sorted(poly.solve()) == [-5.0, 1.5]
