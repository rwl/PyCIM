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

class RecloserAssetModel(ElectricalAssetModel):
    """Documentation for a type of a recloser asset of a particular product model made by a manufacturer.
    """

    def __init__(self, RecloserInfo=None, RecloserTypeAsset=None, RecloserAssets=None, **kw_args):
        """Initializes a new 'RecloserAssetModel' instance.

        @param RecloserInfo:
        @param RecloserTypeAsset:
        @param RecloserAssets:
        """
        self._RecloserInfo = None
        self.RecloserInfo = RecloserInfo

        self._RecloserTypeAsset = None
        self.RecloserTypeAsset = RecloserTypeAsset

        self._RecloserAssets = []
        self.RecloserAssets = [] if RecloserAssets is None else RecloserAssets

        super(RecloserAssetModel, self).__init__(**kw_args)

    def getRecloserInfo(self):
        
        return self._RecloserInfo

    def setRecloserInfo(self, value):
        if self._RecloserInfo is not None:
            filtered = [x for x in self.RecloserInfo.RecloserAssetModels if x != self]
            self._RecloserInfo._RecloserAssetModels = filtered

        self._RecloserInfo = value
        if self._RecloserInfo is not None:
            self._RecloserInfo._RecloserAssetModels.append(self)

    RecloserInfo = property(getRecloserInfo, setRecloserInfo)

    def getRecloserTypeAsset(self):
        
        return self._RecloserTypeAsset

    def setRecloserTypeAsset(self, value):
        if self._RecloserTypeAsset is not None:
            filtered = [x for x in self.RecloserTypeAsset.RecloserAssetModels if x != self]
            self._RecloserTypeAsset._RecloserAssetModels = filtered

        self._RecloserTypeAsset = value
        if self._RecloserTypeAsset is not None:
            self._RecloserTypeAsset._RecloserAssetModels.append(self)

    RecloserTypeAsset = property(getRecloserTypeAsset, setRecloserTypeAsset)

    def getRecloserAssets(self):
        
        return self._RecloserAssets

    def setRecloserAssets(self, value):
        for x in self._RecloserAssets:
            x._RecloserAssetModel = None
        for y in value:
            y._RecloserAssetModel = self
        self._RecloserAssets = value

    RecloserAssets = property(getRecloserAssets, setRecloserAssets)

    def addRecloserAssets(self, *RecloserAssets):
        for obj in RecloserAssets:
            obj._RecloserAssetModel = self
            self._RecloserAssets.append(obj)

    def removeRecloserAssets(self, *RecloserAssets):
        for obj in RecloserAssets:
            obj._RecloserAssetModel = None
            self._RecloserAssets.remove(obj)

