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

from CIM14v13.IEC61968.AssetModels.AssetModel import AssetModel

class CompositeSwitchAssetModel(AssetModel):
    """Documentation for a type of a composite switch asset of a particular product model made by a manufacturer.
    """

    def __init__(self, CompositeSwitchInfo=None, CompositeSwitchAssets=None, CompositeSwitchTypeAsset=None, **kw_args):
        """Initializes a new 'CompositeSwitchAssetModel' instance.

        @param CompositeSwitchInfo:
        @param CompositeSwitchAssets:
        @param CompositeSwitchTypeAsset:
        """
        self._CompositeSwitchInfo = None
        self.CompositeSwitchInfo = CompositeSwitchInfo

        self._CompositeSwitchAssets = []
        self.CompositeSwitchAssets = [] if CompositeSwitchAssets is None else CompositeSwitchAssets

        self._CompositeSwitchTypeAsset = None
        self.CompositeSwitchTypeAsset = CompositeSwitchTypeAsset

        super(CompositeSwitchAssetModel, self).__init__(**kw_args)

    def getCompositeSwitchInfo(self):
        
        return self._CompositeSwitchInfo

    def setCompositeSwitchInfo(self, value):
        if self._CompositeSwitchInfo is not None:
            self._CompositeSwitchInfo._CompositeSwitchAssetModel = None

        self._CompositeSwitchInfo = value
        if self._CompositeSwitchInfo is not None:
            self._CompositeSwitchInfo._CompositeSwitchAssetModel = self

    CompositeSwitchInfo = property(getCompositeSwitchInfo, setCompositeSwitchInfo)

    def getCompositeSwitchAssets(self):
        
        return self._CompositeSwitchAssets

    def setCompositeSwitchAssets(self, value):
        for x in self._CompositeSwitchAssets:
            x._CompositeSwitchAssetModel = None
        for y in value:
            y._CompositeSwitchAssetModel = self
        self._CompositeSwitchAssets = value

    CompositeSwitchAssets = property(getCompositeSwitchAssets, setCompositeSwitchAssets)

    def addCompositeSwitchAssets(self, *CompositeSwitchAssets):
        for obj in CompositeSwitchAssets:
            obj._CompositeSwitchAssetModel = self
            self._CompositeSwitchAssets.append(obj)

    def removeCompositeSwitchAssets(self, *CompositeSwitchAssets):
        for obj in CompositeSwitchAssets:
            obj._CompositeSwitchAssetModel = None
            self._CompositeSwitchAssets.remove(obj)

    def getCompositeSwitchTypeAsset(self):
        
        return self._CompositeSwitchTypeAsset

    def setCompositeSwitchTypeAsset(self, value):
        if self._CompositeSwitchTypeAsset is not None:
            filtered = [x for x in self.CompositeSwitchTypeAsset.CompositeSwitchAssetModels if x != self]
            self._CompositeSwitchTypeAsset._CompositeSwitchAssetModels = filtered

        self._CompositeSwitchTypeAsset = value
        if self._CompositeSwitchTypeAsset is not None:
            self._CompositeSwitchTypeAsset._CompositeSwitchAssetModels.append(self)

    CompositeSwitchTypeAsset = property(getCompositeSwitchTypeAsset, setCompositeSwitchTypeAsset)

