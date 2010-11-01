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

class Connection(IdentifiedObject):
    """A structure can have multiple connection points for electrical connections (e.g. line) each with multiple mounting points, one for each phase. e.g. a Tower may have three Connections, two with three mounting points, one for each phase and a third with a single mounting point for the neutral line. A pole, on the other hand, may have a single Connection with one, two or three mounting points depending on whether it is carrying 1,2 or 3 phases.
    """

    def __init__(self, StructureTypeAssets=None, MountingPoints=None, *args, **kw_args):
        """Initializes a new 'Connection' instance.

        @param StructureTypeAssets:
        @param MountingPoints:
        """
        self._StructureTypeAssets = []
        self.StructureTypeAssets = [] if StructureTypeAssets is None else StructureTypeAssets

        self._MountingPoints = []
        self.MountingPoints = [] if MountingPoints is None else MountingPoints

        super(Connection, self).__init__(*args, **kw_args)

    def getStructureTypeAssets(self):
        
        return self._StructureTypeAssets

    def setStructureTypeAssets(self, value):
        for p in self._StructureTypeAssets:
            filtered = [q for q in p.MountConnections if q != self]
            self._StructureTypeAssets._MountConnections = filtered
        for r in value:
            if self not in r._MountConnections:
                r._MountConnections.append(self)
        self._StructureTypeAssets = value

    StructureTypeAssets = property(getStructureTypeAssets, setStructureTypeAssets)

    def addStructureTypeAssets(self, *StructureTypeAssets):
        for obj in StructureTypeAssets:
            if self not in obj._MountConnections:
                obj._MountConnections.append(self)
            self._StructureTypeAssets.append(obj)

    def removeStructureTypeAssets(self, *StructureTypeAssets):
        for obj in StructureTypeAssets:
            if self in obj._MountConnections:
                obj._MountConnections.remove(self)
            self._StructureTypeAssets.remove(obj)

    def getMountingPoints(self):
        
        return self._MountingPoints

    def setMountingPoints(self, value):
        for p in self._MountingPoints:
            filtered = [q for q in p.Connections if q != self]
            self._MountingPoints._Connections = filtered
        for r in value:
            if self not in r._Connections:
                r._Connections.append(self)
        self._MountingPoints = value

    MountingPoints = property(getMountingPoints, setMountingPoints)

    def addMountingPoints(self, *MountingPoints):
        for obj in MountingPoints:
            if self not in obj._Connections:
                obj._Connections.append(self)
            self._MountingPoints.append(obj)

    def removeMountingPoints(self, *MountingPoints):
        for obj in MountingPoints:
            if self in obj._Connections:
                obj._Connections.remove(self)
            self._MountingPoints.remove(obj)

