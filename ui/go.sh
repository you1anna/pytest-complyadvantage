#!/usr/bin/env bash

sudo chmod +x ./tests/chromedriver
cd tests
export PATH=$PATH:$(pwd)
cd ..
python3 -m venv venv
source ./venv/bin/activate
python3 -m pip install -r requirements.txt --disable-pip-version-check
pytest "tests"