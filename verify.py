#!/usr/bin/env python3
"""Exact diagnostic checks, not a computational proof of the all-rank theorem.

Run with Python 3.10+; uses only the standard library. No network or local inputs.
"""

from fractions import Fraction as Q
from functools import lru_cache
from math import comb, factorial
import json


def require(condition, detail="exact diagnostic failed"):
    """Release checks must remain active under python -O and -OO."""
    if not condition:
        raise ValueError(detail)


def partitions(n, ceiling=None):
    if n == 0:
        yield ()
        return
    for first in range(min(n, n if ceiling is None else ceiling), 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def hook_dimension(shape):
    denominator = 1
    for i, row in enumerate(shape):
        for j in range(row):
            denominator *= row - j + sum(v > j for v in shape[i + 1:])
    numerator = factorial(sum(shape))
    require(numerator % denominator == 0, "nonintegral hook dimension")
    return numerator // denominator


@lru_cache(None)
def corner_dimension(shape):
    if not shape:
        return 1
    answer = 0
    for i, row in enumerate(shape):
        if i + 1 == len(shape) or row > shape[i + 1]:
            smaller = list(shape)
            smaller[i] -= 1
            answer += corner_dimension(tuple(v for v in smaller if v))
    return answer


def coefficient_table(max_rank, max_n):
    rows = [[0] * (max_n + 1) for _ in range(max_rank + 1)]
    compared = 0
    for n in range(max_n + 1):
        for lam in partitions(n):
            if len(lam) > max_rank:
                continue
            shape = tuple(2 * v for v in lam)
            value = hook_dimension(shape)
            require(value == corner_dimension(shape), (shape, value))
            compared += 1
            for rank in range(len(lam), max_rank + 1):
                rows[rank][n] += value
    return rows, compared


def spin_one_moments(max_degree):
    """Multiplicity propagation using W_j tensor W_1; not tableau enumeration."""
    multiplicities = {0: 1}
    answer = [1]
    for _ in range(max_degree):
        updated = {}
        for spin, multiplicity in multiplicities.items():
            destinations = (1,) if spin == 0 else (spin - 1, spin, spin + 1)
            for dest in destinations:
                updated[dest] = updated.get(dest, 0) + multiplicity
        multiplicities = updated
        answer.append(multiplicities.get(0, 0))
    return answer


def binomial_series(exponent, scale, degree):
    """Coefficients of (1+scale*t)^exponent over Q."""
    values = [Q(1)]
    for k in range(1, degree + 1):
        values.append(values[-1] * (exponent - k + 1) * scale / k)
    return values


def multiply(left, right, degree):
    return [sum((left[i] * right[k - i] for i in range(k + 1)), Q(0))
            for k in range(degree + 1)]


def rank_three_radical(max_n):
    degree = 2 * max_n + 1
    positive = multiply(binomial_series(Q(1, 2), 3, degree),
                        binomial_series(Q(-1, 2), -1, degree), degree)
    negative = multiply(binomial_series(Q(1, 2), -3, degree),
                        binomial_series(Q(-1, 2), 1, degree), degree)
    return [(positive[2 * n + 1] - negative[2 * n + 1]) / 4
            for n in range(max_n + 1)]


def stripped_gamma(j):
    """Gamma(j/2), with the sqrt(pi) removed if j is odd."""
    if j % 2 == 0:
        return Q(factorial(j // 2 - 1))
    k = (j - 1) // 2
    return Q(factorial(2 * k), 4 ** k * factorial(k))


def constant_square(rank):
    """Exact A_m^2 where c_m = A_m*pi^(-floor(m/2)/2)."""
    dimension = rank * (rank - 1) // 2
    value = Q(2) ** (2 - 2 * rank) * Q(rank, 2) ** dimension
    for j in range(1, rank + 1):
        value *= stripped_gamma(j) ** 2
    return value


def main():
    max_n = 14
    max_rank = 8
    table, shape_checks = coefficient_table(max_rank, max_n)
    spin_moments = spin_one_moments(2 * max_n)
    radicals = rank_three_radical(max_n)
    rank_two_expansion = binomial_series(Q(-1, 2), -4, max_n)
    for n in range(max_n + 1):
        require(table[0][n] == int(n == 0))
        require(table[1][n] == 1)
        expected_two = 1 if n == 0 else comb(2 * n, n) // 2
        require(table[2][n] == expected_two)
        require(table[2][n] == (rank_two_expansion[n] + int(n == 0)) / 2)
        require(table[3][n] == spin_moments[2 * n] == radicals[n], ("rank-three", n))
        catalan = comb(2 * n, n) // (n + 1)
        require(table[4][n] == catalan * (catalan + 1) // 2)
        for rank in range(max_rank + 1):
            if n <= rank:
                unrestricted = factorial(2 * n) // (2 ** n * factorial(n))
                require(table[rank][n] == unrestricted)
            if rank:
                require(table[rank][n] >= table[rank - 1][n])

    # Independent constants from binomial, Riordan and Catalan formulas.
    require(constant_square(2) == Q(1, 4))
    require(constant_square(3) == Q(27, 512))
    require(constant_square(4) == Q(1, 4))

    # Polynomial witnesses are identities of truncated exact power series.
    witness_degree = 20
    f2 = binomial_series(Q(-1, 2), -4, witness_degree)
    f2 = [(v + int(i == 0)) / 2 for i, v in enumerate(f2)]
    shifted = [2 * v - int(i == 0) for i, v in enumerate(f2)]
    square = multiply(shifted, shifted, witness_degree)
    for i in range(witness_degree + 1):
        require(square[i] - (4 * square[i-1] if i else 0) == int(i == 0),
                ("rank-two polynomial witness", i))
    f3 = rank_three_radical(witness_degree)
    square = multiply(f3, f3, witness_degree)
    fourth = multiply(square, square, witness_degree)
    for i in range(witness_degree + 1):
        lhs = sum(c * fourth[i-j] for j, c in [(1, 4), (2, -8), (3, 4)] if i >= j)
        lhs -= sum(c * square[i-j] for j, c in [(0, 1), (1, 2), (2, -3)] if i >= j)
        require(lhs + int(i == 0) == 0, ("rank-three polynomial witness", i))

    # These deliberately incorrect normalizations must disagree with exact data.
    require(table[2][2] != comb(4, 2))  # O(2), not just SO(2).
    require(table[2][2] != comb(4, 2) // 3)  # Not the Catalan sequence.
    require(table[4][2] != (comb(4, 2) // 3) ** 2)  # O(4), not SO(4).

    constant_rows = []
    for rank in range(2, 17):
        dimension = rank * (rank - 1) // 2
        pi_power = Q(-(rank // 2), 2)
        alpha = Q(dimension, 2)
        if rank >= 4:
            if dimension % 2 == 0:
                require(rank % 4 in (0, 1))
                obstruction = "logarithm"
            else:
                require(rank % 4 in (2, 3))
                require(-(pi_power + Q(1, 2)) >= 1)
                require((pi_power + Q(1, 2)).denominator == 1)
                obstruction = "transcendental square-root amplitude"
        else:
            obstruction = "none; explicit algebraic formula"
        constant_rows.append({"rank": rank, "alpha": str(alpha),
                              "A_squared": str(constant_square(rank)),
                              "pi_exponent_in_c": str(pi_power),
                              "obstruction": obstruction})

    print(json.dumps({
        "status": "PASS",
        "scope": "Finite exact diagnostic checks; all-rank proof is SOLUTION.md",
        "max_rank": max_rank,
        "max_n": max_n,
        "hook_vs_corner_shapes": shape_checks,
        "polynomial_witness_degree": witness_degree,
        "constant_evidence_boundary": "Ranks 2,3,4 matched to closed-form asymptotics; ranks 5..16 evaluate the proved formula, not independent estimates",
        "coefficient_rows": table,
        "constant_checks": constant_rows,
        "negative_controls": "All three incorrect formulas rejected",
        "dependencies": "Python standard library only"
    }, indent=2))


if __name__ == "__main__":
    main()
