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

class DiagramObject(IdentifiedObject):
    """This class defines an object that defines one or more points in a given space. This object can be associated with anything that subclasses Identified Object in IEC 61970-301This class defines an object that defines one or more points in a given space. This object can be associated with anything that subclasses Identified Object in IEC 61970-301
    """

    def __init__(self, offsetY=0.0, offsetX=0.0, isPolygon=False, rotation=0.0, drawingOrder=0, VisibilityLayers=None, IdentifiedObject=None, DiagramObjectStyle=None, DiagramObjectPoints=None, Diagram=None, *args, **kw_args):
        """Initialises a new 'DiagramObject' instance.

        @param offsetY: The offset in the Y direction. This is used for defining the offset from centre for rendering an icon (the default is that a single point specifies the centre of the icon).  The offset is in per-unit with 0 indicating there is no offset from the vertical centre of the icon.  The offset direction is dependent on the orientation of the diagram, with -0.5 and 0.5 indicating an offset of +/- 50% on the vertical axis. 
        @param offsetX: The offset in the X direction. This is used for defining the offset from centre for rendering an icon (the default is that a single point specifies the centre of the icon).  The offset is in per-unit with 0 indicating there is no offset from the horizontal centre of the icon.  -0.5 indicates it is offset by 50% to the left and 0.5 indicates an offset of 50% to the right. 
        @param isPolygon: Defines whether or not the diagram objects points define the boundaries of a polygon or the routing of a polyline. If this value is true then a receiving application should consider the first and last points to be connected. 
        @param rotation: Sets the angle of rotation (in Degrees) of the diagram object in a clockwise direction from the normal 
        @param drawingOrder: The drawing order of this element. The higher the number, the later the element is drawn in sequence. This is used to ensure that elements that overlap are rendered in the correct order. 
        @param VisibilityLayers: A diagram object can be part of multiple visibility layers
        @param IdentifiedObject: The domain object that this diagram object is associated with
        @param DiagramObjectStyle: A diagram object has a style associated that provides a reference for the style used in the originating system
        @param DiagramObjectPoints: A diagram object can have 0 or more points to reflect its layout position, routing (for polylines) or boundary (for polygons)
        @param Diagram: A diagram object is part of a Diagram
        """
        #: The offset in the Y direction. This is used for defining the offset from centre for rendering an icon (the default is that a single point specifies the centre of the icon).  The offset is in per-unit with 0 indicating there is no offset from the vertical centre of the icon.  The offset direction is dependent on the orientation of the diagram, with -0.5 and 0.5 indicating an offset of +/- 50% on the vertical axis.
        self.offsetY = offsetY

        #: The offset in the X direction. This is used for defining the offset from centre for rendering an icon (the default is that a single point specifies the centre of the icon).  The offset is in per-unit with 0 indicating there is no offset from the horizontal centre of the icon.  -0.5 indicates it is offset by 50% to the left and 0.5 indicates an offset of 50% to the right.
        self.offsetX = offsetX

        #: Defines whether or not the diagram objects points define the boundaries of a polygon or the routing of a polyline. If this value is true then a receiving application should consider the first and last points to be connected.
        self.isPolygon = isPolygon

        #: Sets the angle of rotation (in Degrees) of the diagram object in a clockwise direction from the normal
        self.rotation = rotation

        #: The drawing order of this element. The higher the number, the later the element is drawn in sequence. This is used to ensure that elements that overlap are rendered in the correct order.
        self.drawingOrder = drawingOrder

        self._VisibilityLayers = []
        self.VisibilityLayers = [] if VisibilityLayers is None else VisibilityLayers

        self._IdentifiedObject = None
        self.IdentifiedObject = IdentifiedObject

        self._DiagramObjectStyle = None
        self.DiagramObjectStyle = DiagramObjectStyle

        self._DiagramObjectPoints = []
        self.DiagramObjectPoints = [] if DiagramObjectPoints is None else DiagramObjectPoints

        self._Diagram = None
        self.Diagram = Diagram

        super(DiagramObject, self).__init__(*args, **kw_args)

    _attrs = ["offsetY", "offsetX", "isPolygon", "rotation", "drawingOrder"]
    _attr_types = {"offsetY": float, "offsetX": float, "isPolygon": bool, "rotation": float, "drawingOrder": int}
    _defaults = {"offsetY": 0.0, "offsetX": 0.0, "isPolygon": False, "rotation": 0.0, "drawingOrder": 0}
    _enums = {}
    _refs = ["VisibilityLayers", "IdentifiedObject", "DiagramObjectStyle", "DiagramObjectPoints", "Diagram"]
    _many_refs = ["VisibilityLayers", "DiagramObjectPoints"]

    def getVisibilityLayers(self):
        """A diagram object can be part of multiple visibility layers
        """
        return self._VisibilityLayers

    def setVisibilityLayers(self, value):
        for p in self._VisibilityLayers:
            filtered = [q for q in p.DiagramObjects if q != self]
            self._VisibilityLayers._DiagramObjects = filtered
        for r in value:
            if self not in r._DiagramObjects:
                r._DiagramObjects.append(self)
        self._VisibilityLayers = value

    VisibilityLayers = property(getVisibilityLayers, setVisibilityLayers)

    def addVisibilityLayers(self, *VisibilityLayers):
        for obj in VisibilityLayers:
            if self not in obj._DiagramObjects:
                obj._DiagramObjects.append(self)
            self._VisibilityLayers.append(obj)

    def removeVisibilityLayers(self, *VisibilityLayers):
        for obj in VisibilityLayers:
            if self in obj._DiagramObjects:
                obj._DiagramObjects.remove(self)
            self._VisibilityLayers.remove(obj)

    def getIdentifiedObject(self):
        """The domain object that this diagram object is associated with
        """
        return self._IdentifiedObject

    def setIdentifiedObject(self, value):
        if self._IdentifiedObject is not None:
            filtered = [x for x in self.IdentifiedObject.DiagramObjects if x != self]
            self._IdentifiedObject._DiagramObjects = filtered

        self._IdentifiedObject = value
        if self._IdentifiedObject is not None:
            if self not in self._IdentifiedObject._DiagramObjects:
                self._IdentifiedObject._DiagramObjects.append(self)

    IdentifiedObject = property(getIdentifiedObject, setIdentifiedObject)

    def getDiagramObjectStyle(self):
        """A diagram object has a style associated that provides a reference for the style used in the originating system
        """
        return self._DiagramObjectStyle

    def setDiagramObjectStyle(self, value):
        if self._DiagramObjectStyle is not None:
            filtered = [x for x in self.DiagramObjectStyle.DiagramObjects if x != self]
            self._DiagramObjectStyle._DiagramObjects = filtered

        self._DiagramObjectStyle = value
        if self._DiagramObjectStyle is not None:
            if self not in self._DiagramObjectStyle._DiagramObjects:
                self._DiagramObjectStyle._DiagramObjects.append(self)

    DiagramObjectStyle = property(getDiagramObjectStyle, setDiagramObjectStyle)

    def getDiagramObjectPoints(self):
        """A diagram object can have 0 or more points to reflect its layout position, routing (for polylines) or boundary (for polygons)
        """
        return self._DiagramObjectPoints

    def setDiagramObjectPoints(self, value):
        for x in self._DiagramObjectPoints:
            x.DiagramObject = None
        for y in value:
            y._DiagramObject = self
        self._DiagramObjectPoints = value

    DiagramObjectPoints = property(getDiagramObjectPoints, setDiagramObjectPoints)

    def addDiagramObjectPoints(self, *DiagramObjectPoints):
        for obj in DiagramObjectPoints:
            obj.DiagramObject = self

    def removeDiagramObjectPoints(self, *DiagramObjectPoints):
        for obj in DiagramObjectPoints:
            obj.DiagramObject = None

    def getDiagram(self):
        """A diagram object is part of a Diagram
        """
        return self._Diagram

    def setDiagram(self, value):
        if self._Diagram is not None:
            filtered = [x for x in self.Diagram.DiagramObjects if x != self]
            self._Diagram._DiagramObjects = filtered

        self._Diagram = value
        if self._Diagram is not None:
            if self not in self._Diagram._DiagramObjects:
                self._Diagram._DiagramObjects.append(self)

    Diagram = property(getDiagram, setDiagram)

