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

from CIM14v13.IEC61968.Informative.InfAssets.ElectricalAsset import ElectricalAsset

class ProtectionEquipmentAsset(ElectricalAsset):
    """Physical asset performing ProtectionEquipment function.
    """

    def __init__(self, phaseTrip=0.0, groundTrip=0.0, ProtectionEquipmentAssetModel=None, *args, **kw_args):
        """Initializes a new 'ProtectionEquipmentAsset' instance.

        @param phaseTrip: Actual phase trip for this type of relay, if applicable. 
        @param groundTrip: Actual ground trip for this type of relay, if applicable. 
        @param ProtectionEquipmentAssetModel:
        """
        #: Actual phase trip for this type of relay, if applicable.
        self.phaseTrip = phaseTrip

        #: Actual ground trip for this type of relay, if applicable.
        self.groundTrip = groundTrip

        self._ProtectionEquipmentAssetModel = None
        self.ProtectionEquipmentAssetModel = ProtectionEquipmentAssetModel

        super(ProtectionEquipmentAsset, self).__init__(*args, **kw_args)

    def getProtectionEquipmentAssetModel(self):
        
        return self._ProtectionEquipmentAssetModel

    def setProtectionEquipmentAssetModel(self, value):
        if self._ProtectionEquipmentAssetModel is not None:
            filtered = [x for x in self.ProtectionEquipmentAssetModel.ProtectionEquipmentAssets if x != self]
            self._ProtectionEquipmentAssetModel._ProtectionEquipmentAssets = filtered

        self._ProtectionEquipmentAssetModel = value
        if self._ProtectionEquipmentAssetModel is not None:
            self._ProtectionEquipmentAssetModel._ProtectionEquipmentAssets.append(self)

    ProtectionEquipmentAssetModel = property(getProtectionEquipmentAssetModel, setProtectionEquipmentAssetModel)

