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

