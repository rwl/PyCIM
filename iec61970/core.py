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

""" Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from iec61970.domain import Boolean
from iec61970.domain import UnitSymbol
from iec61970.domain import UnitMultiplier
from iec61970.domain import Float
from iec61970.domain import Voltage
from iec61970.domain import ApparentPower
from iec61970.domain import String
from iec61970.domain import AbsoluteDateTime
from iec61970.domain import Seconds
from iec61970.domain import Integer



from enthought.traits.api import HasTraits, Instance, List, Enum, Bool, Float, Int
# <<< imports

# >>> imports

#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Enumeration of phase identifiers.
PhaseCode = Enum("ABCN", "ABC", "ABN", "ACN", "BCN", "AB", "AC", "BC", "AN", "BN", "CN", "A", "B", "C", "N", desc="Enumeration of phase identifiers.")
# Switching arrangement for Bay. 
BreakerConfiguration = Enum("singleBreaker", "breakerAndAHalf", "doubleBreaker", "noBreaker", desc="Switching arrangement for Bay. ")
# Busbar layout for Bay.
BusbarConfiguration = Enum("singleBus", "doubleBus", "mainWithTransfer", "ringBus", desc="Busbar layout for Bay.")
# Type of company.
CompanyType = Enum("pool", "municipal", "isPrivate", desc="Type of company.")
# Style or shape of curve.
CurveStyle = Enum("constantYValue", "straightLineYValues", "rampYValue", "formula", desc="Style or shape of curve.")

#------------------------------------------------------------------------------
#  "CurveData" class:
#------------------------------------------------------------------------------

class CurveData(HasTraits):
    """ Data point values for defining a curve or schedule 
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The point data values that define a curve
    CurveSchedule = Instance("iec61970.core.Curve", allow_none=False)

    # The data value of the X-axis variable,  depending on the X-axis units
    xvalue = Float

    # The data value of the  first Y-axis variable, depending on the Y-axis units
    y1value = Float

    # The data value of the second Y-axis variable (if present), depending on the Y-axis units
    y2value = Float

    #--------------------------------------------------------------------------
    #  Begin curveData user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End curveData user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "IdentifiedObject" class:
#------------------------------------------------------------------------------

class IdentifiedObject(HasTraits):
    """ This is a root class to provide common naming attributes for all classes needing naming attributes
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique.
    mRID = String

    # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.
    name = String

    # The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead.
    localName = String

    # The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.
    pathName = String

    # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.
    aliasName = String

    # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
    description = String

    #--------------------------------------------------------------------------
    #  Begin identifiedObject user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End identifiedObject user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegularTimePoint" class:
#------------------------------------------------------------------------------

class RegularTimePoint(HasTraits):
    """ TimePoints for a schedule where the time between the points is constant.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The point data values that define a curve
    IntervalSchedule = Instance("iec61970.core.RegularIntervalSchedule", allow_none=False)

    sequenceNumber = Integer

    value1 = Float

    value2 = Float

    #--------------------------------------------------------------------------
    #  Begin regularTimePoint user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End regularTimePoint user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "IrregularTimePoint" class:
#------------------------------------------------------------------------------

class IrregularTimePoint(HasTraits):
    """ TimePoints for a schedule where the time between the points varies.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The point data values that define a curve
    IntervalSchedule = Instance("iec61970.core.IrregularIntervalSchedule", allow_none=False)

    # The time is relative the BasicTimeSchedule.startTime.
    time = Seconds

    value1 = Float

    value2 = Float

    #--------------------------------------------------------------------------
    #  Begin irregularTimePoint user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End irregularTimePoint user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CoreVersion" class:
#------------------------------------------------------------------------------

class CoreVersion(HasTraits):
    version = String

    date = AbsoluteDateTime

    #--------------------------------------------------------------------------
    #  Begin coreVersion user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End coreVersion user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Company" class:
#------------------------------------------------------------------------------

class Company(IdentifiedObject):
    """ A company is a legal entity that owns and operates power system resources and is a party to interchange and transmission contracts.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A power system resource may be part of one or more companies
    Operates_PSRs = List(Instance("iec61970.core.PowerSystemResource"))

    # The type of company, e.g.: pool, municipal, private
    companyType = CompanyType

    #--------------------------------------------------------------------------
    #  Begin company user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End company user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PowerSystemResource" class:
#------------------------------------------------------------------------------

class PowerSystemResource(IdentifiedObject):
    """ A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A power system resource may be part of one or more companies
    OperatedBy_Companies = List(Instance("iec61970.core.Company"))

    PSRType = Instance("iec61970.core.PSRType")

    # The Measurements that are included in the naming hierarchy where the PSR is the containing object
    Contains_Measurements = List(Instance("iec61970.meas.Measurement"))

    # A power system resource may have an outage schedule
    OutageSchedule = Instance("iec61970.outage.OutageSchedule")

    #--------------------------------------------------------------------------
    #  Begin powerSystemResource user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End powerSystemResource user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Terminal" class:
#------------------------------------------------------------------------------

class Terminal(IdentifiedObject):
    """ An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.  
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
    ConductingEquipment = Instance("iec61970.core.ConductingEquipment", allow_none=False)

    # One or more measurements may be associated with a terminal in the network
    Measurements = List(Instance("iec61970.meas.Measurement"))

    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
    ConnectivityNode = Instance("iec61970.topology.ConnectivityNode")

    # The regulating equipment that are controlling the equipment at the Terminal.
    RegulatingCondEqs = List(Instance("iec61970.wires.RegulatingCondEq"))

    # The TapChangers that are controlling the equipment at the Terminal.
    TapChangers = List(Instance("iec61970.wires.TapChanger"))

    #--------------------------------------------------------------------------
    #  Begin terminal user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End terminal user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SubControlArea" class:
#------------------------------------------------------------------------------

class SubControlArea(PowerSystemResource):
    """ An area defined for the purpose of tracking interchange with surrounding areas via tie points; may or may not serve as a control area.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A GeneratingUnit injects energy into a SubControlArea.
    GeneratingUnits = List(Instance("iec61970.generation.production.GeneratingUnit"))

    #--------------------------------------------------------------------------
    #  Begin subControlArea user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End subControlArea user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Curve" class:
#------------------------------------------------------------------------------

class Curve(IdentifiedObject, CoreVersion):
    """ Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules. 
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The point data values that define a curve
    CurveScheduleDatas = List(Instance("iec61970.core.CurveData"))

    # The style or shape of the curve.
    curveStyle = CurveStyle

    xUnit = UnitSymbol

    xMultiplier = UnitMultiplier

    # The Y1-axis units of measure.
    y1Unit = UnitSymbol

    y1Multiplier = UnitMultiplier

    # The Y2-axis units of measure.
    y2Unit = UnitSymbol

    y2Multiplier = UnitMultiplier

    #--------------------------------------------------------------------------
    #  Begin curve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End curve user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BaseVoltage" class:
#------------------------------------------------------------------------------

class BaseVoltage(IdentifiedObject):
    """ Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ConductingEquipment = List(Instance("iec61970.core.ConductingEquipment"))

    VoltageLevel = List(Instance("iec61970.core.VoltageLevel"))

    # The PowerSystemResource's base voltage.
    nominalVoltage = Voltage

    #--------------------------------------------------------------------------
    #  Begin baseVoltage user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End baseVoltage user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BasePower" class:
#------------------------------------------------------------------------------

class BasePower(IdentifiedObject):
    """ The BasePower class defines the base power used in the per unit calculations.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Definition of base power.
    basePower = ApparentPower

    #--------------------------------------------------------------------------
    #  Begin basePower user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End basePower user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Equipment" class:
#------------------------------------------------------------------------------

class Equipment(PowerSystemResource):
    """ The parts of a power system that are physical devices, electronic or mechanical
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.
    MemberOf_EquipmentContainer = Instance("iec61970.core.EquipmentContainer")

    #--------------------------------------------------------------------------
    #  Begin equipment user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End equipment user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Unit" class:
#------------------------------------------------------------------------------

class Unit(IdentifiedObject):
    """ Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The Measurements having the Unit
    Measurements = List(Instance("iec61970.meas.Measurement"))

    Controls = List(Instance("iec61970.meas.Control"))

    ProtectionEquipments = List(Instance("iec61970.protection.ProtectionEquipment"))

    #--------------------------------------------------------------------------
    #  Begin unit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End unit user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PSRType" class:
#------------------------------------------------------------------------------

class PSRType(IdentifiedObject):
    """ Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    PowerSystemResource = List(Instance("iec61970.core.PowerSystemResource"))

    #--------------------------------------------------------------------------
    #  Begin pSRType user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End pSRType user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SubGeographicalRegion" class:
#------------------------------------------------------------------------------

class SubGeographicalRegion(IdentifiedObject):
    """ A subset of a geographical region of a power system network model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.
    Substations = List(Instance("iec61970.core.Substation"))

    # The association is used in the naming hierarchy.
    Region = Instance("iec61970.core.GeographicalRegion")

    Lines = List(Instance("iec61970.wires.Line"))

    #--------------------------------------------------------------------------
    #  Begin subGeographicalRegion user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End subGeographicalRegion user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GeographicalRegion" class:
#------------------------------------------------------------------------------

class GeographicalRegion(IdentifiedObject):
    """ A geographical region of a power system network model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.
    Regions = List(Instance("iec61970.core.SubGeographicalRegion"))

    #--------------------------------------------------------------------------
    #  Begin geographicalRegion user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End geographicalRegion user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BasicIntervalSchedule" class:
#------------------------------------------------------------------------------

class BasicIntervalSchedule(IdentifiedObject):
    """ Schedule of values at points in time.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    startTime = AbsoluteDateTime

    value1Unit = UnitSymbol

    value1Multiplier = UnitMultiplier

    value2Unit = UnitSymbol

    value2Multiplier = UnitMultiplier

    #--------------------------------------------------------------------------
    #  Begin basicIntervalSchedule user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End basicIntervalSchedule user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegularIntervalSchedule" class:
#------------------------------------------------------------------------------

class RegularIntervalSchedule(BasicIntervalSchedule):
    """ The schedule has TimePoints where the time between them is constant.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The point data values that define a curve
    TimePoints = List(Instance("iec61970.core.RegularTimePoint"))

    timeStep = Seconds

    endTime = AbsoluteDateTime

    #--------------------------------------------------------------------------
    #  Begin regularIntervalSchedule user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End regularIntervalSchedule user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "IrregularIntervalSchedule" class:
#------------------------------------------------------------------------------

class IrregularIntervalSchedule(BasicIntervalSchedule):
    """ The schedule has TimePoints where the time between them varies.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The point data values that define a curve
    TimePoints = List(Instance("iec61970.core.IrregularTimePoint"))

    #--------------------------------------------------------------------------
    #  Begin irregularIntervalSchedule user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End irregularIntervalSchedule user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ModelingAuthoritySet" class:
#------------------------------------------------------------------------------

class ModelingAuthoritySet(IdentifiedObject):
    """ A Modeling Authority Set is a group of objects in a network model where the data is supplied and maintained by the same Modeling Authority.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin modelingAuthoritySet user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End modelingAuthoritySet user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ModelingAuthority" class:
#------------------------------------------------------------------------------

class ModelingAuthority(IdentifiedObject):
    """ A Modeling Authority is an entity responsible for supplying and maintaining the data defining a specific set of objects in a network model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin modelingAuthority user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End modelingAuthority user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConnectivityNodeContainer" class:
#------------------------------------------------------------------------------

class ConnectivityNodeContainer(PowerSystemResource):
    """ A base class for all objects that may contain ConnectivityNodes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ConnectivityNodes = List(Instance("iec61970.topology.ConnectivityNode"))

    #--------------------------------------------------------------------------
    #  Begin connectivityNodeContainer user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End connectivityNodeContainer user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConductingEquipment" class:
#------------------------------------------------------------------------------

class ConductingEquipment(Equipment):
    """ The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
    Terminals = List(Instance("iec61970.core.Terminal"))

    BaseVoltage = Instance("iec61970.core.BaseVoltage")

    # Conducting equipment may have multiple clearance tags for authorized field work
    ClearanceTags = List(Instance("iec61970.outage.ClearanceTag"))

    # Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
    ProtectionEquipments = List(Instance("iec61970.protection.ProtectionEquipment"))

    # Describes the phases carried by a conducting equipment. Possible values { ABCN , ABC, ABN, ACN, BCN, AB, AC, BC, AN, BN, CN, A, B, C, N }.
    phases = PhaseCode

    #--------------------------------------------------------------------------
    #  Begin conductingEquipment user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End conductingEquipment user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquipmentContainer" class:
#------------------------------------------------------------------------------

class EquipmentContainer(ConnectivityNodeContainer):
    """ A modeling construct to provide a root class for all Equipment classes
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.
    Contains_Equipments = List(Instance("iec61970.core.Equipment"))

    #--------------------------------------------------------------------------
    #  Begin equipmentContainer user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End equipmentContainer user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Bay" class:
#------------------------------------------------------------------------------

class Bay(EquipmentContainer):
    """ A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry. 
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.
    MemberOf_VoltageLevel = Instance("iec61970.core.VoltageLevel")

    # The association is used in the naming hierarchy.
    MemberOf_Substation = Instance("iec61970.core.Substation")

    # Indicates the presence/absence of energy measurements.
    bayEnergyMeasFlag = Boolean

    # Indicates the presence/absence of active/reactive power measurements.
    bayPowerMeasFlag = Boolean

    # Breaker configuration. 
    breakerConfiguration = BreakerConfiguration

    # Bus bar configuration.
    busBarConfiguration = BusbarConfiguration

    #--------------------------------------------------------------------------
    #  Begin bay user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End bay user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Substation" class:
#------------------------------------------------------------------------------

class Substation(EquipmentContainer):
    """ A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics. 
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.
    Region = Instance("iec61970.core.SubGeographicalRegion")

    # The association is used in the naming hierarchy.
    Contains_VoltageLevels = List(Instance("iec61970.core.VoltageLevel"))

    # The association is used in the naming hierarchy.
    Contains_Bays = List(Instance("iec61970.core.Bay"))

    Contains_CompositeSwitches = List(Instance("iec61970.wires.CompositeSwitch"))

    #--------------------------------------------------------------------------
    #  Begin substation user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End substation user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "VoltageLevel" class:
#------------------------------------------------------------------------------

class VoltageLevel(EquipmentContainer):
    """ A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulationand protection devices as well as assemblies of all these.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.
    MemberOf_Substation = Instance("iec61970.core.Substation", allow_none=False)

    # The association is used in the naming hierarchy.
    Contains_Bays = List(Instance("iec61970.core.Bay"))

    BaseVoltage = Instance("iec61970.core.BaseVoltage", allow_none=False)

    # The bus bar's high voltage limit
    highVoltageLimit = Voltage

    # The bus bar's low voltage limit
    lowVoltageLimit = Voltage

    #--------------------------------------------------------------------------
    #  Begin voltageLevel user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End voltageLevel user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
