#!/usr/bin/env python
from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    name='dmp',
    version='1.0.0',
    packages = ['dmp'],
    ext_modules = cythonize('diff_match_patch.pyx'),
    license = "Apache",
)
