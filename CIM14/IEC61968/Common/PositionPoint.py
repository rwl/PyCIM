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

