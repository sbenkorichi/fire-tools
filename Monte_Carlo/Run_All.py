#!/usr/bin/env python

import os

os.chdir('Scripts/')

print 'Running cfast_monte_carlo ...'
os.system('python cfast_monte_carlo.py')

print 'Running generate_figures ...'
os.system('python generate_figures.py')
