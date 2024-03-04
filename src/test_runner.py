import subprocess

from typing import Sequence

def main(argv: Sequence[str] | None = None) -> int:
    print('Running flutter test')

    cmd = 'flutter test --machine'

    if argv is not None:
        cmd = '%s %s' %(cmd, ' '.join(argv[1:]))

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print('Failed test see below: \n', result.stdout)
        return result.returncode

    print('All Test Succeeded: \n', result.stdout)

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
