#!/bin/bash

python3 /opt/app/pre_flight.py

jupyter lab --ip=0.0.0.0 --port=8888 --allow-root  --no-browser --NotebookApp.token='' --NotebookApp.password=''