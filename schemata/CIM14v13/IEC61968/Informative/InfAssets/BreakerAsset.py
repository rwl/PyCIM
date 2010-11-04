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

from CIM14v13.IEC61968.Informative.InfAssets.ElectricalAsset import ElectricalAsset

class BreakerAsset(ElectricalAsset):
    """Physical asset performing Breaker role.
    """

    def __init__(self, BreakerInfo=None, BreakerAssetModel=None, **kw_args):
        """Initializes a new 'BreakerAsset' instance.

        @param BreakerInfo:
        @param BreakerAssetModel:
        """
        self._BreakerInfo = None
        self.BreakerInfo = BreakerInfo

        self._BreakerAssetModel = None
        self.BreakerAssetModel = BreakerAssetModel

        super(BreakerAsset, self).__init__(**kw_args)

    def getBreakerInfo(self):
        
        return self._BreakerInfo

    def setBreakerInfo(self, value):
        if self._BreakerInfo is not None:
            filtered = [x for x in self.BreakerInfo.BreakerAssets if x != self]
            self._BreakerInfo._BreakerAssets = filtered

        self._BreakerInfo = value
        if self._BreakerInfo is not None:
            self._BreakerInfo._BreakerAssets.append(self)

    BreakerInfo = property(getBreakerInfo, setBreakerInfo)

    def getBreakerAssetModel(self):
        
        return self._BreakerAssetModel

    def setBreakerAssetModel(self, value):
        if self._BreakerAssetModel is not None:
            filtered = [x for x in self.BreakerAssetModel.BreakerAssets if x != self]
            self._BreakerAssetModel._BreakerAssets = filtered

        self._BreakerAssetModel = value
        if self._BreakerAssetModel is not None:
            self._BreakerAssetModel._BreakerAssets.append(self)

    BreakerAssetModel = property(getBreakerAssetModel, setBreakerAssetModel)

