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

from CIM14v13.IEC61970.Core.Curve import Curve

class AssetPropertyCurve(Curve):
    """An Asset Property that is described through curves rather than as a data point. The relationship is to be defined between an independent variable (X-axis) and one or two dependent variables (Y1-axis and Y2-axis).
    """

    def __init__(self, Specification=None, Assets=None, **kw_args):
        """Initializes a new 'AssetPropertyCurve' instance.

        @param Specification:
        @param Assets:
        """
        self._Specification = None
        self.Specification = Specification

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        super(AssetPropertyCurve, self).__init__(**kw_args)

    def getSpecification(self):
        
        return self._Specification

    def setSpecification(self, value):
        if self._Specification is not None:
            filtered = [x for x in self.Specification.AssetPropertyCurves if x != self]
            self._Specification._AssetPropertyCurves = filtered

        self._Specification = value
        if self._Specification is not None:
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

