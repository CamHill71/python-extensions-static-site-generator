# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 11:26:38 2022

@author: Cameron Hill
"""



from ssg import hooks
import time


start_time = None
total_written = 0


@hooks.register("start_build")
def start_build():
    """ """
    global start_time
    start_time = time.time()

@hooks.register("written")
def written():
    """ """ 
    global total_written
    total_written += 1
