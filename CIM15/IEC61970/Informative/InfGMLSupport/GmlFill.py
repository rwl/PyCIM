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

class GmlFill(IdentifiedObject):
    """Specifies how the area of the geometry will be filled.Specifies how the area of the geometry will be filled.
    """

    def __init__(self, opacity=0.0, GmlColour=None, GmlMarks=None, GmlTextSymbols=None, GmlSvgParameters=None, GmlPolygonSymbols=None, *args, **kw_args):
        """Initialises a new 'GmlFill' instance.

        @param opacity: Specifies the level of translucency to use when rendering the Fill. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0 
        @param GmlColour:
        @param GmlMarks:
        @param GmlTextSymbols:
        @param GmlSvgParameters:
        @param GmlPolygonSymbols:
        """
        #: Specifies the level of translucency to use when rendering the Fill. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0
        self.opacity = opacity

        self._GmlColour = None
        self.GmlColour = GmlColour

        self._GmlMarks = []
        self.GmlMarks = [] if GmlMarks is None else GmlMarks

        self._GmlTextSymbols = []
        self.GmlTextSymbols = [] if GmlTextSymbols is None else GmlTextSymbols

        self._GmlSvgParameters = []
        self.GmlSvgParameters = [] if GmlSvgParameters is None else GmlSvgParameters

        self._GmlPolygonSymbols = []
        self.GmlPolygonSymbols = [] if GmlPolygonSymbols is None else GmlPolygonSymbols

        super(GmlFill, self).__init__(*args, **kw_args)

    _attrs = ["opacity"]
    _attr_types = {"opacity": float}
    _defaults = {"opacity": 0.0}
    _enums = {}
    _refs = ["GmlColour", "GmlMarks", "GmlTextSymbols", "GmlSvgParameters", "GmlPolygonSymbols"]
    _many_refs = ["GmlMarks", "GmlTextSymbols", "GmlSvgParameters", "GmlPolygonSymbols"]

    def getGmlColour(self):
        
        return self._GmlColour

    def setGmlColour(self, value):
        if self._GmlColour is not None:
            filtered = [x for x in self.GmlColour.GmlFills if x != self]
            self._GmlColour._GmlFills = filtered

        self._GmlColour = value
        if self._GmlColour is not None:
            if self not in self._GmlColour._GmlFills:
                self._GmlColour._GmlFills.append(self)

    GmlColour = property(getGmlColour, setGmlColour)

    def getGmlMarks(self):
        
        return self._GmlMarks

    def setGmlMarks(self, value):
        for p in self._GmlMarks:
            filtered = [q for q in p.GmlFIlls if q != self]
            self._GmlMarks._GmlFIlls = filtered
        for r in value:
            if self not in r._GmlFIlls:
                r._GmlFIlls.append(self)
        self._GmlMarks = value

    GmlMarks = property(getGmlMarks, setGmlMarks)

    def addGmlMarks(self, *GmlMarks):
        for obj in GmlMarks:
            if self not in obj._GmlFIlls:
                obj._GmlFIlls.append(self)
            self._GmlMarks.append(obj)

    def removeGmlMarks(self, *GmlMarks):
        for obj in GmlMarks:
            if self in obj._GmlFIlls:
                obj._GmlFIlls.remove(self)
            self._GmlMarks.remove(obj)

    def getGmlTextSymbols(self):
        
        return self._GmlTextSymbols

    def setGmlTextSymbols(self, value):
        for x in self._GmlTextSymbols:
            x.GmlFill = None
        for y in value:
            y._GmlFill = self
        self._GmlTextSymbols = value

    GmlTextSymbols = property(getGmlTextSymbols, setGmlTextSymbols)

    def addGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj.GmlFill = self

    def removeGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj.GmlFill = None

    def getGmlSvgParameters(self):
        
        return self._GmlSvgParameters

    def setGmlSvgParameters(self, value):
        for p in self._GmlSvgParameters:
            filtered = [q for q in p.GmlFills if q != self]
            self._GmlSvgParameters._GmlFills = filtered
        for r in value:
            if self not in r._GmlFills:
                r._GmlFills.append(self)
        self._GmlSvgParameters = value

    GmlSvgParameters = property(getGmlSvgParameters, setGmlSvgParameters)

    def addGmlSvgParameters(self, *GmlSvgParameters):
        for obj in GmlSvgParameters:
            if self not in obj._GmlFills:
                obj._GmlFills.append(self)
            self._GmlSvgParameters.append(obj)

    def removeGmlSvgParameters(self, *GmlSvgParameters):
        for obj in GmlSvgParameters:
            if self in obj._GmlFills:
                obj._GmlFills.remove(self)
            self._GmlSvgParameters.remove(obj)

    def getGmlPolygonSymbols(self):
        
        return self._GmlPolygonSymbols

    def setGmlPolygonSymbols(self, value):
        for x in self._GmlPolygonSymbols:
            x.GmlFill = None
        for y in value:
            y._GmlFill = self
        self._GmlPolygonSymbols = value

    GmlPolygonSymbols = property(getGmlPolygonSymbols, setGmlPolygonSymbols)

    def addGmlPolygonSymbols(self, *GmlPolygonSymbols):
        for obj in GmlPolygonSymbols:
            obj.GmlFill = self

    def removeGmlPolygonSymbols(self, *GmlPolygonSymbols):
        for obj in GmlPolygonSymbols:
            obj.GmlFill = None

