# @copyright: 2009 Richard W. Lincoln
# @contact: r.w.lincoln@gmail.com
# @license: GPLv3

""" The Generation Dynamics package contains prime movers, such as turbines and boilers, which are needed for simulation and educational purposes. 
"""
from iec61970.core import PowerSystemResource
from iec61970.core import Curve
from iec61970.domain import Seconds
from iec61970.domain import Float
from iec61970.domain import PU
from iec61970.domain import ActivePower
from iec61970.domain import RotationSpeed
from iec61970.domain import Integer
from iec61970.domain import Temperature
from iec61970.domain import Boolean



from enthought.traits.api import Instance, List, Enum, Float, Int, Bool


# Boiler { Following, Coordinated}
BoilerControlMode = Enum("following", "coordinated", desc="Boiler { Following, Coordinated}")
# Type of turbine.
TurbineType = Enum("francis", "pelton", "kaplan", desc="Type of turbine.")

class SteamSupply(PowerSystemResource):
    """ Steam supply for steam turbine
    """
    # Steam turbines may have steam supplied by a steam supply
    SteamTurbines = List(Instance("iec61970.generation.generationdynamics.SteamTurbine.SteamTurbine"))
    # Rating of steam supply
    steamSupplyRating = Float

class PrimeMover(PowerSystemResource):
    """ The machine used to develop mechanical energy used to drive a generator.
    """
    Drives_SynchronousMachines = List(Instance("iec61970.wires.SynchronousMachine.SynchronousMachine"))
    # Rating of prime mover
    primeMoverRating = Float

class CTTempActivePowerCurve(Curve):
    """ Relationship between the combustion turbine's power output rating in gross active power (X-axis) and the ambient air temperature (Y-axis)
    """
    # A combustion turbine may have an active power versus ambient temperature relationship
    CombustionTurbine = Instance("iec61970.generation.generationdynamics.CombustionTurbine.CombustionTurbine", allow_none=False)

class SteamTurbine(PrimeMover):
    """ Steam turbine
    """
    # Steam turbines may have steam supplied by a steam supply
    SteamSupplys = List(Instance("iec61970.generation.generationdynamics.SteamSupply.SteamSupply"))
    # Crossover Time Constant
    crossoverTC = Seconds
    # First Reheater Time Constant
    reheater1TC = Seconds
    # Second Reheater Time Constant
    reheater2TC = Seconds
    # Fraction Of Power From Shaft 1 High Pressure Turbine output
    shaft1PowerHP = Float
    # Fraction Of Power From Shaft 1 Intermediate Pressure Turbine output
    shaft1PowerIP = Float
    # Fraction Of Power From Shaft 1 First Low Pressure Turbine output
    shaft1PowerLP1 = Float
    # Fraction Of Power From Shaft 1 Second Low Pressure Turbine output
    shaft1PowerLP2 = Float
    # Fraction Of Power From Shaft 2 High Pressure Turbine output
    shaft2PowerHP = Float
    # Fraction Of Power From Shaft 2 Intermediate Pressure Turbine output
    shaft2PowerIP = Float
    # Fraction Of Power From Shaft 2 First Low Pressure Turbine output
    shaft2PowerLP1 = Float
    # Fraction Of Power From Shaft 2 Second Low Pressure Turbine output
    shaft2PowerLP2 = Float
    # Steam Chest Time Constant
    steamChestTC = Seconds

class PWRSteamSupply(SteamSupply):
    """ Pressurized water reactor used as a steam supply to a steam turbine
    """
    # Cold Leg Feedback Lag Time Constant
    coldLegFBLagTC = PU
    # Cold Leg Feedback Lead Time Constant
    coldLegFBLeadTC1 = PU
    # Cold Leg Feedback Lead Time Constant
    coldLegFBLeadTC2 = PU
    # Cold Leg Feedback Gain 1
    coldLegFG1 = PU
    # Cold Leg Feedback Gain 2
    coldLegFG2 = PU
    # Cold Leg Lag Time Constant
    coldLegLagTC = PU
    # Core Heat Transfer Lag Time Constant
    coreHTLagTC1 = PU
    # Core Heat Transfer Lag Time Constant
    coreHTLagTC2 = PU
    # Core Neutronics Effective Time Constant
    coreNeutronicsEffTC = PU
    # Core Neutronics And Heat Transfer
    coreNeutronicsHT = PU
    # Feedback Factor
    feedbackFactor = PU
    # Hot Leg Lag Time Constant
    hotLegLagTC = PU
    # Hot Leg Steam Gain
    hotLegSteamGain = PU
    # Hot Leg To Cold Leg Gain
    hotLegToColdLegGain = PU
    # Pressure Control Gain
    pressureCG = PU
    # Steam Flow Feedback Gain
    steamFlowFG = PU
    # Steam Pressure Drop Lag Time Constant
    steamPressureDropLagTC = PU
    # Steam Pressure Feedback Gain
    steamPressureFG = PU
    # Throttle Pressure Factor
    throttlePressureFactor = PU
    # Throttle Pressure Setpoint
    throttlePressureSP = PU

class HydroTurbine(PrimeMover):
    """ A water driven prime mover. Typical turbine types are: Francis, Kaplan, and Pelton.
    """
    # Gate Rate Limit
    gateRateLimit = Float
    # Gate Upper Limit
    gateUpperLimit = PU
    # Maximum efficiency active power at minimum head conditions
    minHeadMaxP = ActivePower
    # Maximum efficiency active power at maximum head conditions
    maxHeadMaxP = ActivePower
    # Rated speed in revolutions per minute
    speedRating = RotationSpeed
    # Speed Regulation
    speedRegulation = PU
    # Transient Droop Time Constant
    transientDroopTime = Seconds
    # Transient Regulation
    transientRegulation = PU
    # Rated turbine active power
    turbineRating = ActivePower
    # Type of turbine, e.g.: Francis, Pelton, Kaplan
    turbineType = TurbineType
    # Water Starting Time
    waterStartingTime = Seconds

class FossilSteamSupply(SteamSupply):
    """ Fossil fueled boiler (e.g., coal, oil, gas)
    """
    # Off nominal frequency effect on auxiliary real power. Per unit active power variation versus per unit frequency variation.
    auxPowerVersusFrequency = PU
    # Off nominal voltage effect on auxiliary real power. Per unit active power variation versus per unit voltage variation.
    auxPowerversusVoltage = PU
    # Integral Constant
    controlIC = Float
    # The control mode of the boiler
    boilerControlMode = BoilerControlMode
    # Active power Error Bias ratio
    controlErrorBiasP = Float
    # Proportional Constant
    controlPC = Float
    # Pressure Error Bias ratio
    controlPEB = Float
    # Pressure Error Deadband
    controlPED = PU
    # Time Constant
    controlTC = Float
    # Feedwater Integral Gain ratio
    feedWaterIG = Float
    # Feedwater Proportional Gain ratio
    feedWaterPG = Float
    # Feedwater Time Constant rato
    feedWaterTC = Seconds
    # Fuel Demand Limit
    fuelDemandLimit = PU
    # Fuel Delay
    fuelSupplyDelay = Seconds
    # Mechanical Power Sensor Lag
    mechPowerSensorLag = Seconds
    # Fuel Supply Time Constant
    fuelSupplyTC = Seconds
    # Active powerMaximum Error Rate Limit
    maxErrorRateP = Float
    # Active power Minimum Error Rate Limit
    minErrorRateP = Float
    # Pressure Control Derivative Gain ratio
    pressureCtrlDG = Float
    # Pressure Control Integral Gain ratio
    pressureCtrlIG = Float
    # Pressure Control Proportional Gain ratio
    pressureCtrlPG = Float
    # Pressure Feedback Indicator
    pressureFeedback = Integer
    # Drum/Primary Superheater Capacity
    superHeater1Capacity = Float
    # Secondary Superheater Capacity
    superHeater2Capacity = Float
    # Superheater Pipe Pressure Drop Constant
    superHeaterPipePD = Float
    # Throttle Pressure Setpoint
    throttlePressureSP = PU

class DrumBoiler(FossilSteamSupply):
    """ Drum boiler
    """
    # Rating of drum boiler in steam units
    drumBoilerRating = Float

class CombustionTurbine(PrimeMover):
    """ A prime mover that is typically fueled by gas or light oil
    """
    # A combustion turbine may have a heat recovery boiler for making steam
    HeatRecoveryBoiler = Instance("iec61970.generation.generationdynamics.HeatRecoveryBoiler.HeatRecoveryBoiler")
    # A combustion turbine may have an active power versus ambient temperature relationship
    CTTempActivePowerCurve = Instance("iec61970.generation.generationdynamics.CTTempActivePowerCurve.CTTempActivePowerCurve")
    # A CAES air compressor is driven by combustion turbine
    Drives_AirCompressor = Instance("iec61970.generation.production.AirCompressor.AirCompressor")
    # Default ambient temperature to be used in modeling applications
    ambientTemp = Temperature
    # Off-nominal frequency effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in frequency (from rated frequency).
    auxPowerVersusFrequency = PU
    # Off-nominal voltage effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in auxiliary bus voltage (from a specified voltage level).
    auxPowerVersusVoltage = PU
    # Off-nominal frequency effect on turbine capability. Per unit reduction in unit active power capability versus per unit reduction in frequency (from rated frequency).
    capabilityVersusFrequency = PU
    # Flag that is set to true if the combustion turbine is associated with a heat recovery boiler
    heatRecoveryFlag = Boolean
    # Per unit change in power per (versus) unit change in ambient temperature
    powerVariationByTemp = PU
    # Reference temperature at which the output of the turbine was defined.
    referenceTemp = Temperature
    # The time constant for the turbine.
    timeConstant = Seconds

class BWRSteamSupply(SteamSupply):
    """ Boiling water reactor used as a steam supply to a steam turbine
    """
    # High Power Limit
    highPowerLimit = PU
    # In-Core Thermal Time Constant
    inCoreThermalTC = Seconds
    # Integral Gain
    integralGain = Float
    # Initial Lower Limit
    lowerLimit = PU
    # Low Power Limit
    lowPowerLimit = PU
    # Pressure Limit
    pressureLimit = PU
    # Pressure Setpoint Gain Adjuster
    pressureSetpointGA = Float
    # Pressure Setpoint Time Constant
    pressureSetpointTC1 = Seconds
    # Pressure Setpoint Time Constant
    pressureSetpointTC2 = Seconds
    # Proportional Gain
    proportionalGain = Float
    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux1 = PU
    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux2 = PU
    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux3 = PU
    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux4 = PU
    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux5 = PU
    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux6 = PU
    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux7 = PU
    # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
    rfAux8 = PU
    # Rod Pattern
    rodPattern = PU
    # Constant Associated With Rod Pattern
    rodPatternConstant = Float
    # Initial Upper Limit
    upperLimit = PU

class Supercritical(FossilSteamSupply):
    """ Once-through supercritical boiler
    """
    pass

class Subcritical(FossilSteamSupply):
    """ Once-through subcritical boiler
    """
    pass

class HeatRecoveryBoiler(FossilSteamSupply):
    """ The heat recovery system associated with combustion turbines in order to produce steam for combined cycle plants
    """
    # A combustion turbine may have a heat recovery boiler for making steam
    CombustionTurbines = List(Instance("iec61970.generation.generationdynamics.CombustionTurbine.CombustionTurbine"))
    # The steam supply rating in kilopounds per hour, if dual pressure boiler
    steamSupplyRating2 = Float


