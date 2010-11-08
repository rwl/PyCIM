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
            self._AirCompressor._CombustionTurbine = self

    AirCompressor = property(getAirCompressor, setAirCompressor)

