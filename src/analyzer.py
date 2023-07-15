import subprocess

from typing import Sequence

def main(argv: Sequence[str] | None = None) -> int:
    print('Running flutter analyzer')

    result = subprocess.run('flutter analyze', shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print('Failed analyzer see below: \n', result.stdout)
        return result.returncode

    print('Analysis Succeeded: \n', result.stdout)

    return 0
