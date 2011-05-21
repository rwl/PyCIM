# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.CDPSM.Geographical.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Location(IdentifiedObject):
    """The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It can be defined with one or more postition points (coordinates) in a given coordinate system.
    """

    def __init__(self, PowerSystemResources=None, PositionPoints=None, CoordinateSystem=None, *args, **kw_args):
        """Initialises a new 'Location' instance.

        @param PowerSystemResources: All power system resources at this location.
        @param PositionPoints: Sequence of position points describing this location, expressed in coordinate system 'Location.CoordinateSystem'.
        @param CoordinateSystem: Coordinate system used to describe position points of this location.
        """
        self._PowerSystemResources = []
        self.PowerSystemResources = [] if PowerSystemResources is None else PowerSystemResources

        self._PositionPoints = []
        self.PositionPoints = [] if PositionPoints is None else PositionPoints

        self._CoordinateSystem = None
        self.CoordinateSystem = CoordinateSystem

        super(Location, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["PowerSystemResources", "PositionPoints", "CoordinateSystem"]
    _many_refs = ["PowerSystemResources", "PositionPoints"]

    def getPowerSystemResources(self):
        """All power system resources at this location.
        """
        return self._PowerSystemResources

    def setPowerSystemResources(self, value):
        for x in self._PowerSystemResources:
            x.Location = None
        for y in value:
            y._Location = self
        self._PowerSystemResources = value

    PowerSystemResources = property(getPowerSystemResources, setPowerSystemResources)

    def addPowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            obj.Location = self

    def removePowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            obj.Location = None

    def getPositionPoints(self):
        """Sequence of position points describing this location, expressed in coordinate system 'Location.CoordinateSystem'.
        """
        return self._PositionPoints

    def setPositionPoints(self, value):
        for x in self._PositionPoints:
            x.Location = None
        for y in value:
            y._Location = self
        self._PositionPoints = value

    PositionPoints = property(getPositionPoints, setPositionPoints)

    def addPositionPoints(self, *PositionPoints):
        for obj in PositionPoints:
            obj.Location = self

    def removePositionPoints(self, *PositionPoints):
        for obj in PositionPoints:
            obj.Location = None

    def getCoordinateSystem(self):
        """Coordinate system used to describe position points of this location.
        """
        return self._CoordinateSystem

    def setCoordinateSystem(self, value):
        if self._CoordinateSystem is not None:
            filtered = [x for x in self.CoordinateSystem.Location if x != self]
            self._CoordinateSystem._Location = filtered

        self._CoordinateSystem = value
        if self._CoordinateSystem is not None:
            if self not in self._CoordinateSystem._Location:
                self._CoordinateSystem._Location.append(self)

    CoordinateSystem = property(getCoordinateSystem, setCoordinateSystem)

