#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 13:48:27 2026

@author: madslober
"""
import physics
import math_util as mutil

print(physics.getGravitationForce(1,1,1))

Jorden = physics.Planet('Jorden', 5.97*10**24, 6371000, 15, 0, mutil.Vector(0,0))
Mars = physics.Planet('Mars', 6.417*10**23, 3389500, 25, 5, mutil.Vector(0,0))

planetList= [
    Jorden, Mars
    ]

print((Jorden.getXPosition()),':',(Jorden.getName()))
print((Mars.getXPosition()),':', (Mars.getName()))

physics.gravityOnObject(planetList)
