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

from CIM14v13.IEC61970.Core.PowerSystemResource import PowerSystemResource

class CAESPlant(PowerSystemResource):
    """Compressed air energy storage plant
    """

    def __init__(self, ratedCapacityP=0.0, energyStorageCapacity=0.0, ThermalGeneratingUnit=None, AirCompressor=None, *args, **kw_args):
        """Initializes a new 'CAESPlant' instance.

        @param ratedCapacityP: The CAES plant's gross rated generating capacity 
        @param energyStorageCapacity: The rated energy storage capacity. 
        @param ThermalGeneratingUnit: A thermal generating unit may be a member of a compressed air energy storage plant
        @param AirCompressor: An air compressor may be a member of a compressed air energy storage plant
        """
        #: The CAES plant's gross rated generating capacity
        self.ratedCapacityP = ratedCapacityP

        #: The rated energy storage capacity.
        self.energyStorageCapacity = energyStorageCapacity

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        self._AirCompressor = None
        self.AirCompressor = AirCompressor

        super(CAESPlant, self).__init__(*args, **kw_args)

    def getThermalGeneratingUnit(self):
        """A thermal generating unit may be a member of a compressed air energy storage plant
        """
        return self._ThermalGeneratingUnit

    def setThermalGeneratingUnit(self, value):
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._CAESPlant = None

        self._ThermalGeneratingUnit = value
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._CAESPlant = self

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)

    def getAirCompressor(self):
        """An air compressor may be a member of a compressed air energy storage plant
        """
        return self._AirCompressor

    def setAirCompressor(self, value):
        if self._AirCompressor is not None:
            self._AirCompressor._CAESPlant = None

        self._AirCompressor = value
        if self._AirCompressor is not None:
            self._AirCompressor._CAESPlant = self

    AirCompressor = property(getAirCompressor, setAirCompressor)

