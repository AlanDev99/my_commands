#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''My commands in speed!!'''

import subprocess
import sys
from argparse import ArgumentParser

__author__ = "Alan Viñals <vinals.alan@gmail.com>"
__version__ = "0.0.1"


def make_arguments_parser():
    """Build and return a command line agument parser."""
    parser = ArgumentParser(description='Collected of scripts recurrents.')
    parser.add_argument('-v',
        '--version',
        action='version',
        version=__version__)
    parser.add_argument(
        '-b',
        '--battery',
        action='store_true',
        help='Show porcentage battery')
    parser.add_argument(
        '-f',
        '--firefox',
        action='store_true',
        help='Open Mozilla Firefox in private mode')
    global args
    args = parser.parse_args()


def main():
    '''Function main'''

    make_arguments_parser()

    if len(sys.argv) < 2:
        output = "  -h, --help     show help message"
        print(output)
        exit(0)

    if args.battery:
        response = '''upower -i $(upower -e | grep 'BAT') |
                      grep -E "state|to\ full|percentage"'''
        print(subprocess.getoutput(response))

    if args.firefox:
        subprocess.getoutput('firefox -private "https://duckduckgo.com/"')




if __name__ == "__main__":
    main()
