#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 13:48:14 2026

@author: madslober
"""

# %%

import numpy as np
import math_util as mutil
import math

G= 6.67430*10**-11 #m^3/(kg*s^2)

def getGravitationForce(m1,m2,r):
    return G*((m1*m2)/r**2)

class Planet:
    def __init__(self, name, masse, radius, startXPosition, startYPosition, startVelocityVector):
        self.name = name
        self.masse = masse
        self.radius = radius
        self.XPosition = startXPosition
        self.YPosition = startYPosition
        self.VelocityVector = startVelocityVector
        
    def getName(self):
        return self.name
    def setXPosition(self, newXPosition):
        self.XPosition = newXPosition
    def getXPosition(self): 
        return self.XPosition
    def setYPosition(self, newYPosition):
        self.YPosition = newYPosition
    def getYPosition(self): 
        return self.YPosition
    def getVelocityVector(self):
        return self.VelocityVector
    def getMass(self):
        return self.masse
    
    
def getDistance(planet1, planet2):
    deltaX = np.absolute(planet1.getXPosition() - planet2.getXPosition())
    deltaY = np.absolute(planet1.getYPosition() - planet2.getYPosition())
    return np.sqrt(deltaX**2 + deltaY**2)

def getAngle(planet1, planet2):
    deltaX = (planet1.getXPosition() - planet2.getXPosition())
    deltaY = (planet1.getYPosition() - planet2.getYPosition())
    return math.atan2(deltaX, deltaY)

def getForceVector(angle, totalGravitationForce):
    forceX = math.cos(angle) * totalGravitationForce
    forceY = math.sin(angle) * totalGravitationForce
    return mutil.Vector(forceX, forceY)
      

def gravityOnObject(planetList):
    totalForces = {}
    for planet in planetList:
        totalForceVector = mutil.Vector(0,0)
        for anotherPlanet in planetList:
            if planet.getName == anotherPlanet.getName:
                continue
            
            
            
            distance = getDistance(planet, anotherPlanet)
            
            totalGravitationForce = getGravitationForce(planet.getMass(),anotherPlanet.getMass(),distance)
            angle = getAngle(planet, anotherPlanet)
            
            additionalForceVector = getForceVector(angle, totalGravitationForce)
            totalForceVector = totalForceVector + additionalForceVector
            
        totalForces[planet] = totalForceVector
    return totalForces




            
    
    
        

