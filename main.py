#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 13:48:27 2026

@author: madslober
"""
import physics
import math_util as mutil
import animationbox



print(physics.getGravitationForce(1,1,1))

Jorden = physics.Planet('Jorden', 5.97*10**24, 6371000, 15, 0, mutil.Vector(0,0))
Mars = physics.Planet('Mars', 6.417*10**23, 3389500, 25, 5, mutil.Vector(0,0))
Jupiter =physics.Planet('Jupiter', 1.898*10**27, 89911000, 100, 3, mutil.Vector(0,0))
Solen = physics.Planet('Solen', 1.989*10**30, 696340000,0, 0, mutil.Vector(0,0))


planetList= [
    Jorden, Mars, Jupiter, Solen
    ]

physics.gravityOnObject(planetList)


box = animationbox.animationBox(-1000, 1000, -1000, 1000, "X", "Y", 500)
for planet in planetList:
    box.ax.plot(planet.XPosition, planet.XPosition, 'ro')

box.show()
