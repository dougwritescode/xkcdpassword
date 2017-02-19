#!/usr/bin/env python

from pyperclip import copy
from argparse import ArgumentParser
from os.path import join, dirname, realpath
from sys import stdout
from random import randint, seed

localpath = dirname(realpath(__file__))

parser = ArgumentParser(description='Generate an XKCD-style password.')
outopts = parser.add_argument_group('Output options')
outopts.add_argument('words', nargs='?', metavar='WORDCOUNT', type=int, default=4, help='Number of words to produce (default = 4)')
outopts.add_argument('-c', '--clip', help='Send result to clipboard rather than sys.stdout', action='store_true')
outopts.add_argument('-s', '--seed', metavar='SEEDDATA', help='Seed for random function, if you want predictable results', action='store')
outmutex = outopts.add_mutually_exclusive_group()
outmutex.add_argument('-n', '--nospaces', help='Don\'t separate the output passphrase with spaces', action='store_true')
outmutex.add_argument('-d', '--delimiter', metavar='CHAR/S', default=' ', help='Custom character or string to split words', action='store')
inopts = parser.add_argument_group('Input options')
inmutex = inopts.add_mutually_exclusive_group()
inmutex.add_argument('-e', '--easywords', help='Use an included dictionary of more common words', action='store_true')
inmutex.add_argument('-f', '--dictionaryfile', metavar='FILEPATH', default=join(localpath, 'words.txt'), help='Path to an alternative dictionary', action='store')

def randwords(num, inseed, fn): 
	'''Generates random words from the provided text file
	and ensures uniqueness.'''
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
	'''Primary entry point'''
	args = parser.parse_args()
	fn = join(localpath, 'easywords.txt') if args.easywords else args.dictionaryfile
	rwords = randwords(args.words, args.seed, fn)
	outstr = ('' if args.nospaces else args.delimiter).join(rwords)
	if args.clip:
		copy(outstr)
	else:
		stdout.write(outstr)
		stdout.write('\n')
	
if __name__ == "__main__":
	main()
