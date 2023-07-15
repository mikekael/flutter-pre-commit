import argparse
import subprocess

from typing import Sequence, List

def fix_issues(filename: str, lint_codes: List[str]) -> int:
    options = [
        '--apply',
    ]

    print('Lint codes: {}'.format(lint_codes[0]))

    if len(lint_codes) > 0:
        options.append(f'--code={lint_codes[0]}')

    print('Fixing linter issues for {}'.format(filename))

    cmd = f'dart fix {" ".join(options)} {filename}'

    print('Running CMD: {}'.format(cmd))

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print('Code fix failed due to error: \n', result.stdout)
        return result.returncode

    print('Fix done: {}'.format(result.stdout))
    return 0

def fix_style(filename: str) -> int:
    print('Formatting code for {}'.format(filename))

    cmd = f'dart format {filename}'

    print('Running CMD: {}'.format(cmd))

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print('Code fix failed due to error: \n', result.stdout)
        return result.returncode

    print('Format done: {}'.format(result.stdout))
    return 0

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    parser.add_argument('--lint_codes', nargs='*', help="Lint codes to be fixed automatically", type=str)
    args = parser.parse_args(argv)

    lint_codes = args.lint_codes
    if lint_codes == '*' or lint_codes is None:
        lint_codes = []

    for filename in args.filenames:
        return_code = fix_issues(filename=filename, lint_codes=lint_codes)

        if return_code != 0:
            return return_code

        return_code = fix_style(filename=filename)

        if return_code != 0:
            return return_code

    return 0

if __name__ == '__main__':
    raise SystemExit(main())