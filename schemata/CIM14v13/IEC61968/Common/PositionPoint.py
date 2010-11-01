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

from CIM14v13.Element import Element

class PositionPoint(Element):
    """Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object.
    """

    def __init__(self, sequenceNumber=0, zPosition='', xPosition='', yPosition='', Location=None, *args, **kw_args):
        """Initializes a new 'PositionPoint' instance.

        @param sequenceNumber: Zero-relative sequence number of this point within a series of points. 
        @param zPosition: (if applicable) Z axis position. 
        @param xPosition: X axis position. 
        @param yPosition: Y axis position. 
        @param Location: Location that this position point describes.
        """
        #: Zero-relative sequence number of this point within a series of points. 
        self.sequenceNumber = sequenceNumber

        #: (if applicable) Z axis position. 
        self.zPosition = zPosition

        #: X axis position. 
        self.xPosition = xPosition

        #: Y axis position. 
        self.yPosition = yPosition

        self._Location = None
        self.Location = Location

        super(PositionPoint, self).__init__(*args, **kw_args)

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
            self._Location._PositionPoints.append(self)

    Location = property(getLocation, setLocation)

