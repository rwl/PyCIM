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

class WorkEquipmentAssetModel(AssetModel):
    """Documentation for a type of an equipment used for work of a particular product model made by a manufacturer.
    """

    def __init__(self, WorkEquipmentTypeAsset=None, WorkEquipmentAssets=None, **kw_args):
        """Initializes a new 'WorkEquipmentAssetModel' instance.

        @param WorkEquipmentTypeAsset:
        @param WorkEquipmentAssets:
        """
        self._WorkEquipmentTypeAsset = None
        self.WorkEquipmentTypeAsset = WorkEquipmentTypeAsset

        self._WorkEquipmentAssets = []
        self.WorkEquipmentAssets = [] if WorkEquipmentAssets is None else WorkEquipmentAssets

        super(WorkEquipmentAssetModel, self).__init__(**kw_args)

    def getWorkEquipmentTypeAsset(self):
        
        return self._WorkEquipmentTypeAsset

    def setWorkEquipmentTypeAsset(self, value):
        if self._WorkEquipmentTypeAsset is not None:
            filtered = [x for x in self.WorkEquipmentTypeAsset.WorkEquipmentAssetModels if x != self]
            self._WorkEquipmentTypeAsset._WorkEquipmentAssetModels = filtered

        self._WorkEquipmentTypeAsset = value
        if self._WorkEquipmentTypeAsset is not None:
            self._WorkEquipmentTypeAsset._WorkEquipmentAssetModels.append(self)

    WorkEquipmentTypeAsset = property(getWorkEquipmentTypeAsset, setWorkEquipmentTypeAsset)

    def getWorkEquipmentAssets(self):
        
        return self._WorkEquipmentAssets

    def setWorkEquipmentAssets(self, value):
        for x in self._WorkEquipmentAssets:
            x._WorkEquipmentAssetModel = None
        for y in value:
            y._WorkEquipmentAssetModel = self
        self._WorkEquipmentAssets = value

    WorkEquipmentAssets = property(getWorkEquipmentAssets, setWorkEquipmentAssets)

    def addWorkEquipmentAssets(self, *WorkEquipmentAssets):
        for obj in WorkEquipmentAssets:
            obj._WorkEquipmentAssetModel = self
            self._WorkEquipmentAssets.append(obj)

    def removeWorkEquipmentAssets(self, *WorkEquipmentAssets):
        for obj in WorkEquipmentAssets:
            obj._WorkEquipmentAssetModel = None
            self._WorkEquipmentAssets.remove(obj)

