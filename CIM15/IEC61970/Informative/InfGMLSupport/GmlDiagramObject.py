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

class GmlDiagramObject(IdentifiedObject):
    """Any of the magnitudes that serve to define the position of a point by reference to a fixed figure, system of lines, etc.Any of the magnitudes that serve to define the position of a point by reference to a fixed figure, system of lines, etc.
    """

    def __init__(self, GmlSelectors=None, Diagrams=None, CoordinateSystems=None, GmlPointSymbols=None, GmlLineSymbols=None, GmlRasterSymbols=None, GmlObservatins=None, GmlTextSymbols=None, GmlPolygonSymbols=None, *args, **kw_args):
        """Initialises a new 'GmlDiagramObject' instance.

        @param GmlSelectors:
        @param Diagrams:
        @param CoordinateSystems:
        @param GmlPointSymbols:
        @param GmlLineSymbols:
        @param GmlRasterSymbols:
        @param GmlObservatins:
        @param GmlTextSymbols:
        @param GmlPolygonSymbols:
        """
        self._GmlSelectors = []
        self.GmlSelectors = [] if GmlSelectors is None else GmlSelectors

        self._Diagrams = []
        self.Diagrams = [] if Diagrams is None else Diagrams

        self._CoordinateSystems = []
        self.CoordinateSystems = [] if CoordinateSystems is None else CoordinateSystems

        self._GmlPointSymbols = []
        self.GmlPointSymbols = [] if GmlPointSymbols is None else GmlPointSymbols

        self._GmlLineSymbols = []
        self.GmlLineSymbols = [] if GmlLineSymbols is None else GmlLineSymbols

        self._GmlRasterSymbols = []
        self.GmlRasterSymbols = [] if GmlRasterSymbols is None else GmlRasterSymbols

        self._GmlObservatins = []
        self.GmlObservatins = [] if GmlObservatins is None else GmlObservatins

        self._GmlTextSymbols = []
        self.GmlTextSymbols = [] if GmlTextSymbols is None else GmlTextSymbols

        self._GmlPolygonSymbols = []
        self.GmlPolygonSymbols = [] if GmlPolygonSymbols is None else GmlPolygonSymbols

        super(GmlDiagramObject, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["GmlSelectors", "Diagrams", "CoordinateSystems", "GmlPointSymbols", "GmlLineSymbols", "GmlRasterSymbols", "GmlObservatins", "GmlTextSymbols", "GmlPolygonSymbols"]
    _many_refs = ["GmlSelectors", "Diagrams", "CoordinateSystems", "GmlPointSymbols", "GmlLineSymbols", "GmlRasterSymbols", "GmlObservatins", "GmlTextSymbols", "GmlPolygonSymbols"]

    def getGmlSelectors(self):
        
        return self._GmlSelectors

    def setGmlSelectors(self, value):
        for p in self._GmlSelectors:
            filtered = [q for q in p.GmlDiagramObjects if q != self]
            self._GmlSelectors._GmlDiagramObjects = filtered
        for r in value:
            if self not in r._GmlDiagramObjects:
                r._GmlDiagramObjects.append(self)
        self._GmlSelectors = value

    GmlSelectors = property(getGmlSelectors, setGmlSelectors)

    def addGmlSelectors(self, *GmlSelectors):
        for obj in GmlSelectors:
            if self not in obj._GmlDiagramObjects:
                obj._GmlDiagramObjects.append(self)
            self._GmlSelectors.append(obj)

    def removeGmlSelectors(self, *GmlSelectors):
        for obj in GmlSelectors:
            if self in obj._GmlDiagramObjects:
                obj._GmlDiagramObjects.remove(self)
            self._GmlSelectors.remove(obj)

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

    def getCoordinateSystems(self):
        
        return self._CoordinateSystems

    def setCoordinateSystems(self, value):
        for p in self._CoordinateSystems:
            filtered = [q for q in p.GmlDiagramObjects if q != self]
            self._CoordinateSystems._GmlDiagramObjects = filtered
        for r in value:
            if self not in r._GmlDiagramObjects:
                r._GmlDiagramObjects.append(self)
        self._CoordinateSystems = value

    CoordinateSystems = property(getCoordinateSystems, setCoordinateSystems)

    def addCoordinateSystems(self, *CoordinateSystems):
        for obj in CoordinateSystems:
            if self not in obj._GmlDiagramObjects:
                obj._GmlDiagramObjects.append(self)
            self._CoordinateSystems.append(obj)

    def removeCoordinateSystems(self, *CoordinateSystems):
        for obj in CoordinateSystems:
            if self in obj._GmlDiagramObjects:
                obj._GmlDiagramObjects.remove(self)
            self._CoordinateSystems.remove(obj)

    def getGmlPointSymbols(self):
        
        return self._GmlPointSymbols

    def setGmlPointSymbols(self, value):
        for x in self._GmlPointSymbols:
            x.GmlDiagramObject = None
        for y in value:
            y._GmlDiagramObject = self
        self._GmlPointSymbols = value

    GmlPointSymbols = property(getGmlPointSymbols, setGmlPointSymbols)

    def addGmlPointSymbols(self, *GmlPointSymbols):
        for obj in GmlPointSymbols:
            obj.GmlDiagramObject = self

    def removeGmlPointSymbols(self, *GmlPointSymbols):
        for obj in GmlPointSymbols:
            obj.GmlDiagramObject = None

    def getGmlLineSymbols(self):
        
        return self._GmlLineSymbols

    def setGmlLineSymbols(self, value):
        for x in self._GmlLineSymbols:
            x.GmlDiagramObject = None
        for y in value:
            y._GmlDiagramObject = self
        self._GmlLineSymbols = value

    GmlLineSymbols = property(getGmlLineSymbols, setGmlLineSymbols)

    def addGmlLineSymbols(self, *GmlLineSymbols):
        for obj in GmlLineSymbols:
            obj.GmlDiagramObject = self

    def removeGmlLineSymbols(self, *GmlLineSymbols):
        for obj in GmlLineSymbols:
            obj.GmlDiagramObject = None

    def getGmlRasterSymbols(self):
        
        return self._GmlRasterSymbols

    def setGmlRasterSymbols(self, value):
        for x in self._GmlRasterSymbols:
            x.GmlDiagramObject = None
        for y in value:
            y._GmlDiagramObject = self
        self._GmlRasterSymbols = value

    GmlRasterSymbols = property(getGmlRasterSymbols, setGmlRasterSymbols)

    def addGmlRasterSymbols(self, *GmlRasterSymbols):
        for obj in GmlRasterSymbols:
            obj.GmlDiagramObject = self

    def removeGmlRasterSymbols(self, *GmlRasterSymbols):
        for obj in GmlRasterSymbols:
            obj.GmlDiagramObject = None

    def getGmlObservatins(self):
        
        return self._GmlObservatins

    def setGmlObservatins(self, value):
        for p in self._GmlObservatins:
            filtered = [q for q in p.GmlDiagramObjects if q != self]
            self._GmlObservatins._GmlDiagramObjects = filtered
        for r in value:
            if self not in r._GmlDiagramObjects:
                r._GmlDiagramObjects.append(self)
        self._GmlObservatins = value

    GmlObservatins = property(getGmlObservatins, setGmlObservatins)

    def addGmlObservatins(self, *GmlObservatins):
        for obj in GmlObservatins:
            if self not in obj._GmlDiagramObjects:
                obj._GmlDiagramObjects.append(self)
            self._GmlObservatins.append(obj)

    def removeGmlObservatins(self, *GmlObservatins):
        for obj in GmlObservatins:
            if self in obj._GmlDiagramObjects:
                obj._GmlDiagramObjects.remove(self)
            self._GmlObservatins.remove(obj)

    def getGmlTextSymbols(self):
        
        return self._GmlTextSymbols

    def setGmlTextSymbols(self, value):
        for x in self._GmlTextSymbols:
            x.GmlDiagramObject = None
        for y in value:
            y._GmlDiagramObject = self
        self._GmlTextSymbols = value

    GmlTextSymbols = property(getGmlTextSymbols, setGmlTextSymbols)

    def addGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj.GmlDiagramObject = self

    def removeGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj.GmlDiagramObject = None

    def getGmlPolygonSymbols(self):
        
        return self._GmlPolygonSymbols

    def setGmlPolygonSymbols(self, value):
        for x in self._GmlPolygonSymbols:
            x.GmlDiagramObject = None
        for y in value:
            y._GmlDiagramObject = self
        self._GmlPolygonSymbols = value

    GmlPolygonSymbols = property(getGmlPolygonSymbols, setGmlPolygonSymbols)

    def addGmlPolygonSymbols(self, *GmlPolygonSymbols):
        for obj in GmlPolygonSymbols:
            obj.GmlDiagramObject = self

    def removeGmlPolygonSymbols(self, *GmlPolygonSymbols):
        for obj in GmlPolygonSymbols:
            obj.GmlDiagramObject = None

