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

from CIM13.Core import RegularIntervalSchedule
from CIM13.Core import ConductingEquipment
from CIM13.Core import IdentifiedObject
from CIM13.Core import PowerSystemResource
from CIM13.Core import EquipmentContainer
from CIM13.Core import Equipment
from CIM13 import Root
from CIM13.Core import Curve
from CIM13.Core import PhaseCode



from enthought.traits.api import Instance, List, Enum, Float, Bool, Int, Str
# <<< imports

# >>> imports

#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


WindingConnection = Enum("D", "Z", "Y")

TransformerCoolingType = Enum()

SVCControlMode = Enum("voltage", "reactivePower", "off")

TransformerControlMode = Enum("volt", "off", "local", "reactive", "active")

SynchronousMachineOperatingMode = Enum("generator", "condenser")

RegulatingControlModeKind = Enum("reactivePower", "currentFlow", "fixed", "activePower", "voltage")

WindingType = Enum("quaternary", "tertiary", "primary", "secondary")

CoolantType = Enum("hydrogenGas", "water", "air")

SynchronousMachineType = Enum("generator_or_condenser", "condenser", "generator")

TapChangerKind = Enum("voltageControl", "fixed", "phaseControl", "voltageAndPhaseControl")

#------------------------------------------------------------------------------
#  "RegulationSchedule" class:
#------------------------------------------------------------------------------

class RegulationSchedule(RegularIntervalSchedule):
    """ A pre-established pattern over time for a controlled variable, e.g., busbar voltage.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    RegulatingControl = List(Instance("CIM13.Wires.RegulatingControl"))

    # A VoltageControlZone may have a  voltage regulation schedule.
    VoltageControlZones = List(Instance("CIM13.Wires.VoltageControlZone"))

    # Line drop resistance.
    lineDropR = EFloat

    # Flag to indicate that line drop compensation is to be applied
    lineDropCompensation = EBoolean

    # Line drop reactance.
    lineDropX = EFloat

    #--------------------------------------------------------------------------
    #  Begin regulationSchedule user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End regulationSchedule user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransformerWinding" class:
#------------------------------------------------------------------------------

class TransformerWinding(ConductingEquipment):
    """ A winding is associated with each defined terminal of a transformer (or phase shifter).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The winding to which the test was conducted
    To_WindingTest = List(Instance("CIM13.Wires.WindingTest"))

    # The winding from which the test was conducted
    From_WindingTest = List(Instance("CIM13.Wires.WindingTest"))

    # A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.
    TapChangers = List(Instance("CIM13.Wires.TapChanger"))

    # A transformer has windings
    MemberOf_PowerTransformer = Instance("CIM13.Wires.PowerTransformer")

    # The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.
    ratedU = EFloat

    # Ground resistance path through connected grounding transformer.
    rground = EFloat

    # Zero sequence magnetizing branch susceptance.
    b0 = EFloat

    # Positive sequence series resistance of the winding.
    r = EFloat

    # Ground reactance path through connected grounding transformer.
    xground = EFloat

    # Magnetizing branch susceptance (B mag).
    b = EFloat

    # Zero sequence series resistance of the winding.
    r0 = EFloat

    # Set if the winding is grounded.
    grounded = EBoolean

    # Apparent power that the winding can carry for a short period of time.
    shortTermS = EFloat

    # The normal apparent power rating for the winding
    ratedS = EFloat

    # Positive sequence series reactance of the winding.
    x = EFloat

    # The type of winding.
    windingType = WindingType

    # The apparent power that the winding can carry  under emergency conditions.
    emergencyS = EFloat

    # Basic insulation level voltage rating
    insulationU = EFloat

    # Magnetizing branch conductance (G mag).
    g = EFloat

    # Zero sequence magnetizing branch conductance.
    g0 = EFloat

    # Zero sequence series reactance of the winding.
    x0 = EFloat

    # The type of connection of the winding.
    connectionType = WindingConnection

    #--------------------------------------------------------------------------
    #  Begin transformerWinding user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End transformerWinding user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EnergySource" class:
#------------------------------------------------------------------------------

class EnergySource(ConductingEquipment):
    """ A generic equivalent for an energy supplier on a transmission or distribution voltage level.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Zero sequence Thevenin resistance.
    r0 = EFloat

    # Phase-to-phase nominal voltage.
    nominalVoltage = EFloat

    # Positive sequence Thevenin resistance.
    r = EFloat

    # Phase-to-phase open circuit voltage magnitude.
    voltageMagnitude = EFloat

    # Positive sequence Thevenin reactance.
    x = EFloat

    # Phase angle of a-phase open circuit.
    voltageAngle = EFloat

    # Negative sequence Thevenin resistance.
    rn = EFloat

    # High voltage source load
    activePower = EFloat

    # Negative sequence Thevenin reactance.
    xn = EFloat

    # Zero sequence Thevenin reactance.
    x0 = EFloat

    #--------------------------------------------------------------------------
    #  Begin energySource user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End energySource user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SeriesCompensator" class:
#------------------------------------------------------------------------------

class SeriesCompensator(ConductingEquipment):
    """ A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Positive sequence reactance.
    x = EFloat

    # Positive sequence resistance.
    r = EFloat

    #--------------------------------------------------------------------------
    #  Begin seriesCompensator user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End seriesCompensator user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WireType" class:
#------------------------------------------------------------------------------

class WireType(IdentifiedObject):
    """ Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A WireType is mounted at a specified place in a WireArrangement.
    WireArrangements = List(Instance("CIM13.Wires.WireArrangement"))

    # Number of conductor strands in the (symmetrical) bundle (1-12)
    phaseConductorCount = EInt

    # Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.
    gMR = EFloat

    # Distance between conductor strands in a (symmetrical) bundle.
    phaseConductorSpacing = EFloat

    # Current carrying capacity of a wire or cable under stated thermal conditions
    ratedCurrent = EFloat

    # The radius of the conductor
    radius = EFloat

    # The resistance per unit length of the conductor
    resistance = EFloat

    #--------------------------------------------------------------------------
    #  Begin wireType user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End wireType user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "VoltageControlZone" class:
#------------------------------------------------------------------------------

class VoltageControlZone(PowerSystemResource):
    """ An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A VoltageControlZone may have a  voltage regulation schedule.
    RegulationSchedule = Instance("CIM13.Wires.RegulationSchedule")

    # A VoltageControlZone is controlled by a designated BusbarSection.
    BusbarSection = Instance("CIM13.Wires.BusbarSection")

    #--------------------------------------------------------------------------
    #  Begin voltageControlZone user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End voltageControlZone user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegulatingCondEq" class:
#------------------------------------------------------------------------------

class RegulatingCondEq(ConductingEquipment):
    """ RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    RegulatingControl = Instance("CIM13.Wires.RegulatingControl")

    # The association gives the control output that is used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuators.
    Controls = List(Instance("CIM13.Meas.Control"))

    #--------------------------------------------------------------------------
    #  Begin regulatingCondEq user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End regulatingCondEq user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Conductor" class:
#------------------------------------------------------------------------------

class Conductor(ConductingEquipment):
    """ Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Sections of conductor are physically described by a conductor type
    ConductorType = Instance("CIM13.Wires.ConductorType")

    # Zero sequence series resistance of the entire line section.
    r0 = EFloat

    # Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
    g0ch = EFloat

    # Segment length for calculating line section capabilities
    length = EFloat

    # Positive sequence series reactance of the entire line section.
    x = EFloat

    # Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
    gch = EFloat

    # Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    b0ch = EFloat

    # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    bch = EFloat

    # Zero sequence series reactance of the entire line section.
    x0 = EFloat

    # Positive sequence series resistance of the entire line section.
    r = EFloat

    #--------------------------------------------------------------------------
    #  Begin conductor user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End conductor user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Line" class:
#------------------------------------------------------------------------------

class Line(EquipmentContainer):
    """ A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A Line can be contained by a SubGeographical Region.
    Region = Instance("CIM13.Core.SubGeographicalRegion")

    #--------------------------------------------------------------------------
    #  Begin line user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End line user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Ground" class:
#------------------------------------------------------------------------------

class Ground(ConductingEquipment):
    """ A common point for connecting grounded conducting equipment such as shunt capacitors. The power system model can have more than one ground.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin ground user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End ground user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TapChanger" class:
#------------------------------------------------------------------------------

class TapChanger(PowerSystemResource):
    """ Mechanism for changing transformer winding tap positions.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.
    TransformerWinding = Instance("CIM13.Wires.TransformerWinding")

    RegulatingControl = Instance("CIM13.Wires.RegulatingControl")

    # The neutral tap step position for this winding.
    neutralStep = EInt

    # Lowest possible tap step position, retard from neutral
    lowStep = EInt

    # For an LTC, the tap changer control mode.
    tculControlMode = TransformerControlMode

    # Voltage at which the winding operates at the neutral tap setting.
    neutralU = EFloat

    # The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.
    normalStep = EInt

    # Highest possible tap step position, advance from neutral
    highStep = EInt

    # The type of tap changer. Indicates the ability of the transformer to perform various regulation tasks. The tap changer must be also be associated wtih a RegulationControl object before any regulation is possible.
    type = TapChangerKind

    # Tap step increment, in per cent of nominal voltage, per step position.
    stepVoltageIncrement = EFloat

    # For an LTC, the delay for subsequent tap changer operation (second and later step changes)
    subsequentDelay = EFloat

    # For an LTC, the delay for initial tap changer operation (first step change)
    initialDelay = EFloat

    # Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer).
    stepPhaseShiftIncrement = EFloat

    #--------------------------------------------------------------------------
    #  Begin tapChanger user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End tapChanger user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CompositeSwitch" class:
#------------------------------------------------------------------------------

class CompositeSwitch(Equipment):
    """ A model of a set of individual Switches normally enclosed within the same cabinet and possibly with interlocks that restrict the combination of switch positions. These are typically found in medium voltage distribution networks.  A CompositeSwitch could represent a Ring-Main-Unit (RMU), or pad-mounted switchgear, with primitive internal devices such as an internal bus-bar plus 3 or 4 internal switches each of which may individually be open or closed. A CompositeSwitch and a set of contained Switches can also be used to represent a multi-position switch e.g. a switch that can connect a circuit to Ground, Open or Busbar.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Switches = List(Instance("CIM13.Wires.Switch"))

    # An alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any
    compositeSwitchType = EString

    #--------------------------------------------------------------------------
    #  Begin compositeSwitch user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End compositeSwitch user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WireArrangement" class:
#------------------------------------------------------------------------------

class WireArrangement(IdentifiedObject):
    """ Identification, spacing and configuration of the wires of a ConductorType, with reference to their type.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A ConductorType is made up of wires that can be configured in several ways.
    ConductorType = Instance("CIM13.Wires.ConductorType")

    # A WireType is mounted at a specified place in a WireArrangement.
    WireType = Instance("CIM13.Wires.WireType")

    # Mounting point where wire One is mounted.
    mountingPointX = EInt

    # Mounting point where wire One is mounted.
    mountingPointY = EInt

    #--------------------------------------------------------------------------
    #  Begin wireArrangement user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End wireArrangement user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PowerTransformer" class:
#------------------------------------------------------------------------------

class PowerTransformer(Equipment):
    """ An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transformer has windings
    Contains_TransformerWindings = List(Instance("CIM13.Wires.TransformerWinding"))

    # A transformer may have a heat exchanger
    HeatExchanger = Instance("CIM13.Wires.HeatExchanger")

    # Type of transformer cooling
    transfCoolingType = TransformerCoolingType

    # Describes the phases carried by a power transformer.
    phases = PhaseCode

    # Core shunt magnetizing susceptance in the saturation region.
    bmagSat = EFloat

    # Core magnetizing saturation curve knee flux level.
    magSatFlux = EFloat

    # The reference voltage at which the magnetizing saturation measurements were made
    magBaseU = EFloat

    #--------------------------------------------------------------------------
    #  Begin powerTransformer user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End powerTransformer user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MutualCoupling" class:
#------------------------------------------------------------------------------

class MutualCoupling(Root):
    """ This class represents the zero sequence line mutual coupling.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    First_ACLineSegment = Instance("CIM13.Wires.ACLineSegment")

    Second_ACLineSegment = Instance("CIM13.Wires.ACLineSegment")

    # Zero sequence branch-to-branch mutual impedance coupling, reactance
    x0 = EFloat

    # Distance from the second line's from bus to end of coupled region
    distance22 = EFloat

    # Distance from the first line's from bus to start of coupled region
    distance11 = EFloat

    # Distance from the first line's from bus to end of coupled region
    distance12 = EFloat

    # Zero sequence branch-to-branch mutual impedance coupling, resistance
    r0 = EFloat

    # Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.
    b0ch = EFloat

    # Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.
    g0ch = EFloat

    # Distance from the second line's from bus to start of coupled region
    distance21 = EFloat

    #--------------------------------------------------------------------------
    #  Begin mutualCoupling user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End mutualCoupling user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RectifierInverter" class:
#------------------------------------------------------------------------------

class RectifierInverter(ConductingEquipment):
    """ Bi-directional AC-DC conversion equipment that can be used to control DC current, DC voltage, DC power flow, or firing angle.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Rectifier/inverter primary base voltage
    ratedU = EFloat

    # Operating mode for the converter.
    operatingMode = EString

    # Frequency on the AC side.
    frequency = EFloat

    # The maximum voltage on the DC side at which the converter should operate.
    maxU = EFloat

    # Commutating resistance.
    commutatingResistance = EFloat

    # The minimum active power on the DC side at which the converter should operate.
    minP = EFloat

    # Number of bridges
    bridges = EInt

    # Commutating reactance at AC bus frequency.
    commutatingReactance = EFloat

    # The maximum active power on the DC side at which the fconverter should operate.
    maxP = EFloat

    # Minimum compounded DC voltage
    minCompoundVoltage = EFloat

    # Compounding resistance.
    compoundResistance = EFloat

    # The minimum voltage on the DC side at which the converter should operate.
    minU = EFloat

    #--------------------------------------------------------------------------
    #  Begin rectifierInverter user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End rectifierInverter user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "HeatExchanger" class:
#------------------------------------------------------------------------------

class HeatExchanger(Equipment):
    """ Equipment for the cooling of electrical equipment and the extraction of heat
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transformer may have a heat exchanger
    PowerTransformer = Instance("CIM13.Wires.PowerTransformer")

    #--------------------------------------------------------------------------
    #  Begin heatExchanger user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End heatExchanger user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EnergyConsumer" class:
#------------------------------------------------------------------------------

class EnergyConsumer(ConductingEquipment):
    """ Generic user of energy - a  point of consumption on the power system model
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An energy consumer is assigned to a power cut zone
    PowerCutZone = Instance("CIM13.LoadModel.PowerCutZone")

    LoadResponse = Instance("CIM13.LoadModel.LoadResponseCharacteristic")

    # Number of individual customers represented by this Demand
    customerCount = EInt

    # Reactive power of the load that is a fixed quantity.
    qfixed = EFloat

    # Active power of the load that is a fixed quantity.
    pfixed = EFloat

    # Fixed reactive power as per cent of load group fixed reactive power.
    qfixedPct = EFloat

    # Fixed active power as per cent of load group fixed active power
    pfixedPct = EFloat

    #--------------------------------------------------------------------------
    #  Begin energyConsumer user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End energyConsumer user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Switch" class:
#------------------------------------------------------------------------------

class Switch(ConductingEquipment):
    """ A generic device designed to close, or open, or both, one or more electric circuits.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A switch may be operated by many schedules.
    SwitchingOperations = List(Instance("CIM13.Outage.SwitchingOperation"))

    CompositeSwitch = Instance("CIM13.Wires.CompositeSwitch")

    # Branch is retained in a bus branch model.
    retained = EBoolean

    # The date and time when the switch was last switched on.
    switchOnDate = EString

    # The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.
    normalOpen = EBoolean

    # The switch on count since the switch was last reset or initialized.
    switchOnCount = EInt

    #--------------------------------------------------------------------------
    #  Begin switch user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End switch user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegulatingControl" class:
#------------------------------------------------------------------------------

class RegulatingControl(PowerSystemResource):
    """ Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    RegulatingCondEq = List(Instance("CIM13.Wires.RegulatingCondEq"))

    TapChanger = List(Instance("CIM13.Wires.TapChanger"))

    Terminal = Instance("CIM13.Core.Terminal")

    RegulationSchedule = Instance("CIM13.Wires.RegulationSchedule")

    # The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute.
    targetValue = EFloat

    # The regulation is performed in a discrete mode.
    discrete = EBoolean

    # This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode.
    targetRange = EFloat

    # The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule.
    mode = RegulatingControlModeKind

    #--------------------------------------------------------------------------
    #  Begin regulatingControl user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End regulatingControl user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Connector" class:
#------------------------------------------------------------------------------

class Connector(ConductingEquipment):
    """ A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation and are modelled with a single logical terminal.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin connector user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End connector user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WindingTest" class:
#------------------------------------------------------------------------------

class WindingTest(IdentifiedObject):
    """ Physical winding test data for the winding/tap pairs of a transformer (or phase shifter). This test data can be used to derive other attributes of specific transformer or phase shifter models.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The winding to which the test was conducted
    To_TransformerWinding = Instance("CIM13.Wires.TransformerWinding")

    # The winding from which the test was conducted
    From_TransformerWinding = Instance("CIM13.Wires.TransformerWinding")

    # The load loss kW ('to' winding short-circuited) from the test report.
    loadLoss = EFloat

    # The tap step number for the 'to' winding of the test pair.
    toTapStep = EInt

    # The tap step number for the 'from' winding of the test pair.
    fromTapStep = EInt

    # The no load loss kW 'to' winding open-circuited) from the test report.
    noLoadLoss = EFloat

    # The voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    voltage = EFloat

    # The phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    phaseShift = EFloat

    # The leakage impedance measured at the 'from' winding  with the 'to' winding short-circuited and all other windings open-circuited.  Leakage impedance is expressed in units based on the apparent power and voltage ratings of the 'from' winding.
    leakageImpedance = EFloat

    # The exciting current on open-circuit test, expressed as a percentage of rated current, at nominal voltage
    excitingCurrent = EFloat

    #--------------------------------------------------------------------------
    #  Begin windingTest user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End windingTest user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConductorType" class:
#------------------------------------------------------------------------------

class ConductorType(IdentifiedObject):
    """ Wire or cable conductor (per IEEE specs). A specific type of wire or combination of wires not insulated from one another, suitable for carrying electric current. It may be bare or insulated.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Sections of conductor are physically described by a conductor type
    Conductors = List(Instance("CIM13.Wires.Conductor"))

    # A ConductorType is made up of wires that can be configured in several ways.
    WireArrangements = List(Instance("CIM13.Wires.WireArrangement"))

    # Reactance of the sheath for cable conductors.
    sheathReactance = EFloat

    # Resistance of the sheath for cable conductors.
    sheathResistance = EFloat

    #--------------------------------------------------------------------------
    #  Begin conductorType user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End conductorType user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Plant" class:
#------------------------------------------------------------------------------

class Plant(EquipmentContainer):
    """ A Plant is a collection of equipment for purposes of generation.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin plant user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End plant user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ReactiveCapabilityCurve" class:
#------------------------------------------------------------------------------

class ReactiveCapabilityCurve(Curve):
    """ Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SynchronousMachines = List(Instance("CIM13.Wires.SynchronousMachine"))

    # Defines the default MVArCapabilityCurve for use by a SynchronousMachine.
    InitiallyUsedBySynchronousMachine = List(Instance("CIM13.Wires.SynchronousMachine"))

    # The machine's coolant temperature (e.g., ambient air or stator circulating water).
    coolantTemperature = EFloat

    # The hydrogen coolant pressure
    hydrogenPressure = EFloat

    #--------------------------------------------------------------------------
    #  Begin reactiveCapabilityCurve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End reactiveCapabilityCurve user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GroundDisconnector" class:
#------------------------------------------------------------------------------

class GroundDisconnector(Switch):
    """ A manually operated or motor operated mechanical switching device used for isolating a circuit or equipment from Ground.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin groundDisconnector user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End groundDisconnector user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FrequencyConverter" class:
#------------------------------------------------------------------------------

class FrequencyConverter(RegulatingCondEq):
    """ A device to convert from one frequency to another (e.g., frequency F1 to F2) comprises a pair of FrequencyConverter instances. One converts from F1 to DC, the other converts the DC to F2.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The maximum active power on the DC side at which the frequence converter should operate.
    maxP = EFloat

    # Frequency on the AC side.
    frequency = EFloat

    # The minimum voltage on the DC side at which the frequency converter should operate.
    minU = EFloat

    # The minimum active power on the DC side at which the frequence converter should operate.
    minP = EFloat

    # Operating mode for the frequency converter
    operatingMode = EString

    # The maximum voltage on the DC side at which the frequency converter should operate.
    maxU = EFloat

    #--------------------------------------------------------------------------
    #  Begin frequencyConverter user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End frequencyConverter user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ProtectedSwitch" class:
#------------------------------------------------------------------------------

class ProtectedSwitch(Switch):
    """ A ProtectedSwitch is a switching device that can be operated by ProtectionEquipment.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Circuit breakers may be operated by protection relays.
    OperatedBy_ProtectionEquipments = List(Instance("CIM13.Protection.ProtectionEquipment"))

    # A breaker may have zero or more automatic reclosures after a trip occurs.
    RecloseSequences = List(Instance("CIM13.Protection.RecloseSequence"))

    #--------------------------------------------------------------------------
    #  Begin protectedSwitch user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End protectedSwitch user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Jumper" class:
#------------------------------------------------------------------------------

class Jumper(Switch):
    """ A short section of conductor with negligible impedance which can be manually removed and replaced if the circuit is de-energized. Note that zero-impedance branches can be modelled by an ACLineSegment with a zero impedance ConductorType
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin jumper user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End jumper user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DCLineSegment" class:
#------------------------------------------------------------------------------

class DCLineSegment(Conductor):
    """ A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to carry direct current between points in the DC region of the power system.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Inductance of the DC line segment.
    dcSegmentInductance = EFloat

    # Resistance of the DC line segment.
    dcSegmentResistance = EFloat

    #--------------------------------------------------------------------------
    #  Begin dCLineSegment user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End dCLineSegment user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BusbarSection" class:
#------------------------------------------------------------------------------

class BusbarSection(Connector):
    """ A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A VoltageControlZone is controlled by a designated BusbarSection.
    VoltageControlZone = Instance("CIM13.Wires.VoltageControlZone")

    #--------------------------------------------------------------------------
    #  Begin busbarSection user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End busbarSection user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ACLineSegment" class:
#------------------------------------------------------------------------------

class ACLineSegment(Conductor):
    """ A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    HasFirst_MutualCoupling = List(Instance("CIM13.Wires.MutualCoupling"))

    HasSecond_MutualCoupling = List(Instance("CIM13.Wires.MutualCoupling"))

    #--------------------------------------------------------------------------
    #  Begin aCLineSegment user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End aCLineSegment user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ShuntCompensator" class:
#------------------------------------------------------------------------------

class ShuntCompensator(RegulatingCondEq):
    """ A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The date and time when the capacitor bank was last switched on.
    switchOnDate = EString

    # The maximum voltage at which the capacitor bank should operate.
    maxU = EFloat

    # Time delay required for the device to be connected or disconnected by automatic voltage regulation (AVR).
    aVRDelay = EFloat

    # For a capacitor bank, the maximum number of sections that may be switched in.
    maximumSections = EInt

    # For a capacitor bank, the admittance of each switchable section. Calculated using the reactive power per section and corrected for network voltage.
    yPerSection = EFloat

    # Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power.
    voltageSensitivity = EFloat

    # The switch on count since the capacitor count was last reset or initialized.
    switchOnCount = EInt

    # For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).
    normalSections = EInt

    # Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.
    nomQ = EFloat

    # For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.
    reactivePerSection = EFloat

    # Zero sequence shunt (charging) conductance per section
    g0PerSection = EFloat

    # The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.
    nomU = EFloat

    # The minimum voltage at which the capacitor bank should operate.
    minU = EFloat

    # Zero sequence shunt (charging) susceptance per section
    b0PerSection = EFloat

    #--------------------------------------------------------------------------
    #  Begin shuntCompensator user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End shuntCompensator user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Fuse" class:
#------------------------------------------------------------------------------

class Fuse(Switch):
    """ An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Fault interrupting current rating.
    ampRating = EFloat

    #--------------------------------------------------------------------------
    #  Begin fuse user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End fuse user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SynchronousMachine" class:
#------------------------------------------------------------------------------

class SynchronousMachine(RegulatingCondEq):
    """ An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ReactiveCapabilityCurves = List(Instance("CIM13.Wires.ReactiveCapabilityCurve"))

    # The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
    Drives_HydroPump = Instance("CIM13.Generation.Production.HydroPump")

    # A synchronous machine may operate as a generator and as such becomes a member of a generating unit
    MemberOf_GeneratingUnit = Instance("CIM13.Generation.Production.GeneratingUnit")

    # Defines the default MVArCapabilityCurve for use by a SynchronousMachine.
    InitialReactiveCapabilityCurve = Instance("CIM13.Wires.ReactiveCapabilityCurve")

    DrivenBy_PrimeMover = List(Instance("CIM13.Generation.GenerationDynamics.PrimeMover"))

    # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
    maxQ = EFloat

    # Method of cooling the machine.
    coolantType = CoolantType

    # Quadrature-axis subtransient reactance, also known as X'q.
    xQuadSubtrans = EFloat

    # Quadrature-axis synchronous reactance (Xq) , the ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.
    xQuadSync = EFloat

    # Current mode of operation.
    operatingMode = SynchronousMachineOperatingMode

    # Minimum reactive power limit for the unit.
    minQ = EFloat

    # Zero sequence reactance of the synchronous machine.
    x0 = EFloat

    # Time delay required when switching from Manual to Automatic Voltage Regulation. This value is used in the accelerating power reference frame for powerflow solutions
    manualToAVR = EFloat

    # Maximum voltage limit for the unit.
    maxU = EFloat

    # Negative sequence resistance.
    r2 = EFloat

    # Direct-axis transient reactance, also known as X'd.
    xDirectTrans = EFloat

    # Damping torque coefficient, a proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.
    damping = EFloat

    # Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a lagging MVAr violation.
    aVRToManualLag = EFloat

    # Positive sequence reactance of the synchronous machine.
    x = EFloat

    # Minimum voltage  limit for the unit.
    minU = EFloat

    # The energy stored in the rotor when operating at rated speed. This value is used in the accelerating power reference frame for  operator training simulator solutions.
    inertia = EFloat

    # Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a leading MVAr violation.
    aVRToManualLead = EFloat

    # Positive sequence resistance of the synchronous machine.
    r = EFloat

    # Nameplate apparent power rating for the unit
    ratedS = EFloat

    # Active power consumed when in condenser mode operation.
    condenserP = EFloat

    # Default base reactive power value. This value represents the initial reactive power that can be used by any application function.
    baseQ = EFloat

    # Quadrature-axis transient reactance, also known as X'q.
    xQuadTrans = EFloat

    # Zero sequence resistance of the synchronous machine.
    r0 = EFloat

    # Priority of unit for reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on.
    referencePriority = EInt

    # Percent of the coordinated reactive control that comes from this machine.
    qPercent = EFloat

    # Direct-axis synchronous reactance. The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. (Xd)
    xDirectSync = EFloat

    # Negative sequence reactance.
    x2 = EFloat

    # Temperature or pressure of coolant medium
    coolantCondition = EFloat

    # Modes that this synchronous machine can operate in.
    type = SynchronousMachineType

    # Direct-axis subtransient reactance, also known as X'd.
    xDirectSubtrans = EFloat

    #--------------------------------------------------------------------------
    #  Begin synchronousMachine user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End synchronousMachine user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StaticVarCompensator" class:
#------------------------------------------------------------------------------

class StaticVarCompensator(RegulatingCondEq):
    """ A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.
    voltageSetPoint = EFloat

    # Maximum available capacitive reactive power
    capacitiveRating = EFloat

    # SVC control mode.
    sVCControlMode = SVCControlMode

    # The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.
    slope = EFloat

    # Maximum available inductive reactive power
    inductiveRating = EFloat

    #--------------------------------------------------------------------------
    #  Begin staticVarCompensator user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End staticVarCompensator user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Junction" class:
#------------------------------------------------------------------------------

class Junction(Connector):
    """ A point where one or more conducting equipments are connected with zero resistance.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin junction user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End junction user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Disconnector" class:
#------------------------------------------------------------------------------

class Disconnector(Switch):
    """ A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin disconnector user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End disconnector user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Breaker" class:
#------------------------------------------------------------------------------

class Breaker(ProtectedSwitch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The transition time from open to close.
    inTransitTime = EFloat

    # Fault interrupting current rating.
    ratedCurrent = EFloat

    #--------------------------------------------------------------------------
    #  Begin breaker user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End breaker user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadBreakSwitch" class:
#------------------------------------------------------------------------------

class LoadBreakSwitch(ProtectedSwitch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Current carrying capacity of a wire or cable under stated thermal conditions.
    ratedCurrent = EFloat

    #--------------------------------------------------------------------------
    #  Begin loadBreakSwitch user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End loadBreakSwitch user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
