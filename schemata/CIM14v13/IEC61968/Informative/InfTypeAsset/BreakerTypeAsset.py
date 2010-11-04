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

class BreakerTypeAsset(ElectricalTypeAsset):
    """Documentation for a generic breaker asset that may be used for design purposes.
    """

    def __init__(self, BreakerInfo=None, BreakerAssetModels=None, **kw_args):
        """Initializes a new 'BreakerTypeAsset' instance.

        @param BreakerInfo:
        @param BreakerAssetModels:
        """
        self._BreakerInfo = None
        self.BreakerInfo = BreakerInfo

        self._BreakerAssetModels = []
        self.BreakerAssetModels = [] if BreakerAssetModels is None else BreakerAssetModels

        super(BreakerTypeAsset, self).__init__(**kw_args)

    def getBreakerInfo(self):
        
        return self._BreakerInfo

    def setBreakerInfo(self, value):
        if self._BreakerInfo is not None:
            self._BreakerInfo._BreakerTypeAsset = None

        self._BreakerInfo = value
        if self._BreakerInfo is not None:
            self._BreakerInfo._BreakerTypeAsset = self

    BreakerInfo = property(getBreakerInfo, setBreakerInfo)

    def getBreakerAssetModels(self):
        
        return self._BreakerAssetModels

    def setBreakerAssetModels(self, value):
        for x in self._BreakerAssetModels:
            x._BreakerTypeAsset = None
        for y in value:
            y._BreakerTypeAsset = self
        self._BreakerAssetModels = value

    BreakerAssetModels = property(getBreakerAssetModels, setBreakerAssetModels)

    def addBreakerAssetModels(self, *BreakerAssetModels):
        for obj in BreakerAssetModels:
            obj._BreakerTypeAsset = self
            self._BreakerAssetModels.append(obj)

    def removeBreakerAssetModels(self, *BreakerAssetModels):
        for obj in BreakerAssetModels:
            obj._BreakerTypeAsset = None
            self._BreakerAssetModels.remove(obj)

