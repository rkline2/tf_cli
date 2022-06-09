#!/bin/bash

echo -e "Building venv..."
python3 -m venv tf_env  # tmp
source tf_env/bin/activate # tmp

echo -e "\nInstalling requirements..."
pip install -r .dev_req
pip install .[dev]

echo -e "\nBuild complete!"