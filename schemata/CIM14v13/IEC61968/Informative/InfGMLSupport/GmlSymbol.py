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

class GmlSymbol(IdentifiedObject):
    """Describes how a feature is to appear on a map or display. The symbol describes not just the shape that should appear but also such graphical properties as color and opacity.
    """

    def __init__(self, level='', type='', version='', GmlFeatureStyles=None, GmlBaseSymbol=None, *args, **kw_args):
        """Initializes a new 'GmlSymbol' instance.

        @param level: The level (of the map) where the symbol exists or the zoom levels at which this diagram object is displayed. As a way of de-cluttering displays, for example, some symbols and annotations are only shown when zoomed in. 
        @param type: The Symbol type. 
        @param version: The version of the Symbol. 
        @param GmlFeatureStyles:
        @param GmlBaseSymbol:
        """
        #: The level (of the map) where the symbol exists or the zoom levels at which this diagram object is displayed. As a way of de-cluttering displays, for example, some symbols and annotations are only shown when zoomed in.
        self.level = level

        #: The Symbol type.
        self.type = type

        #: The version of the Symbol.
        self.version = version

        self._GmlFeatureStyles = []
        self.GmlFeatureStyles = [] if GmlFeatureStyles is None else GmlFeatureStyles

        self._GmlBaseSymbol = None
        self.GmlBaseSymbol = GmlBaseSymbol

        super(GmlSymbol, self).__init__(*args, **kw_args)

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
            self._GmlBaseSymbol._GmlSymbols.append(self)

    GmlBaseSymbol = property(getGmlBaseSymbol, setGmlBaseSymbol)

