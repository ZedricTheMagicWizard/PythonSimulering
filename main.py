#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 13:48:27 2026

@author: madslober
"""
import physics
import math_util as mutil
import animationbox

t=0
dt= 0.1
tmax= 10

print(physics.getGravitationForce(1,1,1))

Jorden = physics.Planet('Jorden', 0.00597, 6371000, 1, 0, mutil.Vector(0,0))
Mars = physics.Planet('Mars', 0.0006417, 3389500, 2, 0, mutil.Vector(0,0))
Jupiter =physics.Planet('Jupiter', 1.898, 89911000, 3, 0, mutil.Vector(0,0))
Solen = physics.Planet('Solen', 1989, 696340000,0, 0, mutil.Vector(0,0))


planetList= [
    Jorden, Mars, Jupiter, Solen
    ]

box = animationbox.animationBox(-6, 6, -6, 6, "X", "Y", 500)
box.show()  

planetPoints = []
for planet in planetList:
    point = animationbox.planetPoint(box.ax, planet)
    planetPoints.append(point)
    
while t<tmax:
    t=t+dt
    
    Jorden.setYPosition(Jorden.getYPosition()+1)
    
  
    for point in planetPoints:
        point.update()

