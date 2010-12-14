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

from CIM14.Element import Element

class CoordinateSystem(Element):
    """Coordinate reference system.
    """

    def __init__(self, name='', Location=None, PositionPoints=None, *args, **kw_args):
        """Initialises a new 'CoordinateSystem' instance.

        @param name: Name of this coordinate system. 
        @param Location: Location described by using position points in this coordinate system.
        @param PositionPoints: Sequence of position points expressed in this coordinate system.
        """
        #: Name of this coordinate system.
        self.name = name

        self._Location = None
        self.Location = Location

        self._PositionPoints = []
        self.PositionPoints = [] if PositionPoints is None else PositionPoints

        super(CoordinateSystem, self).__init__(*args, **kw_args)

    _attrs = ["name"]
    _attr_types = {"name": str}
    _defaults = {"name": ''}
    _enums = {}
    _refs = ["Location", "PositionPoints"]
    _many_refs = ["PositionPoints"]

    def getLocation(self):
        """Location described by using position points in this coordinate system.
        """
        return self._Location

    def setLocation(self, value):
        if self._Location is not None:
            filtered = [x for x in self.Location.CoordinateSystems if x != self]
            self._Location._CoordinateSystems = filtered

        self._Location = value
        if self._Location is not None:
            if self not in self._Location._CoordinateSystems:
                self._Location._CoordinateSystems.append(self)

    Location = property(getLocation, setLocation)

    def getPositionPoints(self):
        """Sequence of position points expressed in this coordinate system.
        """
        return self._PositionPoints

    def setPositionPoints(self, value):
        for x in self._PositionPoints:
            x.CoordinateSystem = None
        for y in value:
            y._CoordinateSystem = self
        self._PositionPoints = value

    PositionPoints = property(getPositionPoints, setPositionPoints)

    def addPositionPoints(self, *PositionPoints):
        for obj in PositionPoints:
            obj.CoordinateSystem = self

    def removePositionPoints(self, *PositionPoints):
        for obj in PositionPoints:
            obj.CoordinateSystem = None

