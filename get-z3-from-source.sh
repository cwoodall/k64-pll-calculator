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
  virtualenv --python=python2.7 venv
  source ./venv/bin/activate
}

get_z3 () {
  z3_git_repo="https://github.com/Z3Prover/z3.git"
  git clone $z3_git_repo;

  cd z3;
  python scripts/mk_make.py --python --staticlib
  cd build;
  make
  make install
}


test_z3 () {
  cd $starting_dir;

  # Check python bindings
  python -c 'import z3; print(z3.get_version_string())'
}

make_install() {
  cd z3/build;
  make install
}

setup_venv

if [ -d z3 ]; then
  echo "Trying to install z3"
  trap make_install EXIT
else
  echo "Fetching z3"
  get_z3
fi

cd $starting_dir
