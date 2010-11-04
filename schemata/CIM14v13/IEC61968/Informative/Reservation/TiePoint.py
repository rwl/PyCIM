# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class TiePoint(IdentifiedObject):
    """Site of an interface between interchange areas. The tie point can be a network branch (e.g., transmission line or transformer) or a switching device. For transmission lines, the interchange area boundary is usually at a designated point such as the middle of the line. Line end metering is then corrected for line losses.
    """

    def __init__(self, tiePointMWRating=0.0, Declared_ServicePoint=None, For_Measurements=None, By_Measurements=None, **kw_args):
        """Initializes a new 'TiePoint' instance.

        @param tiePointMWRating: The MW rating of the tie point 
        @param Declared_ServicePoint: A tiepoint may be declared as a service point.
        @param For_Measurements: A measurement is made on the A side of a tie point
        @param By_Measurements: A measurement is made on the B side of a tie point
        """
        #: The MW rating of the tie point
        self.tiePointMWRating = tiePointMWRating

        self._Declared_ServicePoint = None
        self.Declared_ServicePoint = Declared_ServicePoint

        self._For_Measurements = []
        self.For_Measurements = [] if For_Measurements is None else For_Measurements

        self._By_Measurements = []
        self.By_Measurements = [] if By_Measurements is None else By_Measurements

        super(TiePoint, self).__init__(**kw_args)

    def getDeclared_ServicePoint(self):
        """A tiepoint may be declared as a service point.
        """
        return self._Declared_ServicePoint

    def setDeclared_ServicePoint(self, value):
        if self._Declared_ServicePoint is not None:
            self._Declared_ServicePoint._Declare_TiePoint = None

        self._Declared_ServicePoint = value
        if self._Declared_ServicePoint is not None:
            self._Declared_ServicePoint._Declare_TiePoint = self

    Declared_ServicePoint = property(getDeclared_ServicePoint, setDeclared_ServicePoint)

    def getFor_Measurements(self):
        """A measurement is made on the A side of a tie point
        """
        return self._For_Measurements

    def setFor_Measurements(self, value):
        for x in self._For_Measurements:
            x._For_TiePoint = None
        for y in value:
            y._For_TiePoint = self
        self._For_Measurements = value

    For_Measurements = property(getFor_Measurements, setFor_Measurements)

    def addFor_Measurements(self, *For_Measurements):
        for obj in For_Measurements:
            obj._For_TiePoint = self
            self._For_Measurements.append(obj)

    def removeFor_Measurements(self, *For_Measurements):
        for obj in For_Measurements:
            obj._For_TiePoint = None
            self._For_Measurements.remove(obj)

    def getBy_Measurements(self):
        """A measurement is made on the B side of a tie point
        """
        return self._By_Measurements

    def setBy_Measurements(self, value):
        for x in self._By_Measurements:
            x._By_TiePoint = None
        for y in value:
            y._By_TiePoint = self
        self._By_Measurements = value

    By_Measurements = property(getBy_Measurements, setBy_Measurements)

    def addBy_Measurements(self, *By_Measurements):
        for obj in By_Measurements:
            obj._By_TiePoint = self
            self._By_Measurements.append(obj)

    def removeBy_Measurements(self, *By_Measurements):
        for obj in By_Measurements:
            obj._By_TiePoint = None
            self._By_Measurements.remove(obj)

