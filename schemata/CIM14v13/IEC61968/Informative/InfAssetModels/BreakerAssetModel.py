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

from CIM14v13.IEC61968.Informative.InfAssetModels.ElectricalAssetModel import ElectricalAssetModel

class BreakerAssetModel(ElectricalAssetModel):
    """Documentation for a type of a breaker asset of a particular product model made by a manufacturer.
    """

    def __init__(self, BreakerInfo=None, BreakerAssets=None, BreakerTypeAsset=None, **kw_args):
        """Initializes a new 'BreakerAssetModel' instance.

        @param BreakerInfo:
        @param BreakerAssets:
        @param BreakerTypeAsset:
        """
        self._BreakerInfo = None
        self.BreakerInfo = BreakerInfo

        self._BreakerAssets = []
        self.BreakerAssets = [] if BreakerAssets is None else BreakerAssets

        self._BreakerTypeAsset = None
        self.BreakerTypeAsset = BreakerTypeAsset

        super(BreakerAssetModel, self).__init__(**kw_args)

    def getBreakerInfo(self):
        
        return self._BreakerInfo

    def setBreakerInfo(self, value):
        if self._BreakerInfo is not None:
            filtered = [x for x in self.BreakerInfo.BreakerAssetModels if x != self]
            self._BreakerInfo._BreakerAssetModels = filtered

        self._BreakerInfo = value
        if self._BreakerInfo is not None:
            self._BreakerInfo._BreakerAssetModels.append(self)

    BreakerInfo = property(getBreakerInfo, setBreakerInfo)

    def getBreakerAssets(self):
        
        return self._BreakerAssets

    def setBreakerAssets(self, value):
        for x in self._BreakerAssets:
            x._BreakerAssetModel = None
        for y in value:
            y._BreakerAssetModel = self
        self._BreakerAssets = value

    BreakerAssets = property(getBreakerAssets, setBreakerAssets)

    def addBreakerAssets(self, *BreakerAssets):
        for obj in BreakerAssets:
            obj._BreakerAssetModel = self
            self._BreakerAssets.append(obj)

    def removeBreakerAssets(self, *BreakerAssets):
        for obj in BreakerAssets:
            obj._BreakerAssetModel = None
            self._BreakerAssets.remove(obj)

    def getBreakerTypeAsset(self):
        
        return self._BreakerTypeAsset

    def setBreakerTypeAsset(self, value):
        if self._BreakerTypeAsset is not None:
            filtered = [x for x in self.BreakerTypeAsset.BreakerAssetModels if x != self]
            self._BreakerTypeAsset._BreakerAssetModels = filtered

        self._BreakerTypeAsset = value
        if self._BreakerTypeAsset is not None:
            self._BreakerTypeAsset._BreakerAssetModels.append(self)

    BreakerTypeAsset = property(getBreakerTypeAsset, setBreakerTypeAsset)

