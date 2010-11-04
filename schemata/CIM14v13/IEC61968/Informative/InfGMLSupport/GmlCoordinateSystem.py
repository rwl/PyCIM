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

class GmlCoordinateSystem(IdentifiedObject):
    """A coordinate reference system consists of a set of coordinate system axes that is related to the earth through a datum that defines the size and shape of the earth or some abstract reference system such as those used for rendering schemantic diagrams, internal views of items such as cabinets, vaults, etc. Geometries in GML indicate the coordinate reference system in which their measurements have been made.
    """

    def __init__(self, positionUnitName='', zMax='', yMax='', zMin='', yMin='', xMin='', scale='', xMax='', GmlPositions=None, GmlDiagramObjects=None, Diagrams=None, *args, **kw_args):
        """Initializes a new 'GmlCoordinateSystem' instance.

        @param positionUnitName: 
        @param zMax: If applicable, the maximum position allowed along the Z axis of the coordinate reference system. 
        @param yMax: The maximum position allowed along the Y axis of the coordinate reference system. 
        @param zMin: If applicable, the minimum position allowed along the Z axis of the coordinate reference system. 
        @param yMin: The minimum position allowed along the Y axis of the coordinate reference system. 
        @param xMin: The minimum position allowed along the X axis of the coordinate reference system. 
        @param scale: 
        @param xMax: The maximum position allowed along the X axis of the coordinate reference system. 
        @param GmlPositions:
        @param GmlDiagramObjects:
        @param Diagrams:
        """

        self.positionUnitName = positionUnitName

        #: If applicable, the maximum position allowed along the Z axis of the coordinate reference system.
        self.zMax = zMax

        #: The maximum position allowed along the Y axis of the coordinate reference system.
        self.yMax = yMax

        #: If applicable, the minimum position allowed along the Z axis of the coordinate reference system.
        self.zMin = zMin

        #: The minimum position allowed along the Y axis of the coordinate reference system.
        self.yMin = yMin

        #: The minimum position allowed along the X axis of the coordinate reference system.
        self.xMin = xMin


        self.scale = scale

        #: The maximum position allowed along the X axis of the coordinate reference system.
        self.xMax = xMax

        self._GmlPositions = []
        self.GmlPositions = [] if GmlPositions is None else GmlPositions

        self._GmlDiagramObjects = []
        self.GmlDiagramObjects = [] if GmlDiagramObjects is None else GmlDiagramObjects

        self._Diagrams = []
        self.Diagrams = [] if Diagrams is None else Diagrams

        super(GmlCoordinateSystem, self).__init__(*args, **kw_args)

    def getGmlPositions(self):
        
        return self._GmlPositions

    def setGmlPositions(self, value):
        for x in self._GmlPositions:
            x._GmlCoordinateSystem = None
        for y in value:
            y._GmlCoordinateSystem = self
        self._GmlPositions = value

    GmlPositions = property(getGmlPositions, setGmlPositions)

    def addGmlPositions(self, *GmlPositions):
        for obj in GmlPositions:
            obj._GmlCoordinateSystem = self
            self._GmlPositions.append(obj)

    def removeGmlPositions(self, *GmlPositions):
        for obj in GmlPositions:
            obj._GmlCoordinateSystem = None
            self._GmlPositions.remove(obj)

    def getGmlDiagramObjects(self):
        
        return self._GmlDiagramObjects

    def setGmlDiagramObjects(self, value):
        for p in self._GmlDiagramObjects:
            filtered = [q for q in p.GmlCoordinateSystems if q != self]
            self._GmlDiagramObjects._GmlCoordinateSystems = filtered
        for r in value:
            if self not in r._GmlCoordinateSystems:
                r._GmlCoordinateSystems.append(self)
        self._GmlDiagramObjects = value

    GmlDiagramObjects = property(getGmlDiagramObjects, setGmlDiagramObjects)

    def addGmlDiagramObjects(self, *GmlDiagramObjects):
        for obj in GmlDiagramObjects:
            if self not in obj._GmlCoordinateSystems:
                obj._GmlCoordinateSystems.append(self)
            self._GmlDiagramObjects.append(obj)

    def removeGmlDiagramObjects(self, *GmlDiagramObjects):
        for obj in GmlDiagramObjects:
            if self in obj._GmlCoordinateSystems:
                obj._GmlCoordinateSystems.remove(self)
            self._GmlDiagramObjects.remove(obj)

    def getDiagrams(self):
        
        return self._Diagrams

    def setDiagrams(self, value):
        for x in self._Diagrams:
            x._GmlCoordinateSystem = None
        for y in value:
            y._GmlCoordinateSystem = self
        self._Diagrams = value

    Diagrams = property(getDiagrams, setDiagrams)

    def addDiagrams(self, *Diagrams):
        for obj in Diagrams:
            obj._GmlCoordinateSystem = self
            self._Diagrams.append(obj)

    def removeDiagrams(self, *Diagrams):
        for obj in Diagrams:
            obj._GmlCoordinateSystem = None
            self._Diagrams.remove(obj)

