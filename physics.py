#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 13:48:14 2026

@author: madslober
"""

# %%

import numpy as np

G=6.67430*10**-11 #m^3/(kg*s^2)

def getGravitationForce(m1,m2,r):
    return G*((m1*m2)/r**2)

class Planet:
    def __init__(self, name, masse, radius, startXPosition, startYPosition, startXVelocity, startYVelocity):
        self.name = name
        self.masse = masse
        self.radius = radius
        self.XPosition = startXPosition
        self.YPosition = startYPosition
        self.XVelocity = startXVelocity
        self.YVelocity = startYVelocity
    def getName(self):
        return self.name
    def setXPosition(self, newPosition):
        self.XPosition = newPosition
    def getXPosition(self): 
        return self.XPosition
    def setYPosition(self, newPosition):
        self.YPosition = newPosition
    def getYPosition(self): 
        return self.YPosition
    def getMass(self):
        return self.masse
    
    
def getDistance(planet1, planet2):
    deltaX = np.absolute(planet1.getXPosition() - planet2.getXPosition())
    deltaY = np.absolute(planet1.getYPosition() - planet2.getYPosition())
    return np.sqrt(deltaX**2 + deltaY**2)
    
def gravityOnObject(planetList):
    for planet in planetList:
        for anotherPlanet in planetList:
            if planet.getName == anotherPlanet.getName:
                continue
            r = getDistance(planet, anotherPlanet)
            print('Distance from:', planet.getName(), 'to', anotherPlanet.getName(), r)
        
            
            
    
    
        

