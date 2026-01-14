#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 16:38:08 2026

@author: madslober
"""
from dataclasses import dataclass
import math

@dataclass
class Vector:
    x: float
    y: float

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    __rmul__ = __mul__

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def getAngle(self):
        return math.atan2(self.y, self.x)

