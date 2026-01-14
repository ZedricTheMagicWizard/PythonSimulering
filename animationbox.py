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
    def show(self, block=False):
         plt.show(block=block)
         
        
class planetPoint:
    def __init__(self, ax, planet, color='ro'):
        self.planet = planet
        self.point, = ax.plot(
            planet.getXPosition(),
            planet.getYPosition(),
            color
        )

    def update(self):
        self.point.set_data(
            [self.planet.getXPosition()],
            [self.planet.getYPosition()]
        )
    
def simulatePlanets(tMAX, planetList, dt):
    t=0
    while t<tMAX:
        forces = physics.gravityOnObject(planetList)

        for planet in planetList:
            force = forces[planet]
                
            a = mutil.Vector(force.x / planet.getMass(), force.y / planet.getMass())

            planet.VelocityVector = planet.VelocityVector + a * dt

            planet.setXPosition(planet.getXPosition() + planet.VelocityVector.x * dt)
            planet.setYPosition(planet.getYPosition() + planet.VelocityVector.y * dt)
                
        t += dt
        plt.pause(0.05)
            
        yield planetList