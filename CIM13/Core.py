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

from CIM13 import Root
from CIM13.Domain import UnitSymbol
from CIM13.Domain import UnitMultiplier



from enthought.traits.api import Instance, List, Enum, Float, Bool, Str, Int
# <<< imports
from itertools import count
# >>> imports

#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


CompanyType = Enum("isPrivate", "pool", "municipal")

BreakerConfiguration = Enum("noBreaker", "doubleBreaker", "breakerAndAHalf", "singleBreaker")

PhaseCode = Enum("BCN", "ACN", "AB", "A", "B", "ABCN", "AC", "N", "AN", "C", "ABN", "BN", "ABC", "BC", "CN")

CurveStyle = Enum("straightLineYValues", "rampYValue", "constantYValue", "formula")

BusbarConfiguration = Enum("mainWithTransfer", "ringBus", "doubleBus", "singleBus")

#------------------------------------------------------------------------------
#  "IrregularTimePoint" class:
#------------------------------------------------------------------------------

class IrregularTimePoint(Root):
    """ TimePoints for a schedule where the time between the points varies.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An IrregularTimePoint belongs to an IrregularIntervalSchedule.
    IntervalSchedule = Instance("CIM13.Core.IrregularIntervalSchedule")

    # The time is relative the BasicTimeSchedule.startTime.
    time = Float

    # The second value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.
    value2 = Float

    # The first value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.
    value1 = Float

    #--------------------------------------------------------------------------
    #  Begin irregularTimePoint user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End irregularTimePoint user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OperatingShare" class:
#------------------------------------------------------------------------------

class OperatingShare(Root):
    """ Specifies the contract relationship between a PowerSystemResource and a contract participant.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    OperatingParticipant = Instance("CIM13.Core.OperatingParticipant")

    PowerSystemResource = Instance("CIM13.Core.PowerSystemResource")

    # Percentage ownership for this device.   The percentage indicates the percentage ownership of the PSROwner for the PowerSystemResource.  The total percentage ownership for a PowerSystemResource should add to 100%.
    percentage = Float

    #--------------------------------------------------------------------------
    #  Begin operatingShare user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End operatingShare user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CurveData" class:
#------------------------------------------------------------------------------

class CurveData(Root):
    """ Data point values for defining a curve or schedule
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The point data values that define a curve
    CurveSchedule = Instance("CIM13.Core.Curve")

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
#  "RegularTimePoint" class:
#------------------------------------------------------------------------------

class RegularTimePoint(Root):
    """ TimePoints for a schedule where the time between the points is constant.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A RegularTimePoint belongs to a RegularIntervalSchedule.
    IntervalSchedule = Instance("CIM13.Core.RegularIntervalSchedule")

    # The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
    value1 = Float

    # The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
    value2 = Float

    # The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime.
    sequenceNumber = Int

    #--------------------------------------------------------------------------
    #  Begin regularTimePoint user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End regularTimePoint user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "IdentifiedObject" class:
#------------------------------------------------------------------------------

class IdentifiedObject(Root):
    """ This is a root class to provide common naming attributes for all classes needing naming attributes
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.
    ModelingAuthoritySet = Instance("CIM13.Core.ModelingAuthoritySet")

    # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.
    name = Str

    # The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead.
    localName = Str

    # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
    description = Str

    # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.
    aliasName = Str

    # A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique.
    mRID = Str

    # The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.
    pathName = Str

    #--------------------------------------------------------------------------
    #  Begin identifiedObject user definitions:
    #--------------------------------------------------------------------------

    _name_ids = count(0)

    def _name_default(self):
        """ Trait initialiser.
        """
        return self._generate_name()


    def _get_name(self):
        """ Returns the name, which is generated if it has not been already.
        """
        if self._name is None:
            self._name = self._generate_name()
        return self._name


    def _set_name(self, newname):
        """ Change name to newname. Uniqueness is not guaranteed anymore.
        """
        self._name = newname


    def _generate_name(self):
        """ Return a unique name for this object.
        """
        return "%s-%i" % (self.__class__.__name__,  self._name_ids.next())


    def __repr__(self):
        """ The default representation of a named object is its name.
        """
        return "<%s '%s'>" % (self.__class__.__name__, self.name)

    #--------------------------------------------------------------------------
    #  End identifiedObject user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Curve" class:
#------------------------------------------------------------------------------

class Curve(IdentifiedObject):
    """ Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The point data values that define a curve
    CurveScheduleDatas = List(Instance("CIM13.Core.CurveData"))

    # The Y1-axis units of measure.
    y1Unit = UnitSymbol

    # The style or shape of the curve.
    curveStyle = CurveStyle

    # Multiplier for Y2-axis.
    y2Multiplier = UnitMultiplier

    # The Y2-axis units of measure.
    y2Unit = UnitSymbol

    # Multiplier for Y1-axis
    y1Multiplier = UnitMultiplier

    # Multiplier for X-axis.
    xMultiplier = UnitMultiplier

    # The X-axis units of measure.
    xUnit = UnitSymbol

    #--------------------------------------------------------------------------
    #  Begin curve user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End curve user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ReportingGroup" class:
#------------------------------------------------------------------------------

class ReportingGroup(IdentifiedObject):
    """ A reporting group is used for various ad-hoc groupings used for reporting.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    PowerSystemResource = List(Instance("CIM13.Core.PowerSystemResource"))

    ReportingSuperGroup = Instance("CIM13.Core.ReportingSuperGroup")

    BusNameMarker = List(Instance("CIM13.Topology.BusNameMarker"))

    TopologicalNode = List(Instance("CIM13.Topology.TopologicalNode"))

    #--------------------------------------------------------------------------
    #  Begin reportingGroup user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End reportingGroup user definitions:
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

    # An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.
    IdentifiedObjects = List(Instance("CIM13.Core.IdentifiedObject"))

    # A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
    ModelingAuthority = Instance("CIM13.Core.ModelingAuthority")

    #--------------------------------------------------------------------------
    #  Begin modelingAuthoritySet user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End modelingAuthoritySet user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OperatingParticipant" class:
#------------------------------------------------------------------------------

class OperatingParticipant(IdentifiedObject):
    """ An operator of multiple PowerSystemResource objects. Note multple OperatingParticipants may operate the same PowerSystemResource object.   This can be used for modeling jointly owned units where each owner operates as a contractual share.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    OperatingShare = List(Instance("CIM13.Core.OperatingShare"))

    #--------------------------------------------------------------------------
    #  Begin operatingParticipant user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End operatingParticipant user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ReportingSuperGroup" class:
#------------------------------------------------------------------------------

class ReportingSuperGroup(IdentifiedObject):
    """ A reporting super group, groups reporting groups for a higher level report.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ReportingGroup = List(Instance("CIM13.Core.ReportingGroup"))

    #--------------------------------------------------------------------------
    #  Begin reportingSuperGroup user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End reportingSuperGroup user definitions:
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
    Regions = List(Instance("CIM13.Core.SubGeographicalRegion"))

    #--------------------------------------------------------------------------
    #  Begin geographicalRegion user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End geographicalRegion user definitions:
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

    Controls = List(Instance("CIM13.Meas.Control"))

    # The Protection Equipments having the Unit.
    ProtectionEquipments = List(Instance("CIM13.Protection.ProtectionEquipment"))

    Measurements = List(Instance("CIM13.Meas.Measurement"))

    #--------------------------------------------------------------------------
    #  Begin unit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End unit user definitions:
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

    # A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
    ModelingAuthoritySets = List(Instance("CIM13.Core.ModelingAuthoritySet"))

    #--------------------------------------------------------------------------
    #  Begin modelingAuthority user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End modelingAuthority user definitions:
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

    # Use association to ConductingEquipment only when there is no VoltageLevel container used.
    ConductingEquipment = List(Instance("CIM13.Core.ConductingEquipment"))

    VoltageLevel = List(Instance("CIM13.Core.VoltageLevel"))

    # The PowerSystemResource's base voltage.
    nominalVoltage = Float

    # If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current.
    isDC = Bool

    #--------------------------------------------------------------------------
    #  Begin baseVoltage user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End baseVoltage user definitions:
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

    # Value2 units of measure.
    value2Unit = UnitSymbol

    # The time for the first time point.
    startTime = Str

    # Multiplier for value2.
    value2Multiplier = UnitMultiplier

    # Value1 units of measure.
    value1Unit = UnitSymbol

    # Multiplier for value1.
    value1Multiplier = UnitMultiplier

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

    # A RegularTimePoint belongs to a RegularIntervalSchedule.
    TimePoints = List(Instance("CIM13.Core.RegularTimePoint"))

    # The time between each pair of subsequent RegularTimePoints.
    timeStep = Float

    # The time for the last time point.
    endTime = Str

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

    # An IrregularTimePoint belongs to an IrregularIntervalSchedule.
    TimePoints = List(Instance("CIM13.Core.IrregularTimePoint"))

    #--------------------------------------------------------------------------
    #  Begin irregularIntervalSchedule user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End irregularIntervalSchedule user definitions:
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

    # A terminal may participate in zero, one, or two control areas as a tie flow.
    TieFlow = List(Instance("CIM13.ControlArea.TieFlow"))

    OperationalLimitSet = List(Instance("CIM13.OperationalLimits.OperationalLimitSet"))

    BranchGroupTerminal = List(Instance("CIM13.OperationalLimits.BranchGroupTerminal"))

    # ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
    ConductingEquipment = Instance("CIM13.Core.ConductingEquipment")

    RegulatingControl = List(Instance("CIM13.Wires.RegulatingControl"))

    # One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.
    Measurements = List(Instance("CIM13.Meas.Measurement"))

    TopologicalNode = Instance("CIM13.Topology.TopologicalNode")

    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
    ConnectivityNode = Instance("CIM13.Topology.ConnectivityNode")

    #--------------------------------------------------------------------------
    #  Begin terminal user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End terminal user definitions:
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
    Region = Instance("CIM13.Core.GeographicalRegion")

    # A Line can be contained by a SubGeographical Region.
    Lines = List(Instance("CIM13.Wires.Line"))

    # The association is used in the naming hierarchy.
    Substations = List(Instance("CIM13.Core.Substation"))

    #--------------------------------------------------------------------------
    #  Begin subGeographicalRegion user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End subGeographicalRegion user definitions:
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

    PSRType = Instance("CIM13.Core.PSRType")

    # A power system resource may be part of one or more companies
    OperatedBy_Companies = List(Instance("CIM13.Core.Company"))

    ReportingGroup = List(Instance("CIM13.Core.ReportingGroup"))

    OperatingShare = List(Instance("CIM13.Core.OperatingShare"))

    PsrLists = List(Instance("CIM13.Core.PsrList"))

    # A power system resource may have an outage schedule
    OutageSchedule = Instance("CIM13.Outage.OutageSchedule")

    # Measurement-PSR defines the measurements in the naming hierarchy.
    Contains_Measurements = List(Instance("CIM13.Meas.Measurement"))

    #--------------------------------------------------------------------------
    #  Begin powerSystemResource user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End powerSystemResource user definitions:
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
    basePower = Float

    #--------------------------------------------------------------------------
    #  Begin basePower user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End basePower user definitions:
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

    PowerSystemResource = List(Instance("CIM13.Core.PowerSystemResource"))

    #--------------------------------------------------------------------------
    #  Begin pSRType user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End pSRType user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PsrList" class:
#------------------------------------------------------------------------------

class PsrList(IdentifiedObject):
    """ Arbitrary list of PowerSystemResources. Can be used for various purposes, including grouping for report generation.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    PowerSystemResources = List(Instance("CIM13.Core.PowerSystemResource"))

    # Type of power system resources in this list.
    typePSRList = Str

    #--------------------------------------------------------------------------
    #  Begin psrList user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End psrList user definitions:
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
    Operates_PSRs = List(Instance("CIM13.Core.PowerSystemResource"))

    # The type of company.
    companyType = CompanyType

    #--------------------------------------------------------------------------
    #  Begin company user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End company user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConnectivityNodeContainer" class:
#------------------------------------------------------------------------------

class ConnectivityNodeContainer(PowerSystemResource):
    """ A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    TopologicalNode = List(Instance("CIM13.Topology.TopologicalNode"))

    ConnectivityNodes = List(Instance("CIM13.Topology.ConnectivityNode"))

    #--------------------------------------------------------------------------
    #  Begin connectivityNodeContainer user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End connectivityNodeContainer user definitions:
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
    Contains_Equipments = List(Instance("CIM13.Core.Equipment"))

    #--------------------------------------------------------------------------
    #  Begin equipmentContainer user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End equipmentContainer user definitions:
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

    OperationalLimitSet = List(Instance("CIM13.OperationalLimits.OperationalLimitSet"))

    ContingencyEquipment = List(Instance("CIM13.Contingency.ContingencyEquipment"))

    # The association is used in the naming hierarchy.
    MemberOf_EquipmentContainer = Instance("CIM13.Core.EquipmentContainer")

    # The equipment is normally in service.
    normalIlyInService = Bool

    #--------------------------------------------------------------------------
    #  Begin equipment user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End equipment user definitions:
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
    MemberOf_Substation = Instance("CIM13.Core.Substation")

    # The association is used in the naming hierarchy.
    MemberOf_VoltageLevel = Instance("CIM13.Core.VoltageLevel")

    # Bus bar configuration.
    busBarConfiguration = BusbarConfiguration

    # Indicates the presence/absence of active/reactive power measurements.
    bayPowerMeasFlag = Bool

    # Breaker configuration.
    breakerConfiguration = BreakerConfiguration

    # Indicates the presence/absence of energy measurements.
    bayEnergyMeasFlag = Bool

    #--------------------------------------------------------------------------
    #  Begin bay user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End bay user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "VoltageLevel" class:
#------------------------------------------------------------------------------

class VoltageLevel(EquipmentContainer):
    """ A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.
    Contains_Bays = List(Instance("CIM13.Core.Bay"))

    BaseVoltage = Instance("CIM13.Core.BaseVoltage")

    # The association is used in the naming hierarchy.
    MemberOf_Substation = Instance("CIM13.Core.Substation")

    # The bus bar's low voltage limit
    lowVoltageLimit = Float

    # The bus bar's high voltage limit
    highVoltageLimit = Float

    #--------------------------------------------------------------------------
    #  Begin voltageLevel user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End voltageLevel user definitions:
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
    Contains_VoltageLevels = List(Instance("CIM13.Core.VoltageLevel"))

    # The association is used in the naming hierarchy.
    Contains_Bays = List(Instance("CIM13.Core.Bay"))

    # The association is used in the naming hierarchy.
    Region = Instance("CIM13.Core.SubGeographicalRegion")

    #--------------------------------------------------------------------------
    #  Begin substation user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End substation user definitions:
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
    Terminals = List(Instance("CIM13.Core.Terminal"))

    # Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
    ProtectionEquipments = List(Instance("CIM13.Protection.ProtectionEquipment"))

    # Use association to ConductingEquipment only when there is no VoltageLevel container used.
    BaseVoltage = Instance("CIM13.Core.BaseVoltage")

    # Conducting equipment may have multiple clearance tags for authorized field work
    ClearanceTags = List(Instance("CIM13.Outage.ClearanceTag"))

    # Describes the phases carried by a conducting equipment.
    phases = PhaseCode

    #--------------------------------------------------------------------------
    #  Begin conductingEquipment user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End conductingEquipment user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
