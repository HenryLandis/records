#!/usr/bin/env python

"""
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# Build setup.
setup(
    name="records",
    version="0.0.1",
    author="Henry Landis",
    author_email="hnl2109@columbia.edu",
    description="A package to query a database and analyze results.",
)