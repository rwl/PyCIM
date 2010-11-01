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

class GmlGraphic(IdentifiedObject):
    """A 'graphic symbol' with an inherent shape, color(s), and possibly size. A 'graphic' can be very informally defined as 'a little picture' and can be of either a raster or vector-graphic source type.
    """

    def __init__(self, xScale=0.0, size=0, yScale=0.0, opacity=0.0, symbolID='', rotation=0.0, minSize=0, GmlMarks=None, GmlPointSymbols=None, *args, **kw_args):
        """Initializes a new 'GmlGraphic' instance.

        @param xScale: Horizontal scaling factor of normal symbol - particularly applicable to busbars if not described through a sequence of gmlPositions (e.g., Busbar). 
        @param size: Gives the absolute size of the graphic in pixels encoded as a floatingpoint number. The default size for an object is context-dependent. Negative values are not allowed. 
        @param yScale: Vertical scaling factor of normal symbol - particularly applicable to busbars if not described through a sequence of gmlPositions (e.g., Busbars). 
        @param opacity: Specifies the level of translucency to use when rendering the Graphic.The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0 
        @param symbolID: The identifier of the symbol, if not derived from the type of CIM object (PSR, Asset, Organisation, Document, etc.) gmlSymbolPlacement is associated with. 
        @param rotation: Gives the rotation of a graphic in the clockwise direction about its center point in decimal degrees, encoded as a floating-point number. Negative values mean counter-clockwise rotation. The default value is 0.0 (no rotation). Note that there is no connection between source geometry types and rotations; the point used for plotting has no inherent direction. Also, the point within the graphic about which it is rotated is format dependent. If a format does not include an inherent rotation point, then the point of rotation should be the centroid. 
        @param minSize: The minimum symbol size allowed. 
        @param GmlMarks:
        @param GmlPointSymbols:
        """
        #: Horizontal scaling factor of normal symbol - particularly applicable to busbars if not described through a sequence of gmlPositions (e.g., Busbar). 
        self.xScale = xScale

        #: Gives the absolute size of the graphic in pixels encoded as a floatingpoint number. The default size for an object is context-dependent. Negative values are not allowed. 
        self.size = size

        #: Vertical scaling factor of normal symbol - particularly applicable to busbars if not described through a sequence of gmlPositions (e.g., Busbars). 
        self.yScale = yScale

        #: Specifies the level of translucency to use when rendering the Graphic.The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0 
        self.opacity = opacity

        #: The identifier of the symbol, if not derived from the type of CIM object (PSR, Asset, Organisation, Document, etc.) gmlSymbolPlacement is associated with. 
        self.symbolID = symbolID

        #: Gives the rotation of a graphic in the clockwise direction about its center point in decimal degrees, encoded as a floating-point number. Negative values mean counter-clockwise rotation. The default value is 0.0 (no rotation). Note that there is no connection between source geometry types and rotations; the point used for plotting has no inherent direction. Also, the point within the graphic about which it is rotated is format dependent. If a format does not include an inherent rotation point, then the point of rotation should be the centroid. 
        self.rotation = rotation

        #: The minimum symbol size allowed. 
        self.minSize = minSize

        self._GmlMarks = []
        self.GmlMarks = [] if GmlMarks is None else GmlMarks

        self._GmlPointSymbols = []
        self.GmlPointSymbols = [] if GmlPointSymbols is None else GmlPointSymbols

        super(GmlGraphic, self).__init__(*args, **kw_args)

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
            x._GmlGraphic = None
        for y in value:
            y._GmlGraphic = self
        self._GmlPointSymbols = value

    GmlPointSymbols = property(getGmlPointSymbols, setGmlPointSymbols)

    def addGmlPointSymbols(self, *GmlPointSymbols):
        for obj in GmlPointSymbols:
            obj._GmlGraphic = self
            self._GmlPointSymbols.append(obj)

    def removeGmlPointSymbols(self, *GmlPointSymbols):
        for obj in GmlPointSymbols:
            obj._GmlGraphic = None
            self._GmlPointSymbols.remove(obj)

