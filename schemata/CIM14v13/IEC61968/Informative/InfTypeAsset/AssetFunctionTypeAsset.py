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

class AssetFunctionTypeAsset(TypeAsset):
    """Documentation for a generic Asset Function that may be used for various purposes such as work planning.
    """

    def __init__(self, AssetFunctionAssetModels=None, **kw_args):
        """Initializes a new 'AssetFunctionTypeAsset' instance.

        @param AssetFunctionAssetModels:
        """
        self._AssetFunctionAssetModels = []
        self.AssetFunctionAssetModels = [] if AssetFunctionAssetModels is None else AssetFunctionAssetModels

        super(AssetFunctionTypeAsset, self).__init__(**kw_args)

    def getAssetFunctionAssetModels(self):
        
        return self._AssetFunctionAssetModels

    def setAssetFunctionAssetModels(self, value):
        for x in self._AssetFunctionAssetModels:
            x._AssetFunctionTypeAsset = None
        for y in value:
            y._AssetFunctionTypeAsset = self
        self._AssetFunctionAssetModels = value

    AssetFunctionAssetModels = property(getAssetFunctionAssetModels, setAssetFunctionAssetModels)

    def addAssetFunctionAssetModels(self, *AssetFunctionAssetModels):
        for obj in AssetFunctionAssetModels:
            obj._AssetFunctionTypeAsset = self
            self._AssetFunctionAssetModels.append(obj)

    def removeAssetFunctionAssetModels(self, *AssetFunctionAssetModels):
        for obj in AssetFunctionAssetModels:
            obj._AssetFunctionTypeAsset = None
            self._AssetFunctionAssetModels.remove(obj)

