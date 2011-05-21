# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

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

