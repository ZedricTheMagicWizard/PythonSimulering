#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 13:48:27 2026

@author: madslober
"""
import physics

print(physics.getGravitationForce(1,1,1))

jorden = physics.Planet(5.97*10**24, 6371000, 15, 0, 0, 0)


print(jorden.getXPosition())

jorden.setXPosition(10)

print(jorden.getXPosition())