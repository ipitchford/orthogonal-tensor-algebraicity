# The algebraicity threshold for orthogonal tensor multiplicities

Anonymous — version 0.1.0-candidate — unrefereed candidate.

For the defining representation V of O(m,C) and every fixed nonzero finite-dimensional algebraic representation W, the ordinary series of multiplicities Hom(W,V^tensor N) is D-finite, and algebraic exactly when m <= 3. The scalar specialization concerns reduced symmetric determinantal quotients in the symmetric-sequence convention, not finite-variable Hilbert series.

Read [the complete paper](paper.pdf), [accessible source](paper.md), [prior-work audit](CITATION_AUDIT.md), and [review response](RESPONSE_MATRIX.md). The scalar asymptotic and rank-three radical have exact classical antecedents. Historical priority for the classification is not established.

## Reproduce the finite diagnostics

Requires Python 3.10 or newer, standard library only. No downloads or third-party packages are required for replay.

```sh
python3 replay.py
python3 -O replay.py
```

Expected final status: PASS. This checks scalar hook/corner dimensions, rank-three walks, low-rank formulas, optimized-mode mutation rejection and the available package manifest. It does not prove the all-rank theorem. The latter rests on the written mathematical argument and named classical inputs.

To rebuild the PDF, install Pandoc and a working pdflatex distribution, then run:

```sh
pandoc paper.md --from=markdown+tex_math_single_backslash --standalone --pdf-engine=pdflatex -o paper.pdf
```

PDF timestamps can differ; mathematical source and archived artifact hashes are recorded separately. Python versions and CI are specified in ENVIRONMENT.txt and the workflow. This is not a hermetic environment.

## Package map

- `paper.md`, `paper.pdf`: complete integrated proof and prior-work discussion.
- `verify.py`, `verify_covariants.py`, `test_verifier.py`, `replay.py`: exact diagnostics and fail-closed controls.
- `CLAIMS.json`, `AI_INDEX.md`: claims and trust boundaries.
- `CITATION_AUDIT.md`, `SOURCE_RECORD.json`, `PROVENANCE.md`: source comparison and qualified catalogue provenance.
- `reviews/`, `RESPONSE_MATRIX.md`, `EDITORIAL_DECISION.md` when filed: internal editorial history and confirmation.
- `REPLAY_RECEIPT.json`, `PDF_QA.md`, `MANIFEST.sha256`: recorded checks and inventory.
- `CITATION.cff`, `.zenodo.json`: citation and archival metadata.
- `LICENSE`, `LICENSE-CODE`, `LICENSES.md`: component rights.

No machine-specific path is needed to reproduce the checks. Paths in unchanged historical internal-review reports refer only to the original review environment. Third-party full papers and the user's external review are not redistributed.
