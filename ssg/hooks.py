# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 11:26:38 2022

@author: Cameron Hill
"""



_callbacks = {}



def register(hook,order=0):
    """ """

    def register_callback(func):
        """ """
        _callbacks.setdefault(hook,{}).setdefault(order,[]).append(func)
        return func

    return register_callback
