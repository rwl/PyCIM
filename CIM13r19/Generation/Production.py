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

from CIM13r19.Core import Equipment
from CIM13r19.Core import Curve
from CIM13r19.Core import PowerSystemResource
from CIM13r19.Core import IdentifiedObject
from CIM13r19.Core import RegularIntervalSchedule



from enthought.traits.api import Instance, List, Property, Enum, Float, Bool, Int, Str
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
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

    ControlAreaGeneratingUnit = List(Instance("CIM13r19.ControlArea.ControlAreaGeneratingUnit"))

    # A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
    GrossToNetActivePowerCurves = List(Instance("CIM13r19.Generation.Production.GrossToNetActivePowerCurve"),
        desc="A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit")

    # A synchronous machine may operate as a generator and as such becomes a member of a generating unit
    Contains_SynchronousMachines = List(Instance("CIM13r19.Wires.SynchronousMachine"),
        desc="A synchronous machine may operate as a generator and as such becomes a member of a generating unit")

    # A generating unit may have an operating schedule, indicating the planned operation of the unit
    GenUnitOpSchedule = Instance("CIM13r19.Generation.Production.GenUnitOpSchedule",
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
                    "CIM13r19.Generation.Production.GenUnitOpSchedule" ]
        else:
            return []

    _genunitopschedules = Property(fget=_get_genunitopschedules)

    # A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
    GenUnitOpCostCurves = List(Instance("CIM13r19.Generation.Production.GenUnitOpCostCurve"),
        desc="A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.")

    # The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity
    ratedNetMaxP = Float(desc="The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity")

    # Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental Transmission Loss expressed as a plus or minus value. The typical range of penalty factors is (0.9 to 1.1).
    penaltyFactor = Float(desc="Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental Transmission Loss expressed as a plus or minus value. The typical range of penalty factors is (0.9 to 1.1).")

    stepChange = Float

    energyMinP = Float

    # The efficiency of the unit in converting mechanical energy, from the prime mover, into electrical energy.
    efficiency = Float(desc="The efficiency of the unit in converting mechanical energy, from the prime mover, into electrical energy.")

    raiseRampRate = Float

    dispReserveFlag = Bool

    # The initial startup cost incurred for each start of the GeneratingUnit.
    startupCost = Float(desc="The initial startup cost incurred for each start of the GeneratingUnit.")

    # High limit for secondary (AGC) control
    highControlLimit = Float(desc="High limit for secondary (AGC) control")

    spinReserveRamp = Float

    # Pulse low limit which is the smallest control pulse that the unit can respond to
    controlPulseLow = Float(desc="Pulse low limit which is the smallest control pulse that the unit can respond to")

    # The source of controls for a generating unit.
    genControlSource = GeneratorControlSource(desc="The source of controls for a generating unit.")

    # Governor Speed Changer Droop
    governorSCD = Float(desc="Governor Speed Changer Droop")

    # For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits.
    baseP = Float(desc="For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits.")

    fuelPriority = Int

    # This is the maximum operating active power limit the dispatcher can enter for this unit
    maxOperatingP = Float(desc="This is the maximum operating active power limit the dispatcher can enter for this unit")

    # The unit control mode.
    genControlMode = GeneratorControlMode(desc="The unit control mode.")

    # The variable cost component of production per unit of ActivePower.
    variableCost = Float(desc="The variable cost component of production per unit of ActivePower.")

    # Low limit for secondary (AGC) control
    lowControlLimit = Float(desc="Low limit for secondary (AGC) control")

    # Pulse high limit which is the largest control pulse that the unit can respond to
    controlPulseHigh = Float(desc="Pulse high limit which is the largest control pulse that the unit can respond to")

    # Maximum high economic active power limit, that should not exceed the maximum operating active power limit
    maxEconomicP = Float(desc="Maximum high economic active power limit, that should not exceed the maximum operating active power limit")

    # Unit control error deadband. When a unit's desired active power change is less than this deadband, then no control pulses will be sent to the unit.
    controlDeadband = Float(desc="Unit control error deadband. When a unit's desired active power change is less than this deadband, then no control pulses will be sent to the unit.")

    # Governor Motor Position Limit
    governorMPL = Float(desc="Governor Motor Position Limit")

    # Low economic active power limit that must be greater than or equal to the minimum operating active power limit
    minEconomicP = Float(desc="Low economic active power limit that must be greater than or equal to the minimum operating active power limit")

    # This is the minimum operating active power limit the dispatcher can enter for this unit.
    minOperatingP = Float(desc="This is the minimum operating active power limit the dispatcher can enter for this unit.")

    # Unit response rate which specifies the active power change for a control pulse of one second in the most responsive loading level of the unit.
    controlResponseRate = Float(desc="Unit response rate which specifies the active power change for a control pulse of one second in the most responsive loading level of the unit.")

    # Detail level of the generator model data
    modelDetail = Int(desc="Detail level of the generator model data")

    # The planned unused capacity which can be used to support automatic control overruns.
    autoCntrlMarginP = Float(desc="The planned unused capacity which can be used to support automatic control overruns.")

    # The unit's gross rated maximum capacity (Book Value).
    ratedGrossMaxP = Float(desc="The unit's gross rated maximum capacity (Book Value).")

    # Operating mode for secondary control.
    genOperatingMode = GeneratorOperatingMode(desc="Operating mode for secondary control.")

    fastStartFlag = Bool

    # Generating unit economic participation factor
    longPF = Float(desc="Generating unit economic participation factor")

    # Generating unit economic participation factor
    normalPF = Float(desc="Generating unit economic participation factor")

    # Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.
    maximumAllowableSpinningReserve = Float(desc="Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.")

    # The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid
    ratedGrossMinP = Float(desc="The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid")

    # The planned unused capacity (spinning reserve) which can be used to support emergency load
    allocSpinResP = Float(desc="The planned unused capacity (spinning reserve) which can be used to support emergency load")

    # Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied
    startupTime = Float(desc="Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied")

    # Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration
    initialP = Float(desc="Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration")

    # Generating unit economic participation factor
    tieLinePF = Float(desc="Generating unit economic participation factor")

    # Minimum time interval between unit shutdown and startup
    minimumOffTime = Float(desc="Minimum time interval between unit shutdown and startup")

    lowerRampRate = Float

    # Generating unit economic participation factor
    shortPF = Float(desc="Generating unit economic participation factor")

    #--------------------------------------------------------------------------
    #  Begin "GeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "ratedNetMaxP", "penaltyFactor", "stepChange", "energyMinP", "efficiency", "raiseRampRate", "dispReserveFlag", "startupCost", "highControlLimit", "spinReserveRamp", "controlPulseLow", "genControlSource", "governorSCD", "baseP", "fuelPriority", "maxOperatingP", "genControlMode", "variableCost", "lowControlLimit", "controlPulseHigh", "maxEconomicP", "controlDeadband", "governorMPL", "minEconomicP", "minOperatingP", "controlResponseRate", "modelDetail", "autoCntrlMarginP", "ratedGrossMaxP", "genOperatingMode", "fastStartFlag", "longPF", "normalPF", "maximumAllowableSpinningReserve", "ratedGrossMinP", "allocSpinResP", "startupTime", "initialP", "tieLinePF", "minimumOffTime", "lowerRampRate", "shortPF",
                label="Attributes", columns=4),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "ControlAreaGeneratingUnit", "GrossToNetActivePowerCurves", "Contains_SynchronousMachines", "GenUnitOpSchedule", "GenUnitOpCostCurves",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Generation.Production.GeneratingUnit",
        title="GeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GeneratingUnit" user definitions:
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
    StartupModel = Instance("CIM13r19.Generation.Production.StartupModel",
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
                    "CIM13r19.Generation.Production.StartupModel" ]
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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit", "ignitionFuelType",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "StartupModel",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.StartIgnFuelCurve",
        title="StartIgnFuelCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StartIgnFuelCurve" user definitions:
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
    HydroGeneratingUnit = Instance("CIM13r19.Generation.Production.HydroGeneratingUnit",
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
                    "CIM13r19.Generation.Production.HydroGeneratingUnit" ]
        else:
            return []

    _hydrogeneratingunits = Property(fget=_get_hydrogeneratingunits)

    #--------------------------------------------------------------------------
    #  Begin "HydroGeneratingEfficiencyCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "HydroGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.HydroGeneratingEfficiencyCurve",
        title="HydroGeneratingEfficiencyCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HydroGeneratingEfficiencyCurve" user definitions:
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
    Reservoir = Instance("CIM13r19.Generation.Production.Reservoir",
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
                    "CIM13r19.Generation.Production.Reservoir" ]
        else:
            return []

    _reservoirs = Property(fget=_get_reservoirs)

    # Low target level limit, below which the reservoir operation will be penalized
    lowLevelLimit = Float(desc="Low target level limit, below which the reservoir operation will be penalized")

    # High target level limit, above which the reservoir operation will be penalized
    highLevelLimit = Float(desc="High target level limit, above which the reservoir operation will be penalized")

    #--------------------------------------------------------------------------
    #  Begin "TargetLevelSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit", "lowLevelLimit", "highLevelLimit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "Reservoir",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.TargetLevelSchedule",
        title="TargetLevelSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TargetLevelSchedule" user definitions:
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
    GeneratingUnit = Instance("CIM13r19.Generation.Production.GeneratingUnit",
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
                    "CIM13r19.Generation.Production.GeneratingUnit" ]
        else:
            return []

    _generatingunits = Property(fget=_get_generatingunits)

    #--------------------------------------------------------------------------
    #  Begin "GrossToNetActivePowerCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "GeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.GrossToNetActivePowerCurve",
        title="GrossToNetActivePowerCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GrossToNetActivePowerCurve" user definitions:
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
    ThermalGeneratingUnit = Instance("CIM13r19.Generation.Production.ThermalGeneratingUnit",
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
                    "CIM13r19.Generation.Production.ThermalGeneratingUnit" ]
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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit", "isNetGrossP",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.IncrementalHeatRateCurve",
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
    ThermalGeneratingUnit = Instance("CIM13r19.Generation.Production.ThermalGeneratingUnit",
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
                    "CIM13r19.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # Power output - auxiliary power offset adjustment factor
    auxPowerOffset = Float(desc="Power output - auxiliary power offset adjustment factor")

    # Heat input - offset adjustment factor.
    heatInputOffset = Float(desc="Heat input - offset adjustment factor.")

    # Power output - auxiliary power multiplier adjustment factor.
    auxPowerMult = Float(desc="Power output - auxiliary power multiplier adjustment factor.")

    # Heat input - efficiency multiplier adjustment factor.
    heatInputEff = Float(desc="Heat input - efficiency multiplier adjustment factor.")

    # Flag is set to true when output is expressed in net active power
    isNetGrossP = Bool(desc="Flag is set to true when output is expressed in net active power")

    #--------------------------------------------------------------------------
    #  Begin "HeatInputCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit", "auxPowerOffset", "heatInputOffset", "auxPowerMult", "heatInputEff", "isNetGrossP",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.HeatInputCurve",
        title="HeatInputCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HeatInputCurve" user definitions:
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
    StartupModel = Instance("CIM13r19.Generation.Production.StartupModel",
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
                    "CIM13r19.Generation.Production.StartupModel" ]
        else:
            return []

    _startupmodels = Property(fget=_get_startupmodels)

    # The startup ramp rate in gross for a unit that is on hot standby
    hotStandbyRamp = Float(desc="The startup ramp rate in gross for a unit that is on hot standby")

    #--------------------------------------------------------------------------
    #  Begin "StartRampCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit", "hotStandbyRamp",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "StartupModel",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.StartRampCurve",
        title="StartRampCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StartRampCurve" user definitions:
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
    DrivenBy_CombustionTurbine = Instance("CIM13r19.Generation.GenerationDynamics.CombustionTurbine",
        desc="A CAES air compressor is driven by combustion turbine",
        transient=True,
        opposite="Drives_AirCompressor",
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

    # An air compressor may be a member of a compressed air energy storage plant
    MemberOf_CAESPlant = Instance("CIM13r19.Generation.Production.CAESPlant",
        desc="An air compressor may be a member of a compressed air energy storage plant",
        transient=True,
        opposite="Contain_AirCompressor",
        editor=InstanceEditor(name="_caesplants"))

    def _get_caesplants(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Generation.Production.CAESPlant" ]
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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "airCompressorRating",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "DrivenBy_CombustionTurbine", "MemberOf_CAESPlant",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Generation.Production.AirCompressor",
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
    ThermalGeneratingUnit = Instance("CIM13r19.Generation.Production.ThermalGeneratingUnit",
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
                    "CIM13r19.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # Fixed shutdown cost
    shutdownCost = Float(desc="Fixed shutdown cost")

    # The date and time of the most recent generating unit shutdown
    shutdownDate = Str(desc="The date and time of the most recent generating unit shutdown")

    #--------------------------------------------------------------------------
    #  Begin "ShutdownCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit", "shutdownCost", "shutdownDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.ShutdownCurve",
        title="ShutdownCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ShutdownCurve" user definitions:
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
    Contain_ThermalGeneratingUnits = List(Instance("CIM13r19.Generation.Production.ThermalGeneratingUnit"),
        desc="A thermal generating unit may be a member of a combined cycle plant")

    # The combined cycle plant's active power output rating
    combCyclePlantRating = Float(desc="The combined cycle plant's active power output rating")

    #--------------------------------------------------------------------------
    #  Begin "CombinedCyclePlant" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "combCyclePlantRating",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "Contain_ThermalGeneratingUnits",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.CombinedCyclePlant",
        title="CombinedCyclePlant",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CombinedCyclePlant" user definitions:
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
    StartIgnFuelCurve = Instance("CIM13r19.Generation.Production.StartIgnFuelCurve",
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
                    "CIM13r19.Generation.Production.StartIgnFuelCurve" ]
        else:
            return []

    _startignfuelcurves = Property(fget=_get_startignfuelcurves)

    # The unit's startup model may have a startup ramp curve
    StartRampCurve = Instance("CIM13r19.Generation.Production.StartRampCurve",
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
                    "CIM13r19.Generation.Production.StartRampCurve" ]
        else:
            return []

    _startrampcurves = Property(fget=_get_startrampcurves)

    # The unit's startup model may have a startup main fuel curve
    StartMainFuelCurve = Instance("CIM13r19.Generation.Production.StartMainFuelCurve",
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
                    "CIM13r19.Generation.Production.StartMainFuelCurve" ]
        else:
            return []

    _startmainfuelcurves = Property(fget=_get_startmainfuelcurves)

    # A thermal generating unit may have a startup model
    ThermalGeneratingUnit = Instance("CIM13r19.Generation.Production.ThermalGeneratingUnit",
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
                    "CIM13r19.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # The minimum number of hours the unit must be operating before being allowed to shut down
    minimumRunTime = Float(desc="The minimum number of hours the unit must be operating before being allowed to shut down")

    # The date and time of the most recent generating unit startup
    startupDate = Str(desc="The date and time of the most recent generating unit startup")

    # The minimum number of hours the unit must be down before restart
    minimumDownTime = Float(desc="The minimum number of hours the unit must be down before restart")

    # Startup priority within control area where lower numbers indicate higher priorities.  More than one unit in an area may be assigned the same priority.
    startupPriority = Int(desc="Startup priority within control area where lower numbers indicate higher priorities.  More than one unit in an area may be assigned the same priority.")

    # The unit's auxiliary active power consumption to maintain standby mode
    stbyAuxP = Float(desc="The unit's auxiliary active power consumption to maintain standby mode")

    # Total miscellaneous start up costs
    startupCost = Float(desc="Total miscellaneous start up costs")

    # The amount of heat input per time uint required for hot standby operation
    hotStandbyHeat = Float(desc="The amount of heat input per time uint required for hot standby operation")

    # The opportunity cost associated with the return in monetary unit. This represents the restart's 'share' of the unit depreciation and risk of an event which would damage the unit.
    riskFactorCost = Float(desc="The opportunity cost associated with the return in monetary unit. This represents the restart's 'share' of the unit depreciation and risk of an event which would damage the unit.")

    # Fixed Maintenance Cost
    fixedMaintCost = Float(desc="Fixed Maintenance Cost")

    # Incremental Maintenance Cost
    incrementalMaintCost = Float(desc="Incremental Maintenance Cost")

    #--------------------------------------------------------------------------
    #  Begin "StartupModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "minimumRunTime", "startupDate", "minimumDownTime", "startupPriority", "stbyAuxP", "startupCost", "hotStandbyHeat", "riskFactorCost", "fixedMaintCost", "incrementalMaintCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "StartIgnFuelCurve", "StartRampCurve", "StartMainFuelCurve", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.StartupModel",
        title="StartupModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StartupModel" user definitions:
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
    MemberOf_HydroPowerPlant = Instance("CIM13r19.Generation.Production.HydroPowerPlant",
        desc="The hydro pump may be a member of a pumped storage plant or a pump for distributing water",
        transient=True,
        opposite="Contain_HydroPumps",
        editor=InstanceEditor(name="_hydropowerplants"))

    def _get_hydropowerplants(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Generation.Production.HydroPowerPlant" ]
        else:
            return []

    _hydropowerplants = Property(fget=_get_hydropowerplants)

    # The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
    HydroPumpOpSchedule = Instance("CIM13r19.Generation.Production.HydroPumpOpSchedule",
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
                    "CIM13r19.Generation.Production.HydroPumpOpSchedule" ]
        else:
            return []

    _hydropumpopschedules = Property(fget=_get_hydropumpopschedules)

    # The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
    DrivenBy_SynchronousMachine = Instance("CIM13r19.Wires.SynchronousMachine",
        desc="The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.",
        transient=True,
        opposite="Drives_HydroPump",
        editor=InstanceEditor(name="_synchronousmachines"))

    def _get_synchronousmachines(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.SynchronousMachine" ]
        else:
            return []

    _synchronousmachines = Property(fget=_get_synchronousmachines)

    # The pumping power under minimum head conditions, usually at full gate.
    pumpPowerAtMinHead = Float(desc="The pumping power under minimum head conditions, usually at full gate.")

    # The pumping discharge (m3/sec) under maximum head conditions, usually at full gate
    pumpDischAtMaxHead = Float(desc="The pumping discharge (m3/sec) under maximum head conditions, usually at full gate")

    # The pumping discharge (m3/sec) under minimum head conditions, usually at full gate
    pumpDischAtMinHead = Float(desc="The pumping discharge (m3/sec) under minimum head conditions, usually at full gate")

    # The pumping power under maximum head conditions, usually at full gate
    pumpPowerAtMaxHead = Float(desc="The pumping power under maximum head conditions, usually at full gate")

    #--------------------------------------------------------------------------
    #  Begin "HydroPump" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "pumpPowerAtMinHead", "pumpDischAtMaxHead", "pumpDischAtMinHead", "pumpPowerAtMaxHead",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "MemberOf_HydroPowerPlant", "HydroPumpOpSchedule", "DrivenBy_SynchronousMachine",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Generation.Production.HydroPump",
        title="HydroPump",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HydroPump" user definitions:
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
    ThermalGeneratingUnit = Instance("CIM13r19.Generation.Production.ThermalGeneratingUnit",
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
                    "CIM13r19.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # Flag is set to true when output is expressed in net active power
    isNetGrossP = Bool(desc="Flag is set to true when output is expressed in net active power")

    # The type of emission, which also gives the production rate measurement unit. The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide).
    emissionType = EmissionType(desc="The type of emission, which also gives the production rate measurement unit. The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide).")

    # The emission content per quantity of fuel burned
    emissionContent = Float(desc="The emission content per quantity of fuel burned")

    #--------------------------------------------------------------------------
    #  Begin "EmissionCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit", "isNetGrossP", "emissionType", "emissionContent",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.EmissionCurve",
        title="EmissionCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EmissionCurve" user definitions:
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
    GeneratingUnit = Instance("CIM13r19.Generation.Production.GeneratingUnit",
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
                    "CIM13r19.Generation.Production.GeneratingUnit" ]
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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit", "isNetGrossP",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "GeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.GenUnitOpCostCurve",
        title="GenUnitOpCostCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GenUnitOpCostCurve" user definitions:
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
    Contain_HydroGeneratingUnits = List(Instance("CIM13r19.Generation.Production.HydroGeneratingUnit"),
        desc="The hydro generating unit belongs to a hydro power plant")

    # Generators discharge water to or pumps are supplied water from a downstream reservoir
    Reservoir = Instance("CIM13r19.Generation.Production.Reservoir",
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
                    "CIM13r19.Generation.Production.Reservoir" ]
        else:
            return []

    _reservoirs = Property(fget=_get_reservoirs)

    # Generators are supplied water from or pumps discharge water to an upstream reservoir
    GenSourcePumpDischarge = Instance("CIM13r19.Generation.Production.Reservoir",
        desc="Generators are supplied water from or pumps discharge water to an upstream reservoir",
        transient=True,
        opposite="UpstreamFrom",
        editor=InstanceEditor(name="_reservoirs"))

    def _get_reservoirs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Generation.Production.Reservoir" ]
        else:
            return []

    _reservoirs = Property(fget=_get_reservoirs)

    # The hydro pump may be a member of a pumped storage plant or a pump for distributing water
    Contain_HydroPumps = List(Instance("CIM13r19.Generation.Production.HydroPump"),
        desc="The hydro pump may be a member of a pumped storage plant or a pump for distributing water")

    # Water travel delay from tailbay to next downstream hydro power station
    dischargeTravelDelay = Float(desc="Water travel delay from tailbay to next downstream hydro power station")

    # The hydro plant's pumping rating active power for rated head conditions
    pumpRatedP = Float(desc="The hydro plant's pumping rating active power for rated head conditions")

    # Type and configuration of hydro plant penstock(s)
    penstockType = PenstockType(desc="Type and configuration of hydro plant penstock(s)")

    # The plant's rated gross head in meters
    plantRatedHead = Float(desc="The plant's rated gross head in meters")

    # Total plant discharge capacity in cubic meters per second
    plantDischargeCapacity = Float(desc="Total plant discharge capacity in cubic meters per second")

    # The type of hydro power plant.
    hydroPlantType = HydroPlantType(desc="The type of hydro power plant.")

    # A code describing the type (or absence) of surge tank that is associated with the hydro power plant
    surgeTankCode = SurgeTankCode(desc="A code describing the type (or absence) of surge tank that is associated with the hydro power plant")

    # The hydro plant's generating rating active power for rated head conditions
    genRatedP = Float(desc="The hydro plant's generating rating active power for rated head conditions")

    # The level at which the surge tank spills
    surgeTankCrestLevel = Float(desc="The level at which the surge tank spills")

    #--------------------------------------------------------------------------
    #  Begin "HydroPowerPlant" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "dischargeTravelDelay", "pumpRatedP", "penstockType", "plantRatedHead", "plantDischargeCapacity", "hydroPlantType", "surgeTankCode", "genRatedP", "surgeTankCrestLevel",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "Contain_HydroGeneratingUnits", "Reservoir", "GenSourcePumpDischarge", "Contain_HydroPumps",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Generation.Production.HydroPowerPlant",
        title="HydroPowerPlant",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HydroPowerPlant" user definitions:
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
    Contain_AirCompressor = Instance("CIM13r19.Generation.Production.AirCompressor",
        desc="An air compressor may be a member of a compressed air energy storage plant",
        transient=True,
        opposite="MemberOf_CAESPlant",
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

    # A thermal generating unit may be a member of a compressed air energy storage plant
    Contain_ThermalGeneratingUnit = Instance("CIM13r19.Generation.Production.ThermalGeneratingUnit",
        desc="A thermal generating unit may be a member of a compressed air energy storage plant",
        transient=True,
        opposite="MemberOf_CAESPlant",
        editor=InstanceEditor(name="_thermalgeneratingunits"))

    def _get_thermalgeneratingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # The CAES plant's gross rated generating capacity
    ratedCapacityP = Float(desc="The CAES plant's gross rated generating capacity")

    # The rated energy storage capacity.
    energyStorageCapacity = Float(desc="The rated energy storage capacity.")

    #--------------------------------------------------------------------------
    #  Begin "CAESPlant" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "ratedCapacityP", "energyStorageCapacity",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "Contain_AirCompressor", "Contain_ThermalGeneratingUnit",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Generation.Production.CAESPlant",
        title="CAESPlant",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CAESPlant" user definitions:
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
    Reservoir = Instance("CIM13r19.Generation.Production.Reservoir",
        desc="A reservoir may have a level versus volume relationship.",
        transient=True,
        opposite="LevelVsVolumeCurve",
        editor=InstanceEditor(name="_reservoirs"))

    def _get_reservoirs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Generation.Production.Reservoir" ]
        else:
            return []

    _reservoirs = Property(fget=_get_reservoirs)

    #--------------------------------------------------------------------------
    #  Begin "LevelVsVolumeCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "Reservoir",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.LevelVsVolumeCurve",
        title="LevelVsVolumeCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LevelVsVolumeCurve" user definitions:
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
    Reservoir = Instance("CIM13r19.Generation.Production.Reservoir",
        desc="A reservoir may have a 'natural' inflow forecast.",
        transient=True,
        opposite="InflowForecast",
        editor=InstanceEditor(name="_reservoirs"))

    def _get_reservoirs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Generation.Production.Reservoir" ]
        else:
            return []

    _reservoirs = Property(fget=_get_reservoirs)

    #--------------------------------------------------------------------------
    #  Begin "InflowForecast" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "value2Unit", "startTime", "value2Multiplier", "value1Unit", "value1Multiplier", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "Reservoir",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.InflowForecast",
        title="InflowForecast",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "InflowForecast" user definitions:
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
    CogenerationPlant = Instance("CIM13r19.Generation.Production.CogenerationPlant",
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
                    "CIM13r19.Generation.Production.CogenerationPlant" ]
        else:
            return []

    _cogenerationplants = Property(fget=_get_cogenerationplants)

    #--------------------------------------------------------------------------
    #  Begin "SteamSendoutSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "value2Unit", "startTime", "value2Multiplier", "value1Unit", "value1Multiplier", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "CogenerationPlant",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.SteamSendoutSchedule",
        title="SteamSendoutSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SteamSendoutSchedule" user definitions:
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
    FuelAllocationSchedule = List(Instance("CIM13r19.Generation.Production.FuelAllocationSchedule"),
        desc="A fuel allocation schedule must have a fossil fuel")

    # A thermal generating unit may have one or more fossil fuels
    ThermalGeneratingUnit = Instance("CIM13r19.Generation.Production.ThermalGeneratingUnit",
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
                    "CIM13r19.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # The type of fossil fuel, such as coal, oil, or gas.
    fossilFuelType = FuelType(desc="The type of fossil fuel, such as coal, oil, or gas.")

    # The active power output level of the unit at which the given type of fuel is switched off. This fuel (e.g., oil) is sometimes used to stabilize the base fuel (e.g., coal) at low active power output levels.
    lowBreakpointP = Float(desc="The active power output level of the unit at which the given type of fuel is switched off. This fuel (e.g., oil) is sometimes used to stabilize the base fuel (e.g., coal) at low active power output levels.")

    # The cost of fuel used for economic dispatching which includes: fuel cost, transportation cost,  and incremental maintenance cost
    fuelDispatchCost = Float(desc="The cost of fuel used for economic dispatching which includes: fuel cost, transportation cost,  and incremental maintenance cost")

    # The efficiency factor for the fuel (per unit) in terms of the effective energy absorbed
    fuelEffFactor = Float(desc="The efficiency factor for the fuel (per unit) in terms of the effective energy absorbed")

    # The cost in terms of heat value for the given type of fuel
    fuelCost = Float(desc="The cost in terms of heat value for the given type of fuel")

    # The amount of heat per weight (or volume) of the given type of fuel
    fuelHeatContent = Float(desc="The amount of heat per weight (or volume) of the given type of fuel")

    # Handling and processing cost associated with this fuel
    fuelHandlingCost = Float(desc="Handling and processing cost associated with this fuel")

    # Relative amount of the given type of fuel, when multiple fuels are being consumed.
    fuelMixture = Float(desc="Relative amount of the given type of fuel, when multiple fuels are being consumed.")

    # The active power output level of the unit at which the given type of fuel is switched on. This fuel (e.g., oil) is sometimes used to supplement the base fuel (e.g., coal) at high active power output levels.
    highBreakpointP = Float(desc="The active power output level of the unit at which the given type of fuel is switched on. This fuel (e.g., oil) is sometimes used to supplement the base fuel (e.g., coal) at high active power output levels.")

    # The fuel's fraction of pollution credit per unit of heat content
    fuelSulfur = Float(desc="The fuel's fraction of pollution credit per unit of heat content")

    #--------------------------------------------------------------------------
    #  Begin "FossilFuel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "fossilFuelType", "lowBreakpointP", "fuelDispatchCost", "fuelEffFactor", "fuelCost", "fuelHeatContent", "fuelHandlingCost", "fuelMixture", "highBreakpointP", "fuelSulfur",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "FuelAllocationSchedule", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.FossilFuel",
        title="FossilFuel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FossilFuel" user definitions:
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
    FossilFuel = Instance("CIM13r19.Generation.Production.FossilFuel",
        desc="A fuel allocation schedule must have a fossil fuel",
        transient=True,
        opposite="FuelAllocationSchedule",
        editor=InstanceEditor(name="_fossilfuels"))

    def _get_fossilfuels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Generation.Production.FossilFuel" ]
        else:
            return []

    _fossilfuels = Property(fget=_get_fossilfuels)

    # A thermal generating unit may have one or more fuel allocation schedules
    ThermalGeneratingUnit = Instance("CIM13r19.Generation.Production.ThermalGeneratingUnit",
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
                    "CIM13r19.Generation.Production.ThermalGeneratingUnit" ]
        else:
            return []

    _thermalgeneratingunits = Property(fget=_get_thermalgeneratingunits)

    # The minimum amount fuel that is allocated for consumption for the scheduled time period, e.g., based on a 'take-or-pay' contract
    minFuelAllocation = Float(desc="The minimum amount fuel that is allocated for consumption for the scheduled time period, e.g., based on a 'take-or-pay' contract")

    # The start time and date of the fuel allocation schedule
    fuelAllocationStartDate = Str(desc="The start time and date of the fuel allocation schedule")

    # The end time and date of the fuel allocation schedule
    fuelAllocationEndDate = Str(desc="The end time and date of the fuel allocation schedule")

    # The type of fuel, which also indicates the corresponding measurement unit
    fuelType = FuelType(desc="The type of fuel, which also indicates the corresponding measurement unit")

    # The maximum amount fuel that is allocated for consumption for the scheduled time period
    maxFuelAllocation = Float(desc="The maximum amount fuel that is allocated for consumption for the scheduled time period")

    #--------------------------------------------------------------------------
    #  Begin "FuelAllocationSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit", "minFuelAllocation", "fuelAllocationStartDate", "fuelAllocationEndDate", "fuelType", "maxFuelAllocation",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "FossilFuel", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.FuelAllocationSchedule",
        title="FuelAllocationSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FuelAllocationSchedule" user definitions:
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
    ThermalGeneratingUnit = Instance("CIM13r19.Generation.Production.ThermalGeneratingUnit",
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
                    "CIM13r19.Generation.Production.ThermalGeneratingUnit" ]
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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit", "emissionType", "emissionValueSource",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.EmissionAccount",
        title="EmissionAccount",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EmissionAccount" user definitions:
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
    HydroGeneratingUnit = Instance("CIM13r19.Generation.Production.HydroGeneratingUnit",
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
                    "CIM13r19.Generation.Production.HydroGeneratingUnit" ]
        else:
            return []

    _hydrogeneratingunits = Property(fget=_get_hydrogeneratingunits)

    #--------------------------------------------------------------------------
    #  Begin "TailbayLossCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "HydroGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.TailbayLossCurve",
        title="TailbayLossCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TailbayLossCurve" user definitions:
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
    HydroGeneratingUnit = Instance("CIM13r19.Generation.Production.HydroGeneratingUnit",
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
                    "CIM13r19.Generation.Production.HydroGeneratingUnit" ]
        else:
            return []

    _hydrogeneratingunits = Property(fget=_get_hydrogeneratingunits)

    #--------------------------------------------------------------------------
    #  Begin "PenstockLossCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "HydroGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.PenstockLossCurve",
        title="PenstockLossCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PenstockLossCurve" user definitions:
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
    StartupModel = Instance("CIM13r19.Generation.Production.StartupModel",
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
                    "CIM13r19.Generation.Production.StartupModel" ]
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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit", "mainFuelType",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "StartupModel",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.StartMainFuelCurve",
        title="StartMainFuelCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StartMainFuelCurve" user definitions:
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
    SpillsFrom = Instance("CIM13r19.Generation.Production.Reservoir",
        desc="A reservoir may spill into a downstream reservoir",
        transient=True,
        opposite="SpillsInto",
        editor=InstanceEditor(name="_reservoirs"))

    def _get_reservoirs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Generation.Production.Reservoir" ]
        else:
            return []

    _reservoirs = Property(fget=_get_reservoirs)

    # A reservoir may have a level versus volume relationship.
    LevelVsVolumeCurve = List(Instance("CIM13r19.Generation.Production.LevelVsVolumeCurve"),
        desc="A reservoir may have a level versus volume relationship.")

    # A reservoir may have a 'natural' inflow forecast.
    InflowForecast = List(Instance("CIM13r19.Generation.Production.InflowForecast"),
        desc="A reservoir may have a 'natural' inflow forecast.")

    # A reservoir may spill into a downstream reservoir
    SpillsInto = List(Instance("CIM13r19.Generation.Production.Reservoir"),
        desc="A reservoir may spill into a downstream reservoir")

    # Generators discharge water to or pumps are supplied water from a downstream reservoir
    HydroPowerPlants = List(Instance("CIM13r19.Generation.Production.HydroPowerPlant"),
        desc="Generators discharge water to or pumps are supplied water from a downstream reservoir")

    # Generators are supplied water from or pumps discharge water to an upstream reservoir
    UpstreamFrom = List(Instance("CIM13r19.Generation.Production.HydroPowerPlant"),
        desc="Generators are supplied water from or pumps discharge water to an upstream reservoir")

    # A reservoir may have a water level target schedule.
    TargetLevelSchedule = Instance("CIM13r19.Generation.Production.TargetLevelSchedule",
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
                    "CIM13r19.Generation.Production.TargetLevelSchedule" ]
        else:
            return []

    _targetlevelschedules = Property(fget=_get_targetlevelschedules)

    # River outlet works for riparian right releases or other purposes
    riverOutletWorks = Str(desc="River outlet works for riparian right releases or other purposes")

    # Type of spillway gate, including parameters
    spillWayGateType = SpillwayGateType(desc="Type of spillway gate, including parameters")

    # The flow capacity of the spillway in cubic meters per second
    spillwayCapacity = Float(desc="The flow capacity of the spillway in cubic meters per second")

    # The length of the spillway crest in meters
    spillwayCrestLength = Float(desc="The length of the spillway crest in meters")

    # Storage volume between the full supply level and the normal minimum operating level
    activeStorageCapacity = Float(desc="Storage volume between the full supply level and the normal minimum operating level")

    # The spillway water travel delay to the next downstream reservoir
    spillTravelDelay = Float(desc="The spillway water travel delay to the next downstream reservoir")

    # The reservoir's energy storage rating in energy for given head conditions
    energyStorageRating = Float(desc="The reservoir's energy storage rating in energy for given head conditions")

    # Total capacity of reservoir
    grossCapacity = Float(desc="Total capacity of reservoir")

    # Spillway crest level above which water will spill
    spillwayCrestLevel = Float(desc="Spillway crest level above which water will spill")

    # Full supply level, above which water will spill. This can be the spillway crest level or the top of closed gates.
    fullSupplyLevel = Float(desc="Full supply level, above which water will spill. This can be the spillway crest level or the top of closed gates.")

    # Normal minimum operating level below which the penstocks will draw air
    normalMinOperateLevel = Float(desc="Normal minimum operating level below which the penstocks will draw air")

    #--------------------------------------------------------------------------
    #  Begin "Reservoir" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "riverOutletWorks", "spillWayGateType", "spillwayCapacity", "spillwayCrestLength", "activeStorageCapacity", "spillTravelDelay", "energyStorageRating", "grossCapacity", "spillwayCrestLevel", "fullSupplyLevel", "normalMinOperateLevel",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "SpillsFrom", "LevelVsVolumeCurve", "InflowForecast", "SpillsInto", "HydroPowerPlants", "UpstreamFrom", "TargetLevelSchedule",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Generation.Production.Reservoir",
        title="Reservoir",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Reservoir" user definitions:
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
    HydroPump = Instance("CIM13r19.Generation.Production.HydroPump",
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
                    "CIM13r19.Generation.Production.HydroPump" ]
        else:
            return []

    _hydropumps = Property(fget=_get_hydropumps)

    #--------------------------------------------------------------------------
    #  Begin "HydroPumpOpSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "value2Unit", "startTime", "value2Multiplier", "value1Unit", "value1Multiplier", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "HydroPump",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.HydroPumpOpSchedule",
        title="HydroPumpOpSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HydroPumpOpSchedule" user definitions:
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
    ThermalGeneratingUnit = Instance("CIM13r19.Generation.Production.ThermalGeneratingUnit",
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
                    "CIM13r19.Generation.Production.ThermalGeneratingUnit" ]
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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit", "isNetGrossP",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "ThermalGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.HeatRateCurve",
        title="HeatRateCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HeatRateCurve" user definitions:
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
    GeneratingUnit = Instance("CIM13r19.Generation.Production.GeneratingUnit",
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
                    "CIM13r19.Generation.Production.GeneratingUnit" ]
        else:
            return []

    _generatingunits = Property(fget=_get_generatingunits)

    #--------------------------------------------------------------------------
    #  Begin "GenUnitOpSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "value2Unit", "startTime", "value2Multiplier", "value1Unit", "value1Multiplier", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "GeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM13r19.Generation.Production.GenUnitOpSchedule",
        title="GenUnitOpSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GenUnitOpSchedule" user definitions:
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
    Contain_ThermalGeneratingUnits = List(Instance("CIM13r19.Generation.Production.ThermalGeneratingUnit"),
        desc="A thermal generating unit may be a member of a cogeneration plant")

    # A cogeneration plant has a steam sendout schedule
    SteamSendoutSchedule = Instance("CIM13r19.Generation.Production.SteamSendoutSchedule",
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
                    "CIM13r19.Generation.Production.SteamSendoutSchedule" ]
        else:
            return []

    _steamsendoutschedules = Property(fget=_get_steamsendoutschedules)

    # The high pressure steam rating
    cogenHPSteamRating = Float(desc="The high pressure steam rating")

    # The rated output active power of the cogeneration plant
    ratedP = Float(desc="The rated output active power of the cogeneration plant")

    # The low pressure steam sendout
    cogenLPSendoutRating = Float(desc="The low pressure steam sendout")

    # The high pressure steam sendout
    cogenHPSendoutRating = Float(desc="The high pressure steam sendout")

    # The low pressure steam rating
    cogenLPSteamRating = Float(desc="The low pressure steam rating")

    #--------------------------------------------------------------------------
    #  Begin "CogenerationPlant" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "cogenHPSteamRating", "ratedP", "cogenLPSendoutRating", "cogenHPSendoutRating", "cogenLPSteamRating",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "Contain_ThermalGeneratingUnits", "SteamSendoutSchedule",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Generation.Production.CogenerationPlant",
        title="CogenerationPlant",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CogenerationPlant" user definitions:
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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "ratedNetMaxP", "penaltyFactor", "stepChange", "energyMinP", "efficiency", "raiseRampRate", "dispReserveFlag", "startupCost", "highControlLimit", "spinReserveRamp", "controlPulseLow", "genControlSource", "governorSCD", "baseP", "fuelPriority", "maxOperatingP", "genControlMode", "variableCost", "lowControlLimit", "controlPulseHigh", "maxEconomicP", "controlDeadband", "governorMPL", "minEconomicP", "minOperatingP", "controlResponseRate", "modelDetail", "autoCntrlMarginP", "ratedGrossMaxP", "genOperatingMode", "fastStartFlag", "longPF", "normalPF", "maximumAllowableSpinningReserve", "ratedGrossMinP", "allocSpinResP", "startupTime", "initialP", "tieLinePF", "minimumOffTime", "lowerRampRate", "shortPF",
                label="Attributes", columns=4),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "ControlAreaGeneratingUnit", "GrossToNetActivePowerCurves", "Contains_SynchronousMachines", "GenUnitOpSchedule", "GenUnitOpCostCurves",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Generation.Production.NuclearGeneratingUnit",
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

    # A hydro generating unit has an efficiency curve
    HydroGeneratingEfficiencyCurves = List(Instance("CIM13r19.Generation.Production.HydroGeneratingEfficiencyCurve"),
        desc="A hydro generating unit has an efficiency curve")

    # A hydro generating unit has a tailbay loss curve
    TailbayLossCurve = List(Instance("CIM13r19.Generation.Production.TailbayLossCurve"),
        desc="A hydro generating unit has a tailbay loss curve")

    # The hydro generating unit belongs to a hydro power plant
    MemberOf_HydroPowerPlant = Instance("CIM13r19.Generation.Production.HydroPowerPlant",
        desc="The hydro generating unit belongs to a hydro power plant",
        transient=True,
        opposite="Contain_HydroGeneratingUnits",
        editor=InstanceEditor(name="_hydropowerplants"))

    def _get_hydropowerplants(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Generation.Production.HydroPowerPlant" ]
        else:
            return []

    _hydropowerplants = Property(fget=_get_hydropowerplants)

    # A hydro generating unit has a penstock loss curve
    PenstockLossCurve = Instance("CIM13r19.Generation.Production.PenstockLossCurve",
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
                    "CIM13r19.Generation.Production.PenstockLossCurve" ]
        else:
            return []

    _penstocklosscurves = Property(fget=_get_penstocklosscurves)

    # Energy conversion capability for generating.
    energyConversionCapability = HydroEnergyConversionKind(desc="Energy conversion capability for generating.")

    # The equivalent cost of water that drives the hydro turbine, expressed as cost per volume.
    hydroUnitWaterCost = Float(desc="The equivalent cost of water that drives the hydro turbine, expressed as cost per volume.")

    #--------------------------------------------------------------------------
    #  Begin "HydroGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "ratedNetMaxP", "penaltyFactor", "stepChange", "energyMinP", "efficiency", "raiseRampRate", "dispReserveFlag", "startupCost", "highControlLimit", "spinReserveRamp", "controlPulseLow", "genControlSource", "governorSCD", "baseP", "fuelPriority", "maxOperatingP", "genControlMode", "variableCost", "lowControlLimit", "controlPulseHigh", "maxEconomicP", "controlDeadband", "governorMPL", "minEconomicP", "minOperatingP", "controlResponseRate", "modelDetail", "autoCntrlMarginP", "ratedGrossMaxP", "genOperatingMode", "fastStartFlag", "longPF", "normalPF", "maximumAllowableSpinningReserve", "ratedGrossMinP", "allocSpinResP", "startupTime", "initialP", "tieLinePF", "minimumOffTime", "lowerRampRate", "shortPF", "energyConversionCapability", "hydroUnitWaterCost",
                label="Attributes", columns=4),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "ControlAreaGeneratingUnit", "GrossToNetActivePowerCurves", "Contains_SynchronousMachines", "GenUnitOpSchedule", "GenUnitOpCostCurves", "HydroGeneratingEfficiencyCurves", "TailbayLossCurve", "MemberOf_HydroPowerPlant", "PenstockLossCurve",
                label="References", columns=2),
            dock="tab"),
        id="CIM13r19.Generation.Production.HydroGeneratingUnit",
        title="HydroGeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HydroGeneratingUnit" user definitions:
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
    MemberOf_CogenerationPlant = Instance("CIM13r19.Generation.Production.CogenerationPlant",
        desc="A thermal generating unit may be a member of a cogeneration plant",
        transient=True,
        opposite="Contain_ThermalGeneratingUnits",
        editor=InstanceEditor(name="_cogenerationplants"))

    def _get_cogenerationplants(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Generation.Production.CogenerationPlant" ]
        else:
            return []

    _cogenerationplants = Property(fget=_get_cogenerationplants)

    # A thermal generating unit may have one or more fuel allocation schedules
    FuelAllocationSchedules = List(Instance("CIM13r19.Generation.Production.FuelAllocationSchedule"),
        desc="A thermal generating unit may have one or more fuel allocation schedules")

    # A thermal generating unit may have  one or more emission curves
    EmissionCurves = List(Instance("CIM13r19.Generation.Production.EmissionCurve"),
        desc="A thermal generating unit may have  one or more emission curves")

    # A thermal generating unit may have one or more emission allowance accounts
    EmmissionAccounts = List(Instance("CIM13r19.Generation.Production.EmissionAccount"),
        desc="A thermal generating unit may have one or more emission allowance accounts")

    # A thermal generating unit may have a startup model
    StartupModel = Instance("CIM13r19.Generation.Production.StartupModel",
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
                    "CIM13r19.Generation.Production.StartupModel" ]
        else:
            return []

    _startupmodels = Property(fget=_get_startupmodels)

    # A thermal generating unit may have one or more fossil fuels
    FossilFuels = List(Instance("CIM13r19.Generation.Production.FossilFuel"),
        desc="A thermal generating unit may have one or more fossil fuels")

    # A thermal generating unit may have an incremental heat rate curve
    IncrementalHeatRateCurve = Instance("CIM13r19.Generation.Production.IncrementalHeatRateCurve",
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
                    "CIM13r19.Generation.Production.IncrementalHeatRateCurve" ]
        else:
            return []

    _incrementalheatratecurves = Property(fget=_get_incrementalheatratecurves)

    # A thermal generating unit may have a shutdown curve
    ShutdownCurve = Instance("CIM13r19.Generation.Production.ShutdownCurve",
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
                    "CIM13r19.Generation.Production.ShutdownCurve" ]
        else:
            return []

    _shutdowncurves = Property(fget=_get_shutdowncurves)

    # A thermal generating unit may have a heat rate curve
    HeatRateCurve = Instance("CIM13r19.Generation.Production.HeatRateCurve",
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
                    "CIM13r19.Generation.Production.HeatRateCurve" ]
        else:
            return []

    _heatratecurves = Property(fget=_get_heatratecurves)

    # A thermal generating unit may be a member of a compressed air energy storage plant
    MemberOf_CAESPlant = Instance("CIM13r19.Generation.Production.CAESPlant",
        desc="A thermal generating unit may be a member of a compressed air energy storage plant",
        transient=True,
        opposite="Contain_ThermalGeneratingUnit",
        editor=InstanceEditor(name="_caesplants"))

    def _get_caesplants(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Generation.Production.CAESPlant" ]
        else:
            return []

    _caesplants = Property(fget=_get_caesplants)

    # A thermal generating unit may have a heat input curve
    HeatInputCurve = Instance("CIM13r19.Generation.Production.HeatInputCurve",
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
                    "CIM13r19.Generation.Production.HeatInputCurve" ]
        else:
            return []

    _heatinputcurves = Property(fget=_get_heatinputcurves)

    # A thermal generating unit may be a member of a combined cycle plant
    MemberOf_CombinedCyclePlant = Instance("CIM13r19.Generation.Production.CombinedCyclePlant",
        desc="A thermal generating unit may be a member of a combined cycle plant",
        transient=True,
        opposite="Contain_ThermalGeneratingUnits",
        editor=InstanceEditor(name="_combinedcycleplants"))

    def _get_combinedcycleplants(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Generation.Production.CombinedCyclePlant" ]
        else:
            return []

    _combinedcycleplants = Property(fget=_get_combinedcycleplants)

    # Operating and maintenance cost for the thermal unit
    oMCost = Float(desc="Operating and maintenance cost for the thermal unit")

    #--------------------------------------------------------------------------
    #  Begin "ThermalGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "ratedNetMaxP", "penaltyFactor", "stepChange", "energyMinP", "efficiency", "raiseRampRate", "dispReserveFlag", "startupCost", "highControlLimit", "spinReserveRamp", "controlPulseLow", "genControlSource", "governorSCD", "baseP", "fuelPriority", "maxOperatingP", "genControlMode", "variableCost", "lowControlLimit", "controlPulseHigh", "maxEconomicP", "controlDeadband", "governorMPL", "minEconomicP", "minOperatingP", "controlResponseRate", "modelDetail", "autoCntrlMarginP", "ratedGrossMaxP", "genOperatingMode", "fastStartFlag", "longPF", "normalPF", "maximumAllowableSpinningReserve", "ratedGrossMinP", "allocSpinResP", "startupTime", "initialP", "tieLinePF", "minimumOffTime", "lowerRampRate", "shortPF", "oMCost",
                label="Attributes", columns=4),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "ControlAreaGeneratingUnit", "GrossToNetActivePowerCurves", "Contains_SynchronousMachines", "GenUnitOpSchedule", "GenUnitOpCostCurves", "MemberOf_CogenerationPlant", "FuelAllocationSchedules", "EmissionCurves", "EmmissionAccounts", "StartupModel", "FossilFuels", "IncrementalHeatRateCurve", "ShutdownCurve", "HeatRateCurve", "MemberOf_CAESPlant", "HeatInputCurve", "MemberOf_CombinedCyclePlant",
                label="References", columns=2),
            dock="tab"),
        id="CIM13r19.Generation.Production.ThermalGeneratingUnit",
        title="ThermalGeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ThermalGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
