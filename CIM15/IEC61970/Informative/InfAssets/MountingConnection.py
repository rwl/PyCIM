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

class MountingConnection(IdentifiedObject):
    """A structure can have multiple connection points for electrical connections (e.g. line) each with multiple mounting points, one for each phase. e.g. a Tower may have three Connections, two with three mounting points, one for each phase and a third with a single mounting point for the neutral line. A pole, on the other hand, may have a single Connection with one, two or three mounting points depending on whether it is carrying 1,2 or 3 phases.A structure can have multiple connection points for electrical connections (e.g. line) each with multiple mounting points, one for each phase. e.g. a Tower may have three Connections, two with three mounting points, one for each phase and a third with a single mounting point for the neutral line. A pole, on the other hand, may have a single Connection with one, two or three mounting points depending on whether it is carrying 1,2 or 3 phases.
    """

    def __init__(self, StructureInfos=None, MountingPoints=None, *args, **kw_args):
        """Initialises a new 'MountingConnection' instance.

        @param StructureInfos:
        @param MountingPoints:
        """
        self._StructureInfos = []
        self.StructureInfos = [] if StructureInfos is None else StructureInfos

        self._MountingPoints = []
        self.MountingPoints = [] if MountingPoints is None else MountingPoints

        super(MountingConnection, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["StructureInfos", "MountingPoints"]
    _many_refs = ["StructureInfos", "MountingPoints"]

    def getStructureInfos(self):
        
        return self._StructureInfos

    def setStructureInfos(self, value):
        for p in self._StructureInfos:
            filtered = [q for q in p.MountingConnections if q != self]
            self._StructureInfos._MountingConnections = filtered
        for r in value:
            if self not in r._MountingConnections:
                r._MountingConnections.append(self)
        self._StructureInfos = value

    StructureInfos = property(getStructureInfos, setStructureInfos)

    def addStructureInfos(self, *StructureInfos):
        for obj in StructureInfos:
            if self not in obj._MountingConnections:
                obj._MountingConnections.append(self)
            self._StructureInfos.append(obj)

    def removeStructureInfos(self, *StructureInfos):
        for obj in StructureInfos:
            if self in obj._MountingConnections:
                obj._MountingConnections.remove(self)
            self._StructureInfos.remove(obj)

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

