#!/bin/bash

[ -d venv ] || python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -U comfy-cli
comfy install

