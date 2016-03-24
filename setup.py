#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='api-somospool',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='pool portfolio',
    # GETTING-STARTED: set author name (your name):
    author='Mint IT Media',
    # GETTING-STARTED: set author email (your email):
    author_email='info@mintitmedia.com',
    # GETTING-STARTED: set author url (your url):
    url='http://www.mintitmedia.com',
    # GETTING-STARTED: define required django version:
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
