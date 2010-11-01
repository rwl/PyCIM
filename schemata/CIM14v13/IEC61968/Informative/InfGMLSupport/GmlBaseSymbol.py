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

class GmlBaseSymbol(IdentifiedObject):
    """Allows referencing and extension of external symbols, which may be stored in a symbol repository. The graphical properties from a referenced external symbol override the ones read in from the base symbol.
    """

    def __init__(self, GmlSymbols=None, *args, **kw_args):
        """Initializes a new 'GmlBaseSymbol' instance.

        @param GmlSymbols:
        """
        self._GmlSymbols = []
        self.GmlSymbols = [] if GmlSymbols is None else GmlSymbols

        super(GmlBaseSymbol, self).__init__(*args, **kw_args)

    def getGmlSymbols(self):
        
        return self._GmlSymbols

    def setGmlSymbols(self, value):
        for x in self._GmlSymbols:
            x._GmlBaseSymbol = None
        for y in value:
            y._GmlBaseSymbol = self
        self._GmlSymbols = value

    GmlSymbols = property(getGmlSymbols, setGmlSymbols)

    def addGmlSymbols(self, *GmlSymbols):
        for obj in GmlSymbols:
            obj._GmlBaseSymbol = self
            self._GmlSymbols.append(obj)

    def removeGmlSymbols(self, *GmlSymbols):
        for obj in GmlSymbols:
            obj._GmlBaseSymbol = None
            self._GmlSymbols.remove(obj)

