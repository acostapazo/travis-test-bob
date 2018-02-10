#!/usr/bin/env python
from setuptools import setup, find_packages
from version import *

setup(
    name='bob.travis',
    version=get_version(),
    description='Testing bob package with travis',
    url='http://pypi.python.org/pypi/template-gradiant-python',
    license='GPLv3',
    author='Artur Costa-Pazo',
    author_email='acosta@gradiant.org',
    long_description=open('README.md').read(),
    keywords='travis test bob',

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,

    install_requires=[
      "setuptools",
    ],

    entry_points={
      'console_scripts': [
        'script_example.py = bob.travis.scripts.script_example:main',
        ],
    },
)
