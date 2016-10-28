#!/usr/bin/env python
from setuptools import setup, find_packages, Command
from distutils.util import convert_path

main_ns = {}
ver_path = convert_path('k64_pll_calculator/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)


setup(
    name='k64_pll_calculator',
    version=main_ns['__version__'],
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
        'z3-solver==4.4.2.1.post1',
    ],
    zip_safe=False,
    test_suite='nose.collector',
    entry_points={
        "console_scripts": [
            "k64_pll_calculator=k64_pll_calculator.scripts.cli:cli",
            "k64_pll_calculator_web=k64_pll_calculator.scripts.launchserver:main",
        ]}
)
