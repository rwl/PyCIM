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

class PositionPoint(Element):
    """Set of spatial coordinates that determine a point. Use a single position point instance to desribe a point-oriented location. Use a sequence of position points to describe a line-oriented object (physical location of non-point oriented objects like cables or lines), or area of an object (like a substation or a geographical zone - in this case, have first and last position point with the same values).
    """

    def __init__(self, xPosition='', zPosition='', sequenceNumber=0, yPosition='', Location=None, CoordinateSystem=None, *args, **kw_args):
        """Initialises a new 'PositionPoint' instance.

        @param xPosition: X axis position. 
        @param zPosition: (if applicable) Z axis position. 
        @param sequenceNumber: Zero-relative sequence number of this point within a series of points. 
        @param yPosition: Y axis position. 
        @param Location: Location that this position point describes.
        @param CoordinateSystem: Coordinate system in which the coordinates of this position point are expressed.
        """
        #: X axis position.
        self.xPosition = xPosition

        #: (if applicable) Z axis position.
        self.zPosition = zPosition

        #: Zero-relative sequence number of this point within a series of points.
        self.sequenceNumber = sequenceNumber

        #: Y axis position.
        self.yPosition = yPosition

        self._Location = None
        self.Location = Location

        self._CoordinateSystem = None
        self.CoordinateSystem = CoordinateSystem

        super(PositionPoint, self).__init__(*args, **kw_args)

    _attrs = ["xPosition", "zPosition", "sequenceNumber", "yPosition"]
    _attr_types = {"xPosition": str, "zPosition": str, "sequenceNumber": int, "yPosition": str}
    _defaults = {"xPosition": '', "zPosition": '', "sequenceNumber": 0, "yPosition": ''}
    _enums = {}
    _refs = ["Location", "CoordinateSystem"]
    _many_refs = []

    def getLocation(self):
        """Location that this position point describes.
        """
        return self._Location

    def setLocation(self, value):
        if self._Location is not None:
            filtered = [x for x in self.Location.PositionPoints if x != self]
            self._Location._PositionPoints = filtered

        self._Location = value
        if self._Location is not None:
            if self not in self._Location._PositionPoints:
                self._Location._PositionPoints.append(self)

    Location = property(getLocation, setLocation)

    def getCoordinateSystem(self):
        """Coordinate system in which the coordinates of this position point are expressed.
        """
        return self._CoordinateSystem

    def setCoordinateSystem(self, value):
        if self._CoordinateSystem is not None:
            filtered = [x for x in self.CoordinateSystem.PositionPoints if x != self]
            self._CoordinateSystem._PositionPoints = filtered

        self._CoordinateSystem = value
        if self._CoordinateSystem is not None:
            if self not in self._CoordinateSystem._PositionPoints:
                self._CoordinateSystem._PositionPoints.append(self)

    CoordinateSystem = property(getCoordinateSystem, setCoordinateSystem)

