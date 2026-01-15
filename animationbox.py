#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 15:06:33 2026

@author: madslober
"""
import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import physics
import math_util as mutil

class animationBox:
    def __init__(self, minX,maxX,minY,maxY,labelX,labelY,runTime):
        self.labelX = labelX
        self.labelY = labelY
        self.runTime = runTime
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(minX,maxX)
        self.ax.set_ylim(minY,maxY)
        self.ax.set_xlabel(labelX)
        self.ax.set_ylabel(labelY)
        self.ax.set_aspect(1)
        
        # Gemmer planet-navn → plotobjekt Chat kode
        self.planet_points = {}
        self.planet_trails = {}
        
    def add_planet(self, planet, color="ro"):
        """Tilføj planet og tegn punktet."""
        x = planet.getXPosition()
        y = planet.getYPosition()
        plot_obj, = self.ax.plot([x], [y], color)
        self.planet_points[planet.getName()] = (planet, plot_obj)
        plt.draw()
    
    def add_Trail(self, planet, trail_color='r-'):
        trail_line, = self.ax.plot([], [], trail_color, linewidth=2)
        self.planet_trails[planet] = ([planet.getXPosition()],
                              [planet.getYPosition()],
                              trail_line)
        plt.draw()

    def update_all_planets(self):
        """Opdater alle punkter baseret på de gemte planetobjekter"""
        for planet, plot_obj in self.planet_points.values():
            plot_obj.set_data([planet.getXPosition()], [planet.getYPosition()])
        plt.draw()

    def update_all_trails(self, maxLength=200):
        """Opdater banespor for alle planeter"""
        for planet, (xs, ys, line) in self.planet_trails.items():
            xs.append(planet.getXPosition())
            ys.append(planet.getYPosition())
            
            if len(xs)>maxLength:
                xs.pop(0)
                ys.pop(0)
            
            line.set_data(xs, ys)
        plt.draw()

    def show(self, block=False):
        plt.show(block=block)
    
    