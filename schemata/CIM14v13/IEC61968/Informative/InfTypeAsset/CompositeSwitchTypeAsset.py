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

from CIM14v13.IEC61968.Informative.InfTypeAsset.TypeAsset import TypeAsset

class CompositeSwitchTypeAsset(TypeAsset):
    """Documentation for a generic composite switch asset that may be used for design purposes. A composite wwitch is an amalgamation of multiple Switches.
    """

    def __init__(self, CompositeSwitchAssetModels=None, SwitchTypesAssets=None, CompositeSwitchInfo=None, *args, **kw_args):
        """Initializes a new 'CompositeSwitchTypeAsset' instance.

        @param CompositeSwitchAssetModels:
        @param SwitchTypesAssets:
        @param CompositeSwitchInfo:
        """
        self._CompositeSwitchAssetModels = []
        self.CompositeSwitchAssetModels = [] if CompositeSwitchAssetModels is None else CompositeSwitchAssetModels

        self._SwitchTypesAssets = []
        self.SwitchTypesAssets = [] if SwitchTypesAssets is None else SwitchTypesAssets

        self._CompositeSwitchInfo = None
        self.CompositeSwitchInfo = CompositeSwitchInfo

        super(CompositeSwitchTypeAsset, self).__init__(*args, **kw_args)

    def getCompositeSwitchAssetModels(self):
        
        return self._CompositeSwitchAssetModels

    def setCompositeSwitchAssetModels(self, value):
        for x in self._CompositeSwitchAssetModels:
            x._CompositeSwitchTypeAsset = None
        for y in value:
            y._CompositeSwitchTypeAsset = self
        self._CompositeSwitchAssetModels = value

    CompositeSwitchAssetModels = property(getCompositeSwitchAssetModels, setCompositeSwitchAssetModels)

    def addCompositeSwitchAssetModels(self, *CompositeSwitchAssetModels):
        for obj in CompositeSwitchAssetModels:
            obj._CompositeSwitchTypeAsset = self
            self._CompositeSwitchAssetModels.append(obj)

    def removeCompositeSwitchAssetModels(self, *CompositeSwitchAssetModels):
        for obj in CompositeSwitchAssetModels:
            obj._CompositeSwitchTypeAsset = None
            self._CompositeSwitchAssetModels.remove(obj)

    def getSwitchTypesAssets(self):
        
        return self._SwitchTypesAssets

    def setSwitchTypesAssets(self, value):
        for x in self._SwitchTypesAssets:
            x._CompositeSwitchTypeAsset = None
        for y in value:
            y._CompositeSwitchTypeAsset = self
        self._SwitchTypesAssets = value

    SwitchTypesAssets = property(getSwitchTypesAssets, setSwitchTypesAssets)

    def addSwitchTypesAssets(self, *SwitchTypesAssets):
        for obj in SwitchTypesAssets:
            obj._CompositeSwitchTypeAsset = self
            self._SwitchTypesAssets.append(obj)

    def removeSwitchTypesAssets(self, *SwitchTypesAssets):
        for obj in SwitchTypesAssets:
            obj._CompositeSwitchTypeAsset = None
            self._SwitchTypesAssets.remove(obj)

    def getCompositeSwitchInfo(self):
        
        return self._CompositeSwitchInfo

    def setCompositeSwitchInfo(self, value):
        if self._CompositeSwitchInfo is not None:
            self._CompositeSwitchInfo._CompositeSwitchTypeAsset = None

        self._CompositeSwitchInfo = value
        if self._CompositeSwitchInfo is not None:
            self._CompositeSwitchInfo._CompositeSwitchTypeAsset = self

    CompositeSwitchInfo = property(getCompositeSwitchInfo, setCompositeSwitchInfo)

