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

from CIM13.Core import Curve
from CIM13.Core import PowerSystemResource



from enthought.traits.api import Instance, List, Enum, Float, Bool, Int
# <<< imports

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
    CombustionTurbine = Instance("CIM13.Generation.GenerationDynamics.CombustionTurbine")

    #--------------------------------------------------------------------------
    #  Begin cTTempActivePowerCurve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End cTTempActivePowerCurve user definitions:
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

    Drives_SynchronousMachines = List(Instance("CIM13.Wires.SynchronousMachine"))

    # Rating of prime mover
    primeMoverRating = EFloat

    #--------------------------------------------------------------------------
    #  Begin primeMover user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End primeMover user definitions:
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
    SteamTurbines = List(Instance("CIM13.Generation.GenerationDynamics.SteamTurbine"))

    # Rating of steam supply
    steamSupplyRating = EFloat

    #--------------------------------------------------------------------------
    #  Begin steamSupply user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End steamSupply user definitions:
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
    SteamSupplys = List(Instance("CIM13.Generation.GenerationDynamics.SteamSupply"))

    # Fraction Of Power From Shaft 2 Intermediate Pressure Turbine output
    shaft2PowerIP = EFloat

    # Fraction Of Power From Shaft 2 First Low Pressure Turbine output
    shaft2PowerLP1 = EFloat

    # Fraction Of Power From Shaft 2 Second Low Pressure Turbine output
    shaft2PowerLP2 = EFloat

    # Fraction Of Power From Shaft 2 High Pressure Turbine output
    shaft2PowerHP = EFloat

    # Second Reheater Time Constant
    reheater2TC = EFloat

    # Fraction Of Power From Shaft 1 Intermediate Pressure Turbine output
    shaft1PowerIP = EFloat

    # Steam Chest Time Constant
    steamChestTC = EFloat

    # Fraction Of Power From Shaft 1 First Low Pressure Turbine output
    shaft1PowerLP1 = EFloat

    # Crossover Time Constant
    crossoverTC = EFloat

    # First Reheater Time Constant
    reheater1TC = EFloat

    # Fraction Of Power From Shaft 1 High Pressure Turbine output
    shaft1PowerHP = EFloat

    # Fraction Of Power From Shaft 1 Second Low Pressure Turbine output
    shaft1PowerLP2 = EFloat

    #--------------------------------------------------------------------------
    #  Begin steamTurbine user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End steamTurbine user definitions:
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
    coldLegFG2 = EFloat

    # Steam Pressure Drop Lag Time Constant
    steamPressureDropLagTC = EFloat

    # Cold Leg Feedback Lead Time Constant
    coldLegFBLeadTC2 = EFloat

    # Cold Leg Feedback Lag Time Constant
    coldLegFBLagTC = EFloat

    # Hot Leg To Cold Leg Gain
    hotLegToColdLegGain = EFloat

    # Feedback Factor
    feedbackFactor = EFloat

    # Core Neutronics And Heat Transfer
    coreNeutronicsHT = EFloat

    # Throttle Pressure Factor
    throttlePressureFactor = EFloat

    # Core Heat Transfer Lag Time Constant
    coreHTLagTC1 = EFloat

    # Throttle Pressure Setpoint
    throttlePressureSP = EFloat

    # Core Neutronics Effective Time Constant
    coreNeutronicsEffTC = EFloat

    # Cold Leg Feedback Gain 1
    coldLegFG1 = EFloat

    # Steam Pressure Feedback Gain
    steamPressureFG = EFloat

    # Hot Leg Steam Gain
    hotLegSteamGain = EFloat

    # Core Heat Transfer Lag Time Constant
    coreHTLagTC2 = EFloat

    # Cold Leg Lag Time Constant
    coldLegLagTC = EFloat

    # Pressure Control Gain
    pressureCG = EFloat

    # Cold Leg Feedback Lead Time Constant
    coldLegFBLeadTC1 = EFloat

    # Steam Flow Feedback Gain
    steamFlowFG = EFloat

    # Hot Leg Lag Time Constant
    hotLegLagTC = EFloat

    #--------------------------------------------------------------------------
    #  Begin pWRSteamSupply user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End pWRSteamSupply user definitions:
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
    Drives_AirCompressor = Instance("CIM13.Generation.Production.AirCompressor")

    # A combustion turbine may have a active power versus ambient temperature relationship
    CTTempActivePowerCurve = Instance("CIM13.Generation.GenerationDynamics.CTTempActivePowerCurve")

    # A combustion turbine may have a heat recovery boiler for making steam
    HeatRecoveryBoiler = Instance("CIM13.Generation.GenerationDynamics.HeatRecoveryBoiler")

    # Reference temperature at which the output of the turbine was defined.
    referenceTemp = EFloat

    # Per unit change in power per (versus) unit change in ambient temperature
    powerVariationByTemp = EFloat

    # Flag that is set to true if the combustion turbine is associated with a heat recovery boiler
    heatRecoveryFlag = EBoolean

    # Off-nominal voltage effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in auxiliary bus voltage (from a specified voltage level).
    auxPowerVersusVoltage = EFloat

    # Default ambient temperature to be used in modeling applications
    ambientTemp = EFloat

    # The time constant for the turbine.
    timeConstant = EFloat

    # Off-nominal frequency effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in frequency (from rated frequency).
    auxPowerVersusFrequency = EFloat

    # Off-nominal frequency effect on turbine capability. Per unit reduction in unit active power capability versus per unit reduction in frequency (from rated frequency).
    capabilityVersusFrequency = EFloat

    #--------------------------------------------------------------------------
    #  Begin combustionTurbine user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End combustionTurbine user definitions:
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
    rfAux2 = EFloat

    # Initial Lower Limit
    lowerLimit = EFloat

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux6 = EFloat

    # Pressure Limit
    pressureLimit = EFloat

    # Initial Upper Limit
    upperLimit = EFloat

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux3 = EFloat

    # Rod Pattern
    rodPattern = EFloat

    # Proportional Gain
    proportionalGain = EFloat

    # In-Core Thermal Time Constant
    inCoreThermalTC = EFloat

    # High Power Limit
    highPowerLimit = EFloat

    # Constant Associated With Rod Pattern
    rodPatternConstant = EFloat

    # Low Power Limit
    lowPowerLimit = EFloat

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux7 = EFloat

    # Pressure Setpoint Time Constant
    pressureSetpointTC1 = EFloat

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux4 = EFloat

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux1 = EFloat

    # Integral Gain
    integralGain = EFloat

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux8 = EFloat

    # Pressure Setpoint Gain Adjuster
    pressureSetpointGA = EFloat

    # Pressure Setpoint Time Constant
    pressureSetpointTC2 = EFloat

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux5 = EFloat

    #--------------------------------------------------------------------------
    #  Begin bWRSteamSupply user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End bWRSteamSupply user definitions:
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
    minHeadMaxP = EFloat

    # Gate Rate Limit
    gateRateLimit = EFloat

    # Speed Regulation
    speedRegulation = EFloat

    # Transient Regulation
    transientRegulation = EFloat

    # Transient Droop Time Constant
    transientDroopTime = EFloat

    # Maximum efficiency active power at maximum head conditions
    maxHeadMaxP = EFloat

    # Rated turbine active power
    turbineRating = EFloat

    # Water Starting Time
    waterStartingTime = EFloat

    # Type of turbine.
    turbineType = TurbineType

    # Gate Upper Limit
    gateUpperLimit = EFloat

    # Rated speed in number of revolutions.
    speedRating = EFloat

    #--------------------------------------------------------------------------
    #  Begin hydroTurbine user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End hydroTurbine user definitions:
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
    superHeaterPipePD = EFloat

    # Active power Maximum Error Rate Limit
    maxErrorRateP = EFloat

    # Off nominal voltage effect on auxiliary real power. Per unit active power variation versus per unit voltage variation.
    auxPowerversusVoltage = EFloat

    # Pressure Control Proportional Gain ratio
    pressureCtrlPG = EFloat

    # Secondary Superheater Capacity
    superHeater2Capacity = EFloat

    # The control mode of the boiler
    boilerControlMode = BoilerControlMode

    # Mechanical Power Sensor Lag
    mechPowerSensorLag = EFloat

    # Pressure Error Bias ratio
    controlPEB = EFloat

    # Fuel Demand Limit
    fuelDemandLimit = EFloat

    # Proportional Constant
    controlPC = EFloat

    # Pressure Feedback Indicator
    pressureFeedback = EInt

    # Off nominal frequency effect on auxiliary real power. Per unit active power variation versus per unit frequency variation.
    auxPowerVersusFrequency = EFloat

    # Feedwater Integral Gain ratio
    feedWaterIG = EFloat

    # Time Constant
    controlTC = EFloat

    # Active power Error Bias ratio
    controlErrorBiasP = EFloat

    # Feedwater Time Constant rato
    feedWaterTC = EFloat

    # Feedwater Proportional Gain ratio
    feedWaterPG = EFloat

    # Fuel Delay
    fuelSupplyDelay = EFloat

    # Pressure Control Derivative Gain ratio
    pressureCtrlDG = EFloat

    # Pressure Control Integral Gain ratio
    pressureCtrlIG = EFloat

    # Fuel Supply Time Constant
    fuelSupplyTC = EFloat

    # Integral Constant
    controlIC = EFloat

    # Throttle Pressure Setpoint
    throttlePressureSP = EFloat

    # Drum/Primary Superheater Capacity
    superHeater1Capacity = EFloat

    # Pressure Error Deadband
    controlPED = EFloat

    # Active power Minimum Error Rate Limit
    minErrorRateP = EFloat

    #--------------------------------------------------------------------------
    #  Begin fossilSteamSupply user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End fossilSteamSupply user definitions:
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
    #  Begin subcritical user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End subcritical user definitions:
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
    #  Begin supercritical user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End supercritical user definitions:
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
    CombustionTurbines = List(Instance("CIM13.Generation.GenerationDynamics.CombustionTurbine"))

    # The steam supply rating in kilopounds per hour, if dual pressure boiler
    steamSupplyRating2 = EFloat

    #--------------------------------------------------------------------------
    #  Begin heatRecoveryBoiler user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End heatRecoveryBoiler user definitions:
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
    drumBoilerRating = EFloat

    #--------------------------------------------------------------------------
    #  Begin drumBoiler user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End drumBoiler user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
