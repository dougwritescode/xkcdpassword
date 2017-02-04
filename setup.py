#!/usr/bin/env python

from distutils.core import setup
setup(
	name = 'xkcdpassword',
	packages = ['xkcdpassword'],
	version = '0.4',
	description = 'A generator of xkcd-style passwords',
	author = 'Doug Walter',
	author_email = 'dougwritescode@gmail.com',
	url = 'https://github.com/dougwritescode/xkcdpassword',
	download_url = 'https://github.com/dougwritescode/xkcdpassword/tarball/0.4', 
	keywords = 'python xkcd utilities security', 
	classifiers = ['Development Status :: 3 - Alpha',
		'Environment :: Console',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Programming Language :: Python :: 2.7',
		'Topic :: Security',
		'Topic :: Utilities',],
	entry_points = {
		'console_scripts': [
            'xkcdpassword = xkcdpassword.xkcdpassword:__main__',
        ],
        'gui_scripts': []
	},
	include_package_data = True,
)
