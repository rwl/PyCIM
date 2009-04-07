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

""" An extension to the Core and Topology package that models information on the electrical characteristics of Transmission and Distribution networks. This package is used by network applications such as State Estimation, Load Flow and Optimal Power Flow.  
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from iec61970.core import ConductingEquipment
from iec61970.core import IdentifiedObject
from iec61970.core import Equipment
from iec61970.core import RegularIntervalSchedule
from iec61970.core import PowerSystemResource
from iec61970.core import EquipmentContainer
from iec61970.core import Curve
from iec61970.domain import CurrentFlow
from iec61970.domain import Seconds
from iec61970.domain import Impedance
from iec61970.domain import Voltage
from iec61970.domain import Integer
from iec61970.domain import ReactivePower
from iec61970.domain import AbsoluteDateTime
from iec61970.domain import VoltagePerReactivePower
from iec61970.domain import Admittance
from iec61970.domain import Susceptance
from iec61970.domain import Conductance
from iec61970.domain import LongLength
from iec61970.domain import Resistance
from iec61970.domain import Reactance
from iec61970.domain import Inductance
from iec61970.domain import Frequency
from iec61970.domain import ActivePower
from iec61970.domain import Boolean
from iec61970.domain import AngleDegrees
from iec61970.domain import PerCent
from iec61970.core import PhaseCode
from iec61970.domain import ApparentPower
from iec61970.domain import KWActivePower
from iec61970.domain import Float
from iec61970.domain import Damping
from iec61970.domain import PU
from iec61970.domain import Temperature
from iec61970.domain import Pressure
from iec61970.domain import AngleRadians
from iec61970.domain import ShortLength
from iec61970.domain import String



from enthought.traits.api import Instance, List, Str, Enum, Int, Bool, Float
# <<< imports

# >>> imports

#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------
CompositeSwitchType = Str(desc="An alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any")
OperatingMode = Str(desc="Textual name for an operating mode")

# Control modes for a transformer, i.e., Off, Local, Volt, MVAr
TransformerControlMode = Enum("off", "local", "volt", "active", "reactive", desc="Control modes for a transformer, i.e., Off, Local, Volt, MVAr")
# Textual name for a control mode
SVCControlMode = Enum("reactivePower", "voltage", "off", desc="Textual name for a control mode")
# Method of cooling a machine.
CoolantType = Enum("air", "hydrogenGas", "water", desc="Method of cooling a machine.")

SynchronousMachineOperatingMode = Enum("generator", "condenser")

SynchronousMachineType = Enum("generator", "condenser", "generator_or_condenser")
# Type of transformer cooling.
TransformerCoolingType = Enum("Type", "of", "transformer", "cooling", desc="Type of transformer cooling.")

TransformerType = Enum("fix", "voltageControl", "phaseControl", "voltageAndPhaseControl")
# D | Y | Z for Delta | Wye | ZigZag winding connections
WindingConnection = Enum("D", "Y", "Z", desc="D | Y | Z for Delta | Wye | ZigZag winding connections")
# The winding type, i.e., Primary, Secondary, Tertiary, Quaternary.
WindingType = Enum("primary", "secondary", "tertiary", "quaternary", desc="The winding type, i.e., Primary, Secondary, Tertiary, Quaternary.")

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
    ConductorType = Instance("iec61970.wires.ConductorType")

    # Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    b0ch = Susceptance

    # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    bch = Susceptance

    # Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
    g0ch = Conductance

    # Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
    gch = Conductance

    # Segment length for calculating line section capabilities
    length = LongLength

    # Positive sequence series resistance of the entire line section.
    r = Resistance

    # Zero sequence series resistance of the entire line section.
    r0 = Resistance

    # Positive sequence series reactance of the entire line section.
    x = Reactance

    # Zero sequence series reactance of the entire line section.
    x0 = Reactance

    #--------------------------------------------------------------------------
    #  Begin conductor user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End conductor user definitions:
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
    Conductors = List(Instance("iec61970.wires.Conductor"))

    # A ConductorType is made up of wires that can be configured in several ways.
    WireArrangements = List(Instance("iec61970.wires.WireArrangement"))

    # Resistance of the sheath for cable conductors.
    sheathResistance = Resistance

    # Reactance of the sheath for cable conductors.
    sheathReactance = Reactance

    #--------------------------------------------------------------------------
    #  Begin conductorType user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End conductorType user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Ground" class:
#------------------------------------------------------------------------------

class Ground(ConductingEquipment):
    """ A common point for connecting grounded conducting equipment such as shunt capacitors. The power system model can have more than one ground. The typeName indicates the type of ground, e.g., mesh, earth rod. It is recommended to use GroundDisconnector instead of Ground class when applying CIM. In case of grounding a shunt compensator use Compensator of type SHUNT.
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
#  "HeatExchanger" class:
#------------------------------------------------------------------------------

class HeatExchanger(Equipment):
    """ Equipment for the cooling of electrical equipment and the extraction of heat
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transformer may have a heat exchanger
    PowerTransformer = Instance("iec61970.wires.PowerTransformer", allow_none=False)

    #--------------------------------------------------------------------------
    #  Begin heatExchanger user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End heatExchanger user definitions:
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
    ratedU = Voltage

    # Number of bridges
    bridges = Integer

    # Commutating reactance in ohms at AC bus frequency
    commutatingReactance = Reactance

    # Commutating resistance in ohms
    commutatingResistance = Resistance

    # Compounding resistance in ohms
    compoundResistance = Resistance

    # Minimum compounded DC voltage
    minCompoundVoltage = Voltage

    # Frequency on the AC side.
    frequency = Frequency

    # The maximum active power on the DC side at which the frequence converter should operate.
    maxP = ActivePower

    # The minimum active power on the DC side at which the frequence converter should operate.
    minP = ActivePower

    # The maximum voltage on the DC side at which the frequency converter should operate.
    maxU = Voltage

    # The minimum voltage on the DC side at which the frequency converter should operate.
    minU = Voltage

    # Operating mode for the frequency converter
    operatingMode = OperatingMode

    #--------------------------------------------------------------------------
    #  Begin rectifierInverter user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End rectifierInverter user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegulationSchedule" class:
#------------------------------------------------------------------------------

class RegulationSchedule(RegularIntervalSchedule):
    """ A pre-established pattern over time for a controlled variable, e.g., busbar voltage.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A VoltageControlZone may have a  voltage regulation schedule.
    VoltageControlZones = List(Instance("iec61970.wires.VoltageControlZone"))

    # A regulating class may have a voltage regulation schedule.
    RegulatingCondEqs = List(Instance("iec61970.wires.RegulatingCondEq"))

    # An LTC may have a regulation schedule.
    TapChangers = List(Instance("iec61970.wires.TapChanger"))

    # Flag to indicate that line drop compensation is to be applied
    lineDropCompensation = Boolean

    # Line drop resistance.
    lineDropR = Resistance

    # Line drop reactance.
    lineDropX = Reactance

    #--------------------------------------------------------------------------
    #  Begin regulationSchedule user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End regulationSchedule user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Switch" class:
#------------------------------------------------------------------------------

class Switch(ConductingEquipment):
    """ A generic device  designed to close, or open, or both, one or more electric circuits. The typeName attribute may be used to indicate that the database switch does not represent a corresponding real device but has been introduced for modeling purposes only. 
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A switch may be operated by many schedules.
    SwitchingOperations = List(Instance("iec61970.outage.SwitchingOperation"))

    CompositeSwitch = Instance("iec61970.wires.CompositeSwitch")

    # The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Measurement.normalValue is expected to match with the Switch.normalOpen.
    normalOpen = Boolean

    # The switch on count since the switch was last reset or initialized.
    switchOnCount = Integer

    # The date and time when the switch was last switched on.
    switchOnDate = AbsoluteDateTime

    #--------------------------------------------------------------------------
    #  Begin switch user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End switch user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TapChanger" class:
#------------------------------------------------------------------------------

class TapChanger(PowerSystemResource):
    """ Mechanism for changing transformer winding tap positions. The typeName attribute indicates type of changer, designated as 'Fixed' or 'LTC.'
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transformer winding may have tap changers, separately for voltage and phase angle
    TransformerWinding = Instance("iec61970.wires.TransformerWinding", allow_none=False)

    # An LTC may have a regulation schedule.
    RegulationSchedule = Instance("iec61970.wires.RegulationSchedule")

    Terminal = Instance("iec61970.core.Terminal")

    # Highest possible tap step position, advance from neutral
    highStep = Integer

    # For an LTC, the delay for initial tap changer operation (first step change)
    initialDelay = Seconds

    # Lowest possible tap step position, retard from neutral
    lowStep = Integer

    # Voltage at which the winding operates at the neutral tap setting.
    neutralU = Voltage

    # The neutral tap step position for this winding.
    neutralStep = Integer

    # The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.
    normalStep = Integer

    # Phase shift, in degrees, per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer), or to the 
    stepPhaseShiftIncrement = AngleDegrees

    # Tap step increment, in per cent of nominal voltage, per step position.
    stepVoltageIncrement = PerCent

    # For an LTC, the delay for subsequent tap changer operation (second and later step changes)
    subsequentDelay = Seconds

    # For an LTC, the tap changer control mode, e.g.: Off, Local, Volt, MVAr
    tculControlMode = TransformerControlMode

    #--------------------------------------------------------------------------
    #  Begin tapChanger user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End tapChanger user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PowerTransformer" class:
#------------------------------------------------------------------------------

class PowerTransformer(Equipment):
    """ An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow). The typeName attribute indicates type of transformer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transformer may have a heat exchanger
    HeatExchanger = Instance("iec61970.wires.HeatExchanger")

    # A transformer has windings
    Contains_TransformerWindings = List(Instance("iec61970.wires.TransformerWinding"))

    # Core shunt magnetizing susceptance in the saturation region, in per cent.
    bmagSat = PerCent

    # The reference voltage at which the magnetizing saturation measurements were made
    magBaseU = Voltage

    # Core magnetizing saturation curve knee flux level.
    magSatFlux = PerCent

    # Describes the phases carried by a power transformer. Possible values { ABCN , ABC, ABN, ACN, BCN, AB, AC, BC, AN, BN, CN, A, B, C, N }.
    phases = PhaseCode

    # Type of transformer cooling
    transfCoolingType = TransformerCoolingType

    transformerType = TransformerType

    #--------------------------------------------------------------------------
    #  Begin powerTransformer user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End powerTransformer user definitions:
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

    # A transformer has windings
    MemberOf_PowerTransformer = Instance("iec61970.wires.PowerTransformer", allow_none=False)

    # A transformer winding may have tap changers, separately for voltage and phase angle
    TapChangers = List(Instance("iec61970.wires.TapChanger"))

    # The winding from which the test was conducted
    From_WindingTests = List(Instance("iec61970.wires.WindingTest"))

    # The winding to which the test was conducted
    To_WindingTest = Instance("iec61970.wires.WindingTest")

    # Magnetizing branch susceptance (B mag).
    b = Susceptance

    # Basic insulation level voltage rating
    insulationU = Voltage

    # The type of connection of the winding (e.g. Delta, Wye, zigzag)
    connectionType = WindingConnection

    # The MVA that the winding can carry  under emergency conditions.
    emergencyS = ApparentPower

    # Magnetizing branch conductance (G mag).
    g = Conductance

    # Set if the winding is grounded.
    grounded = Boolean

    # Positive sequence series resistance of the winding.
    r = Resistance

    # Zero sequence series resistance of the winding.
    r0 = Resistance

    # The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.
    ratedU = Voltage

    # The normal apparent power rating for the winding
    ratedS = ApparentPower

    # Ground resistance path through connected grounding transformer.
    rground = Resistance

    # Apparent power that the winding can carry for a short period of time.
    shortTermS = ApparentPower

    # The type of winding, i.e., Primary, Secondary, Tertiary, Quaternary.
    windingType = WindingType

    # Positive sequence series reactance of the winding.
    x = Reactance

    # Zero sequence series reactance of the winding.
    x0 = Reactance

    # Ground reactance path through connected grounding transformer.
    xground = Reactance

    #--------------------------------------------------------------------------
    #  Begin transformerWinding user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End transformerWinding user definitions:
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

    Region = Instance("iec61970.core.SubGeographicalRegion")

    #--------------------------------------------------------------------------
    #  Begin line user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End line user definitions:
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

    # A VoltageControlZone is controlled by a designated BusbarSection.
    BusbarSection = Instance("iec61970.wires.BusbarSection", allow_none=False)

    # A VoltageControlZone may have a  voltage regulation schedule.
    RegulationSchedule = Instance("iec61970.wires.RegulationSchedule")

    #--------------------------------------------------------------------------
    #  Begin voltageControlZone user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End voltageControlZone user definitions:
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

    # The winding from which the test was conducted
    From_TransformerWinding = Instance("iec61970.wires.TransformerWinding", allow_none=False)

    # The winding to which the test was conducted
    To_TransformeWindings = List(Instance("iec61970.wires.TransformerWinding"))

    # The exciting current on open-circuit test, expressed as a percentage of rated current, at nominal voltage
    excitingCurrent = PerCent

    # The tap step number for the 'from' winding of the test pair.
    fromTapStep = Integer

    # The leakage impedance measured at the 'from' winding  with the 'to' winding short-circuited and all other windings open-circuited.  Leakage impedance is expressed in units based on the apparent power and voltage ratings of the 'from' winding.
    leakageImpedance = Impedance

    # The load loss kW ('to' winding short-circuited) from the test report.
    loadLoss = KWActivePower

    # The no load loss kW 'to' winding open-circuited) from the test report.
    noLoadLoss = KWActivePower

    # The phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    phaseShift = AngleDegrees

    # The tap step number for the 'to' winding of the test pair.
    toTapStep = Integer

    # The voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    voltage = Voltage

    #--------------------------------------------------------------------------
    #  Begin windingTest user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End windingTest user definitions:
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

    SynchronousMachines = List(Instance("iec61970.wires.SynchronousMachine"))

    # The machine's coolant temperature in degrees Celsius (e.g., ambient air or stator circulating water)
    coolantTemperature = Temperature

    # The hydrogen coolant pressure
    hydrogenPressure = Pressure

    #--------------------------------------------------------------------------
    #  Begin reactiveCapabilityCurve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End reactiveCapabilityCurve user definitions:
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

    # Negative sequence Thevenin reactance in Ohms.
    xn = Reactance

    # Negative sequence Thevenin resistance in Ohms.
    rn = Resistance

    # Phase-to-phase nominal voltage.
    nominalVoltage = Voltage

    # Positive sequence Thevenin reactance in Ohms.
    x = Reactance

    # Positive sequence Thevenin resistance in Ohms.
    r = Resistance

    # Phase angle of a-phase open circuit.
    voltageAngle = AngleRadians

    # Phase-to-phase open circuit voltage magnitude.
    voltageMagnitude = Voltage

    # Zero sequence Thevenin reactance in Ohms.
    x0 = Reactance

    # Zero sequence Thevenin resistance in Ohms.
    r0 = Resistance

    # High voltage source load
    activePower = ActivePower

    #--------------------------------------------------------------------------
    #  Begin energySource user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End energySource user definitions:
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
    WireArrangements = List(Instance("iec61970.wires.WireArrangement"))

    # Number of conductor strands in the (symmetrical) bundle (1-12)
    phaseConductorCount = Integer

    # Distance between conductor strands in a (symmetrical) bundle (short length units)
    phaseConductorSpacing = ShortLength

    # Current carrying capacity, expressed in amperes, of a wire or cable under stated thermal conditions
    ratedCurrent = CurrentFlow

    # Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.
    gMR = ShortLength

    # The radius of the conductor
    radius = ShortLength

    # The resistance per unit length of the conductor
    resistance = Resistance

    #--------------------------------------------------------------------------
    #  Begin wireType user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End wireType user definitions:
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
    ConductorType = Instance("iec61970.wires.ConductorType")

    # A WireType is mounted at a specified place in a WireArrangement.
    WireType = Instance("iec61970.wires.WireType")

    # Mounting point where wire One is mounted.
    mountingPointX = Integer

    # Mounting point where wire One is mounted.
    mountingPointY = Integer

    #--------------------------------------------------------------------------
    #  Begin wireArrangement user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End wireArrangement user definitions:
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
    PowerCutZone = Instance("iec61970.loadmodel.PowerCutZone")

    # Number of individual customers represented by this Demand
    customerCount = Integer

    # Exponent of per unit frequency effecting real power.
    pFexp = PU

    # Exponent of per unit voltage effecting real power.
    pVexp = PU

    # Exponent of per unit frequency effecting reactive power
    qFexp = PU

    # Exponent of per unit voltage effecting reactive power.
    qVexp = PU

    # Active power of the load that is a fixed quantity.
    pfixed = ActivePower

    # Reactive power of the load that is a fixed quantity.
    qfixed = ReactivePower

    # Fixed reactive power as per cent of load group fixed reactive power.
    qfixedPct = PerCent

    # Fixed active power as per cent of load group fixed active power
    pfixedPct = PerCent

    #--------------------------------------------------------------------------
    #  Begin energyConsumer user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End energyConsumer user definitions:
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
#  "RegulatingCondEq" class:
#------------------------------------------------------------------------------

class RegulatingCondEq(ConductingEquipment):
    """ RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Controls = List(Instance("iec61970.meas.Control"))

    # A regulating class may have a voltage regulation schedule.
    RegulationSchedule = Instance("iec61970.wires.RegulationSchedule")

    # The terminal at the controlled equipment.
    Terminal = Instance("iec61970.core.Terminal")

    #--------------------------------------------------------------------------
    #  Begin regulatingCondEq user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End regulatingCondEq user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CompositeSwitch" class:
#------------------------------------------------------------------------------

class CompositeSwitch(EquipmentContainer):
    """ A model of a set of individual Switches normally enclosed within the same cabinet and possibly with interlocks that restrict the combination of switch positions. These are typically found in medium voltage distribution networks.  A CompositeSwitch could represent a Ring-Main-Unit (RMU), or pad-mounted switchgear, with primitive internal devices such as an internal bus-bar plus 3 or 4 internal switches each of which may individually be open or closed. A CompositeSwitch and a set of contained Switches can also be used to represent a multi-position switch e.g. a switch that can connect a circuit to Ground, Open or Busbar.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Switches = List(Instance("iec61970.wires.Switch"))

    MemberOf_Substation = Instance("iec61970.core.Substation")

    # An alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any
    compositeSwitchType = CompositeSwitchType

    #--------------------------------------------------------------------------
    #  Begin compositeSwitch user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End compositeSwitch user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WiresVersion" class:
#------------------------------------------------------------------------------

class WiresVersion(IdentifiedObject):
    version = String

    date = AbsoluteDateTime

    #--------------------------------------------------------------------------
    #  Begin wiresVersion user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End wiresVersion user definitions:
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
#  "SeriesCompensator" class:
#------------------------------------------------------------------------------

class SeriesCompensator(ConductingEquipment):
    """ A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Positive sequence resistance of the capacitor bank.
    r = Resistance

    # Positive sequence reactance of the capacitor bank.
    x = Reactance

    #--------------------------------------------------------------------------
    #  Begin seriesCompensator user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End seriesCompensator user definitions:
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

    pass
    #--------------------------------------------------------------------------
    #  Begin aCLineSegment user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End aCLineSegment user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BusbarSection" class:
#------------------------------------------------------------------------------

class BusbarSection(Connector):
    """ A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal. The typeName attribute indicates the type of bus bar section, e.g.: Main, Transfer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A VoltageControlZone is controlled by a designated BusbarSection.
    VoltageControlZone = Instance("iec61970.wires.VoltageControlZone")

    #--------------------------------------------------------------------------
    #  Begin busbarSection user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End busbarSection user definitions:
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

    # Time delay in seconds required for the device to be connected or disconnected by automatic voltage regulation (AVR).
    aVRDelay = Seconds

    # The positive sequence impedance of the capacitor.
    impedance = Impedance

    # The maximum voltage at which the capacitor bank should operate.
    maxU = Voltage

    # For a capacitor bank, the maximum number of sections that may be switched in. 
    maximumSections = Integer

    # The minimum voltage at which the capacitor bank should operate.
    minU = Voltage

    # For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.
    reactivePerSection = ReactivePower

    # The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.
    nomU = Voltage

    # Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.
    nomQ = ReactivePower

    # For a capacitor bank, the normal number of sections switched in. This number should correspond to the Nominal MVAr.
    normalSections = Integer

    # The switch on count since the capacitor count was last reset or initialized.
    switchOnCount = Integer

    # The date and time when the capacitor bank was last switched on.
    switchOnDate = AbsoluteDateTime

    # Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power.
    voltageSensitivity = VoltagePerReactivePower

    # For a capacitor bank, the admittance of each switchable section. Calculated using the reactive power per section and corrected for network voltage.
    yPerSection = Admittance

    #--------------------------------------------------------------------------
    #  Begin shuntCompensator user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End shuntCompensator user definitions:
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

    # Inductance of the DC line segment, in millihenries
    dcSegmentInductance = Inductance

    # Resistance of the DC line segment, in ohms
    dcSegmentResistance = Resistance

    #--------------------------------------------------------------------------
    #  Begin dCLineSegment user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End dCLineSegment user definitions:
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
#  "Fuse" class:
#------------------------------------------------------------------------------

class Fuse(Switch):
    """ An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Fault interrupting rating in amperes
    ampRating = CurrentFlow

    #--------------------------------------------------------------------------
    #  Begin fuse user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End fuse user definitions:
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
#  "StaticVarCompensator" class:
#------------------------------------------------------------------------------

class StaticVarCompensator(RegulatingCondEq):
    """ A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.  
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Maximum available capacitive reactive power
    capacitiveRating = Reactance

    # Maximum available inductive reactive power
    inductiveRating = Reactance

    # SVC control mode: MVAr, Voltage
    sVCControlMode = SVCControlMode

    # The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.
    slope = VoltagePerReactivePower

    # The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.
    voltageSetPoint = Voltage

    #--------------------------------------------------------------------------
    #  Begin staticVarCompensator user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End staticVarCompensator user definitions:
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

    ReactiveCapabilityCurves = List(Instance("iec61970.wires.ReactiveCapabilityCurve"))

    # The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
    Drives_HydroPump = Instance("iec61970.generation.production.HydroPump")

    # A synchronous machine may operate as a generator and as such becomes a member of a generating unit
    MemberOf_GeneratingUnit = Instance("iec61970.generation.production.GeneratingUnit")

    DrivenBy_PrimeMover = List(Instance("iec61970.generation.generationdynamics.PrimeMover"))

    # Time delay, in seconds, required when switching from AVR to manual for a lagging MVAr violation.
    aVRToManualLag = Seconds

    # Time delay, in seconds, required when switching from Automatic Voltage Regulation to Manual for a leading MVAr violation.
    aVRToManualLead = Seconds

    # Default base reactive power value. This value represents the initial reactive power that can be used by any application function.
    baseQ = ReactivePower

    # Temperature or pressure of coolant medium
    coolantCondition = Float

    # Method of cooling the machine, e.g., air, hydrogen gas, water
    coolantType = CoolantType

    # Damping torque coefficient, a proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.
    damping = Damping

    # The energy stored in the rotor when operating at rated speed. This value is used in the accelerating power reference frame for  operator training simulator solutions.
    inertia = PU

    # Time delay, in seconds, required when switching from Manual to Automatic Voltage Regulation. This value is used in the accelerating power reference frame for powerflow solutions
    manualToAVR = Seconds

    # Maximum voltage limit for the unit.
    maxU = Voltage

    # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
    maxQ = ReactivePower

    # Minimum voltage  limit for the unit.
    minU = Voltage

    # Minimum reactive power limit for the unit.
    minQ = ReactivePower

    # Positive sequence resistance of the synchronous machine.
    r = Resistance

    # Zero sequence resistance of the synchronous machine.
    r0 = Resistance

    # Nameplate apparent power rating for the unit
    ratedS = ApparentPower

    # Positive sequence reactance of the synchronous machine.
    x = Reactance

    # Zero sequence reactance of the synchronous machine.
    x0 = Reactance

    # Direct-axis subtransient reactance, also known as X'd.
    xDirectSubtrans = Reactance

    # Direct-axis synchronous reactance. The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. (Xd)
    xDirectSync = Reactance

    # Direct-axis transient reactance, also known as X'd.
    xDirectTrans = Reactance

    # Quadrature-axis subtransient reactance, also known as X'q.
    xQuadSubtrans = Reactance

    # Quadrature-axis synchronous reactance (Xq) , the ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.
    xQuadSync = Reactance

    # Quadrature-axis transient reactance, also known as X'q.
    xQuadTrans = Reactance

    # Current mode of operation, i.e., generator or condenser
    operatingMode = SynchronousMachineOperatingMode

    # Modes that this synchronous machine can operate in, i.e., as a generator, condenser, or both
    type = SynchronousMachineType

    # Active power consumed when in condenser mode operation.
    condenserP = ActivePower

    # Priority of unit for reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on.
    referencePriority = Integer

    #--------------------------------------------------------------------------
    #  Begin synchronousMachine user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End synchronousMachine user definitions:
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

    # Frequency on the AC side.
    frequency = Frequency

    # The maximum active power on the DC side at which the frequence converter should operate.
    maxP = ActivePower

    # The maximum voltage on the DC side at which the frequency converter should operate.
    maxU = Voltage

    # The minimum active power on the DC side at which the frequence converter should operate.
    minP = ActivePower

    # The minimum voltage on the DC side at which the frequency converter should operate.
    minU = Voltage

    # Operating mode for the frequency converter
    operatingMode = OperatingMode

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
    OperatedBy_ProtectionEquipments = List(Instance("iec61970.protection.ProtectionEquipment"))

    # A breaker may have zero or more automatic reclosures after a trip occurs.
    RecloseSequences = List(Instance("iec61970.protection.RecloseSequence"))

    #--------------------------------------------------------------------------
    #  Begin protectedSwitch user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End protectedSwitch user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Breaker" class:
#------------------------------------------------------------------------------

class Breaker(ProtectedSwitch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit. The typeName is the type of breaker, e.g., oil, air blast, vacuum, SF6.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Fault interrupting rating in amperes
    ratedCurrent = CurrentFlow

    # The transition time from open to close, in seconds
    inTransitTime = Seconds

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

    # Current carrying capacity, expressed in amperes, of a wire or cable under stated thermal conditions
    ratedCurrent = CurrentFlow

    #--------------------------------------------------------------------------
    #  Begin loadBreakSwitch user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End loadBreakSwitch user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
