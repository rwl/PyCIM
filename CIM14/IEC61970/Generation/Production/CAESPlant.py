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

from CIM14.IEC61970.Core.PowerSystemResource import PowerSystemResource

class CAESPlant(PowerSystemResource):
    """Compressed air energy storage plant
    """

    def __init__(self, energyStorageCapacity=0.0, ratedCapacityP=0.0, AirCompressor=None, ThermalGeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'CAESPlant' instance.

        @param energyStorageCapacity: The rated energy storage capacity. 
        @param ratedCapacityP: The CAES plant's gross rated generating capacity 
        @param AirCompressor: An air compressor may be a member of a compressed air energy storage plant
        @param ThermalGeneratingUnit: A thermal generating unit may be a member of a compressed air energy storage plant
        """
        #: The rated energy storage capacity.
        self.energyStorageCapacity = energyStorageCapacity

        #: The CAES plant's gross rated generating capacity
        self.ratedCapacityP = ratedCapacityP

        self._AirCompressor = None
        self.AirCompressor = AirCompressor

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        super(CAESPlant, self).__init__(*args, **kw_args)

    _attrs = ["energyStorageCapacity", "ratedCapacityP"]
    _attr_types = {"energyStorageCapacity": float, "ratedCapacityP": float}
    _defaults = {"energyStorageCapacity": 0.0, "ratedCapacityP": 0.0}
    _enums = {}
    _refs = ["AirCompressor", "ThermalGeneratingUnit"]
    _many_refs = []

    def getAirCompressor(self):
        """An air compressor may be a member of a compressed air energy storage plant
        """
        return self._AirCompressor

    def setAirCompressor(self, value):
        if self._AirCompressor is not None:
            self._AirCompressor._CAESPlant = None

        self._AirCompressor = value
        if self._AirCompressor is not None:
            self._AirCompressor.CAESPlant = None
            self._AirCompressor._CAESPlant = self

    AirCompressor = property(getAirCompressor, setAirCompressor)

    def getThermalGeneratingUnit(self):
        """A thermal generating unit may be a member of a compressed air energy storage plant
        """
        return self._ThermalGeneratingUnit

    def setThermalGeneratingUnit(self, value):
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._CAESPlant = None

        self._ThermalGeneratingUnit = value
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit.CAESPlant = None
            self._ThermalGeneratingUnit._CAESPlant = self

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)

