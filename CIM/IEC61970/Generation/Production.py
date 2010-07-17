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

""" The production package is responsible for classes which describe various kinds of generators. These classes also provide production costing information which is used to economically allocate demand among committed units and calculate reserve quantities.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61970.Core import Curve
from CIM.IEC61970.Core import Equipment
from CIM.IEC61970.Core import PowerSystemResource
from CIM.IEC61970.Core import RegularIntervalSchedule
from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61970.Domain import Money
from CIM.IEC61970.Domain import ActivePower
from CIM.IEC61970.Domain import Seconds
from CIM.IEC61970.Domain import ActivePowerChangeRate
from CIM.IEC61970.Domain import PU
from CIM.IEC61970.Domain import PerCent
from CIM.IEC61970.Domain import Length
from CIM.IEC61970.Domain import Volume
from CIM.IEC61970.Domain import WaterLevel
from CIM.IEC61970.Domain import RealEnergy
from CIM.IEC61970.Domain import CostPerEnergyUnit
from CIM.IEC61970.Domain import CostRate
from CIM.IEC61970.Domain import Hours



from enthought.traits.api import Instance, List, Property, Int, Float, Enum, Bool, Str, Date
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------
Classification = Int(0, desc="http://www.w3.org/2001/XMLSchema#integer1..n, with 1 the most detailed, highest priority, etc.")
CostPerHeatUnit = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatCost, in units of currency, per quantity of heat generated")
HeatRate = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatHeat generated, in energy pertime unit of elapsed time")
Emission = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatQuantity of emission per fuel heat content")

# The type of hydro power plant.
HydroPlantType = Enum("majorStorage", "runOfRiver", "minorStorage", "pumpedStorage", desc="The type of hydro power plant.")
# The source of controls for a generating unit.
GeneratorControlSource = Enum("onAGC", "plantControl", "unavailable", "offAGC", desc="The source of controls for a generating unit.")
# Type (or absence) of surge tank that is associated with the hydro power plant.
SurgeTankCode = Str
# Specifies the capability of the hydro generating unit to convert energy as a generator or pump.
HydroEnergyConversionKind = Enum("generator", "pumpAndGenerator", desc="Specifies the capability of the hydro generating unit to convert energy as a generator or pump.")
# Operating mode for secondary generator control.
GeneratorOperatingMode = Enum("off", "AGC", "manual", "MRN", "LFC", "EDC", "fixed", "REG", desc="Operating mode for secondary generator control.")
# Type of hydro plant penstock.
PenstockType = Str
# Unit control modes.
GeneratorControlMode = Enum("setpoint", "pulse", desc="Unit control modes.")
# The type of emission
EmissionType = Enum("nitrogenOxide", "carbonDisulfide", "hydrogenSulfide", "sulfurDioxide", "chlorine", "carbonDioxide", desc="The type of emission")
# The source of the emission value.
EmissionValueSource = Enum("calculated", "measured", desc="The source of the emission value.")
# Type of spillway gate.
SpillwayGateType = Str
# Type of fuel.
FuelType = Enum("gas", "oil", "coal", "lignite", desc="Type of fuel.")

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
    HydroGeneratingUnit = Instance("CIM.IEC61970.Generation.Production.HydroGeneratingUnit",
        desc="A hydro generating unit has a penstock loss curve",
        transient=True,
        opposite="PenstockLossCurve",
        editor=InstanceEditor(name="_hydrogeneratingunits"))

    def _get_hydrogeneratingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.HydroGeneratingUnit" ]
        else:
            return []

    _hydrogeneratingunits = Property(fget=_get_hydrogeneratingunits)

    #--------------------------------------------------------------------------
    #  Begin "PenstockLossCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "HydroGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.PenstockLossCurve",
        title="PenstockLossCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PenstockLossCurve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GeneratingUnit" class:
#------------------------------------------------------------------------------

class GeneratingUnit(Equipment):
    """ A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A GenerationProvider operates one or more GeneratingUnits.
    OperatedBy_GenerationProvider = Instance("CIM.IEC61968.Informative.Financial.GenerationProvider",
        desc="A GenerationProvider operates one or more GeneratingUnits.",
        transient=True,
        opposite="GeneratingUnits",
        editor=InstanceEditor(name="_generationproviders"))

    def _get_generationproviders(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Financial.GenerationProvider" ]
        else:
            return []

    _generationproviders = Property(fget=_get_generationproviders)

    # ControlArea specifications for this generating unit.
    ControlAreaGeneratingUnit = List(Instance("CIM.IEC61970.ControlArea.ControlAreaGeneratingUnit"),
        desc="ControlArea specifications for this generating unit.")

    # A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
    GenUnitOpCostCurves = List(Instance("CIM.IEC61970.Generation.Production.GenUnitOpCostCurve"),
        desc="A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.")

    # A GeneratingUnit injects energy into a SubControlArea.
    SubControlArea = Instance("CIM.IEC61968.Informative.EnergyScheduling.SubControlArea",
        desc="A GeneratingUnit injects energy into a SubControlArea.",
        transient=True,
        opposite="GeneratingUnits",
        editor=InstanceEditor(name="_subcontrolareas"))

    def _get_subcontrolareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.SubControlArea" ]
        else:
            return []

    _subcontrolareas = Property(fget=_get_subcontrolareas)

    RegisteredGenerator = Instance("CIM.IEC61968.Informative.MarketOperations.RegisteredGenerator",
        transient=True,
        opposite="GeneratingUnit",
        editor=InstanceEditor(name="_registeredgenerators"))

    def _get_registeredgenerators(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.RegisteredGenerator" ]
        else:
            return []

    _registeredgenerators = Property(fget=_get_registeredgenerators)

    # A synchronous machine may operate as a generator and as such becomes a member of a generating unit
    SynchronousMachines = List(Instance("CIM.IEC61970.Wires.SynchronousMachine"),
        desc="A synchronous machine may operate as a generator and as such becomes a member of a generating unit")

    # A generating unit may have an operating schedule, indicating the planned operation of the unit
    GenUnitOpSchedule = Instance("CIM.IEC61970.Generation.Production.GenUnitOpSchedule",
        desc="A generating unit may have an operating schedule, indicating the planned operation of the unit",
        transient=True,
        opposite="GeneratingUnit",
        editor=InstanceEditor(name="_genunitopschedules"))

    def _get_genunitopschedules(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.GenUnitOpSchedule" ]
        else:
            return []

    _genunitopschedules = Property(fget=_get_genunitopschedules)

    # A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
    GrossToNetActivePowerCurves = List(Instance("CIM.IEC61970.Generation.Production.GrossToNetActivePowerCurve"),
        desc="A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit")

    # Operating mode for secondary control.
    genOperatingMode = GeneratorOperatingMode(desc="Operating mode for secondary control.")

    # The unit control mode.
    genControlMode = GeneratorControlMode(desc="The unit control mode.")

    # The source of controls for a generating unit.
    genControlSource = GeneratorControlSource(desc="The source of controls for a generating unit.")

    # The variable cost component of production per unit of ActivePower.
    variableCost = Money(desc="The variable cost component of production per unit of ActivePower.")

    # Generating unit economic participation factor
    shortPF = Float(desc="Generating unit economic participation factor")

    # The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid
    ratedGrossMinP = ActivePower(desc="The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid")

    # This is the maximum operating active power limit the dispatcher can enter for this unit
    maxOperatingP = ActivePower(desc="This is the maximum operating active power limit the dispatcher can enter for this unit")

    # Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.
    maximumAllowableSpinningReserve = ActivePower(desc="Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.")

    # Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied
    startupTime = Seconds(desc="Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied")

    # Generating unit economic participation factor
    longPF = Float(desc="Generating unit economic participation factor")

    # Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration
    initialP = ActivePower(desc="Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration")

    lowerRampRate = ActivePowerChangeRate

    # Minimum time interval between unit shutdown and startup
    minimumOffTime = Seconds(desc="Minimum time interval between unit shutdown and startup")

    spinReserveRamp = ActivePowerChangeRate

    fuelPriority = Int

    # The unit's gross rated maximum capacity (Book Value).
    ratedGrossMaxP = ActivePower(desc="The unit's gross rated maximum capacity (Book Value).")

    # Detail level of the generator model data
    modelDetail = Classification(desc="Detail level of the generator model data")

    # The efficiency of the unit in converting mechanical energy, from the prime mover, into electrical energy.
    efficiency = PU(desc="The efficiency of the unit in converting mechanical energy, from the prime mover, into electrical energy.")

    raiseRampRate = ActivePowerChangeRate

    # Generating unit economic participation factor
    tieLinePF = Float(desc="Generating unit economic participation factor")

    # Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental Transmission Loss expressed as a plus or minus value. The typical range of penalty factors is (0.9 to 1.1).
    penaltyFactor = Float(desc="Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental Transmission Loss expressed as a plus or minus value. The typical range of penalty factors is (0.9 to 1.1).")

    # This is the minimum operating active power limit the dispatcher can enter for this unit.
    minOperatingP = ActivePower(desc="This is the minimum operating active power limit the dispatcher can enter for this unit.")

    # The planned unused capacity which can be used to support automatic control overruns.
    autoCntrlMarginP = ActivePower(desc="The planned unused capacity which can be used to support automatic control overruns.")

    # Low economic active power limit that must be greater than or equal to the minimum operating active power limit
    minEconomicP = ActivePower(desc="Low economic active power limit that must be greater than or equal to the minimum operating active power limit")

    # Unit control error deadband. When a unit's desired active power change is less than this deadband, then no control pulses will be sent to the unit.
    controlDeadband = ActivePower(desc="Unit control error deadband. When a unit's desired active power change is less than this deadband, then no control pulses will be sent to the unit.")

    dispReserveFlag = Bool

    # Generating unit economic participation factor
    normalPF = Float(desc="Generating unit economic participation factor")

    # High limit for secondary (AGC) control
    highControlLimit = ActivePower(desc="High limit for secondary (AGC) control")

    # The planned unused capacity (spinning reserve) which can be used to support emergency load
    allocSpinResP = ActivePower(desc="The planned unused capacity (spinning reserve) which can be used to support emergency load")

    # Low limit for secondary (AGC) control
    lowControlLimit = ActivePower(desc="Low limit for secondary (AGC) control")

    # Governor Motor Position Limit
    governorMPL = PU(desc="Governor Motor Position Limit")

    # Pulse low limit which is the smallest control pulse that the unit can respond to
    controlPulseLow = Seconds(desc="Pulse low limit which is the smallest control pulse that the unit can respond to")

    fastStartFlag = Bool

    # The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute).
    nominalP = ActivePower(desc="The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute).")

    # For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits.
    baseP = ActivePower(desc="For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits.")

    # The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity
    ratedNetMaxP = ActivePower(desc="The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity")

    # Maximum high economic active power limit, that should not exceed the maximum operating active power limit
    maxEconomicP = ActivePower(desc="Maximum high economic active power limit, that should not exceed the maximum operating active power limit")

    # Unit response rate which specifies the active power change for a control pulse of one second in the most responsive loading level of the unit.
    controlResponseRate = ActivePowerChangeRate(desc="Unit response rate which specifies the active power change for a control pulse of one second in the most responsive loading level of the unit.")

    stepChange = ActivePower

    energyMinP = HeatRate

    # The initial startup cost incurred for each start of the GeneratingUnit.
    startupCost = Money(desc="The initial startup cost incurred for each start of the GeneratingUnit.")

    # Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency.
    governorSCD = PerCent(desc="Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency.")

    # Pulse high limit which is the largest control pulse that the unit can respond to
    controlPulseHigh = Seconds(desc="Pulse high limit which is the largest control pulse that the unit can respond to")

    #--------------------------------------------------------------------------
    #  Begin "GeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "genOperatingMode", "genControlMode", "genControlSource", "variableCost", "shortPF", "ratedGrossMinP", "maxOperatingP", "maximumAllowableSpinningReserve", "startupTime", "longPF", "initialP", "lowerRampRate", "minimumOffTime", "spinReserveRamp", "fuelPriority", "ratedGrossMaxP", "modelDetail", "efficiency", "raiseRampRate", "tieLinePF", "penaltyFactor", "minOperatingP", "autoCntrlMarginP", "minEconomicP", "controlDeadband", "dispReserveFlag", "normalPF", "highControlLimit", "allocSpinResP", "lowControlLimit", "governorMPL", "controlPulseLow", "fastStartFlag", "nominalP", "baseP", "ratedNetMaxP", "maxEconomicP", "controlResponseRate", "stepChange", "energyMinP", "startupCost", "governorSCD", "controlPulseHigh",
                label="Attributes", columns=4),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "OperatedBy_GenerationProvider", "ControlAreaGeneratingUnit", "GenUnitOpCostCurves", "SubControlArea", "RegisteredGenerator", "SynchronousMachines", "GenUnitOpSchedule", "GrossToNetActivePowerCurves",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.GeneratingUnit",
        title="GeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GeneratingUnit" user definitions:
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
    ThermalGeneratingUnit = Instance("CIM.IEC61970.Generation.Production.ThermalGeneratingUnit",
        desc="A thermal generating unit may have an incremental heat rate curve",
        transient=True,
        opposite="IncrementalHeatRateCurve",
        editor=InstanceEditor(name="_thermalgeneratingunits"))

    def _get_thermalgeneratingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # Flag is set to true when output is expressed in net active power
    isNetGrossP = Bool(desc="Flag is set to true when output is expressed in net active power")

    #--------------------------------------------------------------------------
    #  Begin "IncrementalHeatRateCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit", "isNetGrossP",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.IncrementalHeatRateCurve",
        title="IncrementalHeatRateCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IncrementalHeatRateCurve" user definitions:
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
    ThermalGeneratingUnit = Instance("CIM.IEC61970.Generation.Production.ThermalGeneratingUnit",
        desc="A thermal generating unit may have a heat input curve",
        transient=True,
        opposite="HeatInputCurve",
        editor=InstanceEditor(name="_thermalgeneratingunits"))

    def _get_thermalgeneratingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # Heat input - efficiency multiplier adjustment factor.
    heatInputEff = PU(desc="Heat input - efficiency multiplier adjustment factor.")

    # Power output - auxiliary power offset adjustment factor
    auxPowerOffset = ActivePower(desc="Power output - auxiliary power offset adjustment factor")

    # Heat input - offset adjustment factor.
    heatInputOffset = HeatRate(desc="Heat input - offset adjustment factor.")

    # Flag is set to true when output is expressed in net active power
    isNetGrossP = Bool(desc="Flag is set to true when output is expressed in net active power")

    # Power output - auxiliary power multiplier adjustment factor.
    auxPowerMult = PU(desc="Power output - auxiliary power multiplier adjustment factor.")

    #--------------------------------------------------------------------------
    #  Begin "HeatInputCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit", "heatInputEff", "auxPowerOffset", "heatInputOffset", "isNetGrossP", "auxPowerMult",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.HeatInputCurve",
        title="HeatInputCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HeatInputCurve" user definitions:
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

    # A reservoir may have a 'natural' inflow forecast.
    InflowForecasts = List(Instance("CIM.IEC61970.Generation.Production.InflowForecast"),
        desc="A reservoir may have a 'natural' inflow forecast.")

    # A reservoir may spill into a downstream reservoir
    SpillsIntoReservoirs = List(Instance("CIM.IEC61970.Generation.Production.Reservoir"),
        desc="A reservoir may spill into a downstream reservoir")

    # A reservoir may spill into a downstream reservoir
    SpillsFromReservoir = Instance("CIM.IEC61970.Generation.Production.Reservoir",
        desc="A reservoir may spill into a downstream reservoir",
        transient=True,
        opposite="SpillsIntoReservoirs",
        editor=InstanceEditor(name="_reservoirs"))

    def _get_reservoirs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.Reservoir" ]
        else:
            return []

    _reservoirs = Property(fget=_get_reservoirs)

    # Generators are supplied water from or pumps discharge water to an upstream reservoir
    UpstreamFromHydroPowerPlants = List(Instance("CIM.IEC61970.Generation.Production.HydroPowerPlant"),
        desc="Generators are supplied water from or pumps discharge water to an upstream reservoir")

    # A reservoir may have a level versus volume relationship.
    LevelVsVolumeCurves = List(Instance("CIM.IEC61970.Generation.Production.LevelVsVolumeCurve"),
        desc="A reservoir may have a level versus volume relationship.")

    # A reservoir may have a water level target schedule.
    TargetLevelSchedule = Instance("CIM.IEC61970.Generation.Production.TargetLevelSchedule",
        desc="A reservoir may have a water level target schedule.",
        transient=True,
        opposite="Reservoir",
        editor=InstanceEditor(name="_targetlevelschedules"))

    def _get_targetlevelschedules(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.TargetLevelSchedule" ]
        else:
            return []

    _targetlevelschedules = Property(fget=_get_targetlevelschedules)

    # Generators discharge water to or pumps are supplied water from a downstream reservoir
    HydroPowerPlants = List(Instance("CIM.IEC61970.Generation.Production.HydroPowerPlant"),
        desc="Generators discharge water to or pumps are supplied water from a downstream reservoir")

    # Type of spillway gate, including parameters
    spillWayGateType = SpillwayGateType(desc="Type of spillway gate, including parameters")

    # The length of the spillway crest
    spillwayCrestLength = Length(desc="The length of the spillway crest")

    # Storage volume between the full supply level and the normal minimum operating level
    activeStorageCapacity = Volume(desc="Storage volume between the full supply level and the normal minimum operating level")

    # Total capacity of reservoir
    grossCapacity = Volume(desc="Total capacity of reservoir")

    # The reservoir's energy storage rating in energy for given head conditions
    energyStorageRating = Float(desc="The reservoir's energy storage rating in energy for given head conditions")

    # Full supply level, above which water will spill. This can be the spillway crest level or the top of closed gates.
    fullSupplyLevel = WaterLevel(desc="Full supply level, above which water will spill. This can be the spillway crest level or the top of closed gates.")

    # The flow capacity of the spillway in cubic meters per second
    spillwayCapacity = Float(desc="The flow capacity of the spillway in cubic meters per second")

    # The spillway water travel delay to the next downstream reservoir
    spillTravelDelay = Seconds(desc="The spillway water travel delay to the next downstream reservoir")

    # River outlet works for riparian right releases or other purposes
    riverOutletWorks = Str(desc="River outlet works for riparian right releases or other purposes")

    # Normal minimum operating level below which the penstocks will draw air
    normalMinOperateLevel = WaterLevel(desc="Normal minimum operating level below which the penstocks will draw air")

    # Spillway crest level above which water will spill
    spillwayCrestLevel = WaterLevel(desc="Spillway crest level above which water will spill")

    #--------------------------------------------------------------------------
    #  Begin "Reservoir" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "spillWayGateType", "spillwayCrestLength", "activeStorageCapacity", "grossCapacity", "energyStorageRating", "fullSupplyLevel", "spillwayCapacity", "spillTravelDelay", "riverOutletWorks", "normalMinOperateLevel", "spillwayCrestLevel",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "InflowForecasts", "SpillsIntoReservoirs", "SpillsFromReservoir", "UpstreamFromHydroPowerPlants", "LevelVsVolumeCurves", "TargetLevelSchedule", "HydroPowerPlants",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.Reservoir",
        title="Reservoir",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Reservoir" user definitions:
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
    GeneratingUnit = Instance("CIM.IEC61970.Generation.Production.GeneratingUnit",
        desc="A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.",
        transient=True,
        opposite="GenUnitOpCostCurves",
        editor=InstanceEditor(name="_generatingunits"))

    def _get_generatingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.GeneratingUnit" ]
        else:
            return []

    _generatingunits = Property(fget=_get_generatingunits)

    # Flag is set to true when output is expressed in net active power
    isNetGrossP = Bool(desc="Flag is set to true when output is expressed in net active power")

    #--------------------------------------------------------------------------
    #  Begin "GenUnitOpCostCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit", "isNetGrossP",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "GeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.GenUnitOpCostCurve",
        title="GenUnitOpCostCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GenUnitOpCostCurve" user definitions:
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
    StartupModel = Instance("CIM.IEC61970.Generation.Production.StartupModel",
        desc="The unit's startup model may have a startup main fuel curve",
        transient=True,
        opposite="StartMainFuelCurve",
        editor=InstanceEditor(name="_startupmodels"))

    def _get_startupmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.StartupModel" ]
        else:
            return []

    _startupmodels = Property(fget=_get_startupmodels)

    # Type of main fuel
    mainFuelType = FuelType(desc="Type of main fuel")

    #--------------------------------------------------------------------------
    #  Begin "StartMainFuelCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit", "mainFuelType",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "StartupModel",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.StartMainFuelCurve",
        title="StartMainFuelCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StartMainFuelCurve" user definitions:
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

    # A cogeneration plant has a steam sendout schedule
    SteamSendoutSchedule = Instance("CIM.IEC61970.Generation.Production.SteamSendoutSchedule",
        desc="A cogeneration plant has a steam sendout schedule",
        transient=True,
        opposite="CogenerationPlant",
        editor=InstanceEditor(name="_steamsendoutschedules"))

    def _get_steamsendoutschedules(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.SteamSendoutSchedule" ]
        else:
            return []

    _steamsendoutschedules = Property(fget=_get_steamsendoutschedules)

    # A thermal generating unit may be a member of a cogeneration plant
    ThermalGeneratingUnits = List(Instance("CIM.IEC61970.Generation.Production.ThermalGeneratingUnit"),
        desc="A thermal generating unit may be a member of a cogeneration plant")

    # The high pressure steam sendout
    cogenHPSendoutRating = Float(desc="The high pressure steam sendout")

    # The rated output active power of the cogeneration plant
    ratedP = ActivePower(desc="The rated output active power of the cogeneration plant")

    # The low pressure steam sendout
    cogenLPSendoutRating = Float(desc="The low pressure steam sendout")

    # The low pressure steam rating
    cogenLPSteamRating = Float(desc="The low pressure steam rating")

    # The high pressure steam rating
    cogenHPSteamRating = Float(desc="The high pressure steam rating")

    #--------------------------------------------------------------------------
    #  Begin "CogenerationPlant" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "cogenHPSendoutRating", "ratedP", "cogenLPSendoutRating", "cogenLPSteamRating", "cogenHPSteamRating",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "SteamSendoutSchedule", "ThermalGeneratingUnits",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.CogenerationPlant",
        title="CogenerationPlant",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CogenerationPlant" user definitions:
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
    GeneratingUnit = Instance("CIM.IEC61970.Generation.Production.GeneratingUnit",
        desc="A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit",
        transient=True,
        opposite="GrossToNetActivePowerCurves",
        editor=InstanceEditor(name="_generatingunits"))

    def _get_generatingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.GeneratingUnit" ]
        else:
            return []

    _generatingunits = Property(fget=_get_generatingunits)

    #--------------------------------------------------------------------------
    #  Begin "GrossToNetActivePowerCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "GeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.GrossToNetActivePowerCurve",
        title="GrossToNetActivePowerCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GrossToNetActivePowerCurve" user definitions:
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
    CombustionTurbine = Instance("CIM.IEC61970.Generation.GenerationDynamics.CombustionTurbine",
        desc="A CAES air compressor is driven by combustion turbine",
        transient=True,
        opposite="AirCompressor",
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

    # An air compressor may be a member of a compressed air energy storage plant
    CAESPlant = Instance("CIM.IEC61970.Generation.Production.CAESPlant",
        desc="An air compressor may be a member of a compressed air energy storage plant",
        transient=True,
        opposite="AirCompressor",
        editor=InstanceEditor(name="_caesplants"))

    def _get_caesplants(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.CAESPlant" ]
        else:
            return []

    _caesplants = Property(fget=_get_caesplants)

    # Rating of the CAES air compressor
    airCompressorRating = Float(desc="Rating of the CAES air compressor")

    #--------------------------------------------------------------------------
    #  Begin "AirCompressor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "airCompressorRating",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "CombustionTurbine", "CAESPlant",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.AirCompressor",
        title="AirCompressor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AirCompressor" user definitions:
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
    ThermalGeneratingUnit = Instance("CIM.IEC61970.Generation.Production.ThermalGeneratingUnit",
        desc="A thermal generating unit may have a shutdown curve",
        transient=True,
        opposite="ShutdownCurve",
        editor=InstanceEditor(name="_thermalgeneratingunits"))

    def _get_thermalgeneratingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # The date and time of the most recent generating unit shutdown
    shutdownDate = Date(desc="The date and time of the most recent generating unit shutdown")

    # Fixed shutdown cost
    shutdownCost = Money(desc="Fixed shutdown cost")

    #--------------------------------------------------------------------------
    #  Begin "ShutdownCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit", "shutdownDate", "shutdownCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.ShutdownCurve",
        title="ShutdownCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ShutdownCurve" user definitions:
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

    # A thermal generating unit may have one or more fuel allocation schedules
    ThermalGeneratingUnit = Instance("CIM.IEC61970.Generation.Production.ThermalGeneratingUnit",
        desc="A thermal generating unit may have one or more fuel allocation schedules",
        transient=True,
        opposite="FuelAllocationSchedules",
        editor=InstanceEditor(name="_thermalgeneratingunits"))

    def _get_thermalgeneratingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # A fuel allocation schedule must have a fossil fuel
    FossilFuel = Instance("CIM.IEC61970.Generation.Production.FossilFuel",
        desc="A fuel allocation schedule must have a fossil fuel",
        transient=True,
        opposite="FuelAllocationSchedules",
        editor=InstanceEditor(name="_fossilfuels"))

    def _get_fossilfuels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.FossilFuel" ]
        else:
            return []

    _fossilfuels = Property(fget=_get_fossilfuels)

    # The type of fuel, which also indicates the corresponding measurement unit
    fuelType = FuelType(desc="The type of fuel, which also indicates the corresponding measurement unit")

    # The minimum amount fuel that is allocated for consumption for the scheduled time period, e.g., based on a 'take-or-pay' contract
    minFuelAllocation = Float(desc="The minimum amount fuel that is allocated for consumption for the scheduled time period, e.g., based on a 'take-or-pay' contract")

    # The start time and date of the fuel allocation schedule
    fuelAllocationStartDate = Date(desc="The start time and date of the fuel allocation schedule")

    # The maximum amount fuel that is allocated for consumption for the scheduled time period
    maxFuelAllocation = Float(desc="The maximum amount fuel that is allocated for consumption for the scheduled time period")

    # The end time and date of the fuel allocation schedule
    fuelAllocationEndDate = Date(desc="The end time and date of the fuel allocation schedule")

    #--------------------------------------------------------------------------
    #  Begin "FuelAllocationSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit", "fuelType", "minFuelAllocation", "fuelAllocationStartDate", "maxFuelAllocation", "fuelAllocationEndDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "ThermalGeneratingUnit", "FossilFuel",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.FuelAllocationSchedule",
        title="FuelAllocationSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FuelAllocationSchedule" user definitions:
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
    HydroGeneratingUnit = Instance("CIM.IEC61970.Generation.Production.HydroGeneratingUnit",
        desc="A hydro generating unit has a tailbay loss curve",
        transient=True,
        opposite="TailbayLossCurve",
        editor=InstanceEditor(name="_hydrogeneratingunits"))

    def _get_hydrogeneratingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.HydroGeneratingUnit" ]
        else:
            return []

    _hydrogeneratingunits = Property(fget=_get_hydrogeneratingunits)

    #--------------------------------------------------------------------------
    #  Begin "TailbayLossCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "HydroGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.TailbayLossCurve",
        title="TailbayLossCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TailbayLossCurve" user definitions:
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
    HydroPump = Instance("CIM.IEC61970.Generation.Production.HydroPump",
        desc="The hydro pump has a pumping schedule over time, indicating when pumping is to occur.",
        transient=True,
        opposite="HydroPumpOpSchedule",
        editor=InstanceEditor(name="_hydropumps"))

    def _get_hydropumps(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.HydroPump" ]
        else:
            return []

    _hydropumps = Property(fget=_get_hydropumps)

    #--------------------------------------------------------------------------
    #  Begin "HydroPumpOpSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value2Multiplier", "value1Unit", "value2Unit", "value1Multiplier", "startTime", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "HydroPump",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.HydroPumpOpSchedule",
        title="HydroPumpOpSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HydroPumpOpSchedule" user definitions:
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
    FuelAllocationSchedules = List(Instance("CIM.IEC61970.Generation.Production.FuelAllocationSchedule"),
        desc="A fuel allocation schedule must have a fossil fuel")

    # A thermal generating unit may have one or more fossil fuels
    ThermalGeneratingUnit = Instance("CIM.IEC61970.Generation.Production.ThermalGeneratingUnit",
        desc="A thermal generating unit may have one or more fossil fuels",
        transient=True,
        opposite="FossilFuels",
        editor=InstanceEditor(name="_thermalgeneratingunits"))

    def _get_thermalgeneratingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # The type of fossil fuel, such as coal, oil, or gas.
    fossilFuelType = FuelType(desc="The type of fossil fuel, such as coal, oil, or gas.")

    # The cost of fuel used for economic dispatching which includes: fuel cost, transportation cost,  and incremental maintenance cost
    fuelDispatchCost = CostPerHeatUnit(desc="The cost of fuel used for economic dispatching which includes: fuel cost, transportation cost,  and incremental maintenance cost")

    # The efficiency factor for the fuel (per unit) in terms of the effective energy absorbed
    fuelEffFactor = PU(desc="The efficiency factor for the fuel (per unit) in terms of the effective energy absorbed")

    # The cost in terms of heat value for the given type of fuel
    fuelCost = CostPerHeatUnit(desc="The cost in terms of heat value for the given type of fuel")

    # The active power output level of the unit at which the given type of fuel is switched off. This fuel (e.g., oil) is sometimes used to stabilize the base fuel (e.g., coal) at low active power output levels.
    lowBreakpointP = ActivePower(desc="The active power output level of the unit at which the given type of fuel is switched off. This fuel (e.g., oil) is sometimes used to stabilize the base fuel (e.g., coal) at low active power output levels.")

    # The active power output level of the unit at which the given type of fuel is switched on. This fuel (e.g., oil) is sometimes used to supplement the base fuel (e.g., coal) at high active power output levels.
    highBreakpointP = ActivePower(desc="The active power output level of the unit at which the given type of fuel is switched on. This fuel (e.g., oil) is sometimes used to supplement the base fuel (e.g., coal) at high active power output levels.")

    # The fuel's fraction of pollution credit per unit of heat content
    fuelSulfur = PU(desc="The fuel's fraction of pollution credit per unit of heat content")

    # Handling and processing cost associated with this fuel
    fuelHandlingCost = CostPerHeatUnit(desc="Handling and processing cost associated with this fuel")

    # The amount of heat per weight (or volume) of the given type of fuel
    fuelHeatContent = Float(desc="The amount of heat per weight (or volume) of the given type of fuel")

    # Relative amount of the given type of fuel, when multiple fuels are being consumed.
    fuelMixture = PerCent(desc="Relative amount of the given type of fuel, when multiple fuels are being consumed.")

    #--------------------------------------------------------------------------
    #  Begin "FossilFuel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "fossilFuelType", "fuelDispatchCost", "fuelEffFactor", "fuelCost", "lowBreakpointP", "highBreakpointP", "fuelSulfur", "fuelHandlingCost", "fuelHeatContent", "fuelMixture",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "FuelAllocationSchedules", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.FossilFuel",
        title="FossilFuel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FossilFuel" user definitions:
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
    Reservoir = Instance("CIM.IEC61970.Generation.Production.Reservoir",
        desc="A reservoir may have a water level target schedule.",
        transient=True,
        opposite="TargetLevelSchedule",
        editor=InstanceEditor(name="_reservoirs"))

    def _get_reservoirs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.Reservoir" ]
        else:
            return []

    _reservoirs = Property(fget=_get_reservoirs)

    # Low target level limit, below which the reservoir operation will be penalized
    lowLevelLimit = WaterLevel(desc="Low target level limit, below which the reservoir operation will be penalized")

    # High target level limit, above which the reservoir operation will be penalized
    highLevelLimit = WaterLevel(desc="High target level limit, above which the reservoir operation will be penalized")

    #--------------------------------------------------------------------------
    #  Begin "TargetLevelSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit", "lowLevelLimit", "highLevelLimit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "Reservoir",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.TargetLevelSchedule",
        title="TargetLevelSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TargetLevelSchedule" user definitions:
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

    # The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
    HydroPumpOpSchedule = Instance("CIM.IEC61970.Generation.Production.HydroPumpOpSchedule",
        desc="The hydro pump has a pumping schedule over time, indicating when pumping is to occur.",
        transient=True,
        opposite="HydroPump",
        editor=InstanceEditor(name="_hydropumpopschedules"))

    def _get_hydropumpopschedules(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.HydroPumpOpSchedule" ]
        else:
            return []

    _hydropumpopschedules = Property(fget=_get_hydropumpopschedules)

    # The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
    SynchronousMachine = Instance("CIM.IEC61970.Wires.SynchronousMachine",
        desc="The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.",
        transient=True,
        opposite="HydroPump",
        editor=InstanceEditor(name="_synchronousmachines"))

    def _get_synchronousmachines(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.SynchronousMachine" ]
        else:
            return []

    _synchronousmachines = Property(fget=_get_synchronousmachines)

    # The hydro pump may be a member of a pumped storage plant or a pump for distributing water
    HydroPowerPlant = Instance("CIM.IEC61970.Generation.Production.HydroPowerPlant",
        desc="The hydro pump may be a member of a pumped storage plant or a pump for distributing water",
        transient=True,
        opposite="HydroPumps",
        editor=InstanceEditor(name="_hydropowerplants"))

    def _get_hydropowerplants(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.HydroPowerPlant" ]
        else:
            return []

    _hydropowerplants = Property(fget=_get_hydropowerplants)

    # The pumping discharge (m3/sec) under minimum head conditions, usually at full gate
    pumpDischAtMinHead = Float(desc="The pumping discharge (m3/sec) under minimum head conditions, usually at full gate")

    # The pumping discharge (m3/sec) under maximum head conditions, usually at full gate
    pumpDischAtMaxHead = Float(desc="The pumping discharge (m3/sec) under maximum head conditions, usually at full gate")

    # The pumping power under minimum head conditions, usually at full gate.
    pumpPowerAtMinHead = ActivePower(desc="The pumping power under minimum head conditions, usually at full gate.")

    # The pumping power under maximum head conditions, usually at full gate
    pumpPowerAtMaxHead = ActivePower(desc="The pumping power under maximum head conditions, usually at full gate")

    #--------------------------------------------------------------------------
    #  Begin "HydroPump" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "pumpDischAtMinHead", "pumpDischAtMaxHead", "pumpPowerAtMinHead", "pumpPowerAtMaxHead",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "HydroPumpOpSchedule", "SynchronousMachine", "HydroPowerPlant",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.HydroPump",
        title="HydroPump",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HydroPump" user definitions:
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

    # Generators are supplied water from or pumps discharge water to an upstream reservoir
    GenSourcePumpDischargeReservoir = Instance("CIM.IEC61970.Generation.Production.Reservoir",
        desc="Generators are supplied water from or pumps discharge water to an upstream reservoir",
        transient=True,
        opposite="UpstreamFromHydroPowerPlants",
        editor=InstanceEditor(name="_reservoirs"))

    def _get_reservoirs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.Reservoir" ]
        else:
            return []

    _reservoirs = Property(fget=_get_reservoirs)

    # The hydro pump may be a member of a pumped storage plant or a pump for distributing water
    HydroPumps = List(Instance("CIM.IEC61970.Generation.Production.HydroPump"),
        desc="The hydro pump may be a member of a pumped storage plant or a pump for distributing water")

    # The hydro generating unit belongs to a hydro power plant
    HydroGeneratingUnits = List(Instance("CIM.IEC61970.Generation.Production.HydroGeneratingUnit"),
        desc="The hydro generating unit belongs to a hydro power plant")

    # Generators discharge water to or pumps are supplied water from a downstream reservoir
    Reservoir = Instance("CIM.IEC61970.Generation.Production.Reservoir",
        desc="Generators discharge water to or pumps are supplied water from a downstream reservoir",
        transient=True,
        opposite="HydroPowerPlants",
        editor=InstanceEditor(name="_reservoirs"))

    def _get_reservoirs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.Reservoir" ]
        else:
            return []

    _reservoirs = Property(fget=_get_reservoirs)

    # The type of hydro power plant.
    hydroPlantType = HydroPlantType(desc="The type of hydro power plant.")

    # A code describing the type (or absence) of surge tank that is associated with the hydro power plant
    surgeTankCode = SurgeTankCode(desc="A code describing the type (or absence) of surge tank that is associated with the hydro power plant")

    # Type and configuration of hydro plant penstock(s)
    penstockType = PenstockType(desc="Type and configuration of hydro plant penstock(s)")

    # The hydro plant's pumping rating active power for rated head conditions
    pumpRatedP = ActivePower(desc="The hydro plant's pumping rating active power for rated head conditions")

    # The hydro plant's generating rating active power for rated head conditions
    genRatedP = ActivePower(desc="The hydro plant's generating rating active power for rated head conditions")

    # Total plant discharge capacity in cubic meters per second
    plantDischargeCapacity = Float(desc="Total plant discharge capacity in cubic meters per second")

    # Water travel delay from tailbay to next downstream hydro power station
    dischargeTravelDelay = Seconds(desc="Water travel delay from tailbay to next downstream hydro power station")

    # The plant's rated gross head
    plantRatedHead = Length(desc="The plant's rated gross head")

    # The level at which the surge tank spills
    surgeTankCrestLevel = WaterLevel(desc="The level at which the surge tank spills")

    #--------------------------------------------------------------------------
    #  Begin "HydroPowerPlant" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "hydroPlantType", "surgeTankCode", "penstockType", "pumpRatedP", "genRatedP", "plantDischargeCapacity", "dischargeTravelDelay", "plantRatedHead", "surgeTankCrestLevel",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "GenSourcePumpDischargeReservoir", "HydroPumps", "HydroGeneratingUnits", "Reservoir",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.HydroPowerPlant",
        title="HydroPowerPlant",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HydroPowerPlant" user definitions:
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
    Reservoir = Instance("CIM.IEC61970.Generation.Production.Reservoir",
        desc="A reservoir may have a 'natural' inflow forecast.",
        transient=True,
        opposite="InflowForecasts",
        editor=InstanceEditor(name="_reservoirs"))

    def _get_reservoirs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.Reservoir" ]
        else:
            return []

    _reservoirs = Property(fget=_get_reservoirs)

    #--------------------------------------------------------------------------
    #  Begin "InflowForecast" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value2Multiplier", "value1Unit", "value2Unit", "value1Multiplier", "startTime", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "Reservoir",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.InflowForecast",
        title="InflowForecast",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "InflowForecast" user definitions:
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
    ThermalGeneratingUnits = List(Instance("CIM.IEC61970.Generation.Production.ThermalGeneratingUnit"),
        desc="A thermal generating unit may be a member of a combined cycle plant")

    # The combined cycle plant's active power output rating
    combCyclePlantRating = ActivePower(desc="The combined cycle plant's active power output rating")

    #--------------------------------------------------------------------------
    #  Begin "CombinedCyclePlant" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "combCyclePlantRating",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ThermalGeneratingUnits",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.CombinedCyclePlant",
        title="CombinedCyclePlant",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CombinedCyclePlant" user definitions:
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
    HydroGeneratingUnit = Instance("CIM.IEC61970.Generation.Production.HydroGeneratingUnit",
        desc="A hydro generating unit has an efficiency curve",
        transient=True,
        opposite="HydroGeneratingEfficiencyCurves",
        editor=InstanceEditor(name="_hydrogeneratingunits"))

    def _get_hydrogeneratingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.HydroGeneratingUnit" ]
        else:
            return []

    _hydrogeneratingunits = Property(fget=_get_hydrogeneratingunits)

    #--------------------------------------------------------------------------
    #  Begin "HydroGeneratingEfficiencyCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "HydroGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.HydroGeneratingEfficiencyCurve",
        title="HydroGeneratingEfficiencyCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HydroGeneratingEfficiencyCurve" user definitions:
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
    StartupModel = Instance("CIM.IEC61970.Generation.Production.StartupModel",
        desc="The unit's startup model may have a startup ignition fuel curve",
        transient=True,
        opposite="StartIgnFuelCurve",
        editor=InstanceEditor(name="_startupmodels"))

    def _get_startupmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.StartupModel" ]
        else:
            return []

    _startupmodels = Property(fget=_get_startupmodels)

    # Type of ignition fuel
    ignitionFuelType = FuelType(desc="Type of ignition fuel")

    #--------------------------------------------------------------------------
    #  Begin "StartIgnFuelCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit", "ignitionFuelType",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "StartupModel",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.StartIgnFuelCurve",
        title="StartIgnFuelCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StartIgnFuelCurve" user definitions:
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

    # A thermal generating unit may be a member of a compressed air energy storage plant
    ThermalGeneratingUnit = Instance("CIM.IEC61970.Generation.Production.ThermalGeneratingUnit",
        desc="A thermal generating unit may be a member of a compressed air energy storage plant",
        transient=True,
        opposite="CAESPlant",
        editor=InstanceEditor(name="_thermalgeneratingunits"))

    def _get_thermalgeneratingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # An air compressor may be a member of a compressed air energy storage plant
    AirCompressor = Instance("CIM.IEC61970.Generation.Production.AirCompressor",
        desc="An air compressor may be a member of a compressed air energy storage plant",
        transient=True,
        opposite="CAESPlant",
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

    # The CAES plant's gross rated generating capacity
    ratedCapacityP = ActivePower(desc="The CAES plant's gross rated generating capacity")

    # The rated energy storage capacity.
    energyStorageCapacity = RealEnergy(desc="The rated energy storage capacity.")

    #--------------------------------------------------------------------------
    #  Begin "CAESPlant" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "ratedCapacityP", "energyStorageCapacity",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ThermalGeneratingUnit", "AirCompressor",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.CAESPlant",
        title="CAESPlant",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CAESPlant" user definitions:
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
    GeneratingUnit = Instance("CIM.IEC61970.Generation.Production.GeneratingUnit",
        desc="A generating unit may have an operating schedule, indicating the planned operation of the unit",
        transient=True,
        opposite="GenUnitOpSchedule",
        editor=InstanceEditor(name="_generatingunits"))

    def _get_generatingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.GeneratingUnit" ]
        else:
            return []

    _generatingunits = Property(fget=_get_generatingunits)

    #--------------------------------------------------------------------------
    #  Begin "GenUnitOpSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value2Multiplier", "value1Unit", "value2Unit", "value1Multiplier", "startTime", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "GeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.GenUnitOpSchedule",
        title="GenUnitOpSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GenUnitOpSchedule" user definitions:
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
    CogenerationPlant = Instance("CIM.IEC61970.Generation.Production.CogenerationPlant",
        desc="A cogeneration plant has a steam sendout schedule",
        transient=True,
        opposite="SteamSendoutSchedule",
        editor=InstanceEditor(name="_cogenerationplants"))

    def _get_cogenerationplants(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.CogenerationPlant" ]
        else:
            return []

    _cogenerationplants = Property(fget=_get_cogenerationplants)

    #--------------------------------------------------------------------------
    #  Begin "SteamSendoutSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value2Multiplier", "value1Unit", "value2Unit", "value1Multiplier", "startTime", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "CogenerationPlant",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.SteamSendoutSchedule",
        title="SteamSendoutSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SteamSendoutSchedule" user definitions:
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
    StartupModel = Instance("CIM.IEC61970.Generation.Production.StartupModel",
        desc="The unit's startup model may have a startup ramp curve",
        transient=True,
        opposite="StartRampCurve",
        editor=InstanceEditor(name="_startupmodels"))

    def _get_startupmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.StartupModel" ]
        else:
            return []

    _startupmodels = Property(fget=_get_startupmodels)

    # The startup ramp rate in gross for a unit that is on hot standby
    hotStandbyRamp = ActivePowerChangeRate(desc="The startup ramp rate in gross for a unit that is on hot standby")

    #--------------------------------------------------------------------------
    #  Begin "StartRampCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit", "hotStandbyRamp",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "StartupModel",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.StartRampCurve",
        title="StartRampCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StartRampCurve" user definitions:
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
    ThermalGeneratingUnit = Instance("CIM.IEC61970.Generation.Production.ThermalGeneratingUnit",
        desc="A thermal generating unit may have a heat rate curve",
        transient=True,
        opposite="HeatRateCurve",
        editor=InstanceEditor(name="_thermalgeneratingunits"))

    def _get_thermalgeneratingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # Flag is set to true when output is expressed in net active power
    isNetGrossP = Bool(desc="Flag is set to true when output is expressed in net active power")

    #--------------------------------------------------------------------------
    #  Begin "HeatRateCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit", "isNetGrossP",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.HeatRateCurve",
        title="HeatRateCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HeatRateCurve" user definitions:
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
    Reservoir = Instance("CIM.IEC61970.Generation.Production.Reservoir",
        desc="A reservoir may have a level versus volume relationship.",
        transient=True,
        opposite="LevelVsVolumeCurves",
        editor=InstanceEditor(name="_reservoirs"))

    def _get_reservoirs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.Reservoir" ]
        else:
            return []

    _reservoirs = Property(fget=_get_reservoirs)

    #--------------------------------------------------------------------------
    #  Begin "LevelVsVolumeCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "Reservoir",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.LevelVsVolumeCurve",
        title="LevelVsVolumeCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LevelVsVolumeCurve" user definitions:
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
    ThermalGeneratingUnit = Instance("CIM.IEC61970.Generation.Production.ThermalGeneratingUnit",
        desc="A thermal generating unit may have  one or more emission curves",
        transient=True,
        opposite="EmissionCurves",
        editor=InstanceEditor(name="_thermalgeneratingunits"))

    def _get_thermalgeneratingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # The type of emission, which also gives the production rate measurement unit. The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide).
    emissionType = EmissionType(desc="The type of emission, which also gives the production rate measurement unit. The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide).")

    # Flag is set to true when output is expressed in net active power
    isNetGrossP = Bool(desc="Flag is set to true when output is expressed in net active power")

    # The emission content per quantity of fuel burned
    emissionContent = Emission(desc="The emission content per quantity of fuel burned")

    #--------------------------------------------------------------------------
    #  Begin "EmissionCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit", "emissionType", "isNetGrossP", "emissionContent",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.EmissionCurve",
        title="EmissionCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EmissionCurve" user definitions:
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

    # The unit's startup model may have a startup main fuel curve
    StartMainFuelCurve = Instance("CIM.IEC61970.Generation.Production.StartMainFuelCurve",
        desc="The unit's startup model may have a startup main fuel curve",
        transient=True,
        opposite="StartupModel",
        editor=InstanceEditor(name="_startmainfuelcurves"))

    def _get_startmainfuelcurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.StartMainFuelCurve" ]
        else:
            return []

    _startmainfuelcurves = Property(fget=_get_startmainfuelcurves)

    # The unit's startup model may have a startup ignition fuel curve
    StartIgnFuelCurve = Instance("CIM.IEC61970.Generation.Production.StartIgnFuelCurve",
        desc="The unit's startup model may have a startup ignition fuel curve",
        transient=True,
        opposite="StartupModel",
        editor=InstanceEditor(name="_startignfuelcurves"))

    def _get_startignfuelcurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.StartIgnFuelCurve" ]
        else:
            return []

    _startignfuelcurves = Property(fget=_get_startignfuelcurves)

    # The unit's startup model may have a startup ramp curve
    StartRampCurve = Instance("CIM.IEC61970.Generation.Production.StartRampCurve",
        desc="The unit's startup model may have a startup ramp curve",
        transient=True,
        opposite="StartupModel",
        editor=InstanceEditor(name="_startrampcurves"))

    def _get_startrampcurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.StartRampCurve" ]
        else:
            return []

    _startrampcurves = Property(fget=_get_startrampcurves)

    # A thermal generating unit may have a startup model
    ThermalGeneratingUnit = Instance("CIM.IEC61970.Generation.Production.ThermalGeneratingUnit",
        desc="A thermal generating unit may have a startup model",
        transient=True,
        opposite="StartupModel",
        editor=InstanceEditor(name="_thermalgeneratingunits"))

    def _get_thermalgeneratingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # Incremental Maintenance Cost
    incrementalMaintCost = CostPerEnergyUnit(desc="Incremental Maintenance Cost")

    # The date and time of the most recent generating unit startup
    startupDate = Date(desc="The date and time of the most recent generating unit startup")

    # Total miscellaneous start up costs
    startupCost = Money(desc="Total miscellaneous start up costs")

    # The unit's auxiliary active power consumption to maintain standby mode
    stbyAuxP = ActivePower(desc="The unit's auxiliary active power consumption to maintain standby mode")

    # Startup priority within control area where lower numbers indicate higher priorities.  More than one unit in an area may be assigned the same priority.
    startupPriority = Int(desc="Startup priority within control area where lower numbers indicate higher priorities.  More than one unit in an area may be assigned the same priority.")

    # Fixed Maintenance Cost
    fixedMaintCost = CostRate(desc="Fixed Maintenance Cost")

    # The minimum number of hours the unit must be down before restart
    minimumDownTime = Hours(desc="The minimum number of hours the unit must be down before restart")

    # The opportunity cost associated with the return in monetary unit. This represents the restart's 'share' of the unit depreciation and risk of an event which would damage the unit.
    riskFactorCost = Money(desc="The opportunity cost associated with the return in monetary unit. This represents the restart's 'share' of the unit depreciation and risk of an event which would damage the unit.")

    # The minimum number of hours the unit must be operating before being allowed to shut down
    minimumRunTime = Hours(desc="The minimum number of hours the unit must be operating before being allowed to shut down")

    # The amount of heat input per time uint required for hot standby operation
    hotStandbyHeat = HeatRate(desc="The amount of heat input per time uint required for hot standby operation")

    #--------------------------------------------------------------------------
    #  Begin "StartupModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "incrementalMaintCost", "startupDate", "startupCost", "stbyAuxP", "startupPriority", "fixedMaintCost", "minimumDownTime", "riskFactorCost", "minimumRunTime", "hotStandbyHeat",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "StartMainFuelCurve", "StartIgnFuelCurve", "StartRampCurve", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.StartupModel",
        title="StartupModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StartupModel" user definitions:
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
    ThermalGeneratingUnit = Instance("CIM.IEC61970.Generation.Production.ThermalGeneratingUnit",
        desc="A thermal generating unit may have one or more emission allowance accounts",
        transient=True,
        opposite="EmmissionAccounts",
        editor=InstanceEditor(name="_thermalgeneratingunits"))

    def _get_thermalgeneratingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # The type of emission, for example sulfur dioxide (SO2). The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide).
    emissionType = EmissionType(desc="The type of emission, for example sulfur dioxide (SO2). The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide).")

    # The source of the emission value.
    emissionValueSource = EmissionValueSource(desc="The source of the emission value.")

    #--------------------------------------------------------------------------
    #  Begin "EmissionAccount" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit", "emissionType", "emissionValueSource",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.EmissionAccount",
        title="EmissionAccount",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EmissionAccount" user definitions:
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

    # A thermal generating unit may have a heat rate curve
    HeatRateCurve = Instance("CIM.IEC61970.Generation.Production.HeatRateCurve",
        desc="A thermal generating unit may have a heat rate curve",
        transient=True,
        opposite="ThermalGeneratingUnit",
        editor=InstanceEditor(name="_heatratecurves"))

    def _get_heatratecurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.HeatRateCurve" ]
        else:
            return []

    _heatratecurves = Property(fget=_get_heatratecurves)

    # A thermal generating unit may have one or more emission allowance accounts
    EmmissionAccounts = List(Instance("CIM.IEC61970.Generation.Production.EmissionAccount"),
        desc="A thermal generating unit may have one or more emission allowance accounts")

    # A thermal generating unit may have one or more fuel allocation schedules
    FuelAllocationSchedules = List(Instance("CIM.IEC61970.Generation.Production.FuelAllocationSchedule"),
        desc="A thermal generating unit may have one or more fuel allocation schedules")

    # A thermal generating unit may have a heat input curve
    HeatInputCurve = Instance("CIM.IEC61970.Generation.Production.HeatInputCurve",
        desc="A thermal generating unit may have a heat input curve",
        transient=True,
        opposite="ThermalGeneratingUnit",
        editor=InstanceEditor(name="_heatinputcurves"))

    def _get_heatinputcurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.HeatInputCurve" ]
        else:
            return []

    _heatinputcurves = Property(fget=_get_heatinputcurves)

    # A thermal generating unit may be a member of a combined cycle plant
    CombinedCyclePlant = Instance("CIM.IEC61970.Generation.Production.CombinedCyclePlant",
        desc="A thermal generating unit may be a member of a combined cycle plant",
        transient=True,
        opposite="ThermalGeneratingUnits",
        editor=InstanceEditor(name="_combinedcycleplants"))

    def _get_combinedcycleplants(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.CombinedCyclePlant" ]
        else:
            return []

    _combinedcycleplants = Property(fget=_get_combinedcycleplants)

    # A thermal generating unit may be a member of a cogeneration plant
    CogenerationPlant = Instance("CIM.IEC61970.Generation.Production.CogenerationPlant",
        desc="A thermal generating unit may be a member of a cogeneration plant",
        transient=True,
        opposite="ThermalGeneratingUnits",
        editor=InstanceEditor(name="_cogenerationplants"))

    def _get_cogenerationplants(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.CogenerationPlant" ]
        else:
            return []

    _cogenerationplants = Property(fget=_get_cogenerationplants)

    # A thermal generating unit may have  one or more emission curves
    EmissionCurves = List(Instance("CIM.IEC61970.Generation.Production.EmissionCurve"),
        desc="A thermal generating unit may have  one or more emission curves")

    # A thermal generating unit may have a shutdown curve
    ShutdownCurve = Instance("CIM.IEC61970.Generation.Production.ShutdownCurve",
        desc="A thermal generating unit may have a shutdown curve",
        transient=True,
        opposite="ThermalGeneratingUnit",
        editor=InstanceEditor(name="_shutdowncurves"))

    def _get_shutdowncurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.ShutdownCurve" ]
        else:
            return []

    _shutdowncurves = Property(fget=_get_shutdowncurves)

    # A thermal generating unit may be a member of a compressed air energy storage plant
    CAESPlant = Instance("CIM.IEC61970.Generation.Production.CAESPlant",
        desc="A thermal generating unit may be a member of a compressed air energy storage plant",
        transient=True,
        opposite="ThermalGeneratingUnit",
        editor=InstanceEditor(name="_caesplants"))

    def _get_caesplants(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.CAESPlant" ]
        else:
            return []

    _caesplants = Property(fget=_get_caesplants)

    # A thermal generating unit may have an incremental heat rate curve
    IncrementalHeatRateCurve = Instance("CIM.IEC61970.Generation.Production.IncrementalHeatRateCurve",
        desc="A thermal generating unit may have an incremental heat rate curve",
        transient=True,
        opposite="ThermalGeneratingUnit",
        editor=InstanceEditor(name="_incrementalheatratecurves"))

    def _get_incrementalheatratecurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.IncrementalHeatRateCurve" ]
        else:
            return []

    _incrementalheatratecurves = Property(fget=_get_incrementalheatratecurves)

    # A thermal generating unit may have a startup model
    StartupModel = Instance("CIM.IEC61970.Generation.Production.StartupModel",
        desc="A thermal generating unit may have a startup model",
        transient=True,
        opposite="ThermalGeneratingUnit",
        editor=InstanceEditor(name="_startupmodels"))

    def _get_startupmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.StartupModel" ]
        else:
            return []

    _startupmodels = Property(fget=_get_startupmodels)

    # A thermal generating unit may have one or more fossil fuels
    FossilFuels = List(Instance("CIM.IEC61970.Generation.Production.FossilFuel"),
        desc="A thermal generating unit may have one or more fossil fuels")

    # Operating and maintenance cost for the thermal unit
    oMCost = CostPerHeatUnit(desc="Operating and maintenance cost for the thermal unit")

    #--------------------------------------------------------------------------
    #  Begin "ThermalGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "genOperatingMode", "genControlMode", "genControlSource", "variableCost", "shortPF", "ratedGrossMinP", "maxOperatingP", "maximumAllowableSpinningReserve", "startupTime", "longPF", "initialP", "lowerRampRate", "minimumOffTime", "spinReserveRamp", "fuelPriority", "ratedGrossMaxP", "modelDetail", "efficiency", "raiseRampRate", "tieLinePF", "penaltyFactor", "minOperatingP", "autoCntrlMarginP", "minEconomicP", "controlDeadband", "dispReserveFlag", "normalPF", "highControlLimit", "allocSpinResP", "lowControlLimit", "governorMPL", "controlPulseLow", "fastStartFlag", "nominalP", "baseP", "ratedNetMaxP", "maxEconomicP", "controlResponseRate", "stepChange", "energyMinP", "startupCost", "governorSCD", "controlPulseHigh", "oMCost",
                label="Attributes", columns=4),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "OperatedBy_GenerationProvider", "ControlAreaGeneratingUnit", "GenUnitOpCostCurves", "SubControlArea", "RegisteredGenerator", "SynchronousMachines", "GenUnitOpSchedule", "GrossToNetActivePowerCurves", "HeatRateCurve", "EmmissionAccounts", "FuelAllocationSchedules", "HeatInputCurve", "CombinedCyclePlant", "CogenerationPlant", "EmissionCurves", "ShutdownCurve", "CAESPlant", "IncrementalHeatRateCurve", "StartupModel", "FossilFuels",
                label="References", columns=4),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.ThermalGeneratingUnit",
        title="ThermalGeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ThermalGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WindGeneratingUnit" class:
#------------------------------------------------------------------------------

class WindGeneratingUnit(GeneratingUnit):
    """ A wind driven generating unit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "WindGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "genOperatingMode", "genControlMode", "genControlSource", "variableCost", "shortPF", "ratedGrossMinP", "maxOperatingP", "maximumAllowableSpinningReserve", "startupTime", "longPF", "initialP", "lowerRampRate", "minimumOffTime", "spinReserveRamp", "fuelPriority", "ratedGrossMaxP", "modelDetail", "efficiency", "raiseRampRate", "tieLinePF", "penaltyFactor", "minOperatingP", "autoCntrlMarginP", "minEconomicP", "controlDeadband", "dispReserveFlag", "normalPF", "highControlLimit", "allocSpinResP", "lowControlLimit", "governorMPL", "controlPulseLow", "fastStartFlag", "nominalP", "baseP", "ratedNetMaxP", "maxEconomicP", "controlResponseRate", "stepChange", "energyMinP", "startupCost", "governorSCD", "controlPulseHigh",
                label="Attributes", columns=4),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "OperatedBy_GenerationProvider", "ControlAreaGeneratingUnit", "GenUnitOpCostCurves", "SubControlArea", "RegisteredGenerator", "SynchronousMachines", "GenUnitOpSchedule", "GrossToNetActivePowerCurves",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.WindGeneratingUnit",
        title="WindGeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WindGeneratingUnit" user definitions:
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
    #  Begin "NuclearGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "genOperatingMode", "genControlMode", "genControlSource", "variableCost", "shortPF", "ratedGrossMinP", "maxOperatingP", "maximumAllowableSpinningReserve", "startupTime", "longPF", "initialP", "lowerRampRate", "minimumOffTime", "spinReserveRamp", "fuelPriority", "ratedGrossMaxP", "modelDetail", "efficiency", "raiseRampRate", "tieLinePF", "penaltyFactor", "minOperatingP", "autoCntrlMarginP", "minEconomicP", "controlDeadband", "dispReserveFlag", "normalPF", "highControlLimit", "allocSpinResP", "lowControlLimit", "governorMPL", "controlPulseLow", "fastStartFlag", "nominalP", "baseP", "ratedNetMaxP", "maxEconomicP", "controlResponseRate", "stepChange", "energyMinP", "startupCost", "governorSCD", "controlPulseHigh",
                label="Attributes", columns=4),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "OperatedBy_GenerationProvider", "ControlAreaGeneratingUnit", "GenUnitOpCostCurves", "SubControlArea", "RegisteredGenerator", "SynchronousMachines", "GenUnitOpSchedule", "GrossToNetActivePowerCurves",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.NuclearGeneratingUnit",
        title="NuclearGeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "NuclearGeneratingUnit" user definitions:
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

    # A hydro generating unit has a tailbay loss curve
    TailbayLossCurve = List(Instance("CIM.IEC61970.Generation.Production.TailbayLossCurve"),
        desc="A hydro generating unit has a tailbay loss curve")

    # The hydro generating unit belongs to a hydro power plant
    HydroPowerPlant = Instance("CIM.IEC61970.Generation.Production.HydroPowerPlant",
        desc="The hydro generating unit belongs to a hydro power plant",
        transient=True,
        opposite="HydroGeneratingUnits",
        editor=InstanceEditor(name="_hydropowerplants"))

    def _get_hydropowerplants(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.HydroPowerPlant" ]
        else:
            return []

    _hydropowerplants = Property(fget=_get_hydropowerplants)

    # A hydro generating unit has a penstock loss curve
    PenstockLossCurve = Instance("CIM.IEC61970.Generation.Production.PenstockLossCurve",
        desc="A hydro generating unit has a penstock loss curve",
        transient=True,
        opposite="HydroGeneratingUnit",
        editor=InstanceEditor(name="_penstocklosscurves"))

    def _get_penstocklosscurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.PenstockLossCurve" ]
        else:
            return []

    _penstocklosscurves = Property(fget=_get_penstocklosscurves)

    # A hydro generating unit has an efficiency curve
    HydroGeneratingEfficiencyCurves = List(Instance("CIM.IEC61970.Generation.Production.HydroGeneratingEfficiencyCurve"),
        desc="A hydro generating unit has an efficiency curve")

    # Energy conversion capability for generating.
    energyConversionCapability = HydroEnergyConversionKind(desc="Energy conversion capability for generating.")

    # The equivalent cost of water that drives the hydro turbine, expressed as cost per volume.
    hydroUnitWaterCost = Float(desc="The equivalent cost of water that drives the hydro turbine, expressed as cost per volume.")

    #--------------------------------------------------------------------------
    #  Begin "HydroGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "genOperatingMode", "genControlMode", "genControlSource", "variableCost", "shortPF", "ratedGrossMinP", "maxOperatingP", "maximumAllowableSpinningReserve", "startupTime", "longPF", "initialP", "lowerRampRate", "minimumOffTime", "spinReserveRamp", "fuelPriority", "ratedGrossMaxP", "modelDetail", "efficiency", "raiseRampRate", "tieLinePF", "penaltyFactor", "minOperatingP", "autoCntrlMarginP", "minEconomicP", "controlDeadband", "dispReserveFlag", "normalPF", "highControlLimit", "allocSpinResP", "lowControlLimit", "governorMPL", "controlPulseLow", "fastStartFlag", "nominalP", "baseP", "ratedNetMaxP", "maxEconomicP", "controlResponseRate", "stepChange", "energyMinP", "startupCost", "governorSCD", "controlPulseHigh", "energyConversionCapability", "hydroUnitWaterCost",
                label="Attributes", columns=4),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "OperatedBy_GenerationProvider", "ControlAreaGeneratingUnit", "GenUnitOpCostCurves", "SubControlArea", "RegisteredGenerator", "SynchronousMachines", "GenUnitOpSchedule", "GrossToNetActivePowerCurves", "TailbayLossCurve", "HydroPowerPlant", "PenstockLossCurve", "HydroGeneratingEfficiencyCurves",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Generation.Production.HydroGeneratingUnit",
        title="HydroGeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HydroGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
