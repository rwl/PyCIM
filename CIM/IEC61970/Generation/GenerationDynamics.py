#------------------------------------------------------------------------------
# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

""" The Generation Dynamics package contains prime movers, such as turbines and boilers, which are needed for simulation and educational purposes.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61970.Core import PowerSystemResource
from CIM.IEC61970.Core import Curve
from CIM.IEC61970.Domain import Seconds
from CIM.IEC61970.Domain import PU
from CIM.IEC61970.Domain import RotationSpeed
from CIM.IEC61970.Domain import ActivePower
from CIM.IEC61970.Domain import Temperature



from enthought.traits.api import Instance, List, Property, Enum, Float, Int, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Boiler control mode.
BoilerControlMode = Enum("following", "coordinated", desc="Boiler control mode.")
# Type of turbine.
TurbineType = Enum("francis", "kaplan", "pelton", desc="Type of turbine.")

#------------------------------------------------------------------------------
#  "SteamSupply" class:
#------------------------------------------------------------------------------

class SteamSupply(PowerSystemResource):
    """ Steam supply for steam turbine
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Steam turbines may have steam supplied by a steam supply
    SteamTurbines = List(Instance("CIM.IEC61970.Generation.GenerationDynamics.SteamTurbine"),
        desc="Steam turbines may have steam supplied by a steam supply")

    # Rating of steam supply
    steamSupplyRating = Float(desc="Rating of steam supply")

    #--------------------------------------------------------------------------
    #  Begin "SteamSupply" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "steamSupplyRating",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "SteamTurbines",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Generation.GenerationDynamics.SteamSupply",
        title="SteamSupply",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SteamSupply" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PrimeMover" class:
#------------------------------------------------------------------------------

class PrimeMover(PowerSystemResource):
    """ The machine used to develop mechanical energy used to drive a generator.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Synchronous machines this Prime mover drives.
    SynchronousMachines = List(Instance("CIM.IEC61970.Wires.SynchronousMachine"),
        desc="Synchronous machines this Prime mover drives.")

    # Rating of prime mover
    primeMoverRating = Float(desc="Rating of prime mover")

    #--------------------------------------------------------------------------
    #  Begin "PrimeMover" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "primeMoverRating",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "SynchronousMachines",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Generation.GenerationDynamics.PrimeMover",
        title="PrimeMover",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PrimeMover" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CTTempActivePowerCurve" class:
#------------------------------------------------------------------------------

class CTTempActivePowerCurve(Curve):
    """ Relationship between the combustion turbine's power output rating in gross active power (X-axis) and the ambient air temperature (Y-axis)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A combustion turbine may have an active power versus ambient temperature relationship
    CombustionTurbine = Instance("CIM.IEC61970.Generation.GenerationDynamics.CombustionTurbine",
        desc="A combustion turbine may have an active power versus ambient temperature relationship",
        transient=True,
        opposite="CTTempActivePowerCurve",
        editor=InstanceEditor(name="_combustionturbines"))

    def _get_combustionturbines(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.GenerationDynamics.CombustionTurbine" ]
        else:
            return []

    _combustionturbines = Property(fget=_get_combustionturbines)

    #--------------------------------------------------------------------------
    #  Begin "CTTempActivePowerCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "CombustionTurbine",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.GenerationDynamics.CTTempActivePowerCurve",
        title="CTTempActivePowerCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CTTempActivePowerCurve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FossilSteamSupply" class:
#------------------------------------------------------------------------------

class FossilSteamSupply(SteamSupply):
    """ Fossil fueled boiler (e.g., coal, oil, gas)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The control mode of the boiler
    boilerControlMode = BoilerControlMode(desc="The control mode of the boiler")

    # Fuel Supply Time Constant
    fuelSupplyTC = Seconds(desc="Fuel Supply Time Constant")

    # Pressure Control Derivative Gain ratio
    pressureCtrlDG = Float(desc="Pressure Control Derivative Gain ratio")

    # Secondary Superheater Capacity
    superHeater2Capacity = Float(desc="Secondary Superheater Capacity")

    # Time Constant
    controlTC = Float(desc="Time Constant")

    # Active power Error Bias ratio
    controlErrorBiasP = Float(desc="Active power Error Bias ratio")

    # Pressure Control Proportional Gain ratio
    pressureCtrlPG = Float(desc="Pressure Control Proportional Gain ratio")

    # Pressure Control Integral Gain ratio
    pressureCtrlIG = Float(desc="Pressure Control Integral Gain ratio")

    # Feedwater Integral Gain ratio
    feedWaterIG = Float(desc="Feedwater Integral Gain ratio")

    # Drum/Primary Superheater Capacity
    superHeater1Capacity = Float(desc="Drum/Primary Superheater Capacity")

    # Mechanical Power Sensor Lag
    mechPowerSensorLag = Seconds(desc="Mechanical Power Sensor Lag")

    # Integral Constant
    controlIC = Float(desc="Integral Constant")

    # Proportional Constant
    controlPC = Float(desc="Proportional Constant")

    # Pressure Feedback Indicator
    pressureFeedback = Int(desc="Pressure Feedback Indicator")

    # Feedwater Proportional Gain ratio
    feedWaterPG = Float(desc="Feedwater Proportional Gain ratio")

    # Fuel Demand Limit
    fuelDemandLimit = PU(desc="Fuel Demand Limit")

    # Pressure Error Deadband
    controlPED = PU(desc="Pressure Error Deadband")

    # Off nominal frequency effect on auxiliary real power. Per unit active power variation versus per unit frequency variation.
    auxPowerVersusFrequency = PU(desc="Off nominal frequency effect on auxiliary real power. Per unit active power variation versus per unit frequency variation.")

    # Off nominal voltage effect on auxiliary real power. Per unit active power variation versus per unit voltage variation.
    auxPowerVersusVoltage = PU(desc="Off nominal voltage effect on auxiliary real power. Per unit active power variation versus per unit voltage variation.")

    # Active power Maximum Error Rate Limit
    maxErrorRateP = Float(desc="Active power Maximum Error Rate Limit")

    # Fuel Delay
    fuelSupplyDelay = Seconds(desc="Fuel Delay")

    # Superheater Pipe Pressure Drop Constant
    superHeaterPipePD = Float(desc="Superheater Pipe Pressure Drop Constant")

    # Pressure Error Bias ratio
    controlPEB = Float(desc="Pressure Error Bias ratio")

    # Feedwater Time Constant rato
    feedWaterTC = Seconds(desc="Feedwater Time Constant rato")

    # Throttle Pressure Setpoint
    throttlePressureSP = PU(desc="Throttle Pressure Setpoint")

    # Active power Minimum Error Rate Limit
    minErrorRateP = Float(desc="Active power Minimum Error Rate Limit")

    #--------------------------------------------------------------------------
    #  Begin "FossilSteamSupply" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "steamSupplyRating", "boilerControlMode", "fuelSupplyTC", "pressureCtrlDG", "superHeater2Capacity", "controlTC", "controlErrorBiasP", "pressureCtrlPG", "pressureCtrlIG", "feedWaterIG", "superHeater1Capacity", "mechPowerSensorLag", "controlIC", "controlPC", "pressureFeedback", "feedWaterPG", "fuelDemandLimit", "controlPED", "auxPowerVersusFrequency", "auxPowerVersusVoltage", "maxErrorRateP", "fuelSupplyDelay", "superHeaterPipePD", "controlPEB", "feedWaterTC", "throttlePressureSP", "minErrorRateP",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "SteamTurbines",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Generation.GenerationDynamics.FossilSteamSupply",
        title="FossilSteamSupply",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FossilSteamSupply" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "HeatRecoveryBoiler" class:
#------------------------------------------------------------------------------

class HeatRecoveryBoiler(FossilSteamSupply):
    """ The heat recovery system associated with combustion turbines in order to produce steam for combined cycle plants
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A combustion turbine may have a heat recovery boiler for making steam
    CombustionTurbines = List(Instance("CIM.IEC61970.Generation.GenerationDynamics.CombustionTurbine"),
        desc="A combustion turbine may have a heat recovery boiler for making steam")

    # The steam supply rating in kilopounds per hour, if dual pressure boiler
    steamSupplyRating2 = Float(desc="The steam supply rating in kilopounds per hour, if dual pressure boiler")

    #--------------------------------------------------------------------------
    #  Begin "HeatRecoveryBoiler" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "steamSupplyRating", "boilerControlMode", "fuelSupplyTC", "pressureCtrlDG", "superHeater2Capacity", "controlTC", "controlErrorBiasP", "pressureCtrlPG", "pressureCtrlIG", "feedWaterIG", "superHeater1Capacity", "mechPowerSensorLag", "controlIC", "controlPC", "pressureFeedback", "feedWaterPG", "fuelDemandLimit", "controlPED", "auxPowerVersusFrequency", "auxPowerVersusVoltage", "maxErrorRateP", "fuelSupplyDelay", "superHeaterPipePD", "controlPEB", "feedWaterTC", "throttlePressureSP", "minErrorRateP", "steamSupplyRating2",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "SteamTurbines", "CombustionTurbines",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Generation.GenerationDynamics.HeatRecoveryBoiler",
        title="HeatRecoveryBoiler",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HeatRecoveryBoiler" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "HydroTurbine" class:
#------------------------------------------------------------------------------

class HydroTurbine(PrimeMover):
    """ A water driven prime mover. Typical turbine types are: Francis, Kaplan, and Pelton.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Type of turbine.
    turbineType = TurbineType(desc="Type of turbine.")

    # Rated speed in number of revolutions.
    speedRating = RotationSpeed(desc="Rated speed in number of revolutions.")

    # Speed Regulation
    speedRegulation = PU(desc="Speed Regulation")

    # Rated turbine active power
    turbineRating = ActivePower(desc="Rated turbine active power")

    # Transient Droop Time Constant
    transientDroopTime = Seconds(desc="Transient Droop Time Constant")

    # Maximum efficiency active power at minimum head conditions
    minHeadMaxP = ActivePower(desc="Maximum efficiency active power at minimum head conditions")

    # Transient Regulation
    transientRegulation = PU(desc="Transient Regulation")

    # Gate Rate Limit
    gateRateLimit = Float(desc="Gate Rate Limit")

    # Maximum efficiency active power at maximum head conditions
    maxHeadMaxP = ActivePower(desc="Maximum efficiency active power at maximum head conditions")

    # Water Starting Time
    waterStartingTime = Seconds(desc="Water Starting Time")

    # Gate Upper Limit
    gateUpperLimit = PU(desc="Gate Upper Limit")

    #--------------------------------------------------------------------------
    #  Begin "HydroTurbine" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "primeMoverRating", "turbineType", "speedRating", "speedRegulation", "turbineRating", "transientDroopTime", "minHeadMaxP", "transientRegulation", "gateRateLimit", "maxHeadMaxP", "waterStartingTime", "gateUpperLimit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "SynchronousMachines",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Generation.GenerationDynamics.HydroTurbine",
        title="HydroTurbine",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HydroTurbine" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Subcritical" class:
#------------------------------------------------------------------------------

class Subcritical(FossilSteamSupply):
    """ Once-through subcritical boiler
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "Subcritical" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "steamSupplyRating", "boilerControlMode", "fuelSupplyTC", "pressureCtrlDG", "superHeater2Capacity", "controlTC", "controlErrorBiasP", "pressureCtrlPG", "pressureCtrlIG", "feedWaterIG", "superHeater1Capacity", "mechPowerSensorLag", "controlIC", "controlPC", "pressureFeedback", "feedWaterPG", "fuelDemandLimit", "controlPED", "auxPowerVersusFrequency", "auxPowerVersusVoltage", "maxErrorRateP", "fuelSupplyDelay", "superHeaterPipePD", "controlPEB", "feedWaterTC", "throttlePressureSP", "minErrorRateP",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "SteamTurbines",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Generation.GenerationDynamics.Subcritical",
        title="Subcritical",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Subcritical" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BWRSteamSupply" class:
#------------------------------------------------------------------------------

class BWRSteamSupply(SteamSupply):
    """ Boiling water reactor used as a steam supply to a steam turbine
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Proportional Gain
    proportionalGain = Float(desc="Proportional Gain")

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux3 = PU(desc="Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.")

    # Constant Associated With Rod Pattern
    rodPatternConstant = Float(desc="Constant Associated With Rod Pattern")

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux4 = PU(desc="Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.")

    # Pressure Setpoint Gain Adjuster
    pressureSetpointGA = Float(desc="Pressure Setpoint Gain Adjuster")

    # In-Core Thermal Time Constant
    inCoreThermalTC = Seconds(desc="In-Core Thermal Time Constant")

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux2 = PU(desc="Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.")

    # Pressure Limit
    pressureLimit = PU(desc="Pressure Limit")

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux1 = PU(desc="Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.")

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux7 = PU(desc="Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.")

    # High Power Limit
    highPowerLimit = PU(desc="High Power Limit")

    # Low Power Limit
    lowPowerLimit = PU(desc="Low Power Limit")

    # Initial Lower Limit
    lowerLimit = PU(desc="Initial Lower Limit")

    # Initial Upper Limit
    upperLimit = PU(desc="Initial Upper Limit")

    # Pressure Setpoint Time Constant
    pressureSetpointTC1 = Seconds(desc="Pressure Setpoint Time Constant")

    # Rod Pattern
    rodPattern = PU(desc="Rod Pattern")

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux8 = PU(desc="Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.")

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux5 = PU(desc="Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.")

    # Integral Gain
    integralGain = Float(desc="Integral Gain")

    # Pressure Setpoint Time Constant
    pressureSetpointTC2 = Seconds(desc="Pressure Setpoint Time Constant")

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux6 = PU(desc="Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.")

    #--------------------------------------------------------------------------
    #  Begin "BWRSteamSupply" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "steamSupplyRating", "proportionalGain", "rfAux3", "rodPatternConstant", "rfAux4", "pressureSetpointGA", "inCoreThermalTC", "rfAux2", "pressureLimit", "rfAux1", "rfAux7", "highPowerLimit", "lowPowerLimit", "lowerLimit", "upperLimit", "pressureSetpointTC1", "rodPattern", "rfAux8", "rfAux5", "integralGain", "pressureSetpointTC2", "rfAux6",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "SteamTurbines",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Generation.GenerationDynamics.BWRSteamSupply",
        title="BWRSteamSupply",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BWRSteamSupply" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DrumBoiler" class:
#------------------------------------------------------------------------------

class DrumBoiler(FossilSteamSupply):
    """ Drum boiler
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Rating of drum boiler in steam units
    drumBoilerRating = Float(desc="Rating of drum boiler in steam units")

    #--------------------------------------------------------------------------
    #  Begin "DrumBoiler" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "steamSupplyRating", "boilerControlMode", "fuelSupplyTC", "pressureCtrlDG", "superHeater2Capacity", "controlTC", "controlErrorBiasP", "pressureCtrlPG", "pressureCtrlIG", "feedWaterIG", "superHeater1Capacity", "mechPowerSensorLag", "controlIC", "controlPC", "pressureFeedback", "feedWaterPG", "fuelDemandLimit", "controlPED", "auxPowerVersusFrequency", "auxPowerVersusVoltage", "maxErrorRateP", "fuelSupplyDelay", "superHeaterPipePD", "controlPEB", "feedWaterTC", "throttlePressureSP", "minErrorRateP", "drumBoilerRating",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "SteamTurbines",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Generation.GenerationDynamics.DrumBoiler",
        title="DrumBoiler",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DrumBoiler" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CombustionTurbine" class:
#------------------------------------------------------------------------------

class CombustionTurbine(PrimeMover):
    """ A prime mover that is typically fueled by gas or light oil
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A combustion turbine may have a heat recovery boiler for making steam
    HeatRecoveryBoiler = Instance("CIM.IEC61970.Generation.GenerationDynamics.HeatRecoveryBoiler",
        desc="A combustion turbine may have a heat recovery boiler for making steam",
        transient=True,
        opposite="CombustionTurbines",
        editor=InstanceEditor(name="_heatrecoveryboilers"))

    def _get_heatrecoveryboilers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.GenerationDynamics.HeatRecoveryBoiler" ]
        else:
            return []

    _heatrecoveryboilers = Property(fget=_get_heatrecoveryboilers)

    # A combustion turbine may have an active power versus ambient temperature relationship
    CTTempActivePowerCurve = Instance("CIM.IEC61970.Generation.GenerationDynamics.CTTempActivePowerCurve",
        desc="A combustion turbine may have an active power versus ambient temperature relationship",
        transient=True,
        opposite="CombustionTurbine",
        editor=InstanceEditor(name="_cttempactivepowercurves"))

    def _get_cttempactivepowercurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.GenerationDynamics.CTTempActivePowerCurve" ]
        else:
            return []

    _cttempactivepowercurves = Property(fget=_get_cttempactivepowercurves)

    # A CAES air compressor is driven by combustion turbine
    AirCompressor = Instance("CIM.IEC61970.Generation.Production.AirCompressor",
        desc="A CAES air compressor is driven by combustion turbine",
        transient=True,
        opposite="CombustionTurbine",
        editor=InstanceEditor(name="_aircompressors"))

    def _get_aircompressors(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.AirCompressor" ]
        else:
            return []

    _aircompressors = Property(fget=_get_aircompressors)

    # Off-nominal voltage effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in auxiliary bus voltage (from a specified voltage level).
    auxPowerVersusVoltage = PU(desc="Off-nominal voltage effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in auxiliary bus voltage (from a specified voltage level).")

    # Default ambient temperature to be used in modeling applications
    ambientTemp = Temperature(desc="Default ambient temperature to be used in modeling applications")

    # Flag that is set to true if the combustion turbine is associated with a heat recovery boiler
    heatRecoveryFlag = Bool(desc="Flag that is set to true if the combustion turbine is associated with a heat recovery boiler")

    # Off-nominal frequency effect on turbine capability. Per unit reduction in unit active power capability versus per unit reduction in frequency (from rated frequency).
    capabilityVersusFrequency = PU(desc="Off-nominal frequency effect on turbine capability. Per unit reduction in unit active power capability versus per unit reduction in frequency (from rated frequency).")

    # Per unit change in power per (versus) unit change in ambient temperature
    powerVariationByTemp = PU(desc="Per unit change in power per (versus) unit change in ambient temperature")

    # Reference temperature at which the output of the turbine was defined.
    referenceTemp = Temperature(desc="Reference temperature at which the output of the turbine was defined.")

    # The time constant for the turbine.
    timeConstant = Seconds(desc="The time constant for the turbine.")

    # Off-nominal frequency effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in frequency (from rated frequency).
    auxPowerVersusFrequency = PU(desc="Off-nominal frequency effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in frequency (from rated frequency).")

    #--------------------------------------------------------------------------
    #  Begin "CombustionTurbine" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "primeMoverRating", "auxPowerVersusVoltage", "ambientTemp", "heatRecoveryFlag", "capabilityVersusFrequency", "powerVariationByTemp", "referenceTemp", "timeConstant", "auxPowerVersusFrequency",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "SynchronousMachines", "HeatRecoveryBoiler", "CTTempActivePowerCurve", "AirCompressor",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Generation.GenerationDynamics.CombustionTurbine",
        title="CombustionTurbine",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CombustionTurbine" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Supercritical" class:
#------------------------------------------------------------------------------

class Supercritical(FossilSteamSupply):
    """ Once-through supercritical boiler
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "Supercritical" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "steamSupplyRating", "boilerControlMode", "fuelSupplyTC", "pressureCtrlDG", "superHeater2Capacity", "controlTC", "controlErrorBiasP", "pressureCtrlPG", "pressureCtrlIG", "feedWaterIG", "superHeater1Capacity", "mechPowerSensorLag", "controlIC", "controlPC", "pressureFeedback", "feedWaterPG", "fuelDemandLimit", "controlPED", "auxPowerVersusFrequency", "auxPowerVersusVoltage", "maxErrorRateP", "fuelSupplyDelay", "superHeaterPipePD", "controlPEB", "feedWaterTC", "throttlePressureSP", "minErrorRateP",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "SteamTurbines",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Generation.GenerationDynamics.Supercritical",
        title="Supercritical",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Supercritical" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PWRSteamSupply" class:
#------------------------------------------------------------------------------

class PWRSteamSupply(SteamSupply):
    """ Pressurized water reactor used as a steam supply to a steam turbine
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Core Heat Transfer Lag Time Constant
    coreHTLagTC1 = PU(desc="Core Heat Transfer Lag Time Constant")

    # Hot Leg Steam Gain
    hotLegSteamGain = PU(desc="Hot Leg Steam Gain")

    # Cold Leg Lag Time Constant
    coldLegLagTC = PU(desc="Cold Leg Lag Time Constant")

    # Core Neutronics Effective Time Constant
    coreNeutronicsEffTC = PU(desc="Core Neutronics Effective Time Constant")

    # Steam Flow Feedback Gain
    steamFlowFG = PU(desc="Steam Flow Feedback Gain")

    # Throttle Pressure Factor
    throttlePressureFactor = PU(desc="Throttle Pressure Factor")

    # Hot Leg To Cold Leg Gain
    hotLegToColdLegGain = PU(desc="Hot Leg To Cold Leg Gain")

    # Throttle Pressure Setpoint
    throttlePressureSP = PU(desc="Throttle Pressure Setpoint")

    # Steam Pressure Drop Lag Time Constant
    steamPressureDropLagTC = PU(desc="Steam Pressure Drop Lag Time Constant")

    # Core Heat Transfer Lag Time Constant
    coreHTLagTC2 = PU(desc="Core Heat Transfer Lag Time Constant")

    # Cold Leg Feedback Gain 1
    coldLegFG1 = PU(desc="Cold Leg Feedback Gain 1")

    # Cold Leg Feedback Lag Time Constant
    coldLegFBLagTC = PU(desc="Cold Leg Feedback Lag Time Constant")

    # Hot Leg Lag Time Constant
    hotLegLagTC = PU(desc="Hot Leg Lag Time Constant")

    # Cold Leg Feedback Lead Time Constant
    coldLegFBLeadTC2 = PU(desc="Cold Leg Feedback Lead Time Constant")

    # Pressure Control Gain
    pressureCG = PU(desc="Pressure Control Gain")

    # Cold Leg Feedback Lead Time Constant
    coldLegFBLeadTC1 = PU(desc="Cold Leg Feedback Lead Time Constant")

    # Cold Leg Feedback Gain 2
    coldLegFG2 = PU(desc="Cold Leg Feedback Gain 2")

    # Core Neutronics And Heat Transfer
    coreNeutronicsHT = PU(desc="Core Neutronics And Heat Transfer")

    # Steam Pressure Feedback Gain
    steamPressureFG = PU(desc="Steam Pressure Feedback Gain")

    # Feedback Factor
    feedbackFactor = PU(desc="Feedback Factor")

    #--------------------------------------------------------------------------
    #  Begin "PWRSteamSupply" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "steamSupplyRating", "coreHTLagTC1", "hotLegSteamGain", "coldLegLagTC", "coreNeutronicsEffTC", "steamFlowFG", "throttlePressureFactor", "hotLegToColdLegGain", "throttlePressureSP", "steamPressureDropLagTC", "coreHTLagTC2", "coldLegFG1", "coldLegFBLagTC", "hotLegLagTC", "coldLegFBLeadTC2", "pressureCG", "coldLegFBLeadTC1", "coldLegFG2", "coreNeutronicsHT", "steamPressureFG", "feedbackFactor",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "SteamTurbines",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Generation.GenerationDynamics.PWRSteamSupply",
        title="PWRSteamSupply",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PWRSteamSupply" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SteamTurbine" class:
#------------------------------------------------------------------------------

class SteamTurbine(PrimeMover):
    """ Steam turbine
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Steam turbines may have steam supplied by a steam supply
    SteamSupplys = List(Instance("CIM.IEC61970.Generation.GenerationDynamics.SteamSupply"),
        desc="Steam turbines may have steam supplied by a steam supply")

    # Crossover Time Constant
    crossoverTC = Seconds(desc="Crossover Time Constant")

    # Fraction Of Power From Shaft 2 First Low Pressure Turbine output
    shaft2PowerLP1 = Float(desc="Fraction Of Power From Shaft 2 First Low Pressure Turbine output")

    # Fraction Of Power From Shaft 1 Intermediate Pressure Turbine output
    shaft1PowerIP = Float(desc="Fraction Of Power From Shaft 1 Intermediate Pressure Turbine output")

    # Fraction Of Power From Shaft 2 Intermediate Pressure Turbine output
    shaft2PowerIP = Float(desc="Fraction Of Power From Shaft 2 Intermediate Pressure Turbine output")

    # First Reheater Time Constant
    reheater1TC = Seconds(desc="First Reheater Time Constant")

    # Fraction Of Power From Shaft 2 Second Low Pressure Turbine output
    shaft2PowerLP2 = Float(desc="Fraction Of Power From Shaft 2 Second Low Pressure Turbine output")

    # Steam Chest Time Constant
    steamChestTC = Seconds(desc="Steam Chest Time Constant")

    # Fraction Of Power From Shaft 1 High Pressure Turbine output
    shaft1PowerHP = Float(desc="Fraction Of Power From Shaft 1 High Pressure Turbine output")

    # Fraction Of Power From Shaft 1 Second Low Pressure Turbine output
    shaft1PowerLP2 = Float(desc="Fraction Of Power From Shaft 1 Second Low Pressure Turbine output")

    # Fraction Of Power From Shaft 2 High Pressure Turbine output
    shaft2PowerHP = Float(desc="Fraction Of Power From Shaft 2 High Pressure Turbine output")

    # Second Reheater Time Constant
    reheater2TC = Seconds(desc="Second Reheater Time Constant")

    # Fraction Of Power From Shaft 1 First Low Pressure Turbine output
    shaft1PowerLP1 = Float(desc="Fraction Of Power From Shaft 1 First Low Pressure Turbine output")

    #--------------------------------------------------------------------------
    #  Begin "SteamTurbine" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "primeMoverRating", "crossoverTC", "shaft2PowerLP1", "shaft1PowerIP", "shaft2PowerIP", "reheater1TC", "shaft2PowerLP2", "steamChestTC", "shaft1PowerHP", "shaft1PowerLP2", "shaft2PowerHP", "reheater2TC", "shaft1PowerLP1",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "SynchronousMachines", "SteamSupplys",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Generation.GenerationDynamics.SteamTurbine",
        title="SteamTurbine",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SteamTurbine" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
