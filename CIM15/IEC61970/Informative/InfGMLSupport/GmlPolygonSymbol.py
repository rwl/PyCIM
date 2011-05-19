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

from CIM15.IEC61970.Informative.InfGMLSupport.GmlSymbol import GmlSymbol

class GmlPolygonSymbol(GmlSymbol):
    """Used to draw a polygon (or other area-type geometries), including filling its interior and stroking its border (outline).Used to draw a polygon (or other area-type geometries), including filling its interior and stroking its border (outline).
    """

    def __init__(self, GmlDiagramObject=None, GmlFill=None, GmlStroke=None, *args, **kw_args):
        """Initialises a new 'GmlPolygonSymbol' instance.

        @param GmlDiagramObject:
        @param GmlFill:
        @param GmlStroke:
        """
        self._GmlDiagramObject = None
        self.GmlDiagramObject = GmlDiagramObject

        self._GmlFill = None
        self.GmlFill = GmlFill

        self._GmlStroke = None
        self.GmlStroke = GmlStroke

        super(GmlPolygonSymbol, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["GmlDiagramObject", "GmlFill", "GmlStroke"]
    _many_refs = []

    def getGmlDiagramObject(self):
        
        return self._GmlDiagramObject

    def setGmlDiagramObject(self, value):
        if self._GmlDiagramObject is not None:
            filtered = [x for x in self.GmlDiagramObject.GmlPolygonSymbols if x != self]
            self._GmlDiagramObject._GmlPolygonSymbols = filtered

        self._GmlDiagramObject = value
        if self._GmlDiagramObject is not None:
            if self not in self._GmlDiagramObject._GmlPolygonSymbols:
                self._GmlDiagramObject._GmlPolygonSymbols.append(self)

    GmlDiagramObject = property(getGmlDiagramObject, setGmlDiagramObject)

    def getGmlFill(self):
        
        return self._GmlFill

    def setGmlFill(self, value):
        if self._GmlFill is not None:
            filtered = [x for x in self.GmlFill.GmlPolygonSymbols if x != self]
            self._GmlFill._GmlPolygonSymbols = filtered

        self._GmlFill = value
        if self._GmlFill is not None:
            if self not in self._GmlFill._GmlPolygonSymbols:
                self._GmlFill._GmlPolygonSymbols.append(self)

    GmlFill = property(getGmlFill, setGmlFill)

    def getGmlStroke(self):
        
        return self._GmlStroke

    def setGmlStroke(self, value):
        if self._GmlStroke is not None:
            filtered = [x for x in self.GmlStroke.GmlPolygonSymbols if x != self]
            self._GmlStroke._GmlPolygonSymbols = filtered

        self._GmlStroke = value
        if self._GmlStroke is not None:
            if self not in self._GmlStroke._GmlPolygonSymbols:
                self._GmlStroke._GmlPolygonSymbols.append(self)

    GmlStroke = property(getGmlStroke, setGmlStroke)

