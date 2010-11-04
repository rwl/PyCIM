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

class SwitchAsset(ElectricalAsset):
    """Physical asset performing Switch function.
    """

    def __init__(self, SwitchInfo=None, SwitchAssetModel=None, **kw_args):
        """Initializes a new 'SwitchAsset' instance.

        @param SwitchInfo:
        @param SwitchAssetModel:
        """
        self._SwitchInfo = None
        self.SwitchInfo = SwitchInfo

        self._SwitchAssetModel = None
        self.SwitchAssetModel = SwitchAssetModel

        super(SwitchAsset, self).__init__(**kw_args)

    def getSwitchInfo(self):
        
        return self._SwitchInfo

    def setSwitchInfo(self, value):
        if self._SwitchInfo is not None:
            filtered = [x for x in self.SwitchInfo.SwitchAssets if x != self]
            self._SwitchInfo._SwitchAssets = filtered

        self._SwitchInfo = value
        if self._SwitchInfo is not None:
            self._SwitchInfo._SwitchAssets.append(self)

    SwitchInfo = property(getSwitchInfo, setSwitchInfo)

    def getSwitchAssetModel(self):
        
        return self._SwitchAssetModel

    def setSwitchAssetModel(self, value):
        if self._SwitchAssetModel is not None:
            filtered = [x for x in self.SwitchAssetModel.SwitchAssets if x != self]
            self._SwitchAssetModel._SwitchAssets = filtered

        self._SwitchAssetModel = value
        if self._SwitchAssetModel is not None:
            self._SwitchAssetModel._SwitchAssets.append(self)

    SwitchAssetModel = property(getSwitchAssetModel, setSwitchAssetModel)

