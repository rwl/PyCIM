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

class VisibilityLayer(IdentifiedObject):
    """Layers are typically used for grouping diagram objects according to themes and scales. Themes are used to display or hide certain information (e.g., lakes, borders), while scales are used for hiding or displaying information depending on the current zoom level (hide text when it is too small to be read, or when it exceeds the screen size). This is also called de-cluttering.  CIM based graphics exchange will support an m:n relationship between diagram objects and layers. It will be the task of the importing system to convert an m:n case into an appropriate 1:n representation if the importing system does not support m:n.Layers are typically used for grouping diagram objects according to themes and scales. Themes are used to display or hide certain information (e.g., lakes, borders), while scales are used for hiding or displaying information depending on the current zoom level (hide text when it is too small to be read, or when it exceeds the screen size). This is also called de-cluttering.  CIM based graphics exchange will support an m:n relationship between diagram objects and layers. It will be the task of the importing system to convert an m:n case into an appropriate 1:n representation if the importing system does not support m:n.
    """

    def __init__(self, drawingOrder=0, DiagramObjects=None, *args, **kw_args):
        """Initialises a new 'VisibilityLayer' instance.

        @param drawingOrder: The drawing order for this layer.  As with the drawingOrder for diagram objects, the higher the number, the later the layer and the objects within it are rendered. 
        @param DiagramObjects: A visibility layer can contain one or more diagram objects
        """
        #: The drawing order for this layer.  As with the drawingOrder for diagram objects, the higher the number, the later the layer and the objects within it are rendered.
        self.drawingOrder = drawingOrder

        self._DiagramObjects = []
        self.DiagramObjects = [] if DiagramObjects is None else DiagramObjects

        super(VisibilityLayer, self).__init__(*args, **kw_args)

    _attrs = ["drawingOrder"]
    _attr_types = {"drawingOrder": int}
    _defaults = {"drawingOrder": 0}
    _enums = {}
    _refs = ["DiagramObjects"]
    _many_refs = ["DiagramObjects"]

    def getDiagramObjects(self):
        """A visibility layer can contain one or more diagram objects
        """
        return self._DiagramObjects

    def setDiagramObjects(self, value):
        for p in self._DiagramObjects:
            filtered = [q for q in p.VisibilityLayers if q != self]
            self._DiagramObjects._VisibilityLayers = filtered
        for r in value:
            if self not in r._VisibilityLayers:
                r._VisibilityLayers.append(self)
        self._DiagramObjects = value

    DiagramObjects = property(getDiagramObjects, setDiagramObjects)

    def addDiagramObjects(self, *DiagramObjects):
        for obj in DiagramObjects:
            if self not in obj._VisibilityLayers:
                obj._VisibilityLayers.append(self)
            self._DiagramObjects.append(obj)

    def removeDiagramObjects(self, *DiagramObjects):
        for obj in DiagramObjects:
            if self in obj._VisibilityLayers:
                obj._VisibilityLayers.remove(self)
            self._DiagramObjects.remove(obj)

