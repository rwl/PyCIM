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

from CIM14v13.IEC61968.Assets.Asset import Asset

class CompositeSwitchAsset(Asset):
    """Physical asset that performs a given CompositeSwitch's role.
    """

    def __init__(self, kind='ugMultiSwitch', CompositeSwitchInfo=None, CompositeSwitchAssetModel=None, *args, **kw_args):
        """Initializes a new 'CompositeSwitchAsset' instance.

        @param kind: Kind of composite switch. Values are: "ugMultiSwitch", "throwOver", "escoThrowOver", "gral", "ral", "other", "regulatorBypass"
        @param CompositeSwitchInfo:
        @param CompositeSwitchAssetModel:
        """
        #: Kind of composite switch.Values are: "ugMultiSwitch", "throwOver", "escoThrowOver", "gral", "ral", "other", "regulatorBypass"
        self.kind = kind

        self._CompositeSwitchInfo = None
        self.CompositeSwitchInfo = CompositeSwitchInfo

        self._CompositeSwitchAssetModel = None
        self.CompositeSwitchAssetModel = CompositeSwitchAssetModel

        super(CompositeSwitchAsset, self).__init__(*args, **kw_args)

    def getCompositeSwitchInfo(self):
        
        return self._CompositeSwitchInfo

    def setCompositeSwitchInfo(self, value):
        if self._CompositeSwitchInfo is not None:
            filtered = [x for x in self.CompositeSwitchInfo.CompositeSwitchAssets if x != self]
            self._CompositeSwitchInfo._CompositeSwitchAssets = filtered

        self._CompositeSwitchInfo = value
        if self._CompositeSwitchInfo is not None:
            self._CompositeSwitchInfo._CompositeSwitchAssets.append(self)

    CompositeSwitchInfo = property(getCompositeSwitchInfo, setCompositeSwitchInfo)

    def getCompositeSwitchAssetModel(self):
        
        return self._CompositeSwitchAssetModel

    def setCompositeSwitchAssetModel(self, value):
        if self._CompositeSwitchAssetModel is not None:
            filtered = [x for x in self.CompositeSwitchAssetModel.CompositeSwitchAssets if x != self]
            self._CompositeSwitchAssetModel._CompositeSwitchAssets = filtered

        self._CompositeSwitchAssetModel = value
        if self._CompositeSwitchAssetModel is not None:
            self._CompositeSwitchAssetModel._CompositeSwitchAssets.append(self)

    CompositeSwitchAssetModel = property(getCompositeSwitchAssetModel, setCompositeSwitchAssetModel)

