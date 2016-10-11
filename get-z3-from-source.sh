#!/usr/bin/env sh
##
# Call with source:
#   $ . ./get-z3-from-source.sh
#
# Requires:
#  - python
#  - virtualenv
##

starting_dir=$PWD


setup_venv () {
  # Create a virtual env if one doesn't exist
  if [ ! -d venv ]; then
    virtualenv --python=python2.7 venv
  fi
  source ./venv/bin/activate
}

get_z3 () {
  z3_git_repo="https://github.com/Z3Prover/z3.git"
  git clone $z3_git_repo;

  cd z3;
  python scripts/mk_make.py --python
  cd build;
  make
  make install
}


test_z3 () {
  cd $starting_dir;
  # You will find Z3 and the Python bindings installed in the virtual environment
  venv/bin/z3 -h

  # Check python bindings
  python -c 'import z3; print(z3.get_version_string())'
}

setup_venv
get_z3
test_z3
