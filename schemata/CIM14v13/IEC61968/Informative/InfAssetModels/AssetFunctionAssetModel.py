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

class AssetFunctionAssetModel(AssetModel):
    """Documentation for a type of an asset function of a particular product model made by a manufacturer.(Organisation). Asset Functions are typically component parts of Assets or Asset Containers.
    """

    def __init__(self, AssetFunctionTypeAsset=None, AssetFunctions=None, *args, **kw_args):
        """Initializes a new 'AssetFunctionAssetModel' instance.

        @param AssetFunctionTypeAsset:
        @param AssetFunctions:
        """
        self._AssetFunctionTypeAsset = None
        self.AssetFunctionTypeAsset = AssetFunctionTypeAsset

        self._AssetFunctions = []
        self.AssetFunctions = [] if AssetFunctions is None else AssetFunctions

        super(AssetFunctionAssetModel, self).__init__(*args, **kw_args)

    def getAssetFunctionTypeAsset(self):
        
        return self._AssetFunctionTypeAsset

    def setAssetFunctionTypeAsset(self, value):
        if self._AssetFunctionTypeAsset is not None:
            filtered = [x for x in self.AssetFunctionTypeAsset.AssetFunctionAssetModels if x != self]
            self._AssetFunctionTypeAsset._AssetFunctionAssetModels = filtered

        self._AssetFunctionTypeAsset = value
        if self._AssetFunctionTypeAsset is not None:
            self._AssetFunctionTypeAsset._AssetFunctionAssetModels.append(self)

    AssetFunctionTypeAsset = property(getAssetFunctionTypeAsset, setAssetFunctionTypeAsset)

    def getAssetFunctions(self):
        
        return self._AssetFunctions

    def setAssetFunctions(self, value):
        for x in self._AssetFunctions:
            x._AssetFunctionAssetModel = None
        for y in value:
            y._AssetFunctionAssetModel = self
        self._AssetFunctions = value

    AssetFunctions = property(getAssetFunctions, setAssetFunctions)

    def addAssetFunctions(self, *AssetFunctions):
        for obj in AssetFunctions:
            obj._AssetFunctionAssetModel = self
            self._AssetFunctions.append(obj)

    def removeAssetFunctions(self, *AssetFunctions):
        for obj in AssetFunctions:
            obj._AssetFunctionAssetModel = None
            self._AssetFunctions.remove(obj)

