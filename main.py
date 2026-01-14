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
dt= 3600



#Planeter oprettes
Solen1 = physics.Planet('Solen1', 1e30, 6.96e10, -5e10, 0, mutil.Vector(0, 8.17e6))
Solen2 = physics.Planet('Solen2', 1e30, 6.96e10, 5e10, 0, mutil.Vector(0, -8.17e6))

'''
Jorden = physics.Planet('Jorden', 5.97e24, 6.37e6, 1.5e11, 0, mutil.Vector(0, 3.25e4))
Mars = physics.Planet('Mars', 6.417e23, 3.39e6, 2.28e11, 0, mutil.Vector(0, 2.40e4))
Jupiter = physics.Planet('Jupiter', 1.898e27, 8.99e7, 7.78e11, 0, mutil.Vector(0, 1.31e4))
'''

#Planeter tilføjes til liste
planetList= [
      Solen1, Solen2] #Jupiter, Mars, Jorden,]



#AnimationBox startes
box = animationbox.animationBox(-80e10, 80e10, -80e10, 80e10, "X", "Y", tMAX)   
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


