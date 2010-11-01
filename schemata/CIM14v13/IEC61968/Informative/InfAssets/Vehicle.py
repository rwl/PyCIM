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

from CIM14v13.IEC61968.Assets.Asset import Asset

class Vehicle(Asset):
    """A vehicle is a type of utility asset.
    """

    def __init__(self, usageKind='contractor', odometerReading=0.0, odometerReadDateTime='', Crew=None, VehicleAssetModel=None, *args, **kw_args):
        """Initializes a new 'Vehicle' instance.

        @param usageKind: The general categorization type of vehicle as categorized by the utility's asset management standards and practices. Note: (1) Vehicle model is defined by VehicleAssetModel, and (2) Specific people and organizations and their roles relative to this vehicle may be determined by the inherited Asset-ErpPerson and Asset-Organization associations. Values are: "contractor", "other", "crew", "user"
        @param odometerReading: Odometer reading of this vehicle as of the 'odometerReadingDateTime'. Refer to associated ActivityRecords for earlier readings. 
        @param odometerReadDateTime: Date and time the last odometer reading was recorded. 
        @param Crew:
        @param VehicleAssetModel:
        """
        #: The general categorization type of vehicle as categorized by the utility's asset management standards and practices. Note: (1) Vehicle model is defined by VehicleAssetModel, and (2) Specific people and organizations and their roles relative to this vehicle may be determined by the inherited Asset-ErpPerson and Asset-Organization associations. Values are: "contractor", "other", "crew", "user"
        self.usageKind = usageKind

        #: Odometer reading of this vehicle as of the 'odometerReadingDateTime'. Refer to associated ActivityRecords for earlier readings. 
        self.odometerReading = odometerReading

        #: Date and time the last odometer reading was recorded. 
        self.odometerReadDateTime = odometerReadDateTime

        self._Crew = None
        self.Crew = Crew

        self._VehicleAssetModel = None
        self.VehicleAssetModel = VehicleAssetModel

        super(Vehicle, self).__init__(*args, **kw_args)

    def getCrew(self):
        
        return self._Crew

    def setCrew(self, value):
        if self._Crew is not None:
            filtered = [x for x in self.Crew.Vehicles if x != self]
            self._Crew._Vehicles = filtered

        self._Crew = value
        if self._Crew is not None:
            self._Crew._Vehicles.append(self)

    Crew = property(getCrew, setCrew)

    def getVehicleAssetModel(self):
        
        return self._VehicleAssetModel

    def setVehicleAssetModel(self, value):
        if self._VehicleAssetModel is not None:
            filtered = [x for x in self.VehicleAssetModel.Vehicles if x != self]
            self._VehicleAssetModel._Vehicles = filtered

        self._VehicleAssetModel = value
        if self._VehicleAssetModel is not None:
            self._VehicleAssetModel._Vehicles.append(self)

    VehicleAssetModel = property(getVehicleAssetModel, setVehicleAssetModel)

