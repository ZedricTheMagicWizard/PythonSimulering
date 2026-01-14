#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 13:48:27 2026

@author: madslober
"""
import physics
import math_util as mutil
import animationbox
import matplotlib.pyplot as plt

t=0
dt= 0.1
tMAX= 100


Animate = True

print(physics.getGravitationForce(1,1,1))

Jorden = physics.Planet('Jorden', 0.00597, 637.1, 1, 0, mutil.Vector(0,0))
Mars = physics.Planet('Mars', 0.0006417, 338.95, 2, 0, mutil.Vector(0,0))
Jupiter =physics.Planet('Jupiter', 1.898, 8991.1, 3, 0, mutil.Vector(0,0))
Solen = physics.Planet('Solen', 1989, 69634,0, 0, mutil.Vector(0,0))


planetList= [
    Jorden, Mars, Jupiter, Solen]

box = animationbox.animationBox(0, 3, -1.5, 1.5, "X", "Y", tMAX)
box.show(block=False)  

planetPoints = []
for planet in planetList:
    point = animationbox.planetPoint(box.ax, planet)
    planetPoints.append(point)
    
while t<=tMAX:
    planetSimulation = animationbox.simulatePlanets(tMAX, planetList, dt)

    for planets in planetSimulation:

        for pP in planetPoints:
            pP.update()
            
    forces = physics.gravityOnObject(planetList)        
    for planet in planetList:
        force = forces[planet]
        box.ax.arrow(planet.getXPosition(), planet.getYPosition(),
         force.x*1e3, force.y*1e3, head_width=0.05, color='blue')
        