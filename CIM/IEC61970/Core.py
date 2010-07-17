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

""" Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.  This package does not depend on any other package except the Domain package, but most of the other packages have associations and generalizations that depend on it.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM import Element
from CIM.IEC61970.Domain import UnitMultiplier
from CIM.IEC61970.Domain import UnitSymbol
from CIM.IEC61970.Domain import Seconds
from CIM.IEC61970.Domain import Voltage
from CIM.IEC61970.Domain import PerCent
from CIM.IEC61970.Domain import ApparentPower



from enthought.traits.api import Instance, List, Property, Enum, Str, Bool, Date, Float, Int
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Switching arrangement for Bay.
BreakerConfiguration = Enum("noBreaker", "doubleBreaker", "singleBreaker", "breakerAndAHalf", desc="Switching arrangement for Bay.")
# Style or shape of curve.
CurveStyle = Enum("constantYValue", "rampYValue", "formula", "straightLineYValues", desc="Style or shape of curve.")
# Type of company.
CompanyType = Enum("pool", "municipal", "isPrivate", desc="Type of company.")
# Enumeration of phase identifiers.
PhaseCode = Enum("ABC", "AB", "B", "BC", "AC", "splitSecondary1N", "ABN", "ABCN", "CN", "AN", "splitSecondary12N", "BCN", "splitSecondary2N", "ACN", "A", "C", "N", "BN", desc="Enumeration of phase identifiers.")
# Busbar layout for Bay.
BusbarConfiguration = Enum("ringBus", "doubleBus", "mainWithTransfer", "singleBus", desc="Busbar layout for Bay.")

#------------------------------------------------------------------------------
#  "IdentifiedObject" class:
#------------------------------------------------------------------------------

class IdentifiedObject(Element):
    """ This is a root class to provide common naming attributes for all classes needing naming attributes
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.
    ModelingAuthoritySet = Instance("CIM.IEC61970.Core.ModelingAuthoritySet",
        desc="An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.",
        transient=True,
        opposite="IdentifiedObjects",
        editor=InstanceEditor(name="_modelingauthoritysets"))

    def _get_modelingauthoritysets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.ModelingAuthoritySet" ]
        else:
            return []

    _modelingauthoritysets = Property(fget=_get_modelingauthoritysets)

    # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
    description = Str(desc="The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.")

    # A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique.
    mRID = Str(desc="A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique.")

    # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.
    name = Str(desc="The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.")

    # The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.
    pathName = Str(desc="The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.")

    # The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead.
    localName = Str(desc="The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead.")

    # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.
    aliasName = Str(desc="The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "IdentifiedObject" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.IdentifiedObject",
        title="IdentifiedObject",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IdentifiedObject" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "IrregularTimePoint" class:
#------------------------------------------------------------------------------

class IrregularTimePoint(Element):
    """ TimePoints for a schedule where the time between the points varies.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An IrregularTimePoint belongs to an IrregularIntervalSchedule.
    IntervalSchedule = Instance("CIM.IEC61970.Core.IrregularIntervalSchedule",
        desc="An IrregularTimePoint belongs to an IrregularIntervalSchedule.",
        transient=True,
        opposite="TimePoints",
        editor=InstanceEditor(name="_irregularintervalschedules"))

    def _get_irregularintervalschedules(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.IrregularIntervalSchedule" ]
        else:
            return []

    _irregularintervalschedules = Property(fget=_get_irregularintervalschedules)

    # The time is relative the BasicTimeSchedule.startTime.
    time = Seconds(desc="The time is relative the BasicTimeSchedule.startTime.")

    # The first value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.
    value1 = Float(desc="The first value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.")

    # The second value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.
    value2 = Float(desc="The second value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.")

    #--------------------------------------------------------------------------
    #  Begin "IrregularTimePoint" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "time", "value1", "value2",
                label="Attributes"),
            VGroup("Parent", "IntervalSchedule",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.IrregularTimePoint",
        title="IrregularTimePoint",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IrregularTimePoint" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegularTimePoint" class:
#------------------------------------------------------------------------------

class RegularTimePoint(Element):
    """ TimePoints for a schedule where the time between the points is constant.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A RegularTimePoint belongs to a RegularIntervalSchedule.
    IntervalSchedule = Instance("CIM.IEC61970.Core.RegularIntervalSchedule",
        desc="A RegularTimePoint belongs to a RegularIntervalSchedule.",
        transient=True,
        opposite="TimePoints",
        editor=InstanceEditor(name="_regularintervalschedules"))

    def _get_regularintervalschedules(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.RegularIntervalSchedule" ]
        else:
            return []

    _regularintervalschedules = Property(fget=_get_regularintervalschedules)

    # The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
    value2 = Float(desc="The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.")

    # The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime.
    sequenceNumber = Int(desc="The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime.")

    # The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
    value1 = Float(desc="The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.")

    #--------------------------------------------------------------------------
    #  Begin "RegularTimePoint" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "value2", "sequenceNumber", "value1",
                label="Attributes"),
            VGroup("Parent", "IntervalSchedule",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.RegularTimePoint",
        title="RegularTimePoint",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegularTimePoint" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CurveData" class:
#------------------------------------------------------------------------------

class CurveData(Element):
    """ Data point values for defining a curve or schedule
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The Curve defined by this CurveData.
    Curve = Instance("CIM.IEC61970.Core.Curve",
        desc="The Curve defined by this CurveData.",
        transient=True,
        opposite="CurveDatas",
        editor=InstanceEditor(name="_curves"))

    def _get_curves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.Curve" ]
        else:
            return []

    _curves = Property(fget=_get_curves)

    # The data value of the  first Y-axis variable, depending on the Y-axis units
    y1value = Float(desc="The data value of the  first Y-axis variable, depending on the Y-axis units")

    # The data value of the second Y-axis variable (if present), depending on the Y-axis units
    y2value = Float(desc="The data value of the second Y-axis variable (if present), depending on the Y-axis units")

    # The data value of the third Y-axis variable (if present), depending on the Y-axis units
    y3value = Float(desc="The data value of the third Y-axis variable (if present), depending on the Y-axis units")

    # The data value of the X-axis variable,  depending on the X-axis units
    xvalue = Float(desc="The data value of the X-axis variable,  depending on the X-axis units")

    #--------------------------------------------------------------------------
    #  Begin "CurveData" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "y1value", "y2value", "y3value", "xvalue",
                label="Attributes"),
            VGroup("Parent", "Curve",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.CurveData",
        title="CurveData",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CurveData" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OperatingShare" class:
#------------------------------------------------------------------------------

class OperatingShare(Element):
    """ Specifies the contract relationship between a PowerSystemResource and a contract participant.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The linkage to a owners  and its linkage attributes like percentage ownership.   The ownership percentage should add to 100% for all owners of a PowerSystemResource, but a PSROwner may own any percentage of any number of PowerSystemResource objects.
    OperatingParticipant = Instance("CIM.IEC61970.Core.OperatingParticipant",
        desc="The linkage to a owners  and its linkage attributes like percentage ownership.   The ownership percentage should add to 100% for all owners of a PowerSystemResource, but a PSROwner may own any percentage of any number of PowerSystemResource objects.",
        transient=True,
        opposite="OperatingShare",
        editor=InstanceEditor(name="_operatingparticipants"))

    def _get_operatingparticipants(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.OperatingParticipant" ]
        else:
            return []

    _operatingparticipants = Property(fget=_get_operatingparticipants)

    # The PowerSystemResource to which the attribues apply.   The percentage ownership of all owners of a PowerSystemResource should add to 100%.
    PowerSystemResource = Instance("CIM.IEC61970.Core.PowerSystemResource",
        desc="The PowerSystemResource to which the attribues apply.   The percentage ownership of all owners of a PowerSystemResource should add to 100%.",
        transient=True,
        opposite="OperatingShare",
        editor=InstanceEditor(name="_powersystemresources"))

    def _get_powersystemresources(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.PowerSystemResource" ]
        else:
            return []

    _powersystemresources = Property(fget=_get_powersystemresources)

    # Percentage ownership for this device.   The percentage indicates the percentage ownership of the PSROwner for the PowerSystemResource.  The total percentage ownership for a PowerSystemResource should add to 100%.
    percentage = PerCent(desc="Percentage ownership for this device.   The percentage indicates the percentage ownership of the PSROwner for the PowerSystemResource.  The total percentage ownership for a PowerSystemResource should add to 100%.")

    #--------------------------------------------------------------------------
    #  Begin "OperatingShare" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "percentage",
                label="Attributes"),
            VGroup("Parent", "OperatingParticipant", "PowerSystemResource",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.OperatingShare",
        title="OperatingShare",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OperatingShare" user definitions:
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
    Regions = List(Instance("CIM.IEC61970.Core.SubGeographicalRegion"),
        desc="The association is used in the naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "GeographicalRegion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Regions",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.GeographicalRegion",
        title="GeographicalRegion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GeographicalRegion" user definitions:
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

    ChangeItems = List(Instance("CIM.IEC61968.Informative.InfOperations.ChangeItem"))

    AssetRoles = List(Instance("CIM.IEC61968.Informative.InfAssets.AssetPsrRole"))

    # Geographical location of this power system resource.
    GeoLocation = Instance("CIM.IEC61968.Common.GeoLocation",
        desc="Geographical location of this power system resource.",
        transient=True,
        opposite="PowerSystemResources",
        editor=InstanceEditor(name="_geolocations"))

    def _get_geolocations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.GeoLocation" ]
        else:
            return []

    _geolocations = Property(fget=_get_geolocations)

    SafetyDocuments = List(Instance("CIM.IEC61968.Informative.InfOperations.SafetyDocument"))

    # A power system resource may have an outage schedule
    OutageSchedule = Instance("CIM.IEC61970.Outage.OutageSchedule",
        desc="A power system resource may have an outage schedule",
        transient=True,
        opposite="PowerSystemResource",
        editor=InstanceEditor(name="_outageschedules"))

    def _get_outageschedules(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Outage.OutageSchedule" ]
        else:
            return []

    _outageschedules = Property(fget=_get_outageschedules)

    # The Measurements that are included in the naming hierarchy where the PSR is the containing object
    Measurements = List(Instance("CIM.IEC61970.Meas.Measurement"),
        desc="The Measurements that are included in the naming hierarchy where the PSR is the containing object")

    ErpOrganisationRoles = List(Instance("CIM.IEC61968.Informative.InfOperations.OrgPsrRole"))

    # PSRType (custom classification) for this PowerSystemResource.
    PSRType = Instance("CIM.IEC61970.Core.PSRType",
        desc="PSRType (custom classification) for this PowerSystemResource.",
        transient=True,
        opposite="PowerSystemResources",
        editor=InstanceEditor(name="_psrtypes"))

    def _get_psrtypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.PSRType" ]
        else:
            return []

    _psrtypes = Property(fget=_get_psrtypes)

    PsrLists = List(Instance("CIM.IEC61970.Core.PsrList"))

    # All events associated with this power system resource.
    PSREvent = List(Instance("CIM.IEC61968.Informative.InfOperations.PSREvent"),
        desc="All events associated with this power system resource.")

    # The linkage to any number of operating share objects.
    OperatingShare = List(Instance("CIM.IEC61970.Core.OperatingShare"),
        desc="The linkage to any number of operating share objects.")

    ScheduleSteps = List(Instance("CIM.IEC61968.Informative.InfOperations.SwitchingStep"))

    DocumentRoles = List(Instance("CIM.IEC61968.Informative.InfCommon.DocPsrRole"))

    # Reporting groups to which this PSR belongs.
    ReportingGroup = List(Instance("CIM.IEC61970.Core.ReportingGroup"),
        desc="Reporting groups to which this PSR belongs.")

    CircuitSections = List(Instance("CIM.IEC61968.Informative.InfOperations.CircuitSection"))

    NetworkDataSets = List(Instance("CIM.IEC61968.Informative.InfOperations.NetworkDataSet"))

    #--------------------------------------------------------------------------
    #  Begin "PowerSystemResource" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Core.PowerSystemResource",
        title="PowerSystemResource",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PowerSystemResource" user definitions:
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

    # The contingency element associated with the equipment.
    ContingencyEquipment = List(Instance("CIM.IEC61970.Contingency.ContingencyEquipment"),
        desc="The contingency element associated with the equipment.")

    CustomerAgreements = List(Instance("CIM.IEC61968.Customers.CustomerAgreement"))

    # The equipment limit sets associated with the equipment.
    OperationalLimitSet = List(Instance("CIM.IEC61970.OperationalLimits.OperationalLimitSet"),
        desc="The equipment limit sets associated with the equipment.")

    # The association is used in the naming hierarchy.
    EquipmentContainer = Instance("CIM.IEC61970.Core.EquipmentContainer",
        desc="The association is used in the naming hierarchy.",
        transient=True,
        opposite="Equipments",
        editor=InstanceEditor(name="_equipmentcontainers"))

    def _get_equipmentcontainers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.EquipmentContainer" ]
        else:
            return []

    _equipmentcontainers = Property(fget=_get_equipmentcontainers)

    # The equipment is normally in service.
    normaIlyInService = Bool(desc="The equipment is normally in service.")

    #--------------------------------------------------------------------------
    #  Begin "Equipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Core.Equipment",
        title="Equipment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Equipment" user definitions:
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
    Terminals = List(Instance("CIM.IEC61970.Core.Terminal"),
        desc="ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes")

    # Conducting equipment may have multiple clearance tags for authorized field work
    ClearanceTags = List(Instance("CIM.IEC61970.Outage.ClearanceTag"),
        desc="Conducting equipment may have multiple clearance tags for authorized field work")

    OutageStepRoles = List(Instance("CIM.IEC61968.Informative.InfOperations.OutageStepPsrRole"))

    # Use association to ConductingEquipment only when there is no VoltageLevel container used.
    BaseVoltage = Instance("CIM.IEC61970.Core.BaseVoltage",
        desc="Use association to ConductingEquipment only when there is no VoltageLevel container used.",
        transient=True,
        opposite="ConductingEquipment",
        editor=InstanceEditor(name="_basevoltages"))

    def _get_basevoltages(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.BaseVoltage" ]
        else:
            return []

    _basevoltages = Property(fget=_get_basevoltages)

    ElectricalAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.ElectricalAsset"))

    # The status state associated with the conducting equipment.
    SvStatus = Instance("CIM.IEC61970.StateVariables.SvStatus",
        desc="The status state associated with the conducting equipment.",
        transient=True,
        opposite="ConductingEquipment",
        editor=InstanceEditor(name="_svstatuss"))

    def _get_svstatuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.StateVariables.SvStatus" ]
        else:
            return []

    _svstatuss = Property(fget=_get_svstatuss)

    # Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
    ProtectionEquipments = List(Instance("CIM.IEC61970.Protection.ProtectionEquipment"),
        desc="Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.")

    # Describes the phases carried by a conducting equipment.
    phases = PhaseCode(desc="Describes the phases carried by a conducting equipment.")

    #--------------------------------------------------------------------------
    #  Begin "ConductingEquipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Core.ConductingEquipment",
        title="ConductingEquipment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConductingEquipment" user definitions:
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
    CurveDatas = List(Instance("CIM.IEC61970.Core.CurveData"),
        desc="The point data values that define a curve")

    # Multiplier for Y3-axis.
    y3Multiplier = UnitMultiplier(desc="Multiplier for Y3-axis.")

    # Multiplier for Y2-axis.
    y2Multiplier = UnitMultiplier(desc="Multiplier for Y2-axis.")

    # Multiplier for X-axis.
    xMultiplier = UnitMultiplier(desc="Multiplier for X-axis.")

    # The Y2-axis units of measure.
    y2Unit = UnitSymbol(desc="The Y2-axis units of measure.")

    # The style or shape of the curve.
    curveStyle = CurveStyle(desc="The style or shape of the curve.")

    # The Y1-axis units of measure.
    y1Unit = UnitSymbol(desc="The Y1-axis units of measure.")

    # Multiplier for Y1-axis
    y1Multiplier = UnitMultiplier(desc="Multiplier for Y1-axis")

    # The Y3-axis units of measure.
    y3Unit = UnitSymbol(desc="The Y3-axis units of measure.")

    # The X-axis units of measure.
    xUnit = UnitSymbol(desc="The X-axis units of measure.")

    #--------------------------------------------------------------------------
    #  Begin "Curve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.Curve",
        title="Curve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Curve" user definitions:
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

    # Reporting groups that are grouped under this group group.
    ReportingGroup = List(Instance("CIM.IEC61970.Core.ReportingGroup"),
        desc="Reporting groups that are grouped under this group group.")

    #--------------------------------------------------------------------------
    #  Begin "ReportingSuperGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ReportingGroup",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.ReportingSuperGroup",
        title="ReportingSuperGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ReportingSuperGroup" user definitions:
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

    # The topological nodes which belong to this connectivity node container.
    TopologicalNode = List(Instance("CIM.IEC61970.Topology.TopologicalNode"),
        desc="The topological nodes which belong to this connectivity node container.")

    # Connectivity nodes contained by this container.
    ConnectivityNodes = List(Instance("CIM.IEC61970.Topology.ConnectivityNode"),
        desc="Connectivity nodes contained by this container.")

    #--------------------------------------------------------------------------
    #  Begin "ConnectivityNodeContainer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "TopologicalNode", "ConnectivityNodes",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Core.ConnectivityNodeContainer",
        title="ConnectivityNodeContainer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConnectivityNodeContainer" user definitions:
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
    Equipments = List(Instance("CIM.IEC61970.Core.Equipment"),
        desc="The association is used in the naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "EquipmentContainer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "TopologicalNode", "ConnectivityNodes", "Equipments",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Core.EquipmentContainer",
        title="EquipmentContainer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquipmentContainer" user definitions:
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
    VoltageLevels = List(Instance("CIM.IEC61970.Core.VoltageLevel"),
        desc="The association is used in the naming hierarchy.")

    # The association is used in the naming hierarchy.
    Region = Instance("CIM.IEC61970.Core.SubGeographicalRegion",
        desc="The association is used in the naming hierarchy.",
        transient=True,
        opposite="Substations",
        editor=InstanceEditor(name="_subgeographicalregions"))

    def _get_subgeographicalregions(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.SubGeographicalRegion" ]
        else:
            return []

    _subgeographicalregions = Property(fget=_get_subgeographicalregions)

    # The association is used in the naming hierarchy.
    Bays = List(Instance("CIM.IEC61970.Core.Bay"),
        desc="The association is used in the naming hierarchy.")

    SubstationAsset = Instance("CIM.IEC61968.Informative.InfAssets.SubstationAsset",
        transient=True,
        opposite="Substation",
        editor=InstanceEditor(name="_substationassets"))

    def _get_substationassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.SubstationAsset" ]
        else:
            return []

    _substationassets = Property(fget=_get_substationassets)

    #--------------------------------------------------------------------------
    #  Begin "Substation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "TopologicalNode", "ConnectivityNodes", "Equipments", "VoltageLevels", "Region", "Bays", "SubstationAsset",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Core.Substation",
        title="Substation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Substation" user definitions:
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

    # Multiplier for value2.
    value2Multiplier = UnitMultiplier(desc="Multiplier for value2.")

    # Value1 units of measure.
    value1Unit = UnitSymbol(desc="Value1 units of measure.")

    # Value2 units of measure.
    value2Unit = UnitSymbol(desc="Value2 units of measure.")

    # Multiplier for value1.
    value1Multiplier = UnitMultiplier(desc="Multiplier for value1.")

    # The time for the first time point.
    startTime = Date(desc="The time for the first time point.")

    #--------------------------------------------------------------------------
    #  Begin "BasicIntervalSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value2Multiplier", "value1Unit", "value2Unit", "value1Multiplier", "startTime",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.BasicIntervalSchedule",
        title="BasicIntervalSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BasicIntervalSchedule" user definitions:
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
    TimePoints = List(Instance("CIM.IEC61970.Core.IrregularTimePoint"),
        desc="The point data values that define a curve")

    #--------------------------------------------------------------------------
    #  Begin "IrregularIntervalSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value2Multiplier", "value1Unit", "value2Unit", "value1Multiplier", "startTime",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.IrregularIntervalSchedule",
        title="IrregularIntervalSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IrregularIntervalSchedule" user definitions:
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

    PowerSystemResources = List(Instance("CIM.IEC61970.Core.PowerSystemResource"))

    # Type of power system resources in this list.
    typePSRList = Str(desc="Type of power system resources in this list.")

    #--------------------------------------------------------------------------
    #  Begin "PsrList" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "typePSRList",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PowerSystemResources",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.PsrList",
        title="PsrList",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PsrList" user definitions:
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
    TimePoints = List(Instance("CIM.IEC61970.Core.RegularTimePoint"),
        desc="The point data values that define a curve")

    # The time between each pair of subsequent RegularTimePoints.
    timeStep = Seconds(desc="The time between each pair of subsequent RegularTimePoints.")

    # The time for the last time point.
    endTime = Date(desc="The time for the last time point.")

    #--------------------------------------------------------------------------
    #  Begin "RegularIntervalSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value2Multiplier", "value1Unit", "value2Unit", "value1Multiplier", "startTime", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.RegularIntervalSchedule",
        title="RegularIntervalSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegularIntervalSchedule" user definitions:
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

    # The operating shares of an operating participant.   An operating participant can be reused for any number of PSR's.
    OperatingShare = List(Instance("CIM.IEC61970.Core.OperatingShare"),
        desc="The operating shares of an operating participant.   An operating participant can be reused for any number of PSR's.")

    #--------------------------------------------------------------------------
    #  Begin "OperatingParticipant" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "OperatingShare",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.OperatingParticipant",
        title="OperatingParticipant",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OperatingParticipant" user definitions:
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
    VoltageLevel = Instance("CIM.IEC61970.Core.VoltageLevel",
        desc="The association is used in the naming hierarchy.",
        transient=True,
        opposite="Bays",
        editor=InstanceEditor(name="_voltagelevels"))

    def _get_voltagelevels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.VoltageLevel" ]
        else:
            return []

    _voltagelevels = Property(fget=_get_voltagelevels)

    # The association is used in the naming hierarchy.
    Substation = Instance("CIM.IEC61970.Core.Substation",
        desc="The association is used in the naming hierarchy.",
        transient=True,
        opposite="Bays",
        editor=InstanceEditor(name="_substations"))

    def _get_substations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.Substation" ]
        else:
            return []

    _substations = Property(fget=_get_substations)

    # Breaker configuration.
    breakerConfiguration = BreakerConfiguration(desc="Breaker configuration.")

    # Bus bar configuration.
    busBarConfiguration = BusbarConfiguration(desc="Bus bar configuration.")

    # Indicates the presence/absence of energy measurements.
    bayEnergyMeasFlag = Bool(desc="Indicates the presence/absence of energy measurements.")

    # Indicates the presence/absence of active/reactive power measurements.
    bayPowerMeasFlag = Bool(desc="Indicates the presence/absence of active/reactive power measurements.")

    #--------------------------------------------------------------------------
    #  Begin "Bay" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "breakerConfiguration", "busBarConfiguration", "bayEnergyMeasFlag", "bayPowerMeasFlag",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "TopologicalNode", "ConnectivityNodes", "Equipments", "VoltageLevel", "Substation",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Core.Bay",
        title="Bay",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Bay" user definitions:
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
    ModelingAuthoritySets = List(Instance("CIM.IEC61970.Core.ModelingAuthoritySet"),
        desc="A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.")

    #--------------------------------------------------------------------------
    #  Begin "ModelingAuthority" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ModelingAuthoritySets",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.ModelingAuthority",
        title="ModelingAuthority",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ModelingAuthority" user definitions:
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
    Bays = List(Instance("CIM.IEC61970.Core.Bay"),
        desc="The association is used in the naming hierarchy.")

    # The association is used in the naming hierarchy.
    Substation = Instance("CIM.IEC61970.Core.Substation",
        desc="The association is used in the naming hierarchy.",
        transient=True,
        opposite="VoltageLevels",
        editor=InstanceEditor(name="_substations"))

    def _get_substations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.Substation" ]
        else:
            return []

    _substations = Property(fget=_get_substations)

    # The base voltage used for all equipment within the VoltageLevel.
    BaseVoltage = Instance("CIM.IEC61970.Core.BaseVoltage",
        desc="The base voltage used for all equipment within the VoltageLevel.",
        transient=True,
        opposite="VoltageLevel",
        editor=InstanceEditor(name="_basevoltages"))

    def _get_basevoltages(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.BaseVoltage" ]
        else:
            return []

    _basevoltages = Property(fget=_get_basevoltages)

    # The bus bar's low voltage limit
    lowVoltageLimit = Voltage(desc="The bus bar's low voltage limit")

    # The bus bar's high voltage limit
    highVoltageLimit = Voltage(desc="The bus bar's high voltage limit")

    #--------------------------------------------------------------------------
    #  Begin "VoltageLevel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "lowVoltageLimit", "highVoltageLimit",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "TopologicalNode", "ConnectivityNodes", "Equipments", "Bays", "Substation", "BaseVoltage",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Core.VoltageLevel",
        title="VoltageLevel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VoltageLevel" user definitions:
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
    ConductingEquipment = Instance("CIM.IEC61970.Core.ConductingEquipment",
        desc="ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes",
        transient=True,
        opposite="Terminals",
        editor=InstanceEditor(name="_conductingequipments"))

    def _get_conductingequipments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.ConductingEquipment" ]
        else:
            return []

    _conductingequipments = Property(fget=_get_conductingequipments)

    BushingAsset = Instance("CIM.IEC61968.Informative.InfAssets.BushingAsset",
        transient=True,
        opposite="Terminal",
        editor=InstanceEditor(name="_bushingassets"))

    def _get_bushingassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.BushingAsset" ]
        else:
            return []

    _bushingassets = Property(fget=_get_bushingassets)

    # Mutual couplings with the branch associated as the first branch.
    HasSecond_MutualCoupling = List(Instance("CIM.IEC61970.Wires.MutualCoupling"),
        desc="Mutual couplings with the branch associated as the first branch.")

    # The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.
    OperationalLimitSet = List(Instance("CIM.IEC61970.OperationalLimits.OperationalLimitSet"),
        desc="The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.")

    # Mutual couplings associated with the branch as the first branch.
    HasFirst_MutualCoupling = List(Instance("CIM.IEC61970.Wires.MutualCoupling"),
        desc="Mutual couplings associated with the branch as the first branch.")

    # The control area tie flows to which this terminal associates.
    TieFlow = List(Instance("CIM.IEC61970.ControlArea.TieFlow"),
        desc="The control area tie flows to which this terminal associates.")

    # One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.
    Measurements = List(Instance("CIM.IEC61970.Meas.Measurement"),
        desc="One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.")

    # The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
    TopologicalNode = Instance("CIM.IEC61970.Topology.TopologicalNode",
        desc="The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.",
        transient=True,
        opposite="Terminal",
        editor=InstanceEditor(name="_topologicalnodes"))

    def _get_topologicalnodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Topology.TopologicalNode" ]
        else:
            return []

    _topologicalnodes = Property(fget=_get_topologicalnodes)

    # The terminal is regulated by a control.
    RegulatingControl = List(Instance("CIM.IEC61970.Wires.RegulatingControl"),
        desc="The terminal is regulated by a control.")

    # The power flow state associated with the terminal.
    SvPowerFlow = Instance("CIM.IEC61970.StateVariables.SvPowerFlow",
        desc="The power flow state associated with the terminal.",
        transient=True,
        opposite="Terminal",
        editor=InstanceEditor(name="_svpowerflows"))

    def _get_svpowerflows(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.StateVariables.SvPowerFlow" ]
        else:
            return []

    _svpowerflows = Property(fget=_get_svpowerflows)

    TerminalConstraints = List(Instance("CIM.IEC61968.Informative.MarketOperations.TerminalConstraintTerm"))

    # The directed branch group terminals for which the terminal is monitored.
    BranchGroupTerminal = List(Instance("CIM.IEC61970.OperationalLimits.BranchGroupTerminal"),
        desc="The directed branch group terminals for which the terminal is monitored.")

    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
    ConnectivityNode = Instance("CIM.IEC61970.Topology.ConnectivityNode",
        desc="Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.",
        transient=True,
        opposite="Terminals",
        editor=InstanceEditor(name="_connectivitynodes"))

    def _get_connectivitynodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Topology.ConnectivityNode" ]
        else:
            return []

    _connectivitynodes = Property(fget=_get_connectivitynodes)

    # The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.
    sequenceNumber = Int(desc="The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.")

    # The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm
    connected = Bool(desc="The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm")

    #--------------------------------------------------------------------------
    #  Begin "Terminal" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "sequenceNumber", "connected",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ConductingEquipment", "BushingAsset", "HasSecond_MutualCoupling", "OperationalLimitSet", "HasFirst_MutualCoupling", "TieFlow", "Measurements", "TopologicalNode", "RegulatingControl", "SvPowerFlow", "TerminalConstraints", "BranchGroupTerminal", "ConnectivityNode",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Core.Terminal",
        title="Terminal",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Terminal" user definitions:
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

    # The Controls having the Unit.
    Controls = List(Instance("CIM.IEC61970.Meas.Control"),
        desc="The Controls having the Unit.")

    # The Protection Equipments having the Unit.
    ProtectionEquipments = List(Instance("CIM.IEC61970.Protection.ProtectionEquipment"),
        desc="The Protection Equipments having the Unit.")

    # The Measurements having the Unit
    Measurements = List(Instance("CIM.IEC61970.Meas.Measurement"),
        desc="The Measurements having the Unit")

    #--------------------------------------------------------------------------
    #  Begin "Unit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Controls", "ProtectionEquipments", "Measurements",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.Unit",
        title="Unit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Unit" user definitions:
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

    # The topological nodes that belong to the reporting group.
    TopologicalNode = List(Instance("CIM.IEC61970.Topology.TopologicalNode"),
        desc="The topological nodes that belong to the reporting group.")

    # The BusNameMarkers that belong to this reporting group.
    BusNameMarker = List(Instance("CIM.IEC61970.Topology.BusNameMarker"),
        desc="The BusNameMarkers that belong to this reporting group.")

    # PSR's which belong to this reporting group.
    PowerSystemResource = List(Instance("CIM.IEC61970.Core.PowerSystemResource"),
        desc="PSR's which belong to this reporting group.")

    # Reporting super group to which this reporting group belongs.
    ReportingSuperGroup = Instance("CIM.IEC61970.Core.ReportingSuperGroup",
        desc="Reporting super group to which this reporting group belongs.",
        transient=True,
        opposite="ReportingGroup",
        editor=InstanceEditor(name="_reportingsupergroups"))

    def _get_reportingsupergroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.ReportingSuperGroup" ]
        else:
            return []

    _reportingsupergroups = Property(fget=_get_reportingsupergroups)

    #--------------------------------------------------------------------------
    #  Begin "ReportingGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "TopologicalNode", "BusNameMarker", "PowerSystemResource", "ReportingSuperGroup",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.ReportingGroup",
        title="ReportingGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ReportingGroup" user definitions:
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

    # Power system resources classified with this PSRType.
    PowerSystemResources = List(Instance("CIM.IEC61970.Core.PowerSystemResource"),
        desc="Power system resources classified with this PSRType.")

    #--------------------------------------------------------------------------
    #  Begin "PSRType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PowerSystemResources",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.PSRType",
        title="PSRType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PSRType" user definitions:
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
    Region = Instance("CIM.IEC61970.Core.GeographicalRegion",
        desc="The association is used in the naming hierarchy.",
        transient=True,
        opposite="Regions",
        editor=InstanceEditor(name="_geographicalregions"))

    def _get_geographicalregions(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.GeographicalRegion" ]
        else:
            return []

    _geographicalregions = Property(fget=_get_geographicalregions)

    # The association is used in the naming hierarchy.
    Substations = List(Instance("CIM.IEC61970.Core.Substation"),
        desc="The association is used in the naming hierarchy.")

    # A Line can be contained by a SubGeographical Region.
    Lines = List(Instance("CIM.IEC61970.Wires.Line"),
        desc="A Line can be contained by a SubGeographical Region.")

    #--------------------------------------------------------------------------
    #  Begin "SubGeographicalRegion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Region", "Substations", "Lines",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.SubGeographicalRegion",
        title="SubGeographicalRegion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SubGeographicalRegion" user definitions:
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

    # The VoltageLevels having this BaseVoltage.
    VoltageLevel = List(Instance("CIM.IEC61970.Core.VoltageLevel"),
        desc="The VoltageLevels having this BaseVoltage.")

    # Use association to ConductingEquipment only when there is no VoltageLevel container used.
    ConductingEquipment = List(Instance("CIM.IEC61970.Core.ConductingEquipment"),
        desc="Use association to ConductingEquipment only when there is no VoltageLevel container used.")

    # The topological nodes at the base voltage.
    TopologicalNode = List(Instance("CIM.IEC61970.Topology.TopologicalNode"),
        desc="The topological nodes at the base voltage.")

    # If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current.
    isDC = Bool(desc="If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current.")

    # The PowerSystemResource's base voltage.
    nominalVoltage = Voltage(desc="The PowerSystemResource's base voltage.")

    #--------------------------------------------------------------------------
    #  Begin "BaseVoltage" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "isDC", "nominalVoltage",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "VoltageLevel", "ConductingEquipment", "TopologicalNode",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.BaseVoltage",
        title="BaseVoltage",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BaseVoltage" user definitions:
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
    basePower = ApparentPower(desc="Definition of base power.")

    #--------------------------------------------------------------------------
    #  Begin "BasePower" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "basePower",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.BasePower",
        title="BasePower",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BasePower" user definitions:
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

    # A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
    ModelingAuthority = Instance("CIM.IEC61970.Core.ModelingAuthority",
        desc="A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.",
        transient=True,
        opposite="ModelingAuthoritySets",
        editor=InstanceEditor(name="_modelingauthoritys"))

    def _get_modelingauthoritys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.ModelingAuthority" ]
        else:
            return []

    _modelingauthoritys = Property(fget=_get_modelingauthoritys)

    # An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.
    IdentifiedObjects = List(Instance("CIM.IEC61970.Core.IdentifiedObject"),
        desc="An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.")

    #--------------------------------------------------------------------------
    #  Begin "ModelingAuthoritySet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ModelingAuthority", "IdentifiedObjects",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Core.ModelingAuthoritySet",
        title="ModelingAuthoritySet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ModelingAuthoritySet" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
