#!/usr/bin/env python
from setuptools import setup, find_packages, Command
from pll_solver import __VERSION__
import subprocess
class SetupHerokuCommand(Command):
    """Setup heroku for website"""
    description = "setup heroku command"
    user_options = []

    def initialize_options(self):
        """init options"""
        pass

    def finalize_options(self):
        """finalize options"""
        pass

    def run(self):
        """runner"""
        try:
            ret = subprocess.call("heroku buildpacks:set heroku/python", shell=True)
            ret = subprocess.call(
                "heroku buildpacks:add https://github.com/cwoodall/heroku-buildpack-z3-python",shell=True)
            ret = subprocess.call(
                "heroku buildpacks",shell=True)
            print("success")
        except Exception as e:
            print(e)
            print("Failed, please verify the heroku toolbelt is installed. Run `gem install heroku`")
            exit(1)
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
    cmdclass={
        'heroku_setup': SetupHerokuCommand
    },
    entry_points='''
        [console_scripts]
        pll_solver=pll_solver.scripts.cli:cli
        pll_solver_web=pll_solver.scripts.launchserver:main
    ''',
)
