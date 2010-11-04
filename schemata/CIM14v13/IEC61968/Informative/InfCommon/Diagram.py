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

from CIM14v13.IEC61968.Common.Document import Document

class Diagram(Document):
    """GML and/or other means are used for rendering objects on various types of displays(geographic, schematic, other) and maps associated with various coordinate systems.
    """

    def __init__(self, kind='geographic', GmlDiagramObjects=None, DesignLocations=None, GmlCoordinateSystem=None, *args, **kw_args):
        """Initializes a new 'Diagram' instance.

        @param kind: Kind of this diagram. Values are: "geographic", "schematic", "designSketch", "internalView", "other"
        @param GmlDiagramObjects:
        @param DesignLocations:
        @param GmlCoordinateSystem:
        """
        #: Kind of this diagram.Values are: "geographic", "schematic", "designSketch", "internalView", "other"
        self.kind = kind

        self._GmlDiagramObjects = []
        self.GmlDiagramObjects = [] if GmlDiagramObjects is None else GmlDiagramObjects

        self._DesignLocations = []
        self.DesignLocations = [] if DesignLocations is None else DesignLocations

        self._GmlCoordinateSystem = None
        self.GmlCoordinateSystem = GmlCoordinateSystem

        super(Diagram, self).__init__(*args, **kw_args)

    def getGmlDiagramObjects(self):
        
        return self._GmlDiagramObjects

    def setGmlDiagramObjects(self, value):
        for p in self._GmlDiagramObjects:
            filtered = [q for q in p.Diagrams if q != self]
            self._GmlDiagramObjects._Diagrams = filtered
        for r in value:
            if self not in r._Diagrams:
                r._Diagrams.append(self)
        self._GmlDiagramObjects = value

    GmlDiagramObjects = property(getGmlDiagramObjects, setGmlDiagramObjects)

    def addGmlDiagramObjects(self, *GmlDiagramObjects):
        for obj in GmlDiagramObjects:
            if self not in obj._Diagrams:
                obj._Diagrams.append(self)
            self._GmlDiagramObjects.append(obj)

    def removeGmlDiagramObjects(self, *GmlDiagramObjects):
        for obj in GmlDiagramObjects:
            if self in obj._Diagrams:
                obj._Diagrams.remove(self)
            self._GmlDiagramObjects.remove(obj)

    def getDesignLocations(self):
        
        return self._DesignLocations

    def setDesignLocations(self, value):
        for p in self._DesignLocations:
            filtered = [q for q in p.Diagrams if q != self]
            self._DesignLocations._Diagrams = filtered
        for r in value:
            if self not in r._Diagrams:
                r._Diagrams.append(self)
        self._DesignLocations = value

    DesignLocations = property(getDesignLocations, setDesignLocations)

    def addDesignLocations(self, *DesignLocations):
        for obj in DesignLocations:
            if self not in obj._Diagrams:
                obj._Diagrams.append(self)
            self._DesignLocations.append(obj)

    def removeDesignLocations(self, *DesignLocations):
        for obj in DesignLocations:
            if self in obj._Diagrams:
                obj._Diagrams.remove(self)
            self._DesignLocations.remove(obj)

    def getGmlCoordinateSystem(self):
        
        return self._GmlCoordinateSystem

    def setGmlCoordinateSystem(self, value):
        if self._GmlCoordinateSystem is not None:
            filtered = [x for x in self.GmlCoordinateSystem.Diagrams if x != self]
            self._GmlCoordinateSystem._Diagrams = filtered

        self._GmlCoordinateSystem = value
        if self._GmlCoordinateSystem is not None:
            self._GmlCoordinateSystem._Diagrams.append(self)

    GmlCoordinateSystem = property(getGmlCoordinateSystem, setGmlCoordinateSystem)

