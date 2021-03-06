import sys
from utils import execute_commands

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 package.py vx.y.z')
        exit(-1)

    versioned_dist = 'slang-lib-' + sys.argv[1].replace('.', '_')

    execute_commands([
        f'mkdir {versioned_dist}',
        f'cp -r slang {versioned_dist}/',
        'mkdir ci/release',
        f'zip -r ci/release/{versioned_dist}.zip {versioned_dist}',
        # f'tar -zcvf ci/{versioned_dist}.zip {versioned_dist}',
    ])
