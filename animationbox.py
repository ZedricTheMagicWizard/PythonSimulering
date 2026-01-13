#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 15:06:33 2026

@author: madslober
"""
import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class animationBox:
    def __init__(self, minX,maxX,minY,maxY,labelX,labelY,runTime):
        self.labelX = labelX
        self.labelY = labelY
        self.runTime = runTime
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(minX,maxX)
        self.ax.set_ylim(minY,maxY)
        self.ax.set_aspect(1)
    def show(self):
         plt.show()
        
