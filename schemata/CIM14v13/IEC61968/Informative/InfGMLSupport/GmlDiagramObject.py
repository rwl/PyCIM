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

from CIM14v13.IEC61968.Common.Location import Location

class GmlDiagramObject(Location):
    """Any of the magnitudes that serve to define the position of a point by reference to a fixed figure, system of lines, etc.
    """

    def __init__(self, Diagrams=None, GmlLineSymbols=None, GmlCoordinateSystems=None, GmlRasterSymbols=None, GmlPolygonSymbols=None, GmlPointSymbols=None, GmlTextSymbols=None, **kw_args):
        """Initializes a new 'GmlDiagramObject' instance.

        @param Diagrams:
        @param GmlLineSymbols:
        @param GmlCoordinateSystems:
        @param GmlRasterSymbols:
        @param GmlPolygonSymbols:
        @param GmlPointSymbols:
        @param GmlTextSymbols:
        """
        self._Diagrams = []
        self.Diagrams = [] if Diagrams is None else Diagrams

        self._GmlLineSymbols = []
        self.GmlLineSymbols = [] if GmlLineSymbols is None else GmlLineSymbols

        self._GmlCoordinateSystems = []
        self.GmlCoordinateSystems = [] if GmlCoordinateSystems is None else GmlCoordinateSystems

        self._GmlRasterSymbols = []
        self.GmlRasterSymbols = [] if GmlRasterSymbols is None else GmlRasterSymbols

        self._GmlPolygonSymbols = []
        self.GmlPolygonSymbols = [] if GmlPolygonSymbols is None else GmlPolygonSymbols

        self._GmlPointSymbols = []
        self.GmlPointSymbols = [] if GmlPointSymbols is None else GmlPointSymbols

        self._GmlTextSymbols = []
        self.GmlTextSymbols = [] if GmlTextSymbols is None else GmlTextSymbols

        super(GmlDiagramObject, self).__init__(**kw_args)

    def getDiagrams(self):
        
        return self._Diagrams

    def setDiagrams(self, value):
        for p in self._Diagrams:
            filtered = [q for q in p.GmlDiagramObjects if q != self]
            self._Diagrams._GmlDiagramObjects = filtered
        for r in value:
            if self not in r._GmlDiagramObjects:
                r._GmlDiagramObjects.append(self)
        self._Diagrams = value

    Diagrams = property(getDiagrams, setDiagrams)

    def addDiagrams(self, *Diagrams):
        for obj in Diagrams:
            if self not in obj._GmlDiagramObjects:
                obj._GmlDiagramObjects.append(self)
            self._Diagrams.append(obj)

    def removeDiagrams(self, *Diagrams):
        for obj in Diagrams:
            if self in obj._GmlDiagramObjects:
                obj._GmlDiagramObjects.remove(self)
            self._Diagrams.remove(obj)

    def getGmlLineSymbols(self):
        
        return self._GmlLineSymbols

    def setGmlLineSymbols(self, value):
        for x in self._GmlLineSymbols:
            x._GmlDiagramObject = None
        for y in value:
            y._GmlDiagramObject = self
        self._GmlLineSymbols = value

    GmlLineSymbols = property(getGmlLineSymbols, setGmlLineSymbols)

    def addGmlLineSymbols(self, *GmlLineSymbols):
        for obj in GmlLineSymbols:
            obj._GmlDiagramObject = self
            self._GmlLineSymbols.append(obj)

    def removeGmlLineSymbols(self, *GmlLineSymbols):
        for obj in GmlLineSymbols:
            obj._GmlDiagramObject = None
            self._GmlLineSymbols.remove(obj)

    def getGmlCoordinateSystems(self):
        
        return self._GmlCoordinateSystems

    def setGmlCoordinateSystems(self, value):
        for p in self._GmlCoordinateSystems:
            filtered = [q for q in p.GmlDiagramObjects if q != self]
            self._GmlCoordinateSystems._GmlDiagramObjects = filtered
        for r in value:
            if self not in r._GmlDiagramObjects:
                r._GmlDiagramObjects.append(self)
        self._GmlCoordinateSystems = value

    GmlCoordinateSystems = property(getGmlCoordinateSystems, setGmlCoordinateSystems)

    def addGmlCoordinateSystems(self, *GmlCoordinateSystems):
        for obj in GmlCoordinateSystems:
            if self not in obj._GmlDiagramObjects:
                obj._GmlDiagramObjects.append(self)
            self._GmlCoordinateSystems.append(obj)

    def removeGmlCoordinateSystems(self, *GmlCoordinateSystems):
        for obj in GmlCoordinateSystems:
            if self in obj._GmlDiagramObjects:
                obj._GmlDiagramObjects.remove(self)
            self._GmlCoordinateSystems.remove(obj)

    def getGmlRasterSymbols(self):
        
        return self._GmlRasterSymbols

    def setGmlRasterSymbols(self, value):
        for x in self._GmlRasterSymbols:
            x._GmlDiagramObject = None
        for y in value:
            y._GmlDiagramObject = self
        self._GmlRasterSymbols = value

    GmlRasterSymbols = property(getGmlRasterSymbols, setGmlRasterSymbols)

    def addGmlRasterSymbols(self, *GmlRasterSymbols):
        for obj in GmlRasterSymbols:
            obj._GmlDiagramObject = self
            self._GmlRasterSymbols.append(obj)

    def removeGmlRasterSymbols(self, *GmlRasterSymbols):
        for obj in GmlRasterSymbols:
            obj._GmlDiagramObject = None
            self._GmlRasterSymbols.remove(obj)

    def getGmlPolygonSymbols(self):
        
        return self._GmlPolygonSymbols

    def setGmlPolygonSymbols(self, value):
        for x in self._GmlPolygonSymbols:
            x._GmlDiagramObject = None
        for y in value:
            y._GmlDiagramObject = self
        self._GmlPolygonSymbols = value

    GmlPolygonSymbols = property(getGmlPolygonSymbols, setGmlPolygonSymbols)

    def addGmlPolygonSymbols(self, *GmlPolygonSymbols):
        for obj in GmlPolygonSymbols:
            obj._GmlDiagramObject = self
            self._GmlPolygonSymbols.append(obj)

    def removeGmlPolygonSymbols(self, *GmlPolygonSymbols):
        for obj in GmlPolygonSymbols:
            obj._GmlDiagramObject = None
            self._GmlPolygonSymbols.remove(obj)

    def getGmlPointSymbols(self):
        
        return self._GmlPointSymbols

    def setGmlPointSymbols(self, value):
        for x in self._GmlPointSymbols:
            x._GmlDiagramObject = None
        for y in value:
            y._GmlDiagramObject = self
        self._GmlPointSymbols = value

    GmlPointSymbols = property(getGmlPointSymbols, setGmlPointSymbols)

    def addGmlPointSymbols(self, *GmlPointSymbols):
        for obj in GmlPointSymbols:
            obj._GmlDiagramObject = self
            self._GmlPointSymbols.append(obj)

    def removeGmlPointSymbols(self, *GmlPointSymbols):
        for obj in GmlPointSymbols:
            obj._GmlDiagramObject = None
            self._GmlPointSymbols.remove(obj)

    def getGmlTextSymbols(self):
        
        return self._GmlTextSymbols

    def setGmlTextSymbols(self, value):
        for x in self._GmlTextSymbols:
            x._GmlDiagramObject = None
        for y in value:
            y._GmlDiagramObject = self
        self._GmlTextSymbols = value

    GmlTextSymbols = property(getGmlTextSymbols, setGmlTextSymbols)

    def addGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj._GmlDiagramObject = self
            self._GmlTextSymbols.append(obj)

    def removeGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj._GmlDiagramObject = None
            self._GmlTextSymbols.remove(obj)

