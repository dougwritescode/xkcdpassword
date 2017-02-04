#!/usr/bin/env python

import argparse, sys, random, os

parser = argparse.ArgumentParser(description='Generate an XKCD-style password.')
parser.add_argument('words', metavar='n', nargs='?', type=int, default=4, help='Number of words to produce (default = 4)', choices=range(1,20))
parser.add_argument('-ns', help='Remove spaces for copy-pasting or piping', action='store_true')
	
#TODO: Maybe hard-code wordlist, for fast retrieval	
	
def randwords(num): 
	'''Generates random words from the provided text file
	and ensures uniqueness.'''
	words = []
	numlines = 0
	with open(os.path.dirname(os.path.realpath(__file__)) + '/words.txt', 'r') as tempfile:
		numlines = sum([1 for x in tempfile])
	with open(os.path.dirname(os.path.realpath(__file__)) + '/words.txt', 'r') as tempfile:
		indset = set()
		while len(indset) < num:
			indset.add(random.randint(0, numlines - 1))
		words = [b.strip() for a, b in enumerate(tempfile.readlines()) if a in indset]
	return words
	
def main():
	'''Primary entry point'''
	args = parser.parse_args()
	sys.stdout.write(('' if args.ns else ' ').join(randwords(args.words))+'\n')
	
if __name__ == "__main__":
	main()
