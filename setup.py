#!/usr/bin/env python

from setuptools import setup
from ack import __version__

long_description = "dak ack"

setup(
    name="ack",
    version=__version__,
    packages=['ack',],
    author="Paul Tagliamonte",
    author_email="paultag@debian.org",
    long_description=long_description,
    description='does some stuff with things & stuff',
    license="GPL-3+",
    url="",
    platforms=['any']
)
