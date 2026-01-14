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


#Planeter oprettes
Jorden = physics.Planet('Jorden', 0.00597, 637.1, 1, 0, mutil.Vector(5,0))
Mars = physics.Planet('Mars', 0.0006417, 338.95, 2, 0, mutil.Vector(-2,0))
Jupiter =physics.Planet('Jupiter', 1.898, 8991.1, 3, 0, mutil.Vector(2,0))
Solen = physics.Planet('Solen', 1989, 69634,0, 0, mutil.Vector(0,0))


#Planeter tilføjes til liste
planetList= [
    Jorden, Mars, Jupiter, Solen]



#AnimationBox startes
box = animationbox.animationBox(-10, 10, -10, 10, "X", "Y", tMAX)   
#points = box.ax.plot([1,2,3], [4,5,6], "ro")

    
for planet in planetList:
    box.add_planet(planet)

box.show(block=False)  


while t < tMAX:
    t = t + dt
    plt.pause(dt)
    for planet in planetList:
        planet.setXPosition(physics.getNewPositionX(planet, planetList, dt))
        planet.setYPosition(physics.getNewPositionY(planet, planetList, dt))
    box.update_all_planets()


