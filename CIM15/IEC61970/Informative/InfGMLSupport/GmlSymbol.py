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

class GmlSymbol(IdentifiedObject):
    """Describes how a feature is to appear on a map or display. The symbol describes not just the shape that should appear but also such graphical properties as color and opacity.Describes how a feature is to appear on a map or display. The symbol describes not just the shape that should appear but also such graphical properties as color and opacity.
    """

    def __init__(self, version='', level='', type='', GmlFeatureStyles=None, GmlBaseSymbol=None, *args, **kw_args):
        """Initialises a new 'GmlSymbol' instance.

        @param version: The version of the Symbol. 
        @param level: The level (of the map) where the symbol exists or the zoom levels at which this diagram object is displayed. As a way of de-cluttering displays, for example, some symbols and annotations are only shown when zoomed in. 
        @param type: The Symbol type. 
        @param GmlFeatureStyles:
        @param GmlBaseSymbol:
        """
        #: The version of the Symbol.
        self.version = version

        #: The level (of the map) where the symbol exists or the zoom levels at which this diagram object is displayed. As a way of de-cluttering displays, for example, some symbols and annotations are only shown when zoomed in.
        self.level = level

        #: The Symbol type.
        self.type = type

        self._GmlFeatureStyles = []
        self.GmlFeatureStyles = [] if GmlFeatureStyles is None else GmlFeatureStyles

        self._GmlBaseSymbol = None
        self.GmlBaseSymbol = GmlBaseSymbol

        super(GmlSymbol, self).__init__(*args, **kw_args)

    _attrs = ["version", "level", "type"]
    _attr_types = {"version": str, "level": str, "type": str}
    _defaults = {"version": '', "level": '', "type": ''}
    _enums = {}
    _refs = ["GmlFeatureStyles", "GmlBaseSymbol"]
    _many_refs = ["GmlFeatureStyles"]

    def getGmlFeatureStyles(self):
        
        return self._GmlFeatureStyles

    def setGmlFeatureStyles(self, value):
        for p in self._GmlFeatureStyles:
            filtered = [q for q in p.GmlSymbols if q != self]
            self._GmlFeatureStyles._GmlSymbols = filtered
        for r in value:
            if self not in r._GmlSymbols:
                r._GmlSymbols.append(self)
        self._GmlFeatureStyles = value

    GmlFeatureStyles = property(getGmlFeatureStyles, setGmlFeatureStyles)

    def addGmlFeatureStyles(self, *GmlFeatureStyles):
        for obj in GmlFeatureStyles:
            if self not in obj._GmlSymbols:
                obj._GmlSymbols.append(self)
            self._GmlFeatureStyles.append(obj)

    def removeGmlFeatureStyles(self, *GmlFeatureStyles):
        for obj in GmlFeatureStyles:
            if self in obj._GmlSymbols:
                obj._GmlSymbols.remove(self)
            self._GmlFeatureStyles.remove(obj)

    def getGmlBaseSymbol(self):
        
        return self._GmlBaseSymbol

    def setGmlBaseSymbol(self, value):
        if self._GmlBaseSymbol is not None:
            filtered = [x for x in self.GmlBaseSymbol.GmlSymbols if x != self]
            self._GmlBaseSymbol._GmlSymbols = filtered

        self._GmlBaseSymbol = value
        if self._GmlBaseSymbol is not None:
            if self not in self._GmlBaseSymbol._GmlSymbols:
                self._GmlBaseSymbol._GmlSymbols.append(self)

    GmlBaseSymbol = property(getGmlBaseSymbol, setGmlBaseSymbol)

