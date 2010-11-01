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

class SwitchTypeAsset(ElectricalTypeAsset):
    """Documentation for a generic switch asset that may be used for design purposes.
    """

    def __init__(self, SwitchAssetModels=None, CompositeSwitchTypeAsset=None, SwitchInfo=None, *args, **kw_args):
        """Initializes a new 'SwitchTypeAsset' instance.

        @param SwitchAssetModels:
        @param CompositeSwitchTypeAsset:
        @param SwitchInfo:
        """
        self._SwitchAssetModels = []
        self.SwitchAssetModels = [] if SwitchAssetModels is None else SwitchAssetModels

        self._CompositeSwitchTypeAsset = None
        self.CompositeSwitchTypeAsset = CompositeSwitchTypeAsset

        self._SwitchInfo = None
        self.SwitchInfo = SwitchInfo

        super(SwitchTypeAsset, self).__init__(*args, **kw_args)

    def getSwitchAssetModels(self):
        
        return self._SwitchAssetModels

    def setSwitchAssetModels(self, value):
        for x in self._SwitchAssetModels:
            x._SwitchTypeAsset = None
        for y in value:
            y._SwitchTypeAsset = self
        self._SwitchAssetModels = value

    SwitchAssetModels = property(getSwitchAssetModels, setSwitchAssetModels)

    def addSwitchAssetModels(self, *SwitchAssetModels):
        for obj in SwitchAssetModels:
            obj._SwitchTypeAsset = self
            self._SwitchAssetModels.append(obj)

    def removeSwitchAssetModels(self, *SwitchAssetModels):
        for obj in SwitchAssetModels:
            obj._SwitchTypeAsset = None
            self._SwitchAssetModels.remove(obj)

    def getCompositeSwitchTypeAsset(self):
        
        return self._CompositeSwitchTypeAsset

    def setCompositeSwitchTypeAsset(self, value):
        if self._CompositeSwitchTypeAsset is not None:
            filtered = [x for x in self.CompositeSwitchTypeAsset.SwitchTypesAssets if x != self]
            self._CompositeSwitchTypeAsset._SwitchTypesAssets = filtered

        self._CompositeSwitchTypeAsset = value
        if self._CompositeSwitchTypeAsset is not None:
            self._CompositeSwitchTypeAsset._SwitchTypesAssets.append(self)

    CompositeSwitchTypeAsset = property(getCompositeSwitchTypeAsset, setCompositeSwitchTypeAsset)

    def getSwitchInfo(self):
        
        return self._SwitchInfo

    def setSwitchInfo(self, value):
        if self._SwitchInfo is not None:
            self._SwitchInfo._SwitchTypeAsset = None

        self._SwitchInfo = value
        if self._SwitchInfo is not None:
            self._SwitchInfo._SwitchTypeAsset = self

    SwitchInfo = property(getSwitchInfo, setSwitchInfo)

