@echo off
title PyWriter
cd src
pip install -r requirements.txt
cd ..
cls
python src\PyWriter.py
