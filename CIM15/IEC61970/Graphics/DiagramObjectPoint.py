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

from CIM15.Element import Element

class DiagramObjectPoint(Element):
    """A point in a given space defined by 3 coordinates and associated to a DiagramObject.  The coordinates may be positive or negative as the origin does not have to be in the corner of a diagram.  The sequence attribute is used when a DiagramObject has more than one DiagramObjectPoint in which case this defines the drawing order.  A DiagramObject may represent any CIM object. For single line diagrams such objects typically are &bull; analog values &bull; breaker/disconnector &bull; power transformer &bull; transmission lineA point in a given space defined by 3 coordinates and associated to a DiagramObject.  The coordinates may be positive or negative as the origin does not have to be in the corner of a diagram.  The sequence attribute is used when a DiagramObject has more than one DiagramObjectPoint in which case this defines the drawing order.  A DiagramObject may represent any CIM object. For single line diagrams such objects typically are &bull; analog values &bull; breaker/disconnector &bull; power transformer &bull; transmission line
    """

    def __init__(self, sequenceNumber=0, xPosition=0.0, yPosition=0.0, zPosition=0.0, DiagramObjectGluePoint=None, DiagramObject=None, *args, **kw_args):
        """Initialises a new 'DiagramObjectPoint' instance.

        @param sequenceNumber: The sequence position of the point, used for defining the order of points for DiagramObjects acting as a polyline or polygon with more than one point 
        @param xPosition: The X coordinate of this point 
        @param yPosition: The Y coordinate of this point 
        @param zPosition: The Z coordinate of this point 
        @param DiagramObjectGluePoint: The 'glue' point that this point is associated with
        @param DiagramObject: The diagram object with which the points are associated
        """
        #: The sequence position of the point, used for defining the order of points for DiagramObjects acting as a polyline or polygon with more than one point
        self.sequenceNumber = sequenceNumber

        #: The X coordinate of this point
        self.xPosition = xPosition

        #: The Y coordinate of this point
        self.yPosition = yPosition

        #: The Z coordinate of this point
        self.zPosition = zPosition

        self._DiagramObjectGluePoint = None
        self.DiagramObjectGluePoint = DiagramObjectGluePoint

        self._DiagramObject = None
        self.DiagramObject = DiagramObject

        super(DiagramObjectPoint, self).__init__(*args, **kw_args)

    _attrs = ["sequenceNumber", "xPosition", "yPosition", "zPosition"]
    _attr_types = {"sequenceNumber": int, "xPosition": float, "yPosition": float, "zPosition": float}
    _defaults = {"sequenceNumber": 0, "xPosition": 0.0, "yPosition": 0.0, "zPosition": 0.0}
    _enums = {}
    _refs = ["DiagramObjectGluePoint", "DiagramObject"]
    _many_refs = []

    def getDiagramObjectGluePoint(self):
        """The 'glue' point that this point is associated with
        """
        return self._DiagramObjectGluePoint

    def setDiagramObjectGluePoint(self, value):
        if self._DiagramObjectGluePoint is not None:
            filtered = [x for x in self.DiagramObjectGluePoint.DiagramObjectPoints if x != self]
            self._DiagramObjectGluePoint._DiagramObjectPoints = filtered

        self._DiagramObjectGluePoint = value
        if self._DiagramObjectGluePoint is not None:
            if self not in self._DiagramObjectGluePoint._DiagramObjectPoints:
                self._DiagramObjectGluePoint._DiagramObjectPoints.append(self)

    DiagramObjectGluePoint = property(getDiagramObjectGluePoint, setDiagramObjectGluePoint)

    def getDiagramObject(self):
        """The diagram object with which the points are associated
        """
        return self._DiagramObject

    def setDiagramObject(self, value):
        if self._DiagramObject is not None:
            filtered = [x for x in self.DiagramObject.DiagramObjectPoints if x != self]
            self._DiagramObject._DiagramObjectPoints = filtered

        self._DiagramObject = value
        if self._DiagramObject is not None:
            if self not in self._DiagramObject._DiagramObjectPoints:
                self._DiagramObject._DiagramObjectPoints.append(self)

    DiagramObject = property(getDiagramObject, setDiagramObject)

