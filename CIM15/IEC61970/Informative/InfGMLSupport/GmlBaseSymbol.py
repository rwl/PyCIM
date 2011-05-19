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

class GmlBaseSymbol(IdentifiedObject):
    """Allows referencing and extension of external symbols, which may be stored in a symbol repository. The graphical properties from a referenced external symbol override the ones read in from the base symbol.Allows referencing and extension of external symbols, which may be stored in a symbol repository. The graphical properties from a referenced external symbol override the ones read in from the base symbol.
    """

    def __init__(self, GmlSymbols=None, *args, **kw_args):
        """Initialises a new 'GmlBaseSymbol' instance.

        @param GmlSymbols:
        """
        self._GmlSymbols = []
        self.GmlSymbols = [] if GmlSymbols is None else GmlSymbols

        super(GmlBaseSymbol, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["GmlSymbols"]
    _many_refs = ["GmlSymbols"]

    def getGmlSymbols(self):
        
        return self._GmlSymbols

    def setGmlSymbols(self, value):
        for x in self._GmlSymbols:
            x.GmlBaseSymbol = None
        for y in value:
            y._GmlBaseSymbol = self
        self._GmlSymbols = value

    GmlSymbols = property(getGmlSymbols, setGmlSymbols)

    def addGmlSymbols(self, *GmlSymbols):
        for obj in GmlSymbols:
            obj.GmlBaseSymbol = self

    def removeGmlSymbols(self, *GmlSymbols):
        for obj in GmlSymbols:
            obj.GmlBaseSymbol = None

