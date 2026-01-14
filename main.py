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
tMAX= 3e7*2
dt= 43200

YdreSystem = True


#Planeter oprettes

Solen = physics.Planet('Solen', 1.982e30, 69634, 0, 0, mutil.Vector(0,0))
Merkur = physics.Planet('Merkur', 3.285e23, 243.97e3, 57.9e9, 0, mutil.Vector(0, 47.4e3))
Venus = physics.Planet('Venus', 4.867e24, 6051.8e3, 108.2e9, 0, mutil.Vector(0, 35.0e3))
Jorden = physics.Planet('Jorden', 1.982e30, 6371e3, 149.6e9, 0, mutil.Vector(0, 29.78e3))
Mars = physics.Planet('Mars', 6.417e23, 3389.5e3, 227.9e9, 0, mutil.Vector(0, 24.07e3))

if YdreSystem==True:
    Jupiter = physics.Planet('Jupiter', 1.898e27, 69911e3, 778.5e9, 0, mutil.Vector(0, 13.07e3))
    Saturn = physics.Planet('Saturn', 5.683e26, 58232e3, 1434e9, 0, mutil.Vector(0, 9.69e3))
    Uranus = physics.Planet('Uranus', 8.681e25, 25362e3, 2871e9, 0, mutil.Vector(0, 6.81e3))
    Neptun = physics.Planet('Neptun', 1.024e26, 24622e3, 4495e9, 0, mutil.Vector(0, 5.43e3))

 


#Planeter tilføjes til liste
if YdreSystem==False:
    planetList= [
    Solen, Merkur, Venus, Jorden, Mars]
    
else:
    planetList= [
      Solen, Merkur, Venus, Jorden, Mars, Jupiter, Saturn, Uranus, Neptun]

#AnimationBox startes
'''if YdreSystem==False:
    box = animationbox.animationBox(-300e9, 300e9, -300e9, 300e9, "X", "Y", tMAX)  
     
else:'''
box = animationbox.animationBox(-450e10, 450e10, -450e10, 450e10, "X", "Y", tMAX)   
#points = box.ax.plot([1,2,3], [4,5,6], "ro")

    
for planet in planetList:
    box.add_planet(planet)

box.show(block=False)  


while t < tMAX:
    t = t + dt
    plt.pause(0.035)
    for planet in planetList:
        newVelocity = physics.getNewVelocityVector(planet, planetList, dt)
    
        # 2. Opdater position med den gamle hastighed
        planet.setXPosition(planet.getXPosition() + planet.getVelocityVector().x * dt)
        planet.setYPosition(planet.getYPosition() + planet.getVelocityVector().y * dt)
    
        # 3. Opdater hastighed
        planet.setVelocityVector(newVelocity)
    box.update_all_planets()


