#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:54:53 2021

@author: cristofer
"""

import matplotlib.pyplot as plt
import numpy as np
from weakref import WeakKeyDictionary


class FloatDescriptor:
    """A floats descriptor"""
    def __init__(self, default):
        self.default = default
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        self.data[instance] = float(value)


class NameDescriptor:
    """A string descriptor"""
    def __init__(self, default):
        self.default = default
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        self.data[instance] = str(value)


class Point:
    Name = NameDescriptor(None)
    Head = FloatDescriptor(None)
    Flow = FloatDescriptor(None)
    P0 = FloatDescriptor(None)
    P3 = FloatDescriptor(None)
    Temp = FloatDescriptor(None)
    HydPower = FloatDescriptor(None)
    NPSH3 = FloatDescriptor(None)
    Rho = FloatDescriptor(None)
    DinVisc = FloatDescriptor(None)
    Speed = FloatDescriptor(None)
    DriverPower = FloatDescriptor(None)
    Efficiency = FloatDescriptor(None)

    def __repr__(self):
        return "%s [Flowrate: %s]" % (self.Name, self.Flow)

    def __call__(self):
        if self.Head is not None:
            return (self.Head,self.Flow)
        else:
            return (self.Flow)


class RatedPoint(Point):

    def __init__(self, Head, Flow):
        super().__init__()
        self.Head = Head
        self.Flow = Flow
        self.Name = "Rated point"


class TestPoint(Point):

    U0 = FloatDescriptor(None)
    U3 = FloatDescriptor(None)

    def __init__(self, Flow, P0, P3, Counter):
        super().__init__()
        self.Flow = Flow
        self.P0 = P0
        self.P3 = P3
        self.Name = "Test point #" + str(Counter)


class Pump:

    Tag = NameDescriptor(None)
    D0 = FloatDescriptor(None)
    D3 = FloatDescriptor(None)
    A0 = FloatDescriptor(None)
    A3 = FloatDescriptor(None)
    Z0 = FloatDescriptor(None)
    Z3 = FloatDescriptor(None)
    ZM0 = FloatDescriptor(None)
    ZM3 = FloatDescriptor(None)

    def __init__(self, Tag="Generic"):
        self.Tag = Tag
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
    def RatedPoint(self):
        """Get the Rated point object"""
        if self._RatedPoint is None:
            return "You shall first create a Rated point"
        else:
            return self._RatedPoint

    def __repr__(self):
        return "Pump TAG: %s" % self.Tag

    def AddRatedPoint(self, Head, Flow):
        self._RatedPoint = RatedPoint(Head, Flow)

    def AddTestPoint(self, Flow, P0, P3):
        self._TestPoints.append(TestPoint(Flow, P0, P3, self._TestPointsCount))
        self._TestPointsCount += 1

    def __UpdateNozzlesArea(self):
        self.A0 = np.pi * self.D0**2 /4
        self.A3 = np.pi * self.D3**2 /4

    def NozzlesSize(self, D0, D3):
        self.D0 = D0
        self.D3 = D3
        self.__UpdateNozzlesArea()

    def Update(self):
        if self.D0 is None or self.D3 is None:
            return "Please add the Pump Inlet and Outlet diameters"

        elif len(self._TestPoints) == 0:
            return "Please add Test Points first"

        else:
            self.__UpdateNozzlesArea()
            return "Values updated succesfully"

        # Continuar a partir daqui

    def Plot(self):
        pass
