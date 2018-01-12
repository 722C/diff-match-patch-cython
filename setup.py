#!/usr/bin/env python
from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    name='dmp',
    version='1.0.0',
    description = "The Diff Match and Patch libraries offer robust algorithms to perform the operations required for synchronizing plain text.",
    long_description = read('README.rst') + "\n\n" + read("CHANGES.rst"),
    packages = ['dmp'],
    package_dir = {'': subdir},
    ext_modules = cythonize('diff_match_patch.pyx'),
    license = "Apache",
)
