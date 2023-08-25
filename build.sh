#!/usr/bin/env bash

# Before running this script, make sure that pyenv installed the current version of python with
# PYTHON_CONFIGURE_OPTS="--enable-shared" set

pip install -r requirements.txt
pip install -U py2app
python setup.py py2app
