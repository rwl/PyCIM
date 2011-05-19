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

from CIM15.IEC61968.Common.Document import Document

class Diagram(Document):
    """The Diagram represents the diagram being exchanged. The initialView attributes can be used to specify an initial view with the x,y coordinates of the diagonal points. The coordinate system is a standard Cartesian coordinate system and the orientation attribute defines a positive or negative orientation.  A positive orientation gives standard &lsquo;right-hand&rsquo; orientation, with negative orientation indicating a &lsquo;left-hand&rsquo; orientation.  For 2D diagrams, a positive orientation will result in X values increasing from left to right and Y values increasing from bottom to top.  A negative orientation gives the &lsquo;left-hand&rsquo; orientation (favoured by computer graphics displays) with X values increasing from left to right and Y values increasing from top to bottom.The Diagram represents the diagram being exchanged. The initialView attributes can be used to specify an initial view with the x,y coordinates of the diagonal points. The coordinate system is a standard Cartesian coordinate system and the orientation attribute defines a positive or negative orientation.  A positive orientation gives standard &lsquo;right-hand&rsquo; orientation, with negative orientation indicating a &lsquo;left-hand&rsquo; orientation.  For 2D diagrams, a positive orientation will result in X values increasing from left to right and Y values increasing from bottom to top.  A negative orientation gives the &lsquo;left-hand&rsquo; orientation (favoured by computer graphics displays) with X values increasing from left to right and Y values increasing from top to bottom.
    """

    def __init__(self, y1InitialView=0.0, kind="other", x2InitialView=0.0, x1InitialView=0.0, orientation="negative", y2InitialView=0.0, DiagramObjects=None, CoordinateSystem=None, GmlDiagramObjects=None, DesignLocations=None, *args, **kw_args):
        """Initialises a new 'Diagram' instance.

        @param y1InitialView: Y coordinate of the first corner of the initial view 
        @param kind: Kind of this diagram. Values are: "other", "geographic", "internalView", "designSketch", "schematic"
        @param x2InitialView: X coordinate of the second corner of the initial view 
        @param x1InitialView: X coordinate of the first corner of the initial view 
        @param orientation: The Diagram represents the diagram being exchanged. The initialView attributes can be used to specify an initial view with the x,y coordinates of the diagonal points. The coordinate system is a standard Cartesian coordinate system and the orientation attribute defines a positive or negative orientation. Values are: "negative", "positive"
        @param y2InitialView: Y coordinate of the second corner of the initial view 
        @param DiagramObjects: A diagram is made up of multiple DiagramObjects
        @param CoordinateSystem:
        @param GmlDiagramObjects:
        @param DesignLocations:
        """
        #: Y coordinate of the first corner of the initial view
        self.y1InitialView = y1InitialView

        #: Kind of this diagram. Values are: "other", "geographic", "internalView", "designSketch", "schematic"
        self.kind = kind

        #: X coordinate of the second corner of the initial view
        self.x2InitialView = x2InitialView

        #: X coordinate of the first corner of the initial view
        self.x1InitialView = x1InitialView

        #: The Diagram represents the diagram being exchanged. The initialView attributes can be used to specify an initial view with the x,y coordinates of the diagonal points. The coordinate system is a standard Cartesian coordinate system and the orientation attribute defines a positive or negative orientation. Values are: "negative", "positive"
        self.orientation = orientation

        #: Y coordinate of the second corner of the initial view
        self.y2InitialView = y2InitialView

        self._DiagramObjects = []
        self.DiagramObjects = [] if DiagramObjects is None else DiagramObjects

        self._CoordinateSystem = None
        self.CoordinateSystem = CoordinateSystem

        self._GmlDiagramObjects = []
        self.GmlDiagramObjects = [] if GmlDiagramObjects is None else GmlDiagramObjects

        self._DesignLocations = []
        self.DesignLocations = [] if DesignLocations is None else DesignLocations

        super(Diagram, self).__init__(*args, **kw_args)

    _attrs = ["y1InitialView", "kind", "x2InitialView", "x1InitialView", "orientation", "y2InitialView"]
    _attr_types = {"y1InitialView": float, "kind": str, "x2InitialView": float, "x1InitialView": float, "orientation": str, "y2InitialView": float}
    _defaults = {"y1InitialView": 0.0, "kind": "other", "x2InitialView": 0.0, "x1InitialView": 0.0, "orientation": "negative", "y2InitialView": 0.0}
    _enums = {"kind": "DiagramKind", "orientation": "OrientationKind"}
    _refs = ["DiagramObjects", "CoordinateSystem", "GmlDiagramObjects", "DesignLocations"]
    _many_refs = ["DiagramObjects", "GmlDiagramObjects", "DesignLocations"]

    def getDiagramObjects(self):
        """A diagram is made up of multiple DiagramObjects
        """
        return self._DiagramObjects

    def setDiagramObjects(self, value):
        for x in self._DiagramObjects:
            x.Diagram = None
        for y in value:
            y._Diagram = self
        self._DiagramObjects = value

    DiagramObjects = property(getDiagramObjects, setDiagramObjects)

    def addDiagramObjects(self, *DiagramObjects):
        for obj in DiagramObjects:
            obj.Diagram = self

    def removeDiagramObjects(self, *DiagramObjects):
        for obj in DiagramObjects:
            obj.Diagram = None

    def getCoordinateSystem(self):
        
        return self._CoordinateSystem

    def setCoordinateSystem(self, value):
        if self._CoordinateSystem is not None:
            filtered = [x for x in self.CoordinateSystem.Diagrams if x != self]
            self._CoordinateSystem._Diagrams = filtered

        self._CoordinateSystem = value
        if self._CoordinateSystem is not None:
            if self not in self._CoordinateSystem._Diagrams:
                self._CoordinateSystem._Diagrams.append(self)

    CoordinateSystem = property(getCoordinateSystem, setCoordinateSystem)

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

