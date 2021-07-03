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

from CIM16.IEC61970.Core.IdentifiedObject import IdentifiedObject

class GmlFeatureType(IdentifiedObject):
    """Type classification of feature.Type classification of feature.
    """

    def __init__(self, GmlFeatureStyles=None, *args, **kw_args):
        """Initialises a new 'GmlFeatureType' instance.

        @param GmlFeatureStyles:
        """
        self._GmlFeatureStyles = []
        self.GmlFeatureStyles = [] if GmlFeatureStyles is None else GmlFeatureStyles

        super(GmlFeatureType, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["GmlFeatureStyles"]
    _many_refs = ["GmlFeatureStyles"]

    def getGmlFeatureStyles(self):
        
        return self._GmlFeatureStyles

    def setGmlFeatureStyles(self, value):
        for p in self._GmlFeatureStyles:
            filtered = [q for q in p.GmlFeatureTypes if q != self]
            self._GmlFeatureStyles._GmlFeatureTypes = filtered
        for r in value:
            if self not in r._GmlFeatureTypes:
                r._GmlFeatureTypes.append(self)
        self._GmlFeatureStyles = value

    GmlFeatureStyles = property(getGmlFeatureStyles, setGmlFeatureStyles)

    def addGmlFeatureStyles(self, *GmlFeatureStyles):
        for obj in GmlFeatureStyles:
            if self not in obj._GmlFeatureTypes:
                obj._GmlFeatureTypes.append(self)
            self._GmlFeatureStyles.append(obj)

    def removeGmlFeatureStyles(self, *GmlFeatureStyles):
        for obj in GmlFeatureStyles:
            if self in obj._GmlFeatureTypes:
                obj._GmlFeatureTypes.remove(self)
            self._GmlFeatureStyles.remove(obj)

