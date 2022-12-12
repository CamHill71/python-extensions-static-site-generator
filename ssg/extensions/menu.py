# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 11:26:38 2022

@author: Cameron Hill
"""


from ssg import hooks,parsers


files = []


def collect_files(source,site_parsers):
    """  """
    hooks.register("collect_files")

    valid = lambda p:isinstance(p)