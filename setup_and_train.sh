#!/bin/bash

# Setup GitHub remote on Replit
git remote add origin https://github.com/shashankt79/sairam.git
git fetch origin main
git checkout main
git pull origin main

# Now train the model
python train_model_fred.py

# Restart Flask with new model
python app.py
