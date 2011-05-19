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

class GmlLineSymbol(GmlSymbol):
    """Used to style a 'stroke' along a linear geometry type, such as a string of line segments.Used to style a 'stroke' along a linear geometry type, such as a string of line segments.
    """

    def __init__(self, sourceSide='', GmlStroke=None, GmlDiagramObject=None, *args, **kw_args):
        """Initialises a new 'GmlLineSymbol' instance.

        @param sourceSide: For dynamic network update (i.e. colouring) purposes 
        @param GmlStroke:
        @param GmlDiagramObject:
        """
        #: For dynamic network update (i.e. colouring) purposes
        self.sourceSide = sourceSide

        self._GmlStroke = None
        self.GmlStroke = GmlStroke

        self._GmlDiagramObject = None
        self.GmlDiagramObject = GmlDiagramObject

        super(GmlLineSymbol, self).__init__(*args, **kw_args)

    _attrs = ["sourceSide"]
    _attr_types = {"sourceSide": str}
    _defaults = {"sourceSide": ''}
    _enums = {}
    _refs = ["GmlStroke", "GmlDiagramObject"]
    _many_refs = []

    def getGmlStroke(self):
        
        return self._GmlStroke

    def setGmlStroke(self, value):
        if self._GmlStroke is not None:
            filtered = [x for x in self.GmlStroke.GmlLineSymbols if x != self]
            self._GmlStroke._GmlLineSymbols = filtered

        self._GmlStroke = value
        if self._GmlStroke is not None:
            if self not in self._GmlStroke._GmlLineSymbols:
                self._GmlStroke._GmlLineSymbols.append(self)

    GmlStroke = property(getGmlStroke, setGmlStroke)

    def getGmlDiagramObject(self):
        
        return self._GmlDiagramObject

    def setGmlDiagramObject(self, value):
        if self._GmlDiagramObject is not None:
            filtered = [x for x in self.GmlDiagramObject.GmlLineSymbols if x != self]
            self._GmlDiagramObject._GmlLineSymbols = filtered

        self._GmlDiagramObject = value
        if self._GmlDiagramObject is not None:
            if self not in self._GmlDiagramObject._GmlLineSymbols:
                self._GmlDiagramObject._GmlLineSymbols.append(self)

    GmlDiagramObject = property(getGmlDiagramObject, setGmlDiagramObject)

