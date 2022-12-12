# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 11:26:38 2022

@author: Cameron Hill
"""


import sys

import importlib
from pathlib import Path


def load_module(directory,name):
    """ """
    sys.path.insert(0,directory)
    importlib.import_module(name)
    sys.path.pop(0)

