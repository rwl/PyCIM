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

from CIM14.IEC61970.Generation.GenerationDynamics.PrimeMover import PrimeMover

class CombustionTurbine(PrimeMover):
    """A prime mover that is typically fueled by gas or light oil
    """

    def __init__(self, capabilityVersusFrequency=0.0, heatRecoveryFlag=False, timeConstant=0.0, auxPowerVersusFrequency=0.0, auxPowerVersusVoltage=0.0, referenceTemp=0.0, ambientTemp=0.0, powerVariationByTemp=0.0, HeatRecoveryBoiler=None, CTTempActivePowerCurve=None, AirCompressor=None, *args, **kw_args):
        """Initialises a new 'CombustionTurbine' instance.

        @param capabilityVersusFrequency: Off-nominal frequency effect on turbine capability. Per unit reduction in unit active power capability versus per unit reduction in frequency (from rated frequency). 
        @param heatRecoveryFlag: Flag that is set to true if the combustion turbine is associated with a heat recovery boiler 
        @param timeConstant: The time constant for the turbine. 
        @param auxPowerVersusFrequency: Off-nominal frequency effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in frequency (from rated frequency). 
        @param auxPowerVersusVoltage: Off-nominal voltage effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in auxiliary bus voltage (from a specified voltage level). 
        @param referenceTemp: Reference temperature at which the output of the turbine was defined. 
        @param ambientTemp: Default ambient temperature to be used in modeling applications 
        @param powerVariationByTemp: Per unit change in power per (versus) unit change in ambient temperature 
        @param HeatRecoveryBoiler: A combustion turbine may have a heat recovery boiler for making steam
        @param CTTempActivePowerCurve: A combustion turbine may have an active power versus ambient temperature relationship
        @param AirCompressor: A CAES air compressor is driven by combustion turbine
        """
        #: Off-nominal frequency effect on turbine capability. Per unit reduction in unit active power capability versus per unit reduction in frequency (from rated frequency).
        self.capabilityVersusFrequency = capabilityVersusFrequency

        #: Flag that is set to true if the combustion turbine is associated with a heat recovery boiler
        self.heatRecoveryFlag = heatRecoveryFlag

        #: The time constant for the turbine.
        self.timeConstant = timeConstant

        #: Off-nominal frequency effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in frequency (from rated frequency).
        self.auxPowerVersusFrequency = auxPowerVersusFrequency

        #: Off-nominal voltage effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in auxiliary bus voltage (from a specified voltage level).
        self.auxPowerVersusVoltage = auxPowerVersusVoltage

        #: Reference temperature at which the output of the turbine was defined.
        self.referenceTemp = referenceTemp

        #: Default ambient temperature to be used in modeling applications
        self.ambientTemp = ambientTemp

        #: Per unit change in power per (versus) unit change in ambient temperature
        self.powerVariationByTemp = powerVariationByTemp

        self._HeatRecoveryBoiler = None
        self.HeatRecoveryBoiler = HeatRecoveryBoiler

        self._CTTempActivePowerCurve = None
        self.CTTempActivePowerCurve = CTTempActivePowerCurve

        self._AirCompressor = None
        self.AirCompressor = AirCompressor

        super(CombustionTurbine, self).__init__(*args, **kw_args)

    _attrs = ["capabilityVersusFrequency", "heatRecoveryFlag", "timeConstant", "auxPowerVersusFrequency", "auxPowerVersusVoltage", "referenceTemp", "ambientTemp", "powerVariationByTemp"]
    _attr_types = {"capabilityVersusFrequency": float, "heatRecoveryFlag": bool, "timeConstant": float, "auxPowerVersusFrequency": float, "auxPowerVersusVoltage": float, "referenceTemp": float, "ambientTemp": float, "powerVariationByTemp": float}
    _defaults = {"capabilityVersusFrequency": 0.0, "heatRecoveryFlag": False, "timeConstant": 0.0, "auxPowerVersusFrequency": 0.0, "auxPowerVersusVoltage": 0.0, "referenceTemp": 0.0, "ambientTemp": 0.0, "powerVariationByTemp": 0.0}
    _enums = {}
    _refs = ["HeatRecoveryBoiler", "CTTempActivePowerCurve", "AirCompressor"]
    _many_refs = []

    def getHeatRecoveryBoiler(self):
        """A combustion turbine may have a heat recovery boiler for making steam
        """
        return self._HeatRecoveryBoiler

    def setHeatRecoveryBoiler(self, value):
        if self._HeatRecoveryBoiler is not None:
            filtered = [x for x in self.HeatRecoveryBoiler.CombustionTurbines if x != self]
            self._HeatRecoveryBoiler._CombustionTurbines = filtered

        self._HeatRecoveryBoiler = value
        if self._HeatRecoveryBoiler is not None:
            if self not in self._HeatRecoveryBoiler._CombustionTurbines:
                self._HeatRecoveryBoiler._CombustionTurbines.append(self)

    HeatRecoveryBoiler = property(getHeatRecoveryBoiler, setHeatRecoveryBoiler)

    def getCTTempActivePowerCurve(self):
        """A combustion turbine may have an active power versus ambient temperature relationship
        """
        return self._CTTempActivePowerCurve

    def setCTTempActivePowerCurve(self, value):
        if self._CTTempActivePowerCurve is not None:
            self._CTTempActivePowerCurve._CombustionTurbine = None

        self._CTTempActivePowerCurve = value
        if self._CTTempActivePowerCurve is not None:
            self._CTTempActivePowerCurve.CombustionTurbine = None
            self._CTTempActivePowerCurve._CombustionTurbine = self

    CTTempActivePowerCurve = property(getCTTempActivePowerCurve, setCTTempActivePowerCurve)

    def getAirCompressor(self):
        """A CAES air compressor is driven by combustion turbine
        """
        return self._AirCompressor

    def setAirCompressor(self, value):
        if self._AirCompressor is not None:
            self._AirCompressor._CombustionTurbine = None

        self._AirCompressor = value
        if self._AirCompressor is not None:
            self._AirCompressor.CombustionTurbine = None
            self._AirCompressor._CombustionTurbine = self

    AirCompressor = property(getAirCompressor, setAirCompressor)

