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

from CIM14.CDPSM.Unbalanced.Element import Element

class PositionPoint(Element):
    """Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object.
    """

    def __init__(self, sequenceNumber=0, xPosition='', yPosition='', Location=None, *args, **kw_args):
        """Initialises a new 'PositionPoint' instance.

        @param sequenceNumber: Zero-relative sequence number of this point within a series of points. 
        @param xPosition: X axis position. 
        @param yPosition: Y axis position. 
        @param Location: Location that this position point describes.
        """
        #: Zero-relative sequence number of this point within a series of points.
        self.sequenceNumber = sequenceNumber

        #: X axis position.
        self.xPosition = xPosition

        #: Y axis position.
        self.yPosition = yPosition

        self._Location = None
        self.Location = Location

        super(PositionPoint, self).__init__(*args, **kw_args)

    _attrs = ["sequenceNumber", "xPosition", "yPosition"]
    _attr_types = {"sequenceNumber": int, "xPosition": str, "yPosition": str}
    _defaults = {"sequenceNumber": 0, "xPosition": '', "yPosition": ''}
    _enums = {}
    _refs = ["Location"]
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

