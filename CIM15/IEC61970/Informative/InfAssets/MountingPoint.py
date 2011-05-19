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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class MountingPoint(IdentifiedObject):
    """Point on a structure that a connection may have a conductor connected to. Defined with an x and y coordinate plus a phase. A connection may have multiple mounting points, one for each phase.Point on a structure that a connection may have a conductor connected to. Defined with an x and y coordinate plus a phase. A connection may have multiple mounting points, one for each phase.
    """

    def __init__(self, xCoord=0, phaseCode="s12N", yCoord=0, Connections=None, OverheadConductors=None, *args, **kw_args):
        """Initialises a new 'MountingPoint' instance.

        @param xCoord: 
        @param phaseCode: Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        @param yCoord: 
        @param Connections:
        @param OverheadConductors:
        """

        self.xCoord = xCoord

        #: Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        self.phaseCode = phaseCode


        self.yCoord = yCoord

        self._Connections = []
        self.Connections = [] if Connections is None else Connections

        self._OverheadConductors = []
        self.OverheadConductors = [] if OverheadConductors is None else OverheadConductors

        super(MountingPoint, self).__init__(*args, **kw_args)

    _attrs = ["xCoord", "phaseCode", "yCoord"]
    _attr_types = {"xCoord": int, "phaseCode": str, "yCoord": int}
    _defaults = {"xCoord": 0, "phaseCode": "s12N", "yCoord": 0}
    _enums = {"phaseCode": "PhaseCode"}
    _refs = ["Connections", "OverheadConductors"]
    _many_refs = ["Connections", "OverheadConductors"]

    def getConnections(self):
        
        return self._Connections

    def setConnections(self, value):
        for p in self._Connections:
            filtered = [q for q in p.MountingPoints if q != self]
            self._Connections._MountingPoints = filtered
        for r in value:
            if self not in r._MountingPoints:
                r._MountingPoints.append(self)
        self._Connections = value

    Connections = property(getConnections, setConnections)

    def addConnections(self, *Connections):
        for obj in Connections:
            if self not in obj._MountingPoints:
                obj._MountingPoints.append(self)
            self._Connections.append(obj)

    def removeConnections(self, *Connections):
        for obj in Connections:
            if self in obj._MountingPoints:
                obj._MountingPoints.remove(self)
            self._Connections.remove(obj)

    def getOverheadConductors(self):
        
        return self._OverheadConductors

    def setOverheadConductors(self, value):
        for x in self._OverheadConductors:
            x.MountingPoint = None
        for y in value:
            y._MountingPoint = self
        self._OverheadConductors = value

    OverheadConductors = property(getOverheadConductors, setOverheadConductors)

    def addOverheadConductors(self, *OverheadConductors):
        for obj in OverheadConductors:
            obj.MountingPoint = self

    def removeOverheadConductors(self, *OverheadConductors):
        for obj in OverheadConductors:
            obj.MountingPoint = None

