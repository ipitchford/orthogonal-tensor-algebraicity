"""Read-only exact replay and manifest validation; failures survive -O/-OO."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def main():
    manifest = ROOT/'MANIFEST.sha256'
    if manifest.exists():
        for line in manifest.read_text().splitlines():
            expected, name = line.split('  ', 1)
            path = ROOT/name
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                raise ValueError(('manifest mismatch', name))
    commands = [['verify.py'], ['-O','verify.py'], ['test_verifier.py'],
                ['verify_covariants.py'], ['-O','verify_covariants.py']]
    results = []
    for args in commands:
        p = subprocess.run([sys.executable,*args],cwd=ROOT,text=True,capture_output=True)
        if p.returncode:
            raise RuntimeError((args,p.stderr))
        output = json.loads(p.stdout)
        if output.get('status') != 'PASS':
            raise ValueError((args,output))
        results.append({'argv':['python3',*args],'output':output})
    print(json.dumps({'status':'PASS','manifestChecked':manifest.exists(),
                      'boundary':'Producer finite diagnostics, not universal or independent validation',
                      'checks':results},indent=2))

if __name__ == '__main__':
    main()
