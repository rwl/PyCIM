#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM13r19.Core import Curve
from CIM13r19.Core import PowerSystemResource



from enthought.traits.api import Instance, List, Property, Enum, Float, Bool, Int
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


BoilerControlMode = Enum("coordinated", "following")

TurbineType = Enum("pelton", "francis", "kaplan")

#------------------------------------------------------------------------------
#  "CTTempActivePowerCurve" class:
#------------------------------------------------------------------------------

class CTTempActivePowerCurve(Curve):
    """ Relationship between the combustion turbine's power output rating in gross active power (X-axis) and the ambient air temperature (Y-axis)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A combustion turbine may have a active power versus ambient temperature relationship
    CombustionTurbine = Instance("CIM13r19.Generation.GenerationDynamics.CombustionTurbine",
        desc="A combustion turbine may have a active power versus ambient temperature relationship",
        transient=True,
        opposite="CTTempActivePowerCurve",
        editor=InstanceEditor(name="_combustionturbines"))

    def _get_combustionturbines(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Generation.GenerationDynamics.CombustionTurbine" ]
        else:
            return []

    _combustionturbines = Property(fget=_get_combustionturbines)

    #--------------------------------------------------------------------------
    #  Begin "CTTempActivePowerCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "CombustionTurbine",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.GenerationDynamics.CTTempActivePowerCurve",
        title="CTTempActivePowerCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CTTempActivePowerCurve" user definitions:
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

    Drives_SynchronousMachines = List(Instance("CIM13r19.Wires.SynchronousMachine"))

    # Rating of prime mover
    primeMoverRating = Float(desc="Rating of prime mover")

    #--------------------------------------------------------------------------
    #  Begin "PrimeMover" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "primeMoverRating",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "Drives_SynchronousMachines",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.GenerationDynamics.PrimeMover",
        title="PrimeMover",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PrimeMover" user definitions:
    #--------------------------------------------------------------------------

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
    SteamTurbines = List(Instance("CIM13r19.Generation.GenerationDynamics.SteamTurbine"),
        desc="Steam turbines may have steam supplied by a steam supply")

    # Rating of steam supply
    steamSupplyRating = Float(desc="Rating of steam supply")

    #--------------------------------------------------------------------------
    #  Begin "SteamSupply" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "steamSupplyRating",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "SteamTurbines",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.GenerationDynamics.SteamSupply",
        title="SteamSupply",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SteamSupply" user definitions:
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
    SteamSupplys = List(Instance("CIM13r19.Generation.GenerationDynamics.SteamSupply"),
        desc="Steam turbines may have steam supplied by a steam supply")

    # Fraction Of Power From Shaft 2 Intermediate Pressure Turbine output
    shaft2PowerIP = Float(desc="Fraction Of Power From Shaft 2 Intermediate Pressure Turbine output")

    # Fraction Of Power From Shaft 2 First Low Pressure Turbine output
    shaft2PowerLP1 = Float(desc="Fraction Of Power From Shaft 2 First Low Pressure Turbine output")

    # Fraction Of Power From Shaft 2 Second Low Pressure Turbine output
    shaft2PowerLP2 = Float(desc="Fraction Of Power From Shaft 2 Second Low Pressure Turbine output")

    # Fraction Of Power From Shaft 2 High Pressure Turbine output
    shaft2PowerHP = Float(desc="Fraction Of Power From Shaft 2 High Pressure Turbine output")

    # Second Reheater Time Constant
    reheater2TC = Float(desc="Second Reheater Time Constant")

    # Fraction Of Power From Shaft 1 Intermediate Pressure Turbine output
    shaft1PowerIP = Float(desc="Fraction Of Power From Shaft 1 Intermediate Pressure Turbine output")

    # Steam Chest Time Constant
    steamChestTC = Float(desc="Steam Chest Time Constant")

    # Fraction Of Power From Shaft 1 First Low Pressure Turbine output
    shaft1PowerLP1 = Float(desc="Fraction Of Power From Shaft 1 First Low Pressure Turbine output")

    # Crossover Time Constant
    crossoverTC = Float(desc="Crossover Time Constant")

    # First Reheater Time Constant
    reheater1TC = Float(desc="First Reheater Time Constant")

    # Fraction Of Power From Shaft 1 High Pressure Turbine output
    shaft1PowerHP = Float(desc="Fraction Of Power From Shaft 1 High Pressure Turbine output")

    # Fraction Of Power From Shaft 1 Second Low Pressure Turbine output
    shaft1PowerLP2 = Float(desc="Fraction Of Power From Shaft 1 Second Low Pressure Turbine output")

    #--------------------------------------------------------------------------
    #  Begin "SteamTurbine" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "primeMoverRating", "shaft2PowerIP", "shaft2PowerLP1", "shaft2PowerLP2", "shaft2PowerHP", "reheater2TC", "shaft1PowerIP", "steamChestTC", "shaft1PowerLP1", "crossoverTC", "reheater1TC", "shaft1PowerHP", "shaft1PowerLP2",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "Drives_SynchronousMachines", "SteamSupplys",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Generation.GenerationDynamics.SteamTurbine",
        title="SteamTurbine",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SteamTurbine" user definitions:
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

    # Cold Leg Feedback Gain 2
    coldLegFG2 = Float(desc="Cold Leg Feedback Gain 2")

    # Steam Pressure Drop Lag Time Constant
    steamPressureDropLagTC = Float(desc="Steam Pressure Drop Lag Time Constant")

    # Cold Leg Feedback Lead Time Constant
    coldLegFBLeadTC2 = Float(desc="Cold Leg Feedback Lead Time Constant")

    # Cold Leg Feedback Lag Time Constant
    coldLegFBLagTC = Float(desc="Cold Leg Feedback Lag Time Constant")

    # Hot Leg To Cold Leg Gain
    hotLegToColdLegGain = Float(desc="Hot Leg To Cold Leg Gain")

    # Feedback Factor
    feedbackFactor = Float(desc="Feedback Factor")

    # Core Neutronics And Heat Transfer
    coreNeutronicsHT = Float(desc="Core Neutronics And Heat Transfer")

    # Throttle Pressure Factor
    throttlePressureFactor = Float(desc="Throttle Pressure Factor")

    # Core Heat Transfer Lag Time Constant
    coreHTLagTC1 = Float(desc="Core Heat Transfer Lag Time Constant")

    # Throttle Pressure Setpoint
    throttlePressureSP = Float(desc="Throttle Pressure Setpoint")

    # Core Neutronics Effective Time Constant
    coreNeutronicsEffTC = Float(desc="Core Neutronics Effective Time Constant")

    # Cold Leg Feedback Gain 1
    coldLegFG1 = Float(desc="Cold Leg Feedback Gain 1")

    # Steam Pressure Feedback Gain
    steamPressureFG = Float(desc="Steam Pressure Feedback Gain")

    # Hot Leg Steam Gain
    hotLegSteamGain = Float(desc="Hot Leg Steam Gain")

    # Core Heat Transfer Lag Time Constant
    coreHTLagTC2 = Float(desc="Core Heat Transfer Lag Time Constant")

    # Cold Leg Lag Time Constant
    coldLegLagTC = Float(desc="Cold Leg Lag Time Constant")

    # Pressure Control Gain
    pressureCG = Float(desc="Pressure Control Gain")

    # Cold Leg Feedback Lead Time Constant
    coldLegFBLeadTC1 = Float(desc="Cold Leg Feedback Lead Time Constant")

    # Steam Flow Feedback Gain
    steamFlowFG = Float(desc="Steam Flow Feedback Gain")

    # Hot Leg Lag Time Constant
    hotLegLagTC = Float(desc="Hot Leg Lag Time Constant")

    #--------------------------------------------------------------------------
    #  Begin "PWRSteamSupply" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "steamSupplyRating", "coldLegFG2", "steamPressureDropLagTC", "coldLegFBLeadTC2", "coldLegFBLagTC", "hotLegToColdLegGain", "feedbackFactor", "coreNeutronicsHT", "throttlePressureFactor", "coreHTLagTC1", "throttlePressureSP", "coreNeutronicsEffTC", "coldLegFG1", "steamPressureFG", "hotLegSteamGain", "coreHTLagTC2", "coldLegLagTC", "pressureCG", "coldLegFBLeadTC1", "steamFlowFG", "hotLegLagTC",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "SteamTurbines",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.GenerationDynamics.PWRSteamSupply",
        title="PWRSteamSupply",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PWRSteamSupply" user definitions:
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

    # A CAES air compressor is driven by combustion turbine
    Drives_AirCompressor = Instance("CIM13r19.Generation.Production.AirCompressor",
        desc="A CAES air compressor is driven by combustion turbine",
        transient=True,
        opposite="DrivenBy_CombustionTurbine",
        editor=InstanceEditor(name="_aircompressors"))

    def _get_aircompressors(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Generation.Production.AirCompressor" ]
        else:
            return []

    _aircompressors = Property(fget=_get_aircompressors)

    # A combustion turbine may have a active power versus ambient temperature relationship
    CTTempActivePowerCurve = Instance("CIM13r19.Generation.GenerationDynamics.CTTempActivePowerCurve",
        desc="A combustion turbine may have a active power versus ambient temperature relationship",
        transient=True,
        opposite="CombustionTurbine",
        editor=InstanceEditor(name="_cttempactivepowercurves"))

    def _get_cttempactivepowercurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Generation.GenerationDynamics.CTTempActivePowerCurve" ]
        else:
            return []

    _cttempactivepowercurves = Property(fget=_get_cttempactivepowercurves)

    # A combustion turbine may have a heat recovery boiler for making steam
    HeatRecoveryBoiler = Instance("CIM13r19.Generation.GenerationDynamics.HeatRecoveryBoiler",
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
                    "CIM13r19.Generation.GenerationDynamics.HeatRecoveryBoiler" ]
        else:
            return []

    _heatrecoveryboilers = Property(fget=_get_heatrecoveryboilers)

    # Reference temperature at which the output of the turbine was defined.
    referenceTemp = Float(desc="Reference temperature at which the output of the turbine was defined.")

    # Per unit change in power per (versus) unit change in ambient temperature
    powerVariationByTemp = Float(desc="Per unit change in power per (versus) unit change in ambient temperature")

    # Flag that is set to true if the combustion turbine is associated with a heat recovery boiler
    heatRecoveryFlag = Bool(desc="Flag that is set to true if the combustion turbine is associated with a heat recovery boiler")

    # Off-nominal voltage effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in auxiliary bus voltage (from a specified voltage level).
    auxPowerVersusVoltage = Float(desc="Off-nominal voltage effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in auxiliary bus voltage (from a specified voltage level).")

    # Default ambient temperature to be used in modeling applications
    ambientTemp = Float(desc="Default ambient temperature to be used in modeling applications")

    # The time constant for the turbine.
    timeConstant = Float(desc="The time constant for the turbine.")

    # Off-nominal frequency effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in frequency (from rated frequency).
    auxPowerVersusFrequency = Float(desc="Off-nominal frequency effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in frequency (from rated frequency).")

    # Off-nominal frequency effect on turbine capability. Per unit reduction in unit active power capability versus per unit reduction in frequency (from rated frequency).
    capabilityVersusFrequency = Float(desc="Off-nominal frequency effect on turbine capability. Per unit reduction in unit active power capability versus per unit reduction in frequency (from rated frequency).")

    #--------------------------------------------------------------------------
    #  Begin "CombustionTurbine" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "primeMoverRating", "referenceTemp", "powerVariationByTemp", "heatRecoveryFlag", "auxPowerVersusVoltage", "ambientTemp", "timeConstant", "auxPowerVersusFrequency", "capabilityVersusFrequency",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "Drives_SynchronousMachines", "Drives_AirCompressor", "CTTempActivePowerCurve", "HeatRecoveryBoiler",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Generation.GenerationDynamics.CombustionTurbine",
        title="CombustionTurbine",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CombustionTurbine" user definitions:
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

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux2 = Float(desc="Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.")

    # Initial Lower Limit
    lowerLimit = Float(desc="Initial Lower Limit")

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux6 = Float(desc="Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.")

    # Pressure Limit
    pressureLimit = Float(desc="Pressure Limit")

    # Initial Upper Limit
    upperLimit = Float(desc="Initial Upper Limit")

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux3 = Float(desc="Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.")

    # Rod Pattern
    rodPattern = Float(desc="Rod Pattern")

    # Proportional Gain
    proportionalGain = Float(desc="Proportional Gain")

    # In-Core Thermal Time Constant
    inCoreThermalTC = Float(desc="In-Core Thermal Time Constant")

    # High Power Limit
    highPowerLimit = Float(desc="High Power Limit")

    # Constant Associated With Rod Pattern
    rodPatternConstant = Float(desc="Constant Associated With Rod Pattern")

    # Low Power Limit
    lowPowerLimit = Float(desc="Low Power Limit")

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux7 = Float(desc="Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.")

    # Pressure Setpoint Time Constant
    pressureSetpointTC1 = Float(desc="Pressure Setpoint Time Constant")

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux4 = Float(desc="Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.")

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux1 = Float(desc="Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.")

    # Integral Gain
    integralGain = Float(desc="Integral Gain")

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux8 = Float(desc="Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.")

    # Pressure Setpoint Gain Adjuster
    pressureSetpointGA = Float(desc="Pressure Setpoint Gain Adjuster")

    # Pressure Setpoint Time Constant
    pressureSetpointTC2 = Float(desc="Pressure Setpoint Time Constant")

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux5 = Float(desc="Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.")

    #--------------------------------------------------------------------------
    #  Begin "BWRSteamSupply" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "steamSupplyRating", "rfAux2", "lowerLimit", "rfAux6", "pressureLimit", "upperLimit", "rfAux3", "rodPattern", "proportionalGain", "inCoreThermalTC", "highPowerLimit", "rodPatternConstant", "lowPowerLimit", "rfAux7", "pressureSetpointTC1", "rfAux4", "rfAux1", "integralGain", "rfAux8", "pressureSetpointGA", "pressureSetpointTC2", "rfAux5",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "SteamTurbines",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.GenerationDynamics.BWRSteamSupply",
        title="BWRSteamSupply",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BWRSteamSupply" user definitions:
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

    # Maximum efficiency active power at minimum head conditions
    minHeadMaxP = Float(desc="Maximum efficiency active power at minimum head conditions")

    # Gate Rate Limit
    gateRateLimit = Float(desc="Gate Rate Limit")

    # Speed Regulation
    speedRegulation = Float(desc="Speed Regulation")

    # Transient Regulation
    transientRegulation = Float(desc="Transient Regulation")

    # Transient Droop Time Constant
    transientDroopTime = Float(desc="Transient Droop Time Constant")

    # Maximum efficiency active power at maximum head conditions
    maxHeadMaxP = Float(desc="Maximum efficiency active power at maximum head conditions")

    # Rated turbine active power
    turbineRating = Float(desc="Rated turbine active power")

    # Water Starting Time
    waterStartingTime = Float(desc="Water Starting Time")

    # Type of turbine.
    turbineType = TurbineType(desc="Type of turbine.")

    # Gate Upper Limit
    gateUpperLimit = Float(desc="Gate Upper Limit")

    # Rated speed in number of revolutions.
    speedRating = Float(desc="Rated speed in number of revolutions.")

    #--------------------------------------------------------------------------
    #  Begin "HydroTurbine" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "primeMoverRating", "minHeadMaxP", "gateRateLimit", "speedRegulation", "transientRegulation", "transientDroopTime", "maxHeadMaxP", "turbineRating", "waterStartingTime", "turbineType", "gateUpperLimit", "speedRating",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "Drives_SynchronousMachines",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.GenerationDynamics.HydroTurbine",
        title="HydroTurbine",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HydroTurbine" user definitions:
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

    # Superheater Pipe Pressure Drop Constant
    superHeaterPipePD = Float(desc="Superheater Pipe Pressure Drop Constant")

    # Active power Maximum Error Rate Limit
    maxErrorRateP = Float(desc="Active power Maximum Error Rate Limit")

    # Off nominal voltage effect on auxiliary real power. Per unit active power variation versus per unit voltage variation.
    auxPowerversusVoltage = Float(desc="Off nominal voltage effect on auxiliary real power. Per unit active power variation versus per unit voltage variation.")

    # Pressure Control Proportional Gain ratio
    pressureCtrlPG = Float(desc="Pressure Control Proportional Gain ratio")

    # Secondary Superheater Capacity
    superHeater2Capacity = Float(desc="Secondary Superheater Capacity")

    # The control mode of the boiler
    boilerControlMode = BoilerControlMode(desc="The control mode of the boiler")

    # Mechanical Power Sensor Lag
    mechPowerSensorLag = Float(desc="Mechanical Power Sensor Lag")

    # Pressure Error Bias ratio
    controlPEB = Float(desc="Pressure Error Bias ratio")

    # Fuel Demand Limit
    fuelDemandLimit = Float(desc="Fuel Demand Limit")

    # Proportional Constant
    controlPC = Float(desc="Proportional Constant")

    # Pressure Feedback Indicator
    pressureFeedback = Int(desc="Pressure Feedback Indicator")

    # Off nominal frequency effect on auxiliary real power. Per unit active power variation versus per unit frequency variation.
    auxPowerVersusFrequency = Float(desc="Off nominal frequency effect on auxiliary real power. Per unit active power variation versus per unit frequency variation.")

    # Feedwater Integral Gain ratio
    feedWaterIG = Float(desc="Feedwater Integral Gain ratio")

    # Time Constant
    controlTC = Float(desc="Time Constant")

    # Active power Error Bias ratio
    controlErrorBiasP = Float(desc="Active power Error Bias ratio")

    # Feedwater Time Constant rato
    feedWaterTC = Float(desc="Feedwater Time Constant rato")

    # Feedwater Proportional Gain ratio
    feedWaterPG = Float(desc="Feedwater Proportional Gain ratio")

    # Fuel Delay
    fuelSupplyDelay = Float(desc="Fuel Delay")

    # Pressure Control Derivative Gain ratio
    pressureCtrlDG = Float(desc="Pressure Control Derivative Gain ratio")

    # Pressure Control Integral Gain ratio
    pressureCtrlIG = Float(desc="Pressure Control Integral Gain ratio")

    # Fuel Supply Time Constant
    fuelSupplyTC = Float(desc="Fuel Supply Time Constant")

    # Integral Constant
    controlIC = Float(desc="Integral Constant")

    # Throttle Pressure Setpoint
    throttlePressureSP = Float(desc="Throttle Pressure Setpoint")

    # Drum/Primary Superheater Capacity
    superHeater1Capacity = Float(desc="Drum/Primary Superheater Capacity")

    # Pressure Error Deadband
    controlPED = Float(desc="Pressure Error Deadband")

    # Active power Minimum Error Rate Limit
    minErrorRateP = Float(desc="Active power Minimum Error Rate Limit")

    #--------------------------------------------------------------------------
    #  Begin "FossilSteamSupply" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "steamSupplyRating", "superHeaterPipePD", "maxErrorRateP", "auxPowerversusVoltage", "pressureCtrlPG", "superHeater2Capacity", "boilerControlMode", "mechPowerSensorLag", "controlPEB", "fuelDemandLimit", "controlPC", "pressureFeedback", "auxPowerVersusFrequency", "feedWaterIG", "controlTC", "controlErrorBiasP", "feedWaterTC", "feedWaterPG", "fuelSupplyDelay", "pressureCtrlDG", "pressureCtrlIG", "fuelSupplyTC", "controlIC", "throttlePressureSP", "superHeater1Capacity", "controlPED", "minErrorRateP",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "SteamTurbines",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.GenerationDynamics.FossilSteamSupply",
        title="FossilSteamSupply",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FossilSteamSupply" user definitions:
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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "steamSupplyRating", "superHeaterPipePD", "maxErrorRateP", "auxPowerversusVoltage", "pressureCtrlPG", "superHeater2Capacity", "boilerControlMode", "mechPowerSensorLag", "controlPEB", "fuelDemandLimit", "controlPC", "pressureFeedback", "auxPowerVersusFrequency", "feedWaterIG", "controlTC", "controlErrorBiasP", "feedWaterTC", "feedWaterPG", "fuelSupplyDelay", "pressureCtrlDG", "pressureCtrlIG", "fuelSupplyTC", "controlIC", "throttlePressureSP", "superHeater1Capacity", "controlPED", "minErrorRateP",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "SteamTurbines",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.GenerationDynamics.Subcritical",
        title="Subcritical",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Subcritical" user definitions:
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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "steamSupplyRating", "superHeaterPipePD", "maxErrorRateP", "auxPowerversusVoltage", "pressureCtrlPG", "superHeater2Capacity", "boilerControlMode", "mechPowerSensorLag", "controlPEB", "fuelDemandLimit", "controlPC", "pressureFeedback", "auxPowerVersusFrequency", "feedWaterIG", "controlTC", "controlErrorBiasP", "feedWaterTC", "feedWaterPG", "fuelSupplyDelay", "pressureCtrlDG", "pressureCtrlIG", "fuelSupplyTC", "controlIC", "throttlePressureSP", "superHeater1Capacity", "controlPED", "minErrorRateP",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "SteamTurbines",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.GenerationDynamics.Supercritical",
        title="Supercritical",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Supercritical" user definitions:
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
    CombustionTurbines = List(Instance("CIM13r19.Generation.GenerationDynamics.CombustionTurbine"),
        desc="A combustion turbine may have a heat recovery boiler for making steam")

    # The steam supply rating in kilopounds per hour, if dual pressure boiler
    steamSupplyRating2 = Float(desc="The steam supply rating in kilopounds per hour, if dual pressure boiler")

    #--------------------------------------------------------------------------
    #  Begin "HeatRecoveryBoiler" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "steamSupplyRating", "superHeaterPipePD", "maxErrorRateP", "auxPowerversusVoltage", "pressureCtrlPG", "superHeater2Capacity", "boilerControlMode", "mechPowerSensorLag", "controlPEB", "fuelDemandLimit", "controlPC", "pressureFeedback", "auxPowerVersusFrequency", "feedWaterIG", "controlTC", "controlErrorBiasP", "feedWaterTC", "feedWaterPG", "fuelSupplyDelay", "pressureCtrlDG", "pressureCtrlIG", "fuelSupplyTC", "controlIC", "throttlePressureSP", "superHeater1Capacity", "controlPED", "minErrorRateP", "steamSupplyRating2",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "SteamTurbines", "CombustionTurbines",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Generation.GenerationDynamics.HeatRecoveryBoiler",
        title="HeatRecoveryBoiler",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HeatRecoveryBoiler" user definitions:
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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "steamSupplyRating", "superHeaterPipePD", "maxErrorRateP", "auxPowerversusVoltage", "pressureCtrlPG", "superHeater2Capacity", "boilerControlMode", "mechPowerSensorLag", "controlPEB", "fuelDemandLimit", "controlPC", "pressureFeedback", "auxPowerVersusFrequency", "feedWaterIG", "controlTC", "controlErrorBiasP", "feedWaterTC", "feedWaterPG", "fuelSupplyDelay", "pressureCtrlDG", "pressureCtrlIG", "fuelSupplyTC", "controlIC", "throttlePressureSP", "superHeater1Capacity", "controlPED", "minErrorRateP", "drumBoilerRating",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "SteamTurbines",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.GenerationDynamics.DrumBoiler",
        title="DrumBoiler",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DrumBoiler" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
