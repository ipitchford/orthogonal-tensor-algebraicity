#!/usr/bin/env python3
"""Exact finite diagnostics for O(2), O(3) fixed-type formulas."""
from math import comb
import json
from verify import Q, binomial_series, multiply, require


def inverse(a, degree):
    require(a[0] != 0)
    b = [1 / a[0]]
    for n in range(1, degree + 1):
        b.append(-sum(a[i] * b[n-i] for i in range(1, n+1)) / a[0])
    return b


def main():
    degree = 28
    compressed = binomial_series(Q(1, 2), -4, degree + 1)
    s = [compressed[n//2] if n % 2 == 0 else Q(0) for n in range(degree+2)]
    q = [-s[n+1] / 2 for n in range(degree+1)]
    compressed = binomial_series(Q(-1, 2), -4, degree)
    invs = [compressed[n//2] if n % 2 == 0 else Q(0) for n in range(degree+1)]
    power = [Q(1)] + [Q(0)] * degree
    checks2 = 0
    for k in range(degree+1):
        formula = multiply(power, invs, degree)
        for n in range(degree+1):
            expected = comb(n, (n-k)//2) if n >= k and (n-k) % 2 == 0 else 0
            require(formula[n] == expected, ("O2 weight", k, n))
            checks2 += 1
        power = multiply(power, q, degree)

    # sqrt(1-2t-3t^2) = sqrt(1-3t)*sqrt(1+t).
    radical = multiply(binomial_series(Q(1, 2), -3, degree+1),
                       binomial_series(Q(1, 2), 1, degree+1), degree+1)
    q = [(-int(n == 0) - radical[n+1]) / 2 for n in range(degree+1)]
    denominator = [Q(1)] + [-q[n-1] for n in range(1, degree+1)]
    r = inverse(denominator, degree)
    walks = [[0]*(degree+1) for _ in range(degree+1)]
    walks[0][0] = 1
    for n in range(degree):
        for j in range(degree+1):
            for dest in ((1,) if j == 0 else (j-1, j, j+1)):
                if dest <= degree:
                    walks[dest][n+1] += walks[j][n]
    power = [Q(1)] + [Q(0)]*degree
    checks3 = 0
    for j in range(degree+1):
        formula = multiply(r, power, degree)
        for n in range(degree+1):
            # Independent character expansion: multiplicity = weight_j-weight_(j+1).
            weights = {0: 1}
            for _ in range(n):
                updated = {}
                for weight, count in weights.items():
                    for step in (-1, 0, 1):
                        updated[weight+step] = updated.get(weight+step, 0) + count
                weights = updated
            require(formula[n] == walks[j][n] == weights.get(j, 0)-weights.get(j+1, 0),
                    ("SO3 spin", j, n))
            for parity in (0, 1):
                projected = formula[n] * (1 + (-1)**(n+parity)) / 2
                require(projected == (walks[j][n] if n % 2 == parity else 0))
            checks3 += 1
        power = multiply(power, q, degree)
    for n in range(degree+1):
        require(sum((2*j+1)*walks[j][n] for j in range(degree+1)) == 3**n)
    print(json.dumps({"status": "PASS", "degree": degree,
                      "O2_weight_checks": checks2, "SO3_spin_checks": checks3,
                      "O3_both_parities_checked": True,
                      "scope": "Finite low-rank formulas only; no novelty or all-rank certificate"}, indent=2))


if __name__ == "__main__":
    main()
