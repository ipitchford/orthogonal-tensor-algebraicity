# Stage 1 methodology review

Date: 2026-09-08. Reviewer: internal AI methodology reviewer (orthogonal_method). This is not external peer review or formal verification.

Frozen review archive SHA-256: `778194477fa5d4a67bed14b9823f38a67582c81f181bd947fbf4e101df02e7a6`.

## Recommendation and scope

**Accept on mathematical methodology. Publication-significance clearance withheld pending the editorial novelty decision.**

I read the complete scalar manuscript and fixed-covariant extension, the prior-work comparison, and the covariant and mutation-regression scripts. I checked that those manuscript files and the three replay scripts are byte-identical to their copies in the frozen archive. I independently recalculated the delicate proof transitions below and consulted the published Sam–Snowden Theorem 6.1 and Section 7.4. I did not inspect other reviewers' reports or edit the manuscripts. Confidence in mathematical adequacy: high, subject to the standard foundational results explicitly invoked. Confidence in historical novelty: not established by this review.

## Mathematical findings

1. **Scalar asymptotic normalization is consistent.** The chosen metric makes the skew-entry coordinates orthonormal, and the last-column map has the claimed horizontal isometry. The sphere-product volume counts both components. The two trace extrema contribute equally, including in even dimension when both lie in the identity component. Substituting the volume into the Gaussian integral gives the displayed gamma product and exponent. No unnoticed replacement of O(m) by SO(m) is present.

2. **The algebraicity obstruction covers all high ranks.** In the integer-exponent cases the indicated derivative grows logarithmically. In the half-integer cases its radial square-root amplitude contains a nonzero integral inverse power of pi after the Gaussian square root is removed. Rational coefficients and an algebraic radial singularity make the Puiseux coefficient arithmetic relevant; the manuscript's finite-column linear-algebra descent correctly extends the conclusion from Q(t) to C(t). The argument does not require a unique dominant complex singularity.

3. **The weighted Laplace extension is valid for every genuine fixed representation of one central parity.** At I the character value is dim W. At -I its parity sign cancels that of the compatible tensor degree, so there is no leading cancellation. A bounded character controls the complement, and smoothness controls the scaled neighborhoods even if the character takes negative or complex values elsewhere. The extra factor m^epsilon comes from the odd tensor degree. The coefficient asymptotic is consequently the stated positive multiple of the scalar one. Splitting an arbitrary W by central parity and applying parity extraction legitimately handles reducible representations. Excluding W=0, varying W, and virtual representations is necessary and is done explicitly.

4. **The low-rank formulas exhaust the stated representation classes.** For O(2), the rotation weights and the reflection contribution distinguish the trivial and determinant characters correctly; the U_k formula has multiplicity, not isotypic-dimension, normalization. For O(3), the spin recurrence has the exceptional zero boundary and the bulk characteristic root q of positive valuation. R q^j satisfies both equations, and coefficientwise recurrence supplies uniqueness. Projection by central parity then gives all O(3) irreducibles. Direct sums preserve algebraicity.

5. **The finite-generation step supplies the missing hypothesis for covariant D-finiteness.** Matrix coefficients and complete reducibility place every algebraic O(m) representation in a finite sum of tensor powers of its faithful self-dual defining representation. For a fixed output tensor degree d, the orthogonal pairing theorem lets every input-input contraction be removed as an invariant-algebra factor. The residual pairing uses at most d inputs, hence generates the module in bounded input degree as a symmetric-sequence module. Relations cannot obstruct this spanning argument. Taking the module projection for a summand preserves finite generation. The Schur–Weyl row bound is m. These are exactly the relevant boundedness and finite-generation conditions of Sam–Snowden Theorem 6.1; Hadamard multiplication by the factorial series supplies the ordinary-series conversion.

6. **The consequences are appropriately delimited.** The result excludes an algebraic generating function for each genuine fixed covariant in high rank, not arbitrary algorithms or every polynomial system. The dimension-ratio consequence follows from the asymptotic but is expressly not claimed as a new general principle. The extension is mathematically broader than the scalar theorem without requiring a new asymptotic technique.

## Replay evidence

- Archive SHA-256 independently matched the supplied frozen hash.
- `python3 candidate/verify_covariants.py`: PASS; 841 O(2) weight comparisons, 841 SO(3) spin comparisons through tensor degree 28, with both O(3) central parities checked.
- `python3 candidate/test_verifier.py`: PASS; the valid scalar verifier passed in normal, -O, and -OO modes; the rank-three divisor-4-to-5 mutant was rejected in all three modes.
- These runs diagnose finite formulas and verifier failure behavior. They are not computational proofs of the all-rank or all-representation theorem, and the mutation test is not an exhaustive fault model.

## Prioritized issues and remedies

**No mathematical blocking finding.** No additional manuscript repair is required by this methodology review.

**Publication gate, high priority:** the comparison itself records uninspected direct literature on the identical tensor-invariant series and concludes that the requested historical-newness/high-quality contribution has not been established. Mathematical acceptance must not be converted into a claim that this gap has closed. Remedy: the editorial novelty decision must either resolve the direct leads against the exact scalar and covariant theorem statements, or expressly decline the requested new-result publication claim. This reviewer supplies no high-three-star originality/significance endorsement.

**Optional clarity improvement, low priority:** the finite-generation proof could name the natural module surjection from B_m tensored with the sum of degrees 0 through d. Its existence is already explained by the contraction argument, so this is exposition only, not a proof gap or acceptance condition.

## Limits and source

I did not audit all of the foundational invariant-theory literature, establish historical priority, inspect every PDF page, perform external specialist review, or formally certify the theorem. The specific D-finiteness hypothesis was checked against the primary published text: [Sam–Snowden, Hilbert series for twisted commutative algebras, Theorem 6.1 and Section 7.4](https://alco.centre-mersenne.org/item/10.5802/alco.9.pdf). The assessment is an internal AI methodological opinion on the frozen bundle, separate from public release readiness.
