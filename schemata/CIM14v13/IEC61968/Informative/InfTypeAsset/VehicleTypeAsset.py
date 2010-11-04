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

class VehicleTypeAsset(TypeAsset):
    """Documentation for a generic vehicle that may be used for various purposes such as work planning.
    """

    def __init__(self, VehicleAssetModels=None, **kw_args):
        """Initializes a new 'VehicleTypeAsset' instance.

        @param VehicleAssetModels:
        """
        self._VehicleAssetModels = []
        self.VehicleAssetModels = [] if VehicleAssetModels is None else VehicleAssetModels

        super(VehicleTypeAsset, self).__init__(**kw_args)

    def getVehicleAssetModels(self):
        
        return self._VehicleAssetModels

    def setVehicleAssetModels(self, value):
        for x in self._VehicleAssetModels:
            x._VehicleTypeAsset = None
        for y in value:
            y._VehicleTypeAsset = self
        self._VehicleAssetModels = value

    VehicleAssetModels = property(getVehicleAssetModels, setVehicleAssetModels)

    def addVehicleAssetModels(self, *VehicleAssetModels):
        for obj in VehicleAssetModels:
            obj._VehicleTypeAsset = self
            self._VehicleAssetModels.append(obj)

    def removeVehicleAssetModels(self, *VehicleAssetModels):
        for obj in VehicleAssetModels:
            obj._VehicleTypeAsset = None
            self._VehicleAssetModels.remove(obj)

