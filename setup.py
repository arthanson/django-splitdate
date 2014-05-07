#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import djangomonthyearfilter

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djangomonthyearfilter.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-month-year-filter',
    version=version,
    description="""MSplit date month and year filter widget""",
    long_description=readme + '\n\n' + history,
    author='Arthur Hanson',
    author_email='worldnomad@gmail.com',
    url='https://github.com/arthanson/djangomonthyearfilter',
    packages=[
        'djangomonthyearfilter',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='djangomonthyearfilter',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)