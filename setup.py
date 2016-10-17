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
        'Flask==0.11.1',
        'gunicorn==19.6.0',
        'itsdangerous==0.24',
        'Jinja2==2.8',
        'MarkupSafe==0.23',
        'nose==1.3.7',
        'nosetests-json-extended==0.1.0',
        'Werkzeug==0.11.11',
    ],
    zip_safe=False,
    test_suite='nose.collector',
    entry_points='''
        [console_scripts]
        pll_solver=pll_solver.scripts.cli:cli
        pll_solver_web=pll_solver.scripts.launchserver:main

    ''',
)
