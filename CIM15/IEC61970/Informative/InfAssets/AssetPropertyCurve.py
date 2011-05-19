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

from CIM15.IEC61970.Core.Curve import Curve

class AssetPropertyCurve(Curve):
    """An Asset Property that is described through curves rather than as a data point. The relationship is to be defined between an independent variable (X-axis) and one or two dependent variables (Y1-axis and Y2-axis).An Asset Property that is described through curves rather than as a data point. The relationship is to be defined between an independent variable (X-axis) and one or two dependent variables (Y1-axis and Y2-axis).
    """

    def __init__(self, Specification=None, Assets=None, *args, **kw_args):
        """Initialises a new 'AssetPropertyCurve' instance.

        @param Specification:
        @param Assets:
        """
        self._Specification = None
        self.Specification = Specification

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        super(AssetPropertyCurve, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Specification", "Assets"]
    _many_refs = ["Assets"]

    def getSpecification(self):
        
        return self._Specification

    def setSpecification(self, value):
        if self._Specification is not None:
            filtered = [x for x in self.Specification.AssetPropertyCurves if x != self]
            self._Specification._AssetPropertyCurves = filtered

        self._Specification = value
        if self._Specification is not None:
            if self not in self._Specification._AssetPropertyCurves:
                self._Specification._AssetPropertyCurves.append(self)

    Specification = property(getSpecification, setSpecification)

    def getAssets(self):
        
        return self._Assets

    def setAssets(self, value):
        for p in self._Assets:
            filtered = [q for q in p.AssetPropertyCurves if q != self]
            self._Assets._AssetPropertyCurves = filtered
        for r in value:
            if self not in r._AssetPropertyCurves:
                r._AssetPropertyCurves.append(self)
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            if self not in obj._AssetPropertyCurves:
                obj._AssetPropertyCurves.append(self)
            self._Assets.append(obj)

    def removeAssets(self, *Assets):
        for obj in Assets:
            if self in obj._AssetPropertyCurves:
                obj._AssetPropertyCurves.remove(self)
            self._Assets.remove(obj)

