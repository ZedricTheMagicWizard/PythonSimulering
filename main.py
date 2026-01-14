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
tMAX= 3e7
dt= 86400



#Planeter oprettes
Jorden = physics.Planet('Jorden', 5.97e24, 637.1, 149.6e9, 0, mutil.Vector(0, 30e3))
Mars = physics.Planet('Mars', 6.417e23, 338.95, 228e9, 0, mutil.Vector(0,24.07e3))
Jupiter =physics.Planet('Jupiter', 1.898e27, 8991.1, 778e9, 0, mutil.Vector(0,13.1e3))
Solen = physics.Planet('Solen', 1.982e30, 69634, 0, 0, mutil.Vector(0,0))
#Solen2 = physics.Planet('Solen2',1e30, 69634,1e9, 0, mutil.Vector(0,1e5))


#Planeter tilføjes til liste
planetList= [
    Jorden, Solen, Jupiter, Mars]



#AnimationBox startes
box = animationbox.animationBox(-100e10, 100e10, -100e10, 100e10, "X", "Y", tMAX)   
#points = box.ax.plot([1,2,3], [4,5,6], "ro")

    
for planet in planetList:
    box.add_planet(planet)

box.show(block=False)  


while t < tMAX:
    t = t + dt
    plt.pause(0.1)
    for planet in planetList:
        newVelocity = physics.getNewVelocityVector(planet, planetList, dt)
    
        # 2. Opdater position med den gamle hastighed
        planet.setXPosition(planet.getXPosition() + planet.getVelocityVector().x * dt)
        planet.setYPosition(planet.getYPosition() + planet.getVelocityVector().y * dt)
    
        # 3. Opdater hastighed
        planet.setVelocityVector(newVelocity)
    box.update_all_planets()


