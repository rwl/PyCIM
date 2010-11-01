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

class VehicleAssetModel(AssetModel):
    """Documentation for a type of a vehicle of a particular product model made by a manufacturer.
    """

    def __init__(self, Vehicles=None, VehicleTypeAsset=None, *args, **kw_args):
        """Initializes a new 'VehicleAssetModel' instance.

        @param Vehicles:
        @param VehicleTypeAsset:
        """
        self._Vehicles = []
        self.Vehicles = [] if Vehicles is None else Vehicles

        self._VehicleTypeAsset = None
        self.VehicleTypeAsset = VehicleTypeAsset

        super(VehicleAssetModel, self).__init__(*args, **kw_args)

    def getVehicles(self):
        
        return self._Vehicles

    def setVehicles(self, value):
        for x in self._Vehicles:
            x._VehicleAssetModel = None
        for y in value:
            y._VehicleAssetModel = self
        self._Vehicles = value

    Vehicles = property(getVehicles, setVehicles)

    def addVehicles(self, *Vehicles):
        for obj in Vehicles:
            obj._VehicleAssetModel = self
            self._Vehicles.append(obj)

    def removeVehicles(self, *Vehicles):
        for obj in Vehicles:
            obj._VehicleAssetModel = None
            self._Vehicles.remove(obj)

    def getVehicleTypeAsset(self):
        
        return self._VehicleTypeAsset

    def setVehicleTypeAsset(self, value):
        if self._VehicleTypeAsset is not None:
            filtered = [x for x in self.VehicleTypeAsset.VehicleAssetModels if x != self]
            self._VehicleTypeAsset._VehicleAssetModels = filtered

        self._VehicleTypeAsset = value
        if self._VehicleTypeAsset is not None:
            self._VehicleTypeAsset._VehicleAssetModels.append(self)

    VehicleTypeAsset = property(getVehicleTypeAsset, setVehicleTypeAsset)

