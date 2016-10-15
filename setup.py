#!/usr/bin/env python
from setuptools import setup, find_packages
from pll_solver import __VERSION__
setup(
    name='pll_solver',
    version=__VERSION__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click==6.6',
        'nose==1.3.7',
        'flask'
    ],
    zip_safe=False,
    test_suite='nose.collector',
    entry_points='''
        [console_scripts]
        pll_solver=pll_solver.scripts.cli:cli
        pll_solver_web=pll_solver.scripts.launchserver:main

    ''',
)
