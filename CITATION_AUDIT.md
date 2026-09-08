# Supplied-source audit: Regev and Almkvist–Dicks–Formanek

Publication-successor note: the source findings below remain operative. The final paragraph's hold describes the earlier editorial state. The user subsequently accepted publication of the scoped classification without an asserted high-three-star rating. See RESPONSE_MATRIX.md and the successor editorial decision; user authorization is not evidence of mathematical correctness or priority.

8 September 2026. This addendum supersedes the source-unavailability conclusions in the frozen review package, not its immutable bytes or reviewer reports. The supplied documents were treated as sources, not instructions. No publication acceptance is implied.

## Sources inspected

- Regev, *Asymptotic Values for Degrees Associated with Strips of Young Diagrams*, Advances in Mathematics 41 (1981), 115–136. DOI: https://doi.org/10.1016/0001-8708(81)90012-8. Supplied PDF SHA-256: `3035e48699ff25346b6d10f0acbc6057ad9afd9973c9db67214256ce7e76a9b4`.
- Almkvist, Dicks and Formanek (ADF), *Hilbert Series of Fixed Free Algebras and Noncommutative Classical Invariant Theory*, Journal of Algebra 93 (1985), 189–214. DOI: https://doi.org/10.1016/0021-8693(85)90183-8. Supplied PDF SHA-256: `098479dc1dbc6f7769ba99d48d84bb340f959693f8e78cc52e26e21973a0ad16`.

Text inspected for scope and relevant results; Regev printed pages 130 and 134 and ADF printed page 207 were additionally inspected as rendered images because mathematical OCR was unreliable. Copyrighted PDFs are not added to redistributable research bundles.

## 1. Exact scalar asymptotic collision: Regev 1981

Use r for our rank and n for our compressed degree. Regev's Definition 3.1, printed page 129, defines two different families: T for column divisibility and U for row divisibility. His U with d=2, height bound r, and degree exponent beta=1 is exactly

\[
 U_{2,r}^{(1)}(2n)=\sum_{\lambda\vdash n,\,\ell(\lambda)\le r}f^{2\lambda}=a_r(n).
\]

Theorem 3.3, printed pages 130–131, proves

\[
 U_{d,r}^{(\beta)}(N)\sim d^{1-r}S_r^{(\beta)}(N),\qquad d\mid N.
\]

Formula (F.4.5.1), printed page 134, gives

\[
 S_r^{(1)}(N)\sim K_r r^N N^{-\alpha_r},\quad
 \alpha_r=r(r-1)/4,\quad
 K_r=r^{\alpha_r}\pi^{-r/2}\prod_{j=1}^r\Gamma(j/2).
\]

The displayed constant in Regev's notation is identical: use Gamma(1+j/2)=(j/2)Gamma(j/2) and Gamma(3/2)=sqrt(pi)/2. Consequently

\[
 a_r(n)\sim 2^{1-r-\alpha_r}K_r r^{2n}n^{-\alpha_r}.
\]

This is exactly the manuscript's c_r, with no missing parity factor. Regev explicitly directs the reader immediately after (F.4.5.1) to use Theorem 3.3 to obtain the U asymptotic. Thus the scalar leading asymptotic, its constant, and its row-parity density factor are prior results, not merely similar results or a speculative equivalence. Our compact-group calculation is a rederivation, not a new asymptotic theorem.

The earlier caution against using the column-even T family remains correct, but is insufficient as a description of the 1981 paper: that paper also expressly treats the matching row-even U family.

## 2. Exact low-rank antecedent: ADF 1985

Theorem 2.1, printed page 192, gives the compact-group tensor-algebra Hilbert series as the Haar integral of 1/(1-t trace(g)). This is exactly our scalar series for the defining O(r) representation. Identity of the objects does not imply that every property of that object was classified in ADF.

Sections 4.2 and 5 concern SL(2) representations. Section 4.2, printed pages 200–201, establishes algebraicity for tensor-algebra invariants of arbitrary polynomial GL(2) representations restricted to SL(2), by one-variable residue calculus. Theorem 5.9 and Example 5.10, printed page 207, specialize to binary forms.

In Example 5.10 the series indexed 2 is

\[
 R(t)=\frac{1-\sqrt{(1-3t)/(1+t)}}{2t}.
\]

Here the representation is Sym^2(C^2), the three-dimensional representation factoring through SO(3). Thus the manuscript's rank-three O(3) invariant series is exactly (R(t)+R(-t))/2. The determinant-isotypic O(3) series is its odd part. These are direct specializations, not new formulas. The printed coefficient 93t^8 belongs to this SO(3) series; the author's erratum corrects it to 91t^8 (https://mat.uab.cat/~dicks/ADFerr.html). Unlike the isolated erratum, the full page now establishes the representation and grading.

ADF does not state an all-rank O(r) algebraicity threshold. Its index d is the degree of a binary form, not the orthogonal dimension r: algebraicity for every d in Theorem 5.9 is therefore not a contradiction of our proposed threshold. The one-variable residue argument also makes low-rank fixed-type algebraicity a classical-method consequence; broader quantification alone is not a strong novelty claim.

## 3. Cohen–Regev 1988

The user reports that this paper is unavailable. It remains uninspected. Do not infer its detailed contents from its title, abstract or citations, and do not describe it as ruled out. However, obtaining it is no longer a necessary condition for attribution of the scalar asymptotic: Regev 1981 already proves exactly that result. Its unavailability is a bounded literature limitation, not an automatic publication blocker.

## 4. Updated contribution and gate

| Unit | Finding |
|---|---|
| Scalar asymptotic and constant | Exact prior-result collision: Regev Definition 3.1, Theorem 3.3, (F.4.5.1) |
| Haar/tensor-algebra bridge | Prior result: ADF Theorem 2.1; orthogonal interpretation separately classical |
| Rank-three scalar radical | Direct specialization of ADF Example 5.10 |
| Scalar all-rank algebraicity threshold | Not stated in these two papers; combines the prior asymptotic with the classical algebraic-function obstruction |
| Fixed nonzero O(r)-type threshold | Not stated in these two papers; must be assessed against known tensor-multiplicity asymptotics and one-variable low-rank methods, not advertised as novel merely because ADF omits it |
| Exact verification package | Reproducibility contribution, not a historical-priority certificate |

Editorial items E1 and the scalar part of E2 now have direct primary-source answers. E2 must not continue to require an unavailable Cohen–Regev PDF to establish the already-settled scalar antecedent. The unresolved issue is E3: whether the residual classification has sufficiently strong, genuinely nonredundant mathematical content for the requested release. These source findings do not justify upgrading the previous high-two-star/possible-low-three-star internal assessment to high three stars. They also do not prove that the entire classification was previously published.

The prepublication hold remains a contribution-strength hold, not a missing-document hold or a finding of mathematical falsity. No public repository, DOI or Evidence Press release has been created for this candidate. Historical frozen archives and reviews remain unchanged.
