import subprocess

from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    print('Running flutter test')

    result = subprocess.run('flutter test --machine', shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print('Failed test see below: \n', result.stdout)
        return result.returncode

    print('All Test Succeeded: \n', result.stdout)

    return 0