import argparse
from doltpy.dolt import Dolt
from doltpy_etl.loaders import load_to_dolt, resolve_loaders


def loader(dolt_load_module: str, dolt_dir: str, commit: bool, message: str, dry_run: bool, branch: str):
    print(
        '''Commencing load to Dolt with the following options, and the following options
                - module    {dolt_load_module}
                - dolt_dir  {dolt_dir}
                - commit    {commit}
                - branch    {branch}
        '''.format(dolt_load_module=dolt_load_module,
                   dolt_dir=dolt_dir,
                   commit=commit,
                   branch=branch)
    )

    if not dry_run:
        load_to_dolt(Dolt(dolt_dir), resolve_loaders(dolt_load_module), commit, message, branch)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dolt_load_module', help='Fully qualified path to a module providing a set of loaders')
    parser.add_argument('-c', '--commit', action='store_true')
    parser.add_argument('-d', '--dolt_dir', type=str, help='The dolt dir', required=True)
    parser.add_argument('-m', '--message', type=str, help='Commit message associated with the commit')
    parser.add_argument('-b', '--branch', type=str, help='Branch to write to, default is master', default='master')
    parser.add_argument('--dry_run', action='store_true')
    args = parser.parse_args()
    loader(dolt_load_module=args.dolt_load_module,
           dolt_dir=args.dolt_dir,
           commit=args.commit,
           message=args.message,
           dry_run=args.dry_run,
           branch=args.branch)


if __name__ == '__main__':
    main()