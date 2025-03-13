import settings
import tkinter
from turtle import *

def hilbert(level,angle,step):
    if level == 0:
        return
    right(angle)

def main():
    level = int(input())
    size = 200
    penup()
    goto(-size/2.0,size/2.0)
    pendown()