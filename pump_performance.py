#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:54:53 2021

@author: cristofer
"""

class RatedPoint:
    
    def __init__(self, Head=0, Flow=0):
        self.Name = "Rated point"
        self.Head = Head
        self.Flow = Flow
        self.Temp = 0
        self.P3 = 0
        self.P0 = 0
        self.HydPower = 0
        self.NPSHA = 0
        self.Rho = 0
        self.DinVisc = 0
        self.Speed = 0
        self.DriverPower = 0
        self.Efficiency = 0
        
        
class TestedPoint:
    
    def __init__(self):
        self.Flow = 0
        self.P3 = 0
        self.P0 = 0
        self.Head = 0
        self.Temp = 0
        self.HydPower = 0
        self.NPSH3 = 0
        self.Rho = 0
        self.DinVisc = 0
        self.Speed = 0
        self.U0 = 0
        self.U3 = 0
        self.DriverPower = 0
        self.Efficiency = 0


class Pump:
    
    def __init__(self, Tag="B-0001"):
        self.__Tag = Tag
        
    def AddRatedPoint(self, Head=0,Flow=0):
        self.RatedPoint = RatedPoint(Head, Flow)
        
        
        
        
        
        
        