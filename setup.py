#!/usr/bin/env python

from setuptools import setup


install_requires = ['pyperclip']

setup(
    name='xkcdpassword',
    packages=['xkcdpassword'],
    version='0.6.6',
    description='A generator of xkcd-style passwords',
    author='Doug Walter',
    author_email='dougwritescode@gmail.com',
    url='https://github.com/dougwritescode/xkcdpassword',
    download_url='https://github.com/dougwritescode/xkcdpassword/tarball/0.6.6',  # noqa
    keywords='python xkcd utilities security password',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Security',
        'Topic :: Utilities',
    ],
    entry_points={
        'console_scripts': [
            'xkcdpassword = xkcdpassword.xkcdpassword:main',
        ],
        'gui_scripts': []
    },
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
