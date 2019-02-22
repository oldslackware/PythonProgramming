#!/usr/bin/python
import sys
import platform
import time
import random

def myoperatingsystem():
    "Info about operating system"
    my = sys.platform+"\n"+str(platform.dist())
    return my

def platformmethod():
    "Show all platform's methods "
    methods=dir(platform)
    print(*methods, sep= "\n")


def todaydate():
    "What date is today"
    mytodaydate=time.localtime()
    dateformatted=time.strftime("%d/%m/%Y, %H:%M:%S", mytodaydate)
    print(dateformatted)

def luckynumber():
    "A random number"
    numberjolly=random.randint(1,90)
    return numberjolly