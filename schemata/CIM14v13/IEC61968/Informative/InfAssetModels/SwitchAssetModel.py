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

class SwitchAssetModel(ElectricalAssetModel):
    """Documentation for a type of a switch asset of a particular product model made by a manufacturer.
    """

    def __init__(self, SwitchTypeAsset=None, SwitchAssets=None, SwitchInfo=None, **kw_args):
        """Initializes a new 'SwitchAssetModel' instance.

        @param SwitchTypeAsset:
        @param SwitchAssets:
        @param SwitchInfo:
        """
        self._SwitchTypeAsset = None
        self.SwitchTypeAsset = SwitchTypeAsset

        self._SwitchAssets = []
        self.SwitchAssets = [] if SwitchAssets is None else SwitchAssets

        self._SwitchInfo = None
        self.SwitchInfo = SwitchInfo

        super(SwitchAssetModel, self).__init__(**kw_args)

    def getSwitchTypeAsset(self):
        
        return self._SwitchTypeAsset

    def setSwitchTypeAsset(self, value):
        if self._SwitchTypeAsset is not None:
            filtered = [x for x in self.SwitchTypeAsset.SwitchAssetModels if x != self]
            self._SwitchTypeAsset._SwitchAssetModels = filtered

        self._SwitchTypeAsset = value
        if self._SwitchTypeAsset is not None:
            self._SwitchTypeAsset._SwitchAssetModels.append(self)

    SwitchTypeAsset = property(getSwitchTypeAsset, setSwitchTypeAsset)

    def getSwitchAssets(self):
        
        return self._SwitchAssets

    def setSwitchAssets(self, value):
        for x in self._SwitchAssets:
            x._SwitchAssetModel = None
        for y in value:
            y._SwitchAssetModel = self
        self._SwitchAssets = value

    SwitchAssets = property(getSwitchAssets, setSwitchAssets)

    def addSwitchAssets(self, *SwitchAssets):
        for obj in SwitchAssets:
            obj._SwitchAssetModel = self
            self._SwitchAssets.append(obj)

    def removeSwitchAssets(self, *SwitchAssets):
        for obj in SwitchAssets:
            obj._SwitchAssetModel = None
            self._SwitchAssets.remove(obj)

    def getSwitchInfo(self):
        
        return self._SwitchInfo

    def setSwitchInfo(self, value):
        if self._SwitchInfo is not None:
            self._SwitchInfo._SwitchAssetModel = None

        self._SwitchInfo = value
        if self._SwitchInfo is not None:
            self._SwitchInfo._SwitchAssetModel = self

    SwitchInfo = property(getSwitchInfo, setSwitchInfo)

