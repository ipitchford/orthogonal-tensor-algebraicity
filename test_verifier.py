#!/usr/bin/env python3
"""Regression: valid verifier passes and a semantic mutant fails in every mode."""
import json
from pathlib import Path
import subprocess
import sys


def main():
    source = Path(__file__).with_name("verify.py").read_text()
    needle = "negative[2 * n + 1]) / 4"
    if source.count(needle) != 1:
        raise RuntimeError("mutation location must be unique")
    mutant = source.replace(needle, "negative[2 * n + 1]) / 5")
    receipts = []
    for mode in [[], ["-O"], ["-OO"]]:
        good = subprocess.run([sys.executable, *mode, "-c", source], capture_output=True, text=True)
        bad = subprocess.run([sys.executable, *mode, "-c", mutant], capture_output=True, text=True)
        if good.returncode != 0 or json.loads(good.stdout)["status"] != "PASS":
            raise RuntimeError(("valid verifier failed", mode, good.stderr))
        if bad.returncode == 0 or "ValueError" not in bad.stderr or '"status": "PASS"' in bad.stdout:
            raise RuntimeError(("semantic mutant not rejected", mode, bad.stdout, bad.stderr))
        receipts.append({"mode": mode or ["normal"], "valid": "PASS", "mutant": "REJECTED"})
    print(json.dumps({"status": "PASS", "mutation": "rank-three divisor 4 to 5", "runs": receipts}, indent=2))


if __name__ == "__main__":
    main()
