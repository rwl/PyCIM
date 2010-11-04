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

class ProtectionEquipmentAssetModel(ElectricalAssetModel):
    """Documentation for a type of protection equipment asset of a particular product model made by a manufacturer.
    """

    def __init__(self, ProtectionEquipmentAssets=None, ProtectionEquipmentTypeAsset=None, **kw_args):
        """Initializes a new 'ProtectionEquipmentAssetModel' instance.

        @param ProtectionEquipmentAssets:
        @param ProtectionEquipmentTypeAsset:
        """
        self._ProtectionEquipmentAssets = []
        self.ProtectionEquipmentAssets = [] if ProtectionEquipmentAssets is None else ProtectionEquipmentAssets

        self._ProtectionEquipmentTypeAsset = None
        self.ProtectionEquipmentTypeAsset = ProtectionEquipmentTypeAsset

        super(ProtectionEquipmentAssetModel, self).__init__(**kw_args)

    def getProtectionEquipmentAssets(self):
        
        return self._ProtectionEquipmentAssets

    def setProtectionEquipmentAssets(self, value):
        for x in self._ProtectionEquipmentAssets:
            x._ProtectionEquipmentAssetModel = None
        for y in value:
            y._ProtectionEquipmentAssetModel = self
        self._ProtectionEquipmentAssets = value

    ProtectionEquipmentAssets = property(getProtectionEquipmentAssets, setProtectionEquipmentAssets)

    def addProtectionEquipmentAssets(self, *ProtectionEquipmentAssets):
        for obj in ProtectionEquipmentAssets:
            obj._ProtectionEquipmentAssetModel = self
            self._ProtectionEquipmentAssets.append(obj)

    def removeProtectionEquipmentAssets(self, *ProtectionEquipmentAssets):
        for obj in ProtectionEquipmentAssets:
            obj._ProtectionEquipmentAssetModel = None
            self._ProtectionEquipmentAssets.remove(obj)

    def getProtectionEquipmentTypeAsset(self):
        
        return self._ProtectionEquipmentTypeAsset

    def setProtectionEquipmentTypeAsset(self, value):
        if self._ProtectionEquipmentTypeAsset is not None:
            filtered = [x for x in self.ProtectionEquipmentTypeAsset.ProtectionEquipmentAssetModels if x != self]
            self._ProtectionEquipmentTypeAsset._ProtectionEquipmentAssetModels = filtered

        self._ProtectionEquipmentTypeAsset = value
        if self._ProtectionEquipmentTypeAsset is not None:
            self._ProtectionEquipmentTypeAsset._ProtectionEquipmentAssetModels.append(self)

    ProtectionEquipmentTypeAsset = property(getProtectionEquipmentTypeAsset, setProtectionEquipmentTypeAsset)

