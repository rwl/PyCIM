# @copyright: 2009 Richard W. Lincoln
# @contact: r.w.lincoln@gmail.com
# @license: GPLv3

""" The production package is responsible for classes which describe various kinds of generators. These classes also provide production costing information which is used to economically allocate demand among committed units and calculate reserve quantities.
"""
from iec61970.core import Curve
from iec61970.core import RegularIntervalSchedule
from iec61970.core import IdentifiedObject
from iec61970.core import PowerSystemResource
from iec61970.core import Equipment
from iec61970.domain import WaterLevel
from iec61970.domain import Hours
from iec61970.domain import Money
from iec61970.domain import AbsoluteDateTime
from iec61970.domain import Integer
from iec61970.domain import ActivePower
from iec61970.domain import ActivePowerChangeRate
from iec61970.domain import Volume
from iec61970.domain import Float
from iec61970.domain import String
from iec61970.domain import Seconds
from iec61970.domain import Boolean
from iec61970.domain import PU
from iec61970.domain import PerCent
from iec61970.domain import RealEnergy



from enthought.traits.api import Instance, List, Str, Enum, Int, Float, Bool

Classification = Str(desc="1..n, with 1 the most detailed, highest priority, etc.")
CostPerEnergyUnit = Str(desc="Cost, in units of currency, per megawatt hour of electricity generated")
CostPerHeatUnit = Str(desc="Cost, in units of currency, per million Btus of heat generated")
CostRate = Str(desc="Cost, in units of currency, per hour of elapsed time")
HeatRate = Str(desc="Heat generated, in energy pertime unit of elapsed time")
Emission = Str(desc="Quantity of emission per fuel heat content")

# The type of emission
EmissionType = Enum("sulfurDioxide", "carbonDioxide", "nitrogenOxide", "hydrogenSulfide", "chlorine", "carbonDisulfide", desc="The type of emission")
# The source of the emission value.
EmissionValueSource = Enum("measured", "calculated", desc="The source of the emission value.")
# Type of fuel.
FuelType = Enum("coal", "oil", "gas", desc="Type of fuel.")
# Unit control modes, i.e., Setpoint  or Pulse
GeneratorControlMode = Enum("setpoint", "pulse", desc="Unit control modes, i.e., Setpoint  or Pulse")
# The source of controls for a generating unit, i.e., Unavailable, Off-AGC, On-AGC, Plant Control
GeneratorControlSource = Enum("Unavailable", "offAGC", "onAGC", "PlantControl", desc="The source of controls for a generating unit, i.e., Unavailable, Off-AGC, On-AGC, Plant Control")
# Operating mode for secondary generator control, e.g.: Unavailable, Manual, Fixed, Load Frequency Control, AGC, EDC, RPN, MRN, or REG
GeneratorOperatingMode = Enum("Off", "Manual", "Fixed", "LFC", "AGC", "EDC", "MRN", "REG", desc="Operating mode for secondary generator control, e.g.: Unavailable, Manual, Fixed, Load Frequency Control, AGC, EDC, RPN, MRN, or REG")
# The type of hydro power plant, e.g.: Run-of-River, Pumped Storage, Major Storage, Minor Storage.
HydroPlantType = Enum("runOfRiver", "pumpedStorage", "majorStorage", "minorStorage", desc="The type of hydro power plant, e.g.: Run-of-River, Pumped Storage, Major Storage, Minor Storage.")
# Type of hydro plant penstock.
PenstockType = Enum("Type", "of", "hydro", "plant", "penstock", desc="Type of hydro plant penstock.")
# Type of spillway gate.
SpillwayGateType = Enum("Type", "of", "spillway", "gate", desc="Type of spillway gate.")
# Type (or absence) of surge tank that is associated with the hydro power plant.
SurgeTankCode = Enum("Type", "_or", "absence", "of", "surge", "tank", "that", "is", "associated", "with", "the", "hydro", "power", "plant", desc="Type (or absence) of surge tank that is associated with the hydro power plant.")

class TargetLevelSchedule(Curve):
    """ Reservoir water level targets from advanced studies or 'rule curves'. Typically in one hour increments for up to 10 days
    """
    # A reservoir may have a water level target schedule.
    Reservoir = Instance("iec61970.generation.production.Reservoir.Reservoir", allow_none=False)
    # High target level limit, above which the reservoir operation will be penalized
    highLevelLimit = WaterLevel
    # Low target level limit, below which the reservoir operation will be penalized
    lowLevelLimit = WaterLevel

class TailbayLossCurve(Curve):
    """ Relationship between tailbay head loss (in meters on the Y-axis) and the total discharge into the power station's tailbay (in m3/sec on the X-axis) . There could be more than one curve depending on the level of the tailbay reservoir or river level
    """
    # A hydro generating unit has a tailbay loss curve
    HydroGeneratingUnit = Instance("iec61970.generation.production.HydroGeneratingUnit.HydroGeneratingUnit", allow_none=False)

class SteamSendoutSchedule(RegularIntervalSchedule):
    """ The cogeneration plant's steam sendout schedule in klb/hour versus time
    """
    # A cogeneration plant has a steam sendout schedule
    CogenerationPlant = Instance("iec61970.generation.production.CogenerationPlant.CogenerationPlant", allow_none=False)

class StartupModel(IdentifiedObject):
    """ Unit start up characteristics depending on how long the unit has been off line
    """
    # The unit's startup model may have a startup ignition fuel curve
    StartIgnFuelCurve = Instance("iec61970.generation.production.StartIgnFuelCurve.StartIgnFuelCurve")
    # The unit's startup model may have a startup main fuel curve
    StartMainFuelCurve = Instance("iec61970.generation.production.StartMainFuelCurve.StartMainFuelCurve")
    # The unit's startup model may have a startup ramp curve
    StartRampCurve = Instance("iec61970.generation.production.StartRampCurve.StartRampCurve")
    # A thermal generating unit may have a startup model
    ThermalGeneratingUnit = Instance("iec61970.generation.production.ThermalGeneratingUnit.ThermalGeneratingUnit", allow_none=False)
    # Fixed Maintenance Cost
    fixedMaintCost = CostRate
    # The amount of heat input per hour required for hot standby operation
    hotStandbyHeat = HeatRate
    # Incremental Maintenance Cost
    incrementalMaintCost = CostPerEnergyUnit
    # The minimum number of hours the unit must be down before restart
    minimumDownTime = Hours
    # The minimum number of hours the unit must be operating before being allowed to shut down
    minimumRunTime = Hours
    # The opportunity cost associated with the return in dollars. This represents the restart's 'share' of the unit depreciation and risk of an event which would damage the unit.
    riskFactorCost = Money
    # Total miscellaneous start up costs
    startupCost = Money
    # The date and time of the most recent generating unit startup
    startupDate = AbsoluteDateTime
    # Startup priority within control area where lower numbers indicate higher priorities.  More than one unit in an area may be assigned the same priority.
    startupPriority = Integer
    # The unit's auxiliary active power consumption to maintain standby mode
    stbyAuxP = ActivePower

class StartRampCurve(Curve):
    """ Rate in gross active power/minute (Y-axis) at which a unit can be loaded versus the number of hours (X-axis) the unit was off line
    """
    # The unit's startup model may have a startup ramp curve
    StartupModel = Instance("iec61970.generation.production.StartupModel.StartupModel", allow_none=False)
    # The startup ramp rate in gross for a unit that is on hot standby
    hotStandbyRamp = ActivePowerChangeRate

class StartMainFuelCurve(Curve):
    """ The quantity of main fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line
    """
    # The unit's startup model may have a startup main fuel curve
    StartupModel = Instance("iec61970.generation.production.StartupModel.StartupModel", allow_none=False)
    # Type of main fuel
    mainFuelType = FuelType

class StartIgnFuelCurve(Curve):
    """ The quantity of ignition fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line
    """
    # The unit's startup model may have a startup ignition fuel curve
    StartupModel = Instance("iec61970.generation.production.StartupModel.StartupModel", allow_none=False)
    # Type of ignition fuel
    ignitionFuelType = FuelType

class ShutdownCurve(Curve):
    """ Relationship between the rate in gross active power/minute (Y-axis) at which a unit should be shutdown and its present gross MW output (X-axis)
    """
    # A thermal generating unit may have a shutdown curve
    ThermalGeneratingUnit = Instance("iec61970.generation.production.ThermalGeneratingUnit.ThermalGeneratingUnit", allow_none=False)
    # Fixed shutdown cost
    shutdownCost = Money
    # The date and time of the most recent generating unit shutdown
    shutdownDate = AbsoluteDateTime

class Reservoir(PowerSystemResource):
    """ A water storage facility within a hydro system, including: ponds, lakes, lagoons, and rivers. The storage is usually behind some type of dam.
    """
    # Generators discharge water to or pumps are supplied water from a downstream reservoir
    HydroPowerPlants = List(Instance("iec61970.generation.production.HydroPowerPlant.HydroPowerPlant"))
    # Generators are supplied water from or pumps discharge water to an upstream reservoir
    UpstreamFrom = List(Instance("iec61970.generation.production.HydroPowerPlant.HydroPowerPlant"))
    # A reservoir may have a level versus volume relationship.
    LevelVsVolumeCurve = List(Instance("iec61970.generation.production.LevelVsVolumeCurve.LevelVsVolumeCurve"))
    # A reservoir may have a water level target schedule.
    TargetLevelSchedule = Instance("iec61970.generation.production.TargetLevelSchedule.TargetLevelSchedule")
    # A reservoir may have a 'natural' inflow forecast.
    InflowForecast = List(Instance("iec61970.generation.production.InflowForecast.InflowForecast"))
    # A reservoir may spill into a downstream reservoir
    SpillsInto = List(Instance("iec61970.generation.production.Reservoir.Reservoir"))
    # A reservoir may spill into a downstream reservoir
    SpillsFrom = Instance("iec61970.generation.production.Reservoir.Reservoir")
    # Storage volume (in Mm3) between the full supply level and the normal minimum operating level
    activeStorageCapacity = Volume
    # The reservoir's energy storage rating in energy for given head conditions
    energyStorageRating = Float
    # Full supply level, above which water will spill. This can be the spillway crest level or the top of closed gates.
    fullSupplyLevel = WaterLevel
    # Total capacity of reservoir
    grossCapacity = Volume
    # Normal minimum operating level below which the penstocks will draw air
    normalMinOperateLevel = WaterLevel
    # River outlet works for riparian right releases or other purposes
    riverOutletWorks = String
    # The spillway water travel delay to the next downstream reservoir
    spillTravelDelay = Seconds
    # The flow capacity of the spillway in cubic meters per second
    spillwayCapacity = Float
    # The length of the spillway crest in meters
    spillwayCrestLength = Float
    # Spillway crest level above which water will spill
    spillwayCrestLevel = WaterLevel
    # Type of spillway gate, including parameters
    spillWayGateType = SpillwayGateType

class PenstockLossCurve(Curve):
    """ Relationship between penstock head loss (in meters) and  total discharge through the penstock (in cubic meters per second). One or more turbines may be connected to the same penstock.
    """
    # A hydro generating unit has a penstock loss curve
    HydroGeneratingUnit = Instance("iec61970.generation.production.HydroGeneratingUnit.HydroGeneratingUnit", allow_none=False)

class LevelVsVolumeCurve(Curve):
    """ Relationship between reservoir volume in millions of cubic meters and reservoir level in meters
    """
    # A reservoir may have a level versus volume relationship.
    Reservoir = Instance("iec61970.generation.production.Reservoir.Reservoir", allow_none=False)

class InflowForecast(RegularIntervalSchedule):
    """ Natural water inflow to a reservoir, usually forecasted from predicted rain and snowmelt. Typically in one hour increments for up to 10 days. The forecast is given in average cubic meters per second over the time increment.
    """
    # A reservoir may have a 'natural' inflow forecast.
    Reservoir = Instance("iec61970.generation.production.Reservoir.Reservoir", allow_none=False)

class IncrementalHeatRateCurve(Curve):
    """ Relationship between unit incremental heat rate in (delta energy/time) per (delta active power) and unit output in active power. The IHR curve represents the slope of the HeatInputCurve. Note that the 'incremental heat rate' and the 'heat rate' have the same engineering units.
    """
    # A thermal generating unit may have an incremental heat rate curve
    ThermalGeneratingUnit = Instance("iec61970.generation.production.ThermalGeneratingUnit.ThermalGeneratingUnit", allow_none=False)
    # Flag is set to YES when output is expressed in net active power
    isNetGrossP = Boolean

class HydroPumpOpSchedule(RegularIntervalSchedule):
    """ The hydro pump's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses.The unit's operating schedule status is typically given as: (0=unavailable)  (1=avilable to startup or shutdown)  (2=must pump)
    """
    # The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
    HydroPump = Instance("iec61970.generation.production.HydroPump.HydroPump", allow_none=False)

class HydroPump(PowerSystemResource):
    """ A synchronous motor-driven pump, typically associated with a pumped storage plant
    """
    # The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
    HydroPumpOpSchedule = Instance("iec61970.generation.production.HydroPumpOpSchedule.HydroPumpOpSchedule")
    # The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
    DrivenBy_SynchronousMachine = Instance("iec61970.wires.SynchronousMachine.SynchronousMachine", allow_none=False)
    # The hydro pump may be a member of a pumped storage plant or a pump for distributing water
    MemberOf_HydroPowerPlant = Instance("iec61970.generation.production.HydroPowerPlant.HydroPowerPlant")
    # The pumping discharge (m3/sec) under maximum head conditions, usually at full gate
    pumpDischAtMaxHead = Float
    # The pumping discharge (m3/sec) under minimum head conditions, usually at full gate
    pumpDischAtMinHead = Float
    # The pumping power under maximum head conditions, usually at full gate
    pumpPowerAtMaxHead = ActivePower
    # The pumping power under minimum head conditions, usually at full gate.
    pumpPowerAtMinHead = ActivePower

class HydroPowerPlant(PowerSystemResource):
    """ A hydro power station which can generate or pump. When generating, the generator turbines receive there water from an upper reservoir. When pumping, the pumps receive their water from a lower reservoir.
    """
    # The hydro generating unit belongs to a hydro power plant
    Contain_HydroGeneratingUnits = List(Instance("iec61970.generation.production.HydroGeneratingUnit.HydroGeneratingUnit"))
    # The hydro pump may be a member of a pumped storage plant or a pump for distributing water
    Contain_HydroPumps = List(Instance("iec61970.generation.production.HydroPump.HydroPump"))
    # Generators discharge water to or pumps are supplied water from a downstream reservoir
    Reservoir = Instance("iec61970.generation.production.Reservoir.Reservoir")
    # Generators are supplied water from or pumps discharge water to an upstream reservoir
    GenSourcePumpDischarge = Instance("iec61970.generation.production.Reservoir.Reservoir", allow_none=False)
    # Water travel delay from tailbay to next downstream hydro power station
    dischargeTravelDelay = Seconds
    # The type of hydro power plant, e.g.: Run-of-River, Pumped Storage, Major Storage, Minor Storage
    hydroPlantType = HydroPlantType
    # Type and configuration of hydro plant penstock(s)
    penstockType = PenstockType
    # Total plant discharge capacity in cubic meters per second
    plantDischargeCapacity = Float
    # The hydro plant's generating rating active power for rated head conditions
    genRatedP = ActivePower
    # The hydro plant's pumping rating active power for rated head conditions
    pumpRatedP = ActivePower
    # The plant's rated gross head in meters
    plantRatedHead = Float
    # A code describing the type (or absence) of surge tank that is associated with the hydro power plant
    surgeTankCode = SurgeTankCode
    # The level at which the surge tank spills
    surgeTankCrestLevel = WaterLevel

class HydroGeneratingEfficiencyCurve(Curve):
    """ Relationship between unit efficiency in percent and unit output active power for a given net head in meters. The relationship between efficiency, discharge, head, and power output is expressed as follows:   E =KP/HQ Where:  (E=percentage)  (P=active power)  (H=height)  (Q=volume/time unit)  (K=constant) For example, a curve instance for a given net head could relate efficiency (Y-axis) versus active power output (X-axis) or versus discharge on the X-axis.
    """
    # A hydro generating unit has an efficiency curve
    HydroGeneratingUnit = Instance("iec61970.generation.production.HydroGeneratingUnit.HydroGeneratingUnit", allow_none=False)

class HeatRateCurve(Curve):
    """ Relationship between unit heat rate per active power (Y-axis) and  unit output (X-axis). The heat input is from all fuels.
    """
    # A thermal generating unit may have a heat rate curve
    ThermalGeneratingUnit = Instance("iec61970.generation.production.ThermalGeneratingUnit.ThermalGeneratingUnit", allow_none=False)
    # Flag is set to YES when output is expressed in net active power
    isNetGrossP = Boolean

class HeatInputCurve(Curve):
    """ Relationship between unit heat input in energy pertime for main fuel (Y1-axis) and supplemental fuel (Y2-axis) versus unit output in active power (X-axis). The quantity of main fuel used to sustain generation at this output level is prorated for throttling between definition points. The quantity of supplemental fuel used at this output level is fixed and not prorated.
    """
    # A thermal generating unit may have a heat input curve
    ThermalGeneratingUnit = Instance("iec61970.generation.production.ThermalGeneratingUnit.ThermalGeneratingUnit", allow_none=False)
    # Power output - auxiliary power offset adjustment factor
    auxPowerOffset = ActivePower
    # Power output - auxiliary power multiplier adjustment factor in per unit
    auxPowerMult = PU
    # Heat input - efficiency multiplier adjustment factor in per unit
    heatInputEff = PU
    # Heat input - offset adjustment factor in MBtu/hr
    heatInputOffset = HeatRate
    # Flag is set to YES when output is expressed in net active power
    isNetGrossP = Boolean

class GrossToNetActivePowerCurve(Curve):
    """ Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.
    """
    # A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
    GeneratingUnit = Instance("iec61970.generation.production.GeneratingUnit.GeneratingUnit", allow_none=False)

class GenUnitOpSchedule(RegularIntervalSchedule):
    """ The generating unit's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses. The X-axis represents absolute time. The Y1-axis represents the status (0=off-line and unavailable: 1=available: 2=must run: 3=must run at fixed power value: etc.). The Y2-axis represents the must run fixed power value where required.
    """
    # A generating unit may have an operating schedule, indicating the planned operation of the unit
    GeneratingUnit = Instance("iec61970.generation.production.GeneratingUnit.GeneratingUnit", allow_none=False)

class GenUnitOpCostCurve(Curve):
    """ Relationship between unit operating cost in $/hour (Y-axis) and unit output active power (X-axis). The operating cost curve for thermal units is derived from heat input and fuel costs. The operating cost curve for hydro units is derived from water flow rates and equivalent water costs.
    """
    # A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
    GeneratingUnit = Instance("iec61970.generation.production.GeneratingUnit.GeneratingUnit", allow_none=False)
    # Flag is set to YES when output is expressed in net active power
    isNetGrossP = Boolean

class GeneratingUnit(Equipment):
    """ A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.
    """
    # A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
    GenUnitOpCostCurves = List(Instance("iec61970.generation.production.GenUnitOpCostCurve.GenUnitOpCostCurve"))
    # A generating unit may have an operating schedule, indicating the planned operation of the unit
    GenUnitOpSchedule = Instance("iec61970.generation.production.GenUnitOpSchedule.GenUnitOpSchedule")
    # A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
    GrossToNetActivePowerCurves = List(Instance("iec61970.generation.production.GrossToNetActivePowerCurve.GrossToNetActivePowerCurve"))
    # A GeneratingUnit injects energy into a SubControlArea.
    SubControlArea = Instance("iec61970.core.SubControlArea.SubControlArea")
    # A synchronous machine may operate as a generator and as such becomes a member of a generating unit
    Contains_SynchronousMachines = List(Instance("iec61970.wires.SynchronousMachine.SynchronousMachine"))
    # Unit control error deadband. When a unit's desired active power change is less than this deadband, then no control pulses will be sent to the unit.
    controlDeadband = ActivePower
    # Pulse high limit which is the largest control pulse that the unit can respond to
    controlPulseHigh = Seconds
    # Pulse low limit which is the smallest control pulse that the unit can respond to
    controlPulseLow = Seconds
    # Unit response rate which specifies the active power change for a control pulse of one second in the most responsive loading level of the unit.
    controlResponseRate = ActivePowerChangeRate
    # The efficiency of the unit in converting mechanical energy, from the prime mover, into electrical energy.
    efficiency = PU
    # Select the unit control mode as Setpoint  (S) or Pulse (P).
    genControlMode = GeneratorControlMode
    # The source of controls for a generating unit, i.e., Unavailable, Off-AGC, On-AGC, Plant Control
    genControlSource = GeneratorControlSource
    # Governor Motor Position Limit
    governorMPL = PU
    # Governor Speed Changer Droop
    governorSCD = PerCent
    # High limit for secondary (AGC) control
    highControlLimit = ActivePower
    # Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration
    initialP = ActivePower
    # Low limit for secondary (AGC) control
    lowControlLimit = ActivePower
    # Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.
    maximumAllowableSpinningReserve = ActivePower
    # Maximum high economic active power limit, that should not exceed the maximum operating active power limit
    maxEconomicP = ActivePower
    # This is the maximum operating active power limit the dispatcher can enter for this unit
    maxOperatingP = ActivePower
    # Low economic active power limit that must be greater than or equal to the minimum operating active power limit
    minEconomicP = ActivePower
    # This is the minimum operating active power limit the dispatcher can enter for this unit.
    minOperatingP = ActivePower
    # Detail level of the generator model data
    modelDetail = Classification
    # The unit's gross rated maximum capacity (Book Value).
    ratedGrossMaxP = ActivePower
    # The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid
    ratedGrossMinP = ActivePower
    # The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity
    ratedNetMaxP = ActivePower
    # Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied
    startupTime = Seconds
    # The planned unused capacity which can be used to support automatic control overruns.
    autoCntrlMarginP = ActivePower
    # The planned unused capacity (spinning reserve) which can be used to support emergency load
    allocSpinResP = ActivePower
    # For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits.
    baseP = ActivePower
    dispReserveFlag = Boolean
    energyMinP = HeatRate
    fastStartFlag = Boolean
    fuelPriority = Integer
    # Operating mode for secondary control, e.g.: Off, Manual, Fixed, LFC, AGC, EDC, RPN, MRN, or REG
    genOperatingMode = GeneratorOperatingMode
    # Generating unit economic participation factor
    longPF = Float
    lowerRampRate = ActivePowerChangeRate
    # Generating unit economic participation factor
    normalPF = Float
    # Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental Transmission Loss expressed as a plus or minus value. The typical range of penalty factors is (0.9 to 1.1).
    penaltyFactor = Float
    raiseRampRate = ActivePowerChangeRate
    # Generating unit economic participation factor
    shortPF = Float
    spinReserveRamp = ActivePowerChangeRate
    stepChange = ActivePower
    # Generating unit economic participation factor
    tieLinePF = Float
    # Minimum time interval between unit shutdown and startup
    minimumOffTime = Seconds

class FuelAllocationSchedule(Curve):
    """ The amount of fuel of a given type which is allocated for consumption over a specified period of time
    """
    # A fuel allocation schedule must have a fossil fuel
    FossilFuel = Instance("iec61970.generation.production.FossilFuel.FossilFuel", allow_none=False)
    # A thermal generating unit may have one or more fuel allocation schedules
    ThermalGeneratingUnit = Instance("iec61970.generation.production.ThermalGeneratingUnit.ThermalGeneratingUnit", allow_none=False)
    # The end time and date of the fuel allocation schedule
    fuelAllocationEndDate = AbsoluteDateTime
    # The start time and date of the fuel allocation schedule
    fuelAllocationStartDate = AbsoluteDateTime
    # The type of fuel, which also indicates the corresponding measurement unit
    fuelType = FuelType
    # The maximum amount fuel that is allocated for consumption for the scheduled time period
    maxFuelAllocation = Float
    # The minimum amount fuel that is allocated for consumption for the scheduled time period, e.g., based on a 'take-or-pay' contract
    minFuelAllocation = Float

class FossilFuel(IdentifiedObject):
    """ The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gas
    """
    # A fuel allocation schedule must have a fossil fuel
    FuelAllocationSchedule = List(Instance("iec61970.generation.production.FuelAllocationSchedule.FuelAllocationSchedule"))
    # A thermal generating unit may have one or more fossil fuels
    ThermalGeneratingUnit = Instance("iec61970.generation.production.ThermalGeneratingUnit.ThermalGeneratingUnit", allow_none=False)
    # The type of fossil fuel, such as coal, oil, or gas.
    fossilFuelType = FuelType
    # The cost in terms of heat value for the given type of fuel
    fuelCost = CostPerHeatUnit
    # The cost of fuel used for economic dispatching which includes: fuel cost, transportation cost,  and incremental maintenance cost
    fuelDispatchCost = CostPerHeatUnit
    # The efficiency factor for the fuel (per unit) in terms of the effective energy absorbed
    fuelEffFactor = PU
    # Handling and processing cost associated with this fuel
    fuelHandlingCost = CostPerHeatUnit
    # The amount of heat per weight (or volume) of the given type of fuel
    fuelHeatContent = Float
    # The amount in percent of the given type of fuel , when multiple fuels are being consumed
    fuelMixture = PerCent
    # The fuel's fraction of pollution credit per unit of heat content
    fuelSulfur = PU
    # The active power output level of the unit at which the given type of fuel is switched on. This fuel (e.g., oil) is sometimes used to supplement the base fuel (e.g., coal) at high active power output levels.
    highBreakpointP = ActivePower
    # The active power output level of the unit at which the given type of fuel is switched off. This fuel (e.g., oil) is sometimes used to stabilize the base fuel (e.g., coal) at low active power output levels.
    lowBreakpointP = ActivePower

class EmissionCurve(Curve):
    """ Relationship between the unit's emission rate in units of mass per hour (Y-axis) and output active power (X-axis) for a given type of emission. This curve applies when only one type of fuel is being burned.
    """
    # A thermal generating unit may have  one or more emission curves
    ThermalGeneratingUnit = Instance("iec61970.generation.production.ThermalGeneratingUnit.ThermalGeneratingUnit", allow_none=False)
    # The emission content per quantity of fuel burned
    emissionContent = Emission
    # The type of emission, which also gives the production rate measurement unit. The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide).
    emissionType = EmissionType
    # Flag is set to YES when output is expressed in net active power
    isNetGrossP = Boolean

class CombinedCyclePlant(PowerSystemResource):
    """ A set of combustion turbines and steam turbines where the exhaust heat from the combustion turbines is recovered to make steam for the steam turbines, resulting in greater overall plant efficiency
    """
    # A thermal generating unit may be a member of a combined cycle plant
    Contain_ThermalGeneratingUnits = List(Instance("iec61970.generation.production.ThermalGeneratingUnit.ThermalGeneratingUnit"))
    # The combined cycle plant's active power output rating
    combCyclePlantRating = ActivePower

class CogenerationPlant(PowerSystemResource):
    """ A set of thermal generating units for the production of electrical energy and process steam (usually from the output of the steam turbines). The steam sendout is typically used for industrial purposes or for municipal heating and cooling.
    """
    # A thermal generating unit may be a member of a cogeneration plant
    Contain_ThermalGeneratingUnits = List(Instance("iec61970.generation.production.ThermalGeneratingUnit.ThermalGeneratingUnit"))
    # A cogeneration plant has a steam sendout schedule
    SteamSendoutSchedule = Instance("iec61970.generation.production.SteamSendoutSchedule.SteamSendoutSchedule", allow_none=False)
    # The high pressure steam sendout
    cogenHPSendoutRating = Float
    # The high pressure steam rating
    cogenHPSteamRating = Float
    # The low pressure steam sendout
    cogenLPSendoutRating = Float
    # The low pressure steam rating
    cogenLPSteamRating = Float
    # The rated output active power of the cogeneration plant
    ratedP = ActivePower

class CAESPlant(PowerSystemResource):
    """ Compressed air energy storage plant
    """
    # An air compressor may be a member of a compressed air energy storage plant
    Contain_AirCompressor = Instance("iec61970.generation.production.AirCompressor.AirCompressor", allow_none=False)
    # A thermal generating unit may be a member of a compressed air energy storage plant
    Contain_ThermalGeneratingUnit = Instance("iec61970.generation.production.ThermalGeneratingUnit.ThermalGeneratingUnit")
    # The rated energy storage capacity in megawatt-hours
    energyStorageCapacity = RealEnergy
    # The CAES plant's gross rated generating capacity
    ratedCapacityP = ActivePower

class AirCompressor(PowerSystemResource):
    """ Combustion turbine air compressor which is an integral part of a compressed air energy storage (CAES) plant
    """
    # An air compressor may be a member of a compressed air energy storage plant
    MemberOf_CAESPlant = Instance("iec61970.generation.production.CAESPlant.CAESPlant", allow_none=False)
    # A CAES air compressor is driven by combustion turbine
    DrivenBy_CombustionTurbine = Instance("iec61970.generation.generationdynamics.CombustionTurbine.CombustionTurbine", allow_none=False)
    # Rating of the CAES air compressor
    airCompressorRating = Float

class AccountBalance(Curve):
    pass

class ThermalGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.
    """
    # A thermal generating unit may have one or more emission allowance accounts
    EmmissionAccounts = List(Instance("iec61970.generation.production.EmissionAccount.EmissionAccount"))
    # A thermal generating unit may have  one or more emission curves
    EmissionCurves = List(Instance("iec61970.generation.production.EmissionCurve.EmissionCurve"))
    # A thermal generating unit may have one or more fossil fuels
    FossilFuels = List(Instance("iec61970.generation.production.FossilFuel.FossilFuel"))
    # A thermal generating unit may have one or more fuel allocation schedules
    FuelAllocationSchedules = List(Instance("iec61970.generation.production.FuelAllocationSchedule.FuelAllocationSchedule"))
    # A thermal generating unit may have a heat input curve
    HeatInputCurve = Instance("iec61970.generation.production.HeatInputCurve.HeatInputCurve")
    # A thermal generating unit may have a heat rate curve
    HeatRateCurve = Instance("iec61970.generation.production.HeatRateCurve.HeatRateCurve")
    # A thermal generating unit may have an incremental heat rate curve
    IncrementalHeatRateCurve = Instance("iec61970.generation.production.IncrementalHeatRateCurve.IncrementalHeatRateCurve")
    # A thermal generating unit may have a shutdown curve
    ShutdownCurve = Instance("iec61970.generation.production.ShutdownCurve.ShutdownCurve")
    # A thermal generating unit may have a startup model
    StartupModel = Instance("iec61970.generation.production.StartupModel.StartupModel")
    # A thermal generating unit may be a member of a compressed air energy storage plant
    MemberOf_CAESPlant = Instance("iec61970.generation.production.CAESPlant.CAESPlant")
    # A thermal generating unit may be a member of a cogeneration plant
    MemberOf_CogenerationPlant = Instance("iec61970.generation.production.CogenerationPlant.CogenerationPlant")
    # A thermal generating unit may be a member of a combined cycle plant
    MemberOf_CombinedCyclePlant = Instance("iec61970.generation.production.CombinedCyclePlant.CombinedCyclePlant")
    # Operating and maintenance cost for the thermal unit
    oMCost = CostPerHeatUnit

class HydroGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)
    """
    # A hydro generating unit has an efficiency curve
    HydroGeneratingEfficiencyCurves = List(Instance("iec61970.generation.production.HydroGeneratingEfficiencyCurve.HydroGeneratingEfficiencyCurve"))
    # A hydro generating unit has a penstock loss curve
    PenstockLossCurve = Instance("iec61970.generation.production.PenstockLossCurve.PenstockLossCurve")
    # A hydro generating unit has a tailbay loss curve
    TailbayLossCurve = List(Instance("iec61970.generation.production.TailbayLossCurve.TailbayLossCurve"))
    # The hydro generating unit belongs to a hydro power plant
    MemberOf_HydroPowerPlant = Instance("iec61970.generation.production.HydroPowerPlant.HydroPowerPlant", allow_none=False)
    # The equivalent cost of water that drives the hydro turbine, expressed as (dollars/hour) per (cubic meters/second)
    hydroUnitWaterCost = Float

class EmissionAccount(AccountBalance):
    """ Accounts for tracking emissions usage and credits for thermal generating units. A unit may have zero or more emission accounts, and will typically have one for tracking usage and one for tracking credits.
    """
    # A thermal generating unit may have one or more emission allowance accounts
    ThermalGeneratingUnit = Instance("iec61970.generation.production.ThermalGeneratingUnit.ThermalGeneratingUnit", allow_none=False)
    # The type of emission, for example sulfur dioxide (SO2). The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide).
    emissionType = EmissionType
    # The source of the emission value: Measured or Calculated
    emissionValueSource = EmissionValueSource


