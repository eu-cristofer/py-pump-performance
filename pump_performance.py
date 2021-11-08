#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:54:53 2021

@author: cristofer
"""

class Point:
    
    def __init__(self):
        self._Name = None
        self._Head = None
        self._Flow = None
        self._P3 = None
        self._P0 = None
        self._Temp = None
        self._HydPower = None
        self._NPSH3 = None
        self._Rho = None
        self._DinVisc = None
        self._Speed = None
        self._U0 = None
        self._U3 = None
        self._DriverPower = None
        self._Efficiency = None
        
    @property
    def Name(self):
        """Get the total head in meters"""
        return self._Name
        
    @Name.setter
    def Name(self, value):
        self._Name = str(value)
    
    @property
    def Head(self):
        """Get the total head in meters"""
        return self._Head
        
    @Head.setter
    def Head(self, value):
        self._Head = float(value)
    
    @property
    def Flow(self):
        """Get the volumetric flowrate in cubic meters"""
        return self._Flow
        
    @Flow.setter
    def Flow(self, value):
        self._Flow = float(value)
        
    @property
    def P3(self):
        """Get the outlet pressure in kgf/cm^2"""
        return self._P3
        
    @P3.setter
    def P3(self, value):
        self._P3 = float(value)
    
    @property
    def P0(self):
        """Get the inlet pressure in kgf/cm^2"""
        return self._P0
        
    @P0.setter
    def P0(self, value):
        self._P0 = float(value)
        
    def __repr__(self):
        return self.Name + ' (Flowrate: %r)' % (self.Flow)
        

class RatedPoint(Point):
    
    def __init__(self, Head, Flow):
        super().__init__()
        self.Head = Head
        self.Flow = Flow
        self.Name = "Rated point"
        

class TestPoint(Point):
    
    def __init__(self, Flow, P0, P3, Counter):
        super().__init__()
        self.Flow = Flow
        self.P0 = P0
        self.P3 = P3
        self.Name = "Test point " + str(Counter)
    

class Pump:
    
    def __init__(self, Tag="Generic"):
        self._Tag = Tag
        self._RatedPoint = None
        self._TestPoints = []
        self._TestPointsCount = 0
        
    @property
    def TestPointsCount(self):
        return self._TestPointsCount
    
    @property
    def TestPoints(self):
        return self._TestPoints
    
    @property
    def Tag(self):
        """Get the pump tag"""
        return self._Tag
    
    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag
        
    @property
    def RatedPoint(self):
        """Get the Rated point object"""
        if self._RatedPoint is None:
            return "You shall first create a Rated point"
        else:
            return self._RatedPoint
    
    def AddRatedPoint(self, Head, Flow):
        self._RatedPoint = RatedPoint(Head, Flow)
        
    def AddTestPoint(self, Flow, P0, P3):
        self._TestPoints.append(TestPoint(Flow, P0, P3, self._TestPointsCount))
        self._TestPointsCount += 1
        
    def __repr__(self):
        return "Pump Tag: %s" % self._Tag
    
    
    
    
    
    
    