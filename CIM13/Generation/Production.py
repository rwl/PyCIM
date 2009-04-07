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

from CIM13.Core import Equipment
from CIM13.Core import Curve
from CIM13.Core import PowerSystemResource
from CIM13.Core import IdentifiedObject
from CIM13.Core import RegularIntervalSchedule



from enthought.traits.api import Instance, List, Enum, Float, Bool, Int, Str
# <<< imports

# >>> imports

#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


EmissionValueSource = Enum("calculated", "measured")

FuelType = Enum("coal", "gas", "oil")

SpillwayGateType = Str

EmissionType = Enum("hydrogenSulfide", "sulfurDioxide", "chlorine", "carbonDioxide", "carbonDisulfide", "nitrogenOxide")

GeneratorOperatingMode = Enum("REG", "Off", "LFC", "MRN", "AGC", "Fixed", "EDC", "Manual")

PenstockType = Str

GeneratorControlSource = Enum("Unavailable", "offAGC", "PlantControl", "onAGC")

HydroPlantType = Enum("runOfRiver", "majorStorage", "pumpedStorage", "minorStorage")

GeneratorControlMode = Enum("pulse", "setpoint")

SurgeTankCode = Str

HydroEnergyConversionKind = Enum("generator", "pumpAndGenerator")

#------------------------------------------------------------------------------
#  "GeneratingUnit" class:
#------------------------------------------------------------------------------

class GeneratingUnit(Equipment):
    """ A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ControlAreaGeneratingUnit = List(Instance("CIM13.ControlArea.ControlAreaGeneratingUnit"))

    # A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
    GrossToNetActivePowerCurves = List(Instance("CIM13.Generation.Production.GrossToNetActivePowerCurve"))

    # A synchronous machine may operate as a generator and as such becomes a member of a generating unit
    Contains_SynchronousMachines = List(Instance("CIM13.Wires.SynchronousMachine"))

    # A generating unit may have an operating schedule, indicating the planned operation of the unit
    GenUnitOpSchedule = Instance("CIM13.Generation.Production.GenUnitOpSchedule")

    # A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
    GenUnitOpCostCurves = List(Instance("CIM13.Generation.Production.GenUnitOpCostCurve"))

    # The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity
    ratedNetMaxP = Float

    # Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental Transmission Loss expressed as a plus or minus value. The typical range of penalty factors is (0.9 to 1.1).
    penaltyFactor = Float

    stepChange = Float

    energyMinP = Float

    # The efficiency of the unit in converting mechanical energy, from the prime mover, into electrical energy.
    efficiency = Float

    raiseRampRate = Float

    dispReserveFlag = Bool

    # The initial startup cost incurred for each start of the GeneratingUnit.
    startupCost = Float

    # High limit for secondary (AGC) control
    highControlLimit = Float

    spinReserveRamp = Float

    # Pulse low limit which is the smallest control pulse that the unit can respond to
    controlPulseLow = Float

    # The source of controls for a generating unit.
    genControlSource = GeneratorControlSource

    # Governor Speed Changer Droop
    governorSCD = Float

    # For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits.
    baseP = Float

    fuelPriority = Int

    # This is the maximum operating active power limit the dispatcher can enter for this unit
    maxOperatingP = Float

    # The unit control mode.
    genControlMode = GeneratorControlMode

    # The variable cost component of production per unit of ActivePower.
    variableCost = Float

    # Low limit for secondary (AGC) control
    lowControlLimit = Float

    # Pulse high limit which is the largest control pulse that the unit can respond to
    controlPulseHigh = Float

    # Maximum high economic active power limit, that should not exceed the maximum operating active power limit
    maxEconomicP = Float

    # Unit control error deadband. When a unit's desired active power change is less than this deadband, then no control pulses will be sent to the unit.
    controlDeadband = Float

    # Governor Motor Position Limit
    governorMPL = Float

    # Low economic active power limit that must be greater than or equal to the minimum operating active power limit
    minEconomicP = Float

    # This is the minimum operating active power limit the dispatcher can enter for this unit.
    minOperatingP = Float

    # Unit response rate which specifies the active power change for a control pulse of one second in the most responsive loading level of the unit.
    controlResponseRate = Float

    # Detail level of the generator model data
    modelDetail = Int

    # The planned unused capacity which can be used to support automatic control overruns.
    autoCntrlMarginP = Float

    # The unit's gross rated maximum capacity (Book Value).
    ratedGrossMaxP = Float

    # Operating mode for secondary control.
    genOperatingMode = GeneratorOperatingMode

    fastStartFlag = Bool

    # Generating unit economic participation factor
    longPF = Float

    # Generating unit economic participation factor
    normalPF = Float

    # Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.
    maximumAllowableSpinningReserve = Float

    # The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid
    ratedGrossMinP = Float

    # The planned unused capacity (spinning reserve) which can be used to support emergency load
    allocSpinResP = Float

    # Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied
    startupTime = Float

    # Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration
    initialP = Float

    # Generating unit economic participation factor
    tieLinePF = Float

    # Minimum time interval between unit shutdown and startup
    minimumOffTime = Float

    lowerRampRate = Float

    # Generating unit economic participation factor
    shortPF = Float

    #--------------------------------------------------------------------------
    #  Begin generatingUnit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End generatingUnit user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StartIgnFuelCurve" class:
#------------------------------------------------------------------------------

class StartIgnFuelCurve(Curve):
    """ The quantity of ignition fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The unit's startup model may have a startup ignition fuel curve
    StartupModel = Instance("CIM13.Generation.Production.StartupModel")

    # Type of ignition fuel
    ignitionFuelType = FuelType

    #--------------------------------------------------------------------------
    #  Begin startIgnFuelCurve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End startIgnFuelCurve user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "HydroGeneratingEfficiencyCurve" class:
#------------------------------------------------------------------------------

class HydroGeneratingEfficiencyCurve(Curve):
    """ Relationship between unit efficiency in percent and unit output active power for a given net head in meters. The relationship between efficiency, discharge, head, and power output is expressed as follows:   E =KP/HQ Where:  (E=percentage)  (P=active power)  (H=height)  (Q=volume/time unit)  (K=constant) For example, a curve instance for a given net head could relate efficiency (Y-axis) versus active power output (X-axis) or versus discharge on the X-axis.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A hydro generating unit has an efficiency curve
    HydroGeneratingUnit = Instance("CIM13.Generation.Production.HydroGeneratingUnit")

    #--------------------------------------------------------------------------
    #  Begin hydroGeneratingEfficiencyCurve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End hydroGeneratingEfficiencyCurve user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TargetLevelSchedule" class:
#------------------------------------------------------------------------------

class TargetLevelSchedule(Curve):
    """ Reservoir water level targets from advanced studies or 'rule curves'. Typically in one hour increments for up to 10 days
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A reservoir may have a water level target schedule.
    Reservoir = Instance("CIM13.Generation.Production.Reservoir")

    # Low target level limit, below which the reservoir operation will be penalized
    lowLevelLimit = Float

    # High target level limit, above which the reservoir operation will be penalized
    highLevelLimit = Float

    #--------------------------------------------------------------------------
    #  Begin targetLevelSchedule user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End targetLevelSchedule user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GrossToNetActivePowerCurve" class:
#------------------------------------------------------------------------------

class GrossToNetActivePowerCurve(Curve):
    """ Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
    GeneratingUnit = Instance("CIM13.Generation.Production.GeneratingUnit")

    #--------------------------------------------------------------------------
    #  Begin grossToNetActivePowerCurve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End grossToNetActivePowerCurve user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "IncrementalHeatRateCurve" class:
#------------------------------------------------------------------------------

class IncrementalHeatRateCurve(Curve):
    """ Relationship between unit incremental heat rate in (delta energy/time) per (delta active power) and unit output in active power. The IHR curve represents the slope of the HeatInputCurve. Note that the 'incremental heat rate' and the 'heat rate' have the same engineering units.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A thermal generating unit may have an incremental heat rate curve
    ThermalGeneratingUnit = Instance("CIM13.Generation.Production.ThermalGeneratingUnit")

    # Flag is set to true when output is expressed in net active power
    isNetGrossP = Bool

    #--------------------------------------------------------------------------
    #  Begin incrementalHeatRateCurve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End incrementalHeatRateCurve user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "HeatInputCurve" class:
#------------------------------------------------------------------------------

class HeatInputCurve(Curve):
    """ Relationship between unit heat input in energy per time for main fuel (Y1-axis) and supplemental fuel (Y2-axis) versus unit output in active power (X-axis). The quantity of main fuel used to sustain generation at this output level is prorated for throttling between definition points. The quantity of supplemental fuel used at this output level is fixed and not prorated.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A thermal generating unit may have a heat input curve
    ThermalGeneratingUnit = Instance("CIM13.Generation.Production.ThermalGeneratingUnit")

    # Power output - auxiliary power offset adjustment factor
    auxPowerOffset = Float

    # Heat input - offset adjustment factor.
    heatInputOffset = Float

    # Power output - auxiliary power multiplier adjustment factor.
    auxPowerMult = Float

    # Heat input - efficiency multiplier adjustment factor.
    heatInputEff = Float

    # Flag is set to true when output is expressed in net active power
    isNetGrossP = Bool

    #--------------------------------------------------------------------------
    #  Begin heatInputCurve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End heatInputCurve user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StartRampCurve" class:
#------------------------------------------------------------------------------

class StartRampCurve(Curve):
    """ Rate in gross active power/minute (Y-axis) at which a unit can be loaded versus the number of hours (X-axis) the unit was off line
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The unit's startup model may have a startup ramp curve
    StartupModel = Instance("CIM13.Generation.Production.StartupModel")

    # The startup ramp rate in gross for a unit that is on hot standby
    hotStandbyRamp = Float

    #--------------------------------------------------------------------------
    #  Begin startRampCurve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End startRampCurve user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AirCompressor" class:
#------------------------------------------------------------------------------

class AirCompressor(PowerSystemResource):
    """ Combustion turbine air compressor which is an integral part of a compressed air energy storage (CAES) plant
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A CAES air compressor is driven by combustion turbine
    DrivenBy_CombustionTurbine = Instance("CIM13.Generation.GenerationDynamics.CombustionTurbine")

    # An air compressor may be a member of a compressed air energy storage plant
    MemberOf_CAESPlant = Instance("CIM13.Generation.Production.CAESPlant")

    # Rating of the CAES air compressor
    airCompressorRating = Float

    #--------------------------------------------------------------------------
    #  Begin airCompressor user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End airCompressor user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ShutdownCurve" class:
#------------------------------------------------------------------------------

class ShutdownCurve(Curve):
    """ Relationship between the rate in gross active power/minute (Y-axis) at which a unit should be shutdown and its present gross MW output (X-axis)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A thermal generating unit may have a shutdown curve
    ThermalGeneratingUnit = Instance("CIM13.Generation.Production.ThermalGeneratingUnit")

    # Fixed shutdown cost
    shutdownCost = Float

    # The date and time of the most recent generating unit shutdown
    shutdownDate = Str

    #--------------------------------------------------------------------------
    #  Begin shutdownCurve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End shutdownCurve user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CombinedCyclePlant" class:
#------------------------------------------------------------------------------

class CombinedCyclePlant(PowerSystemResource):
    """ A set of combustion turbines and steam turbines where the exhaust heat from the combustion turbines is recovered to make steam for the steam turbines, resulting in greater overall plant efficiency
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A thermal generating unit may be a member of a combined cycle plant
    Contain_ThermalGeneratingUnits = List(Instance("CIM13.Generation.Production.ThermalGeneratingUnit"))

    # The combined cycle plant's active power output rating
    combCyclePlantRating = Float

    #--------------------------------------------------------------------------
    #  Begin combinedCyclePlant user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End combinedCyclePlant user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StartupModel" class:
#------------------------------------------------------------------------------

class StartupModel(IdentifiedObject):
    """ Unit start up characteristics depending on how long the unit has been off line
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The unit's startup model may have a startup ignition fuel curve
    StartIgnFuelCurve = Instance("CIM13.Generation.Production.StartIgnFuelCurve")

    # The unit's startup model may have a startup ramp curve
    StartRampCurve = Instance("CIM13.Generation.Production.StartRampCurve")

    # The unit's startup model may have a startup main fuel curve
    StartMainFuelCurve = Instance("CIM13.Generation.Production.StartMainFuelCurve")

    # A thermal generating unit may have a startup model
    ThermalGeneratingUnit = Instance("CIM13.Generation.Production.ThermalGeneratingUnit")

    # The minimum number of hours the unit must be operating before being allowed to shut down
    minimumRunTime = Float

    # The date and time of the most recent generating unit startup
    startupDate = Str

    # The minimum number of hours the unit must be down before restart
    minimumDownTime = Float

    # Startup priority within control area where lower numbers indicate higher priorities.  More than one unit in an area may be assigned the same priority.
    startupPriority = Int

    # The unit's auxiliary active power consumption to maintain standby mode
    stbyAuxP = Float

    # Total miscellaneous start up costs
    startupCost = Float

    # The amount of heat input per time uint required for hot standby operation
    hotStandbyHeat = Float

    # The opportunity cost associated with the return in monetary unit. This represents the restart's 'share' of the unit depreciation and risk of an event which would damage the unit.
    riskFactorCost = Float

    # Fixed Maintenance Cost
    fixedMaintCost = Float

    # Incremental Maintenance Cost
    incrementalMaintCost = Float

    #--------------------------------------------------------------------------
    #  Begin startupModel user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End startupModel user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "HydroPump" class:
#------------------------------------------------------------------------------

class HydroPump(PowerSystemResource):
    """ A synchronous motor-driven pump, typically associated with a pumped storage plant
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The hydro pump may be a member of a pumped storage plant or a pump for distributing water
    MemberOf_HydroPowerPlant = Instance("CIM13.Generation.Production.HydroPowerPlant")

    # The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
    HydroPumpOpSchedule = Instance("CIM13.Generation.Production.HydroPumpOpSchedule")

    # The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
    DrivenBy_SynchronousMachine = Instance("CIM13.Wires.SynchronousMachine")

    # The pumping power under minimum head conditions, usually at full gate.
    pumpPowerAtMinHead = Float

    # The pumping discharge (m3/sec) under maximum head conditions, usually at full gate
    pumpDischAtMaxHead = Float

    # The pumping discharge (m3/sec) under minimum head conditions, usually at full gate
    pumpDischAtMinHead = Float

    # The pumping power under maximum head conditions, usually at full gate
    pumpPowerAtMaxHead = Float

    #--------------------------------------------------------------------------
    #  Begin hydroPump user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End hydroPump user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EmissionCurve" class:
#------------------------------------------------------------------------------

class EmissionCurve(Curve):
    """ Relationship between the unit's emission rate in units of mass per hour (Y-axis) and output active power (X-axis) for a given type of emission. This curve applies when only one type of fuel is being burned.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A thermal generating unit may have  one or more emission curves
    ThermalGeneratingUnit = Instance("CIM13.Generation.Production.ThermalGeneratingUnit")

    # Flag is set to true when output is expressed in net active power
    isNetGrossP = Bool

    # The type of emission, which also gives the production rate measurement unit. The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide).
    emissionType = EmissionType

    # The emission content per quantity of fuel burned
    emissionContent = Float

    #--------------------------------------------------------------------------
    #  Begin emissionCurve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End emissionCurve user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GenUnitOpCostCurve" class:
#------------------------------------------------------------------------------

class GenUnitOpCostCurve(Curve):
    """ Relationship between unit operating cost (Y-axis) and unit output active power (X-axis). The operating cost curve for thermal units is derived from heat input and fuel costs. The operating cost curve for hydro units is derived from water flow rates and equivalent water costs.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
    GeneratingUnit = Instance("CIM13.Generation.Production.GeneratingUnit")

    # Flag is set to true when output is expressed in net active power
    isNetGrossP = Bool

    #--------------------------------------------------------------------------
    #  Begin genUnitOpCostCurve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End genUnitOpCostCurve user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "HydroPowerPlant" class:
#------------------------------------------------------------------------------

class HydroPowerPlant(PowerSystemResource):
    """ A hydro power station which can generate or pump. When generating, the generator turbines receive there water from an upper reservoir. When pumping, the pumps receive their water from a lower reservoir.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The hydro generating unit belongs to a hydro power plant
    Contain_HydroGeneratingUnits = List(Instance("CIM13.Generation.Production.HydroGeneratingUnit"))

    # Generators discharge water to or pumps are supplied water from a downstream reservoir
    Reservoir = Instance("CIM13.Generation.Production.Reservoir")

    # Generators are supplied water from or pumps discharge water to an upstream reservoir
    GenSourcePumpDischarge = Instance("CIM13.Generation.Production.Reservoir")

    # The hydro pump may be a member of a pumped storage plant or a pump for distributing water
    Contain_HydroPumps = List(Instance("CIM13.Generation.Production.HydroPump"))

    # Water travel delay from tailbay to next downstream hydro power station
    dischargeTravelDelay = Float

    # The hydro plant's pumping rating active power for rated head conditions
    pumpRatedP = Float

    # Type and configuration of hydro plant penstock(s)
    penstockType = PenstockType

    # The plant's rated gross head in meters
    plantRatedHead = Float

    # Total plant discharge capacity in cubic meters per second
    plantDischargeCapacity = Float

    # The type of hydro power plant.
    hydroPlantType = HydroPlantType

    # A code describing the type (or absence) of surge tank that is associated with the hydro power plant
    surgeTankCode = SurgeTankCode

    # The hydro plant's generating rating active power for rated head conditions
    genRatedP = Float

    # The level at which the surge tank spills
    surgeTankCrestLevel = Float

    #--------------------------------------------------------------------------
    #  Begin hydroPowerPlant user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End hydroPowerPlant user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CAESPlant" class:
#------------------------------------------------------------------------------

class CAESPlant(PowerSystemResource):
    """ Compressed air energy storage plant
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An air compressor may be a member of a compressed air energy storage plant
    Contain_AirCompressor = Instance("CIM13.Generation.Production.AirCompressor")

    # A thermal generating unit may be a member of a compressed air energy storage plant
    Contain_ThermalGeneratingUnit = Instance("CIM13.Generation.Production.ThermalGeneratingUnit")

    # The CAES plant's gross rated generating capacity
    ratedCapacityP = Float

    # The rated energy storage capacity.
    energyStorageCapacity = Float

    #--------------------------------------------------------------------------
    #  Begin cAESPlant user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End cAESPlant user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LevelVsVolumeCurve" class:
#------------------------------------------------------------------------------

class LevelVsVolumeCurve(Curve):
    """ Relationship between reservoir volume and reservoir level. The  volume is at the y-axis and the reservoir level at the x-axis.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A reservoir may have a level versus volume relationship.
    Reservoir = Instance("CIM13.Generation.Production.Reservoir")

    #--------------------------------------------------------------------------
    #  Begin levelVsVolumeCurve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End levelVsVolumeCurve user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "InflowForecast" class:
#------------------------------------------------------------------------------

class InflowForecast(RegularIntervalSchedule):
    """ Natural water inflow to a reservoir, usually forecasted from predicted rain and snowmelt. Typically in one hour increments for up to 10 days. The forecast is given in average cubic meters per second over the time increment.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A reservoir may have a 'natural' inflow forecast.
    Reservoir = Instance("CIM13.Generation.Production.Reservoir")

    #--------------------------------------------------------------------------
    #  Begin inflowForecast user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End inflowForecast user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SteamSendoutSchedule" class:
#------------------------------------------------------------------------------

class SteamSendoutSchedule(RegularIntervalSchedule):
    """ The cogeneration plant's steam sendout schedule in volume per time unit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A cogeneration plant has a steam sendout schedule
    CogenerationPlant = Instance("CIM13.Generation.Production.CogenerationPlant")

    #--------------------------------------------------------------------------
    #  Begin steamSendoutSchedule user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End steamSendoutSchedule user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FossilFuel" class:
#------------------------------------------------------------------------------

class FossilFuel(IdentifiedObject):
    """ The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gas
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A fuel allocation schedule must have a fossil fuel
    FuelAllocationSchedule = List(Instance("CIM13.Generation.Production.FuelAllocationSchedule"))

    # A thermal generating unit may have one or more fossil fuels
    ThermalGeneratingUnit = Instance("CIM13.Generation.Production.ThermalGeneratingUnit")

    # The type of fossil fuel, such as coal, oil, or gas.
    fossilFuelType = FuelType

    # The active power output level of the unit at which the given type of fuel is switched off. This fuel (e.g., oil) is sometimes used to stabilize the base fuel (e.g., coal) at low active power output levels.
    lowBreakpointP = Float

    # The cost of fuel used for economic dispatching which includes: fuel cost, transportation cost,  and incremental maintenance cost
    fuelDispatchCost = Float

    # The efficiency factor for the fuel (per unit) in terms of the effective energy absorbed
    fuelEffFactor = Float

    # The cost in terms of heat value for the given type of fuel
    fuelCost = Float

    # The amount of heat per weight (or volume) of the given type of fuel
    fuelHeatContent = Float

    # Handling and processing cost associated with this fuel
    fuelHandlingCost = Float

    # Relative amount of the given type of fuel, when multiple fuels are being consumed.
    fuelMixture = Float

    # The active power output level of the unit at which the given type of fuel is switched on. This fuel (e.g., oil) is sometimes used to supplement the base fuel (e.g., coal) at high active power output levels.
    highBreakpointP = Float

    # The fuel's fraction of pollution credit per unit of heat content
    fuelSulfur = Float

    #--------------------------------------------------------------------------
    #  Begin fossilFuel user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End fossilFuel user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FuelAllocationSchedule" class:
#------------------------------------------------------------------------------

class FuelAllocationSchedule(Curve):
    """ The amount of fuel of a given type which is allocated for consumption over a specified period of time
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A fuel allocation schedule must have a fossil fuel
    FossilFuel = Instance("CIM13.Generation.Production.FossilFuel")

    # A thermal generating unit may have one or more fuel allocation schedules
    ThermalGeneratingUnit = Instance("CIM13.Generation.Production.ThermalGeneratingUnit")

    # The minimum amount fuel that is allocated for consumption for the scheduled time period, e.g., based on a 'take-or-pay' contract
    minFuelAllocation = Float

    # The start time and date of the fuel allocation schedule
    fuelAllocationStartDate = Str

    # The end time and date of the fuel allocation schedule
    fuelAllocationEndDate = Str

    # The type of fuel, which also indicates the corresponding measurement unit
    fuelType = FuelType

    # The maximum amount fuel that is allocated for consumption for the scheduled time period
    maxFuelAllocation = Float

    #--------------------------------------------------------------------------
    #  Begin fuelAllocationSchedule user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End fuelAllocationSchedule user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EmissionAccount" class:
#------------------------------------------------------------------------------

class EmissionAccount(Curve):
    """ Accounts for tracking emissions usage and credits for thermal generating units. A unit may have zero or more emission accounts, and will typically have one for tracking usage and one for tracking credits.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A thermal generating unit may have one or more emission allowance accounts
    ThermalGeneratingUnit = Instance("CIM13.Generation.Production.ThermalGeneratingUnit")

    # The type of emission, for example sulfur dioxide (SO2). The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide).
    emissionType = EmissionType

    # The source of the emission value.
    emissionValueSource = EmissionValueSource

    #--------------------------------------------------------------------------
    #  Begin emissionAccount user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End emissionAccount user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TailbayLossCurve" class:
#------------------------------------------------------------------------------

class TailbayLossCurve(Curve):
    """ Relationship between tailbay head loss hight (y-axis) and the total discharge into the power station's tailbay volume per time unit (x-axis) . There could be more than one curve depending on the level of the tailbay reservoir or river level
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A hydro generating unit has a tailbay loss curve
    HydroGeneratingUnit = Instance("CIM13.Generation.Production.HydroGeneratingUnit")

    #--------------------------------------------------------------------------
    #  Begin tailbayLossCurve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End tailbayLossCurve user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PenstockLossCurve" class:
#------------------------------------------------------------------------------

class PenstockLossCurve(Curve):
    """ Relationship between penstock head loss (in meters) and  total discharge through the penstock (in cubic meters per second). One or more turbines may be connected to the same penstock.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A hydro generating unit has a penstock loss curve
    HydroGeneratingUnit = Instance("CIM13.Generation.Production.HydroGeneratingUnit")

    #--------------------------------------------------------------------------
    #  Begin penstockLossCurve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End penstockLossCurve user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StartMainFuelCurve" class:
#------------------------------------------------------------------------------

class StartMainFuelCurve(Curve):
    """ The quantity of main fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The unit's startup model may have a startup main fuel curve
    StartupModel = Instance("CIM13.Generation.Production.StartupModel")

    # Type of main fuel
    mainFuelType = FuelType

    #--------------------------------------------------------------------------
    #  Begin startMainFuelCurve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End startMainFuelCurve user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Reservoir" class:
#------------------------------------------------------------------------------

class Reservoir(PowerSystemResource):
    """ A water storage facility within a hydro system, including: ponds, lakes, lagoons, and rivers. The storage is usually behind some type of dam.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A reservoir may spill into a downstream reservoir
    SpillsFrom = Instance("CIM13.Generation.Production.Reservoir")

    # A reservoir may have a level versus volume relationship.
    LevelVsVolumeCurve = List(Instance("CIM13.Generation.Production.LevelVsVolumeCurve"))

    # A reservoir may have a 'natural' inflow forecast.
    InflowForecast = List(Instance("CIM13.Generation.Production.InflowForecast"))

    # A reservoir may spill into a downstream reservoir
    SpillsInto = List(Instance("CIM13.Generation.Production.Reservoir"))

    # Generators discharge water to or pumps are supplied water from a downstream reservoir
    HydroPowerPlants = List(Instance("CIM13.Generation.Production.HydroPowerPlant"))

    # Generators are supplied water from or pumps discharge water to an upstream reservoir
    UpstreamFrom = List(Instance("CIM13.Generation.Production.HydroPowerPlant"))

    # A reservoir may have a water level target schedule.
    TargetLevelSchedule = Instance("CIM13.Generation.Production.TargetLevelSchedule")

    # River outlet works for riparian right releases or other purposes
    riverOutletWorks = Str

    # Type of spillway gate, including parameters
    spillWayGateType = SpillwayGateType

    # The flow capacity of the spillway in cubic meters per second
    spillwayCapacity = Float

    # The length of the spillway crest in meters
    spillwayCrestLength = Float

    # Storage volume between the full supply level and the normal minimum operating level
    activeStorageCapacity = Float

    # The spillway water travel delay to the next downstream reservoir
    spillTravelDelay = Float

    # The reservoir's energy storage rating in energy for given head conditions
    energyStorageRating = Float

    # Total capacity of reservoir
    grossCapacity = Float

    # Spillway crest level above which water will spill
    spillwayCrestLevel = Float

    # Full supply level, above which water will spill. This can be the spillway crest level or the top of closed gates.
    fullSupplyLevel = Float

    # Normal minimum operating level below which the penstocks will draw air
    normalMinOperateLevel = Float

    #--------------------------------------------------------------------------
    #  Begin reservoir user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End reservoir user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "HydroPumpOpSchedule" class:
#------------------------------------------------------------------------------

class HydroPumpOpSchedule(RegularIntervalSchedule):
    """ The hydro pump's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses.The unit's operating schedule status is typically given as: (0=unavailable)  (1=avilable to startup or shutdown)  (2=must pump)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
    HydroPump = Instance("CIM13.Generation.Production.HydroPump")

    #--------------------------------------------------------------------------
    #  Begin hydroPumpOpSchedule user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End hydroPumpOpSchedule user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "HeatRateCurve" class:
#------------------------------------------------------------------------------

class HeatRateCurve(Curve):
    """ Relationship between unit heat rate per active power (Y-axis) and  unit output (X-axis). The heat input is from all fuels.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A thermal generating unit may have a heat rate curve
    ThermalGeneratingUnit = Instance("CIM13.Generation.Production.ThermalGeneratingUnit")

    # Flag is set to true when output is expressed in net active power
    isNetGrossP = Bool

    #--------------------------------------------------------------------------
    #  Begin heatRateCurve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End heatRateCurve user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GenUnitOpSchedule" class:
#------------------------------------------------------------------------------

class GenUnitOpSchedule(RegularIntervalSchedule):
    """ The generating unit's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses. The X-axis represents absolute time. The Y1-axis represents the status (0=off-line and unavailable: 1=available: 2=must run: 3=must run at fixed power value: etc.). The Y2-axis represents the must run fixed power value where required.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A generating unit may have an operating schedule, indicating the planned operation of the unit
    GeneratingUnit = Instance("CIM13.Generation.Production.GeneratingUnit")

    #--------------------------------------------------------------------------
    #  Begin genUnitOpSchedule user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End genUnitOpSchedule user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CogenerationPlant" class:
#------------------------------------------------------------------------------

class CogenerationPlant(PowerSystemResource):
    """ A set of thermal generating units for the production of electrical energy and process steam (usually from the output of the steam turbines). The steam sendout is typically used for industrial purposes or for municipal heating and cooling.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A thermal generating unit may be a member of a cogeneration plant
    Contain_ThermalGeneratingUnits = List(Instance("CIM13.Generation.Production.ThermalGeneratingUnit"))

    # A cogeneration plant has a steam sendout schedule
    SteamSendoutSchedule = Instance("CIM13.Generation.Production.SteamSendoutSchedule")

    # The high pressure steam rating
    cogenHPSteamRating = Float

    # The rated output active power of the cogeneration plant
    ratedP = Float

    # The low pressure steam sendout
    cogenLPSendoutRating = Float

    # The high pressure steam sendout
    cogenHPSendoutRating = Float

    # The low pressure steam rating
    cogenLPSteamRating = Float

    #--------------------------------------------------------------------------
    #  Begin cogenerationPlant user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End cogenerationPlant user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "NuclearGeneratingUnit" class:
#------------------------------------------------------------------------------

class NuclearGeneratingUnit(GeneratingUnit):
    """ A nuclear generating unit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin nuclearGeneratingUnit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End nuclearGeneratingUnit user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "HydroGeneratingUnit" class:
#------------------------------------------------------------------------------

class HydroGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A hydro generating unit has an efficiency curve
    HydroGeneratingEfficiencyCurves = List(Instance("CIM13.Generation.Production.HydroGeneratingEfficiencyCurve"))

    # A hydro generating unit has a tailbay loss curve
    TailbayLossCurve = List(Instance("CIM13.Generation.Production.TailbayLossCurve"))

    # The hydro generating unit belongs to a hydro power plant
    MemberOf_HydroPowerPlant = Instance("CIM13.Generation.Production.HydroPowerPlant")

    # A hydro generating unit has a penstock loss curve
    PenstockLossCurve = Instance("CIM13.Generation.Production.PenstockLossCurve")

    # Energy conversion capability for generating.
    energyConversionCapability = HydroEnergyConversionKind

    # The equivalent cost of water that drives the hydro turbine, expressed as cost per volume.
    hydroUnitWaterCost = Float

    #--------------------------------------------------------------------------
    #  Begin hydroGeneratingUnit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End hydroGeneratingUnit user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ThermalGeneratingUnit" class:
#------------------------------------------------------------------------------

class ThermalGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A thermal generating unit may be a member of a cogeneration plant
    MemberOf_CogenerationPlant = Instance("CIM13.Generation.Production.CogenerationPlant")

    # A thermal generating unit may have one or more fuel allocation schedules
    FuelAllocationSchedules = List(Instance("CIM13.Generation.Production.FuelAllocationSchedule"))

    # A thermal generating unit may have  one or more emission curves
    EmissionCurves = List(Instance("CIM13.Generation.Production.EmissionCurve"))

    # A thermal generating unit may have one or more emission allowance accounts
    EmmissionAccounts = List(Instance("CIM13.Generation.Production.EmissionAccount"))

    # A thermal generating unit may have a startup model
    StartupModel = Instance("CIM13.Generation.Production.StartupModel")

    # A thermal generating unit may have one or more fossil fuels
    FossilFuels = List(Instance("CIM13.Generation.Production.FossilFuel"))

    # A thermal generating unit may have an incremental heat rate curve
    IncrementalHeatRateCurve = Instance("CIM13.Generation.Production.IncrementalHeatRateCurve")

    # A thermal generating unit may have a shutdown curve
    ShutdownCurve = Instance("CIM13.Generation.Production.ShutdownCurve")

    # A thermal generating unit may have a heat rate curve
    HeatRateCurve = Instance("CIM13.Generation.Production.HeatRateCurve")

    # A thermal generating unit may be a member of a compressed air energy storage plant
    MemberOf_CAESPlant = Instance("CIM13.Generation.Production.CAESPlant")

    # A thermal generating unit may have a heat input curve
    HeatInputCurve = Instance("CIM13.Generation.Production.HeatInputCurve")

    # A thermal generating unit may be a member of a combined cycle plant
    MemberOf_CombinedCyclePlant = Instance("CIM13.Generation.Production.CombinedCyclePlant")

    # Operating and maintenance cost for the thermal unit
    oMCost = Float

    #--------------------------------------------------------------------------
    #  Begin thermalGeneratingUnit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End thermalGeneratingUnit user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
