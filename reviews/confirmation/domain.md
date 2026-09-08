# Domain and prior-art confirmation

Date: 8 September 2026. Recommendation: **Accept for the stated scoped, unrefereed candidate publication.** This is an internal AI domain assessment, not independent specialist peer review, a novelty certificate, or a high-three-star rating.

## Scope and freeze

Independently recomputed SHA-256 of `confirmation-v1.zip`: `2b3e4ccacf01ea9e2770d37e663b9c24af943120f40e5725b6efd2811bb1a0dc`. Extracted to the unique directory `/tmp/domain-confirm.xliyDO`. Read the complete `paper.md`, `CITATION_AUDIT.md`, `RESPONSE_MATRIX.md`, and only my preceding `reviews/substantive/domain.md` report. No other reviewer reports were read. This is a bounded attribution confirmation, not a fresh exhaustive literature search or code replay.

Independently inspected the supplied Regev PDF at printed pages 129–134 and the supplied Almkvist–Dicks–Formanek PDF at printed pages 192, 200–201 and 207. Rendered Regev page 134 and ADF page 207 to check formulas that text extraction obscured.

## Direct comparison

Regev Definition 3.1 distinguishes column divisibility from row divisibility. The row-even family with height bound m is exactly the manuscript's sum of f^(2 lambda). Theorem 3.3 supplies density 2^(1-m). Reading the displayed formula (F.4.5.1) gives the strip constant

`m^[m(m-1)/4] / m! * Gamma(3/2)^(-m) * product_{j=1}^m Gamma(1+j/2)`.

Using `Gamma(1+j/2)=(j/2)Gamma(j/2)` cancels the factorial and powers of two to give `m^alpha pi^(-m/2) product Gamma(j/2)`. Substitution of total degree `2n` introduces the additional `2^(-alpha)`. Together these give exactly the manuscript's `c_m`, including the row-parity density. The sentence below Regev's formula explicitly points back to Theorem 3.3 for the U family. Sections 3 and 14 and the abstract now attribute this scalar asymptotic appropriately; the compact-group argument is honestly presented as a rederivation.

ADF Theorem 2.1 is the compact-group tensor-algebra trace integral used here. Section 4.2 considers polynomial GL(2) representations restricted to SL(2), and establishes algebraicity by one-variable residue calculus. The representation context on page 201 makes its binary-form index d the degree of Sym^d(C^2). In particular, the page-207 radical indexed 2 is exactly `(1-sqrt((1-3t)/(1+t)))/(2t)`. This representation factors through SO(3); extracting even degrees gives O(3) invariants. Thus the manuscript's rank-three scalar attribution is exact, and it no longer rests on an isolated matching coefficient. ADF's all-binary-form algebraicity assertion cannot be read as an all-orthogonal-dimension result. The printed page has 93 at degree eight; the prior domain review already checked the author-hosted erratum correcting it to 91. I did not repeat that web check here.

Cohen–Regev 1988 remains explicitly uninspected. Its absence does not impede attribution of the scalar result now established directly in Regev 1981. It also must not be interpreted as evidence of historical priority for the residual classification. The manuscript observes both limits.

## Disposition of preceding concerns

The earlier major-revision recommendation concerned a novelty-led, high-three-star publication premise and unresolved direct source comparisons. The supplied primary texts and revised attribution resolve the direct comparison and fingerprint concerns. The current authorized scope explicitly drops the stronger significance/priority premise. No additional source retrieval is required to establish the now-stated scalar attribution.

The all-fixed-type theorem, central-parity treatment, explicit low-rank formulas and virtual-difference counterexample form a coherent classification/synthesis. The paper acknowledges that weighted tensor-multiplicity asymptotics, dimension-ratio behavior, D-finiteness and the algebraic-function obstruction are established tools. It does not equate their assembly with a verified first-ever theorem. I found no remaining fatal attribution issue or immediate scientific counterexample in this bounded confirmation. The general proof's correctness remains subject to the method and adversarial confirmation roles; this recommendation does not substitute for those checks.

No mandatory manuscript revisions from this role. Preserve the unrefereed status, the no-priority statement, the unavailable-source limitation and the separation of finite diagnostics from the written all-rank argument in any public description. Acceptance here means the repaired domain/prior-art gate is satisfied for that scope; it establishes neither independent validation nor historical novelty.
