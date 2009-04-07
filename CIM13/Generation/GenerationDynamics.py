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
    primeMoverRating = Float

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
    steamSupplyRating = Float

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
    shaft2PowerIP = Float

    # Fraction Of Power From Shaft 2 First Low Pressure Turbine output
    shaft2PowerLP1 = Float

    # Fraction Of Power From Shaft 2 Second Low Pressure Turbine output
    shaft2PowerLP2 = Float

    # Fraction Of Power From Shaft 2 High Pressure Turbine output
    shaft2PowerHP = Float

    # Second Reheater Time Constant
    reheater2TC = Float

    # Fraction Of Power From Shaft 1 Intermediate Pressure Turbine output
    shaft1PowerIP = Float

    # Steam Chest Time Constant
    steamChestTC = Float

    # Fraction Of Power From Shaft 1 First Low Pressure Turbine output
    shaft1PowerLP1 = Float

    # Crossover Time Constant
    crossoverTC = Float

    # First Reheater Time Constant
    reheater1TC = Float

    # Fraction Of Power From Shaft 1 High Pressure Turbine output
    shaft1PowerHP = Float

    # Fraction Of Power From Shaft 1 Second Low Pressure Turbine output
    shaft1PowerLP2 = Float

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
    coldLegFG2 = Float

    # Steam Pressure Drop Lag Time Constant
    steamPressureDropLagTC = Float

    # Cold Leg Feedback Lead Time Constant
    coldLegFBLeadTC2 = Float

    # Cold Leg Feedback Lag Time Constant
    coldLegFBLagTC = Float

    # Hot Leg To Cold Leg Gain
    hotLegToColdLegGain = Float

    # Feedback Factor
    feedbackFactor = Float

    # Core Neutronics And Heat Transfer
    coreNeutronicsHT = Float

    # Throttle Pressure Factor
    throttlePressureFactor = Float

    # Core Heat Transfer Lag Time Constant
    coreHTLagTC1 = Float

    # Throttle Pressure Setpoint
    throttlePressureSP = Float

    # Core Neutronics Effective Time Constant
    coreNeutronicsEffTC = Float

    # Cold Leg Feedback Gain 1
    coldLegFG1 = Float

    # Steam Pressure Feedback Gain
    steamPressureFG = Float

    # Hot Leg Steam Gain
    hotLegSteamGain = Float

    # Core Heat Transfer Lag Time Constant
    coreHTLagTC2 = Float

    # Cold Leg Lag Time Constant
    coldLegLagTC = Float

    # Pressure Control Gain
    pressureCG = Float

    # Cold Leg Feedback Lead Time Constant
    coldLegFBLeadTC1 = Float

    # Steam Flow Feedback Gain
    steamFlowFG = Float

    # Hot Leg Lag Time Constant
    hotLegLagTC = Float

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
    referenceTemp = Float

    # Per unit change in power per (versus) unit change in ambient temperature
    powerVariationByTemp = Float

    # Flag that is set to true if the combustion turbine is associated with a heat recovery boiler
    heatRecoveryFlag = Bool

    # Off-nominal voltage effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in auxiliary bus voltage (from a specified voltage level).
    auxPowerVersusVoltage = Float

    # Default ambient temperature to be used in modeling applications
    ambientTemp = Float

    # The time constant for the turbine.
    timeConstant = Float

    # Off-nominal frequency effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in frequency (from rated frequency).
    auxPowerVersusFrequency = Float

    # Off-nominal frequency effect on turbine capability. Per unit reduction in unit active power capability versus per unit reduction in frequency (from rated frequency).
    capabilityVersusFrequency = Float

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
    rfAux2 = Float

    # Initial Lower Limit
    lowerLimit = Float

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux6 = Float

    # Pressure Limit
    pressureLimit = Float

    # Initial Upper Limit
    upperLimit = Float

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux3 = Float

    # Rod Pattern
    rodPattern = Float

    # Proportional Gain
    proportionalGain = Float

    # In-Core Thermal Time Constant
    inCoreThermalTC = Float

    # High Power Limit
    highPowerLimit = Float

    # Constant Associated With Rod Pattern
    rodPatternConstant = Float

    # Low Power Limit
    lowPowerLimit = Float

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux7 = Float

    # Pressure Setpoint Time Constant
    pressureSetpointTC1 = Float

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux4 = Float

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux1 = Float

    # Integral Gain
    integralGain = Float

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux8 = Float

    # Pressure Setpoint Gain Adjuster
    pressureSetpointGA = Float

    # Pressure Setpoint Time Constant
    pressureSetpointTC2 = Float

    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux5 = Float

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
    minHeadMaxP = Float

    # Gate Rate Limit
    gateRateLimit = Float

    # Speed Regulation
    speedRegulation = Float

    # Transient Regulation
    transientRegulation = Float

    # Transient Droop Time Constant
    transientDroopTime = Float

    # Maximum efficiency active power at maximum head conditions
    maxHeadMaxP = Float

    # Rated turbine active power
    turbineRating = Float

    # Water Starting Time
    waterStartingTime = Float

    # Type of turbine.
    turbineType = TurbineType

    # Gate Upper Limit
    gateUpperLimit = Float

    # Rated speed in number of revolutions.
    speedRating = Float

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
    superHeaterPipePD = Float

    # Active power Maximum Error Rate Limit
    maxErrorRateP = Float

    # Off nominal voltage effect on auxiliary real power. Per unit active power variation versus per unit voltage variation.
    auxPowerversusVoltage = Float

    # Pressure Control Proportional Gain ratio
    pressureCtrlPG = Float

    # Secondary Superheater Capacity
    superHeater2Capacity = Float

    # The control mode of the boiler
    boilerControlMode = BoilerControlMode

    # Mechanical Power Sensor Lag
    mechPowerSensorLag = Float

    # Pressure Error Bias ratio
    controlPEB = Float

    # Fuel Demand Limit
    fuelDemandLimit = Float

    # Proportional Constant
    controlPC = Float

    # Pressure Feedback Indicator
    pressureFeedback = Int

    # Off nominal frequency effect on auxiliary real power. Per unit active power variation versus per unit frequency variation.
    auxPowerVersusFrequency = Float

    # Feedwater Integral Gain ratio
    feedWaterIG = Float

    # Time Constant
    controlTC = Float

    # Active power Error Bias ratio
    controlErrorBiasP = Float

    # Feedwater Time Constant rato
    feedWaterTC = Float

    # Feedwater Proportional Gain ratio
    feedWaterPG = Float

    # Fuel Delay
    fuelSupplyDelay = Float

    # Pressure Control Derivative Gain ratio
    pressureCtrlDG = Float

    # Pressure Control Integral Gain ratio
    pressureCtrlIG = Float

    # Fuel Supply Time Constant
    fuelSupplyTC = Float

    # Integral Constant
    controlIC = Float

    # Throttle Pressure Setpoint
    throttlePressureSP = Float

    # Drum/Primary Superheater Capacity
    superHeater1Capacity = Float

    # Pressure Error Deadband
    controlPED = Float

    # Active power Minimum Error Rate Limit
    minErrorRateP = Float

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
    steamSupplyRating2 = Float

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
    drumBoilerRating = Float

    #--------------------------------------------------------------------------
    #  Begin drumBoiler user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End drumBoiler user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
