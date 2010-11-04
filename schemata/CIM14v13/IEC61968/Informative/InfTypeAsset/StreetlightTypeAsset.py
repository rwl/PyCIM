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

from CIM14v13.IEC61968.Informative.InfTypeAsset.ElectricalTypeAsset import ElectricalTypeAsset

class StreetlightTypeAsset(ElectricalTypeAsset):
    """Documentation for a generic streetlight that may be used for various purposes such as work planning. Use 'category' for utility specific categorisation, such as luminar, grid light, lantern, open bottom, flood, etc.
    """

    def __init__(self, lightRating=0.0, StreetlightAssetModels=None, **kw_args):
        """Initializes a new 'StreetlightTypeAsset' instance.

        @param lightRating: Nominal (as designed) power rating of light. 
        @param StreetlightAssetModels:
        """
        #: Nominal (as designed) power rating of light.
        self.lightRating = lightRating

        self._StreetlightAssetModels = []
        self.StreetlightAssetModels = [] if StreetlightAssetModels is None else StreetlightAssetModels

        super(StreetlightTypeAsset, self).__init__(**kw_args)

    def getStreetlightAssetModels(self):
        
        return self._StreetlightAssetModels

    def setStreetlightAssetModels(self, value):
        for p in self._StreetlightAssetModels:
            filtered = [q for q in p.StreetlightTypeAssets if q != self]
            self._StreetlightAssetModels._StreetlightTypeAssets = filtered
        for r in value:
            if self not in r._StreetlightTypeAssets:
                r._StreetlightTypeAssets.append(self)
        self._StreetlightAssetModels = value

    StreetlightAssetModels = property(getStreetlightAssetModels, setStreetlightAssetModels)

    def addStreetlightAssetModels(self, *StreetlightAssetModels):
        for obj in StreetlightAssetModels:
            if self not in obj._StreetlightTypeAssets:
                obj._StreetlightTypeAssets.append(self)
            self._StreetlightAssetModels.append(obj)

    def removeStreetlightAssetModels(self, *StreetlightAssetModels):
        for obj in StreetlightAssetModels:
            if self in obj._StreetlightTypeAssets:
                obj._StreetlightTypeAssets.remove(self)
            self._StreetlightAssetModels.remove(obj)

