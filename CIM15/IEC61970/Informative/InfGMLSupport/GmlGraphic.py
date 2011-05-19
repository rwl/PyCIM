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

class GmlGraphic(IdentifiedObject):
    """A 'graphic symbol' with an inherent shape, color(s), and possibly size. A 'graphic' can be very informally defined as 'a little picture' and can be of either a raster or vector-graphic source type.A 'graphic symbol' with an inherent shape, color(s), and possibly size. A 'graphic' can be very informally defined as 'a little picture' and can be of either a raster or vector-graphic source type.
    """

    def __init__(self, rotation=0.0, size=0, symbolID='', minSize=0, opacity=0.0, xScale=0.0, yScale=0.0, GmlMarks=None, GmlPointSymbols=None, *args, **kw_args):
        """Initialises a new 'GmlGraphic' instance.

        @param rotation: Gives the rotation of a graphic in the clockwise direction about its center point in decimal degrees, encoded as a floating-point number. Negative values mean counter-clockwise rotation. The default value is 0.0 (no rotation). Note that there is no connection between source geometry types and rotations; the point used for plotting has no inherent direction. Also, the point within the graphic about which it is rotated is format dependent. If a format does not include an inherent rotation point, then the point of rotation should be the centroid. 
        @param size: Gives the absolute size of the graphic in pixels encoded as a floatingpoint number. The default size for an object is context-dependent. Negative values are not allowed. 
        @param symbolID: The identifier of the symbol, if not derived from the type of CIM object (PSR, Asset, Organisation, Document, etc.) gmlSymbolPlacement is associated with. 
        @param minSize: The minimum symbol size allowed. 
        @param opacity: Specifies the level of translucency to use when rendering the Graphic.The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0 
        @param xScale: Horizontal scaling factor of normal symbol - particularly applicable to busbars if not described through a sequence of gmlPositions (e.g., Busbar). 
        @param yScale: Vertical scaling factor of normal symbol - particularly applicable to busbars if not described through a sequence of gmlPositions (e.g., Busbars). 
        @param GmlMarks:
        @param GmlPointSymbols:
        """
        #: Gives the rotation of a graphic in the clockwise direction about its center point in decimal degrees, encoded as a floating-point number. Negative values mean counter-clockwise rotation. The default value is 0.0 (no rotation). Note that there is no connection between source geometry types and rotations; the point used for plotting has no inherent direction. Also, the point within the graphic about which it is rotated is format dependent. If a format does not include an inherent rotation point, then the point of rotation should be the centroid.
        self.rotation = rotation

        #: Gives the absolute size of the graphic in pixels encoded as a floatingpoint number. The default size for an object is context-dependent. Negative values are not allowed.
        self.size = size

        #: The identifier of the symbol, if not derived from the type of CIM object (PSR, Asset, Organisation, Document, etc.) gmlSymbolPlacement is associated with.
        self.symbolID = symbolID

        #: The minimum symbol size allowed.
        self.minSize = minSize

        #: Specifies the level of translucency to use when rendering the Graphic.The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0
        self.opacity = opacity

        #: Horizontal scaling factor of normal symbol - particularly applicable to busbars if not described through a sequence of gmlPositions (e.g., Busbar).
        self.xScale = xScale

        #: Vertical scaling factor of normal symbol - particularly applicable to busbars if not described through a sequence of gmlPositions (e.g., Busbars).
        self.yScale = yScale

        self._GmlMarks = []
        self.GmlMarks = [] if GmlMarks is None else GmlMarks

        self._GmlPointSymbols = []
        self.GmlPointSymbols = [] if GmlPointSymbols is None else GmlPointSymbols

        super(GmlGraphic, self).__init__(*args, **kw_args)

    _attrs = ["rotation", "size", "symbolID", "minSize", "opacity", "xScale", "yScale"]
    _attr_types = {"rotation": float, "size": int, "symbolID": str, "minSize": int, "opacity": float, "xScale": float, "yScale": float}
    _defaults = {"rotation": 0.0, "size": 0, "symbolID": '', "minSize": 0, "opacity": 0.0, "xScale": 0.0, "yScale": 0.0}
    _enums = {}
    _refs = ["GmlMarks", "GmlPointSymbols"]
    _many_refs = ["GmlMarks", "GmlPointSymbols"]

    def getGmlMarks(self):
        
        return self._GmlMarks

    def setGmlMarks(self, value):
        for p in self._GmlMarks:
            filtered = [q for q in p.GmlGraphics if q != self]
            self._GmlMarks._GmlGraphics = filtered
        for r in value:
            if self not in r._GmlGraphics:
                r._GmlGraphics.append(self)
        self._GmlMarks = value

    GmlMarks = property(getGmlMarks, setGmlMarks)

    def addGmlMarks(self, *GmlMarks):
        for obj in GmlMarks:
            if self not in obj._GmlGraphics:
                obj._GmlGraphics.append(self)
            self._GmlMarks.append(obj)

    def removeGmlMarks(self, *GmlMarks):
        for obj in GmlMarks:
            if self in obj._GmlGraphics:
                obj._GmlGraphics.remove(self)
            self._GmlMarks.remove(obj)

    def getGmlPointSymbols(self):
        
        return self._GmlPointSymbols

    def setGmlPointSymbols(self, value):
        for x in self._GmlPointSymbols:
            x.GmlGraphic = None
        for y in value:
            y._GmlGraphic = self
        self._GmlPointSymbols = value

    GmlPointSymbols = property(getGmlPointSymbols, setGmlPointSymbols)

    def addGmlPointSymbols(self, *GmlPointSymbols):
        for obj in GmlPointSymbols:
            obj.GmlGraphic = self

    def removeGmlPointSymbols(self, *GmlPointSymbols):
        for obj in GmlPointSymbols:
            obj.GmlGraphic = None

