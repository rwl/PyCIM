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

class ProtectionEquipmentTypeAsset(ElectricalTypeAsset):
    """Documentation for generic protection equiment that may be used for design purposes.
    """

    def __init__(self, defaultPhaseTrip=0.0, defaultGroundTrip=0.0, ProtectionEquipmentAssetModels=None, **kw_args):
        """Initializes a new 'ProtectionEquipmentTypeAsset' instance.

        @param defaultPhaseTrip: Default phase trip setting for this type of relay, if applicable. 
        @param defaultGroundTrip: Default ground trip setting for this type of relay, if applicable. 
        @param ProtectionEquipmentAssetModels:
        """
        #: Default phase trip setting for this type of relay, if applicable.
        self.defaultPhaseTrip = defaultPhaseTrip

        #: Default ground trip setting for this type of relay, if applicable.
        self.defaultGroundTrip = defaultGroundTrip

        self._ProtectionEquipmentAssetModels = []
        self.ProtectionEquipmentAssetModels = [] if ProtectionEquipmentAssetModels is None else ProtectionEquipmentAssetModels

        super(ProtectionEquipmentTypeAsset, self).__init__(**kw_args)

    def getProtectionEquipmentAssetModels(self):
        
        return self._ProtectionEquipmentAssetModels

    def setProtectionEquipmentAssetModels(self, value):
        for x in self._ProtectionEquipmentAssetModels:
            x._ProtectionEquipmentTypeAsset = None
        for y in value:
            y._ProtectionEquipmentTypeAsset = self
        self._ProtectionEquipmentAssetModels = value

    ProtectionEquipmentAssetModels = property(getProtectionEquipmentAssetModels, setProtectionEquipmentAssetModels)

    def addProtectionEquipmentAssetModels(self, *ProtectionEquipmentAssetModels):
        for obj in ProtectionEquipmentAssetModels:
            obj._ProtectionEquipmentTypeAsset = self
            self._ProtectionEquipmentAssetModels.append(obj)

    def removeProtectionEquipmentAssetModels(self, *ProtectionEquipmentAssetModels):
        for obj in ProtectionEquipmentAssetModels:
            obj._ProtectionEquipmentTypeAsset = None
            self._ProtectionEquipmentAssetModels.remove(obj)

