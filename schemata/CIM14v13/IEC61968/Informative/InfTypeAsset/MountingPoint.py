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

class MountingPoint(IdentifiedObject):
    """Point on a structure that a connection may have a conductor connected to. Defined with an x and y coordinate plus a phase. A connection may have multiple mounting points, one for each phase.
    """

    def __init__(self, phaseCode='BC', yCoord=0, xCoord=0, OverheadConductors=None, Connections=None, *args, **kw_args):
        """Initializes a new 'MountingPoint' instance.

        @param phaseCode: Values are: "BC", "AB", "B", "AC", "ABC", "splitSecondary1N", "ABN", "ABCN", "CN", "AN", "splitSecondary12N", "BCN", "splitSecondary2N", "ACN", "A", "C", "N", "BN"
        @param yCoord: 
        @param xCoord: 
        @param OverheadConductors:
        @param Connections:
        """
        #: Values are: "BC", "AB", "B", "AC", "ABC", "splitSecondary1N", "ABN", "ABCN", "CN", "AN", "splitSecondary12N", "BCN", "splitSecondary2N", "ACN", "A", "C", "N", "BN"
        self.phaseCode = phaseCode


        self.yCoord = yCoord


        self.xCoord = xCoord

        self._OverheadConductors = []
        self.OverheadConductors = [] if OverheadConductors is None else OverheadConductors

        self._Connections = []
        self.Connections = [] if Connections is None else Connections

        super(MountingPoint, self).__init__(*args, **kw_args)

    def getOverheadConductors(self):
        
        return self._OverheadConductors

    def setOverheadConductors(self, value):
        for x in self._OverheadConductors:
            x._MountingPoint = None
        for y in value:
            y._MountingPoint = self
        self._OverheadConductors = value

    OverheadConductors = property(getOverheadConductors, setOverheadConductors)

    def addOverheadConductors(self, *OverheadConductors):
        for obj in OverheadConductors:
            obj._MountingPoint = self
            self._OverheadConductors.append(obj)

    def removeOverheadConductors(self, *OverheadConductors):
        for obj in OverheadConductors:
            obj._MountingPoint = None
            self._OverheadConductors.remove(obj)

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

