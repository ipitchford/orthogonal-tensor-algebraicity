# Editor-in-Chief internal editorial report

Date: 8 September 2026.

Frozen submission: `revised-review.zip`, SHA-256 `778194477fa5d4a67bed14b9823f38a67582c81f181bd947fbf4e101df02e7a6` (hash checked).

Role and scope: internal AI editorial assessment, not independent human peer review, a priority certificate, or a complete line-by-line proof audit. I read the main statement/conventions, the complete covariant extension, the prior-work comparison, the novelty report and response, and the package README. I did not inspect other editorial reports. I have not obtained the missing primary-source texts or independently rerun the code in this role.

## Decision

**Major revisions; HOLD for the requested research publication.** This is not a rejection of the mathematical argument. It is a finding that the frozen package does not yet meet the user's explicit request to establish a genuinely nontrivial new classification through precise prior-work comparison. Do not create an irreversible publication presenting that request as satisfied on the strength of this report.

The new fixed-covariant statement is a real enlargement of the scalar theorem: it classifies every fixed nonzero algebraic orthogonal representation, gives all low-dimensional multiplicity formulas, and proves the finite-generation hypothesis needed for D-finiteness. Its consequences are clear and appropriately limited. However, an enlargement relative to the previous draft is not evidence of historical novelty. The package explicitly leaves open a source on the identical invariant tensor algebra and the directly signposted asymptotic literature. Its own conclusion that novelty is not cleared is correct.

## Strengths and coherent contribution

The central-parity argument explains why the two dominant character-integral contributions add, and why virtual representations and varying types are excluded. The low-rank formulas and the bounded-output contraction argument give the extension substance beyond merely replacing an invariant by a character in an integral. The obstruction separates D-finiteness from algebraicity without overstating algorithmic consequences. The distinction between finite-variable commutative Hilbert series and symmetric-sequence/tensor-multiplicity series is especially important and is now prominent.

The normalization comparison with Regev's accessible restatement is useful: it tracks total degree, compressed degree, and row versus column parity instead of claiming a new asymptotic constant. This improves scholarship and credibility even though it does not close the direct-source gap.

## Prioritized required revisions

### 1. Blocking: adjudicate the identical-object prior-art lead

Location: `PRIOR_WORK_COMPARISON.md`, claim-level table, Almkvist--Dicks--Formanek (1985) row, and its final decision boundary.

The Hilbert series of invariant tensors is identified as exactly the same scalar series. The 1985 paper is therefore a direct collision risk, not a generic related-work reference. Its erratum's rank-three coefficient fingerprint makes that relevance concrete. Full-text unavailability does not establish either overlap or non-overlap. Obtain an authorized copy or a sufficiently precise reliable theorem statement and compare the groups, defining representations, ordinary versus exponential normalization, algebraicity/transcendence assertions, and any isotypic/covariant scope. Record exact theorem/page locations. If the full classification or covariant consequence follows there, reframe or pivot rather than announce novelty.

### 2. Blocking: finish the specific comparison requested by the supplied review

Location: `PRIOR_WORK_COMPARISON.md`, Cohen--Regev/Regev rows and exact-constant translation.

The 2010 restatement checks a useful unrestricted strip formula but does not establish the exact coverage of the directly cited 1981 and 1988 results. Determine whether their congruence restrictions and weighted/multiplicity families already supply the present asymptotic input in full generality. Separate an old asymptotic theorem, a new inference from it, and a genuinely new classification. A concise proof obtained from old ingredients can be publishable, but its novelty must be stated at the inference level and not transferred to its inputs.

### 3. Major: substantiate the residual contribution and significance after that comparison

Location: `COVARIANT_EXTENSION.md`, Sections 1, 4, and 5; `PRIOR_WORK_COMPARISON.md`, substantive-extension discussion.

The fixed-type robustness statement is clear and nontrivial in scope. Nonetheless its high-rank proof is a short character-weighted adaptation of the scalar proof, while dimension-ratio asymptotics are expressly acknowledged as classical. Provide a precise residual theorem absent from the inspected primary results and explain a concrete use beyond rephrasing 'D-finite but not algebraic'. A worked determinant or other nontrivial fixed-type example, with the exact prior theorem contrasted, would make that contribution easier to assess. Do not demand an artificial application or imply a complexity bound; the present exclusions are sound but limited.

### 4. Minor: make the release manuscript match its proposed contribution

Location: main manuscript Section 1 and package README.

The main title and theorem foreground the scalar classification, while the proposed significance upgrade is in a companion PDF. If the extension becomes the publishable contribution, integrate its theorem and consequences into the principal manuscript or make the two-part structure explicit in the title, abstract, contents, and citation metadata. The current package is intelligible for review, but a public article should not hide its claimed principal advance in a supplementary document.

## Significance and assurance assessment

I cannot support a high-three-star overall assessment from this frozen record. The extension improves scope and exposition, but originality remains unestablished at precisely the points that govern that rating. An indicative **high-two-star overall assessment remains reasonable, with low-three-star potential conditional on the source audit**; this is not a mechanical score or a prediction of external review. I make no negative theorem claim that the result is already known: that too would exceed the evidence.

No substantive mathematical defect is identified in my scoped reading, but the specialist roles must adjudicate proof correctness. The explicit-exception/mutation repairs and bounded diagnostics are appropriate assurance improvements, not substitutes for all-rank proof or novelty.

## Reconsideration condition

Return with the exact direct-source comparisons and a revised residual-contribution statement. If those sources cannot be lawfully obtained through available routes, report a genuine novelty gate rather than treating elapsed effort or the user's persistence instruction as authorization to lower the publication standard. Publishing a carefully labelled expository synthesis would be a different proposition from the requested genuinely new classification and requires an explicit change of scope.
