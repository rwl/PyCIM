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

class GmlPointSymbol(GmlSymbol):
    """Used to draw a 'graphic' at a point.Used to draw a 'graphic' at a point.
    """

    def __init__(self, GmlGraphic=None, GmlDiagramObject=None, *args, **kw_args):
        """Initialises a new 'GmlPointSymbol' instance.

        @param GmlGraphic:
        @param GmlDiagramObject:
        """
        self._GmlGraphic = None
        self.GmlGraphic = GmlGraphic

        self._GmlDiagramObject = None
        self.GmlDiagramObject = GmlDiagramObject

        super(GmlPointSymbol, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["GmlGraphic", "GmlDiagramObject"]
    _many_refs = []

    def getGmlGraphic(self):
        
        return self._GmlGraphic

    def setGmlGraphic(self, value):
        if self._GmlGraphic is not None:
            filtered = [x for x in self.GmlGraphic.GmlPointSymbols if x != self]
            self._GmlGraphic._GmlPointSymbols = filtered

        self._GmlGraphic = value
        if self._GmlGraphic is not None:
            if self not in self._GmlGraphic._GmlPointSymbols:
                self._GmlGraphic._GmlPointSymbols.append(self)

    GmlGraphic = property(getGmlGraphic, setGmlGraphic)

    def getGmlDiagramObject(self):
        
        return self._GmlDiagramObject

    def setGmlDiagramObject(self, value):
        if self._GmlDiagramObject is not None:
            filtered = [x for x in self.GmlDiagramObject.GmlPointSymbols if x != self]
            self._GmlDiagramObject._GmlPointSymbols = filtered

        self._GmlDiagramObject = value
        if self._GmlDiagramObject is not None:
            if self not in self._GmlDiagramObject._GmlPointSymbols:
                self._GmlDiagramObject._GmlPointSymbols.append(self)

    GmlDiagramObject = property(getGmlDiagramObject, setGmlDiagramObject)

