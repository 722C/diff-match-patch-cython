#!/usr/bin/env python
from setuptools import setup, Extension

setup(
    name='dmp',
    version='1.0.0',
    ext_modules=Extension(
        'dmp',
        sources=['diff_match_patch.pyx'],
    ),
    license="Apache",
    setup_requires=[
        # Setuptools 18.0 properly handles Cython extensions.
        'setuptools>=18.0',
        'cython',
    ],
)
