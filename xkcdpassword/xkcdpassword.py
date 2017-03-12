#!/usr/bin/env python
"""Generate xkcd-style multiple-word passwords."""

from argparse import ArgumentParser
from itertools import izip_longest
from os.path import dirname
from os.path import join
from os.path import realpath
from pyperclip import copy
from random import randint
from random import seed
from sys import stdout

localpath = dirname(realpath(__file__))

parser = ArgumentParser(description='Generate an XKCD-style password.')
outopts = parser.add_argument_group('Output options')
outopts.add_argument('words',
                     nargs='?',
                     metavar='WORDCOUNT',
                     type=int,
                     default=4,
                     help='Number of words to produce (default = 4)')
outopts.add_argument('-c',
                     '--clip',
                     help='Send result to clipboard rather than sys.stdout',
                     action='store_true')
outopts.add_argument('-s',
                     '--seed',
                     metavar='SEEDDATA',
                     help='Seed for random function.',
                     action='store')
outmutex = outopts.add_mutually_exclusive_group()
outmutex.add_argument('-n',
                      '--nospaces',
                      help='Don\'t separate the output passphrase with spaces',
                      action='store_true')
outmutex.add_argument('-ds',
                      '--delimiters',
                      metavar='CHAR/S,[CHAR/S, ...]',
                      default=' ',
                      dest='delims',
                      help='Delimiting characters sequence, comma-separated',
                      action='store')
inopts = parser.add_argument_group('Input options')
inmutex = inopts.add_mutually_exclusive_group()
inmutex.add_argument('-e',
                     '--easywords',
                     help='Use an included dictionary of more common words',
                     action='store_true')
inmutex.add_argument('-f',
                     '--dictionaryfile',
                     metavar='FILEPATH',
                     dest='dictfile',
                     default=join(localpath, 'words.txt'),
                     help='Path to an alternative dictionary',
                     action='store')


def randwords(num, inseed, fn):
    """Generate random words from that text file, ensure uniqueness."""
    words = []
    numlines = 0
    with open(fn, 'r') as tempfile:
        numlines = sum([1 for x in tempfile])
    with open(fn, 'r') as tempfile:
        indices = []
        if inseed:
            seed(inseed)
        while len(indices) < num:
            ind = randint(0, numlines - 1)
            if ind not in indices:
                indices.append(ind)
        lines = tempfile.readlines()
        words = [lines[a].strip() for a in indices]
    return words


def main():
    """Primary entry point."""
    args = parser.parse_args()
    fn = join(localpath, 'easywords.txt' if args.easywords else args.dictfile)
    rwords = randwords(args.words, args.seed, fn)
    if args.nospaces:
        delims = ['' for a in range(len(rwords) - 1)]
    elif args.delims != ' ':
        delims = args.delims.split(',')
        while len(delims) < len(rwords) - 1:
            delims.extend(delims)
        delims = delims[:len(rwords) - 1]
    else:
        delims = [' ' for a in range(len(rwords) - 1)]
    outstr = ''.join([''.join(x)
                      for x in izip_longest(rwords, delims, fillvalue='')])
    if args.clip:
        copy(outstr)
    else:
        stdout.write(outstr + '\n')

if __name__ == "__main__":
    main()
