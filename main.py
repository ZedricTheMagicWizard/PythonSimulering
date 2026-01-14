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
tMAX= 31557600000
dt= 0.5



#Planeter oprettes
Jorden = physics.Planet('Jorden', 5.97e24, 637.1, 149.6e9, 0, mutil.Vector(0,5))
Mars = physics.Planet('Mars', 6.417e23, 338.95, 228e9, 0, mutil.Vector(-2,0))
Jupiter =physics.Planet('Jupiter', 1.898e27, 8991.1, 778e9, 0, mutil.Vector(2,0))
Solen = physics.Planet('Solen', 1989e30, 69634,0, 0, mutil.Vector(0,0))


#Planeter tilføjes til liste
planetList= [
    Jorden, Solen] #Jupiter, mars]



#AnimationBox startes
box = animationbox.animationBox(-200e9, 200e9, -200e9, 200e9, "X", "Y", tMAX)   
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


