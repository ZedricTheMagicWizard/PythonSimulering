#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 13:48:27 2026

@author: madslober
"""
import physics

print(physics.getGravitationForce(1,1,1))

brut = physics.Planet('Jorden', 5.97*10**24, 6371000, 15, 0, 0, 0)


print(brut.getXPosition())

brut.setXPosition(10)

print(brut.getXPosition())


print(brut.getName())