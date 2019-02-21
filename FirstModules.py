#!/usr/bin/python
import sys
import platform

def myoperatingsystem():
    my = sys.platform+"\n"+str(platform.dist())
    return my
