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

from CIM14v13.IEC61968.Informative.InfAssets.SwitchInfo import SwitchInfo

class BreakerInfo(SwitchInfo):
    """Properties of breakers.
    """

    def __init__(self, phaseTrip=0.0, BreakerAssets=None, BreakerAssetModels=None, BreakerTypeAsset=None, **kw_args):
        """Initializes a new 'BreakerInfo' instance.

        @param phaseTrip: Phase trip rating. 
        @param BreakerAssets:
        @param BreakerAssetModels:
        @param BreakerTypeAsset:
        """
        #: Phase trip rating.
        self.phaseTrip = phaseTrip

        self._BreakerAssets = []
        self.BreakerAssets = [] if BreakerAssets is None else BreakerAssets

        self._BreakerAssetModels = []
        self.BreakerAssetModels = [] if BreakerAssetModels is None else BreakerAssetModels

        self._BreakerTypeAsset = None
        self.BreakerTypeAsset = BreakerTypeAsset

        super(BreakerInfo, self).__init__(**kw_args)

    def getBreakerAssets(self):
        
        return self._BreakerAssets

    def setBreakerAssets(self, value):
        for x in self._BreakerAssets:
            x._BreakerInfo = None
        for y in value:
            y._BreakerInfo = self
        self._BreakerAssets = value

    BreakerAssets = property(getBreakerAssets, setBreakerAssets)

    def addBreakerAssets(self, *BreakerAssets):
        for obj in BreakerAssets:
            obj._BreakerInfo = self
            self._BreakerAssets.append(obj)

    def removeBreakerAssets(self, *BreakerAssets):
        for obj in BreakerAssets:
            obj._BreakerInfo = None
            self._BreakerAssets.remove(obj)

    def getBreakerAssetModels(self):
        
        return self._BreakerAssetModels

    def setBreakerAssetModels(self, value):
        for x in self._BreakerAssetModels:
            x._BreakerInfo = None
        for y in value:
            y._BreakerInfo = self
        self._BreakerAssetModels = value

    BreakerAssetModels = property(getBreakerAssetModels, setBreakerAssetModels)

    def addBreakerAssetModels(self, *BreakerAssetModels):
        for obj in BreakerAssetModels:
            obj._BreakerInfo = self
            self._BreakerAssetModels.append(obj)

    def removeBreakerAssetModels(self, *BreakerAssetModels):
        for obj in BreakerAssetModels:
            obj._BreakerInfo = None
            self._BreakerAssetModels.remove(obj)

    def getBreakerTypeAsset(self):
        
        return self._BreakerTypeAsset

    def setBreakerTypeAsset(self, value):
        if self._BreakerTypeAsset is not None:
            self._BreakerTypeAsset._BreakerInfo = None

        self._BreakerTypeAsset = value
        if self._BreakerTypeAsset is not None:
            self._BreakerTypeAsset._BreakerInfo = self

    BreakerTypeAsset = property(getBreakerTypeAsset, setBreakerTypeAsset)

