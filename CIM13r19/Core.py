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

from CIM13r19 import Element
from CIM13r19.Domain import UnitSymbol
from CIM13r19.Domain import UnitMultiplier



from enthought.traits.api import Instance, List, Property, Enum, Float, Bool, Str, Int
# <<< imports
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor

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

class IrregularTimePoint(Element):
    """ TimePoints for a schedule where the time between the points varies.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An IrregularTimePoint belongs to an IrregularIntervalSchedule.
    IntervalSchedule = Instance("CIM13r19.Core.IrregularIntervalSchedule",
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
                    "CIM13r19.Core.IrregularIntervalSchedule" ]
        else:
            return []

    _irregularintervalschedules = Property(fget=_get_irregularintervalschedules)

    # The time is relative the BasicTimeSchedule.startTime.
    time = Float(desc="The time is relative the BasicTimeSchedule.startTime.")

    # The second value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.
    value2 = Float(desc="The second value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.")

    # The first value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.
    value1 = Float(desc="The first value at the time. The meaning of the value is defined by the class inhering the IrregularIntervalSchedule.")

    #--------------------------------------------------------------------------
    #  Begin "IrregularTimePoint" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("time", "value2", "value1",
                label="Attributes"),
            VGroup("Parent", "IntervalSchedule",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.IrregularTimePoint",
        title="IrregularTimePoint",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IrregularTimePoint" user definitions:
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

    OperatingParticipant = Instance("CIM13r19.Core.OperatingParticipant",
        transient=True,
        opposite="OperatingShare",
        editor=InstanceEditor(name="_operatingparticipants"))

    def _get_operatingparticipants(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.OperatingParticipant" ]
        else:
            return []

    _operatingparticipants = Property(fget=_get_operatingparticipants)

    PowerSystemResource = Instance("CIM13r19.Core.PowerSystemResource",
        transient=True,
        opposite="OperatingShare",
        editor=InstanceEditor(name="_powersystemresources"))

    def _get_powersystemresources(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.PowerSystemResource" ]
        else:
            return []

    _powersystemresources = Property(fget=_get_powersystemresources)

    # Percentage ownership for this device.   The percentage indicates the percentage ownership of the PSROwner for the PowerSystemResource.  The total percentage ownership for a PowerSystemResource should add to 100%.
    percentage = Float(desc="Percentage ownership for this device.   The percentage indicates the percentage ownership of the PSROwner for the PowerSystemResource.  The total percentage ownership for a PowerSystemResource should add to 100%.")

    #--------------------------------------------------------------------------
    #  Begin "OperatingShare" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("percentage",
                label="Attributes"),
            VGroup("Parent", "OperatingParticipant", "PowerSystemResource",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.OperatingShare",
        title="OperatingShare",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OperatingShare" user definitions:
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

    # The point data values that define a curve
    CurveSchedule = Instance("CIM13r19.Core.Curve",
        desc="The point data values that define a curve",
        transient=True,
        opposite="CurveScheduleDatas",
        editor=InstanceEditor(name="_curves"))

    def _get_curves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.Curve" ]
        else:
            return []

    _curves = Property(fget=_get_curves)

    # The data value of the X-axis variable,  depending on the X-axis units
    xvalue = Float(desc="The data value of the X-axis variable,  depending on the X-axis units")

    # The data value of the  first Y-axis variable, depending on the Y-axis units
    y1value = Float(desc="The data value of the  first Y-axis variable, depending on the Y-axis units")

    # The data value of the second Y-axis variable (if present), depending on the Y-axis units
    y2value = Float(desc="The data value of the second Y-axis variable (if present), depending on the Y-axis units")

    #--------------------------------------------------------------------------
    #  Begin "CurveData" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("xvalue", "y1value", "y2value",
                label="Attributes"),
            VGroup("Parent", "CurveSchedule",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.CurveData",
        title="CurveData",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CurveData" user definitions:
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
    IntervalSchedule = Instance("CIM13r19.Core.RegularIntervalSchedule",
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
                    "CIM13r19.Core.RegularIntervalSchedule" ]
        else:
            return []

    _regularintervalschedules = Property(fget=_get_regularintervalschedules)

    # The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
    value1 = Float(desc="The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.")

    # The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
    value2 = Float(desc="The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.")

    # The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime.
    sequenceNumber = Int(desc="The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime.")

    #--------------------------------------------------------------------------
    #  Begin "RegularTimePoint" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("value1", "value2", "sequenceNumber",
                label="Attributes"),
            VGroup("Parent", "IntervalSchedule",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.RegularTimePoint",
        title="RegularTimePoint",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegularTimePoint" user definitions:
    #--------------------------------------------------------------------------

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
    ModelingAuthoritySet = Instance("CIM13r19.Core.ModelingAuthoritySet",
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
                    "CIM13r19.Core.ModelingAuthoritySet" ]
        else:
            return []

    _modelingauthoritysets = Property(fget=_get_modelingauthoritysets)

    # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.
    name = Str(desc="The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.")

    # The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead.
    localName = Str(desc="The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead.")

    # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
    description = Str(desc="The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.")

    # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.
    aliasName = Str(desc="The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.")

    # A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique.
    mRID = Str(desc="A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique.")

    # The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.
    pathName = Str(desc="The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.")

    #--------------------------------------------------------------------------
    #  Begin "IdentifiedObject" user definitions:
    #--------------------------------------------------------------------------

    _name_ids = count(0)
    _name     = None

    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.IdentifiedObject",
        title="IdentifiedObject",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)


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
    #  End "IdentifiedObject" user definitions:
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
    CurveScheduleDatas = List(Instance("CIM13r19.Core.CurveData"),
        desc="The point data values that define a curve")

    # The Y1-axis units of measure.
    y1Unit = UnitSymbol(desc="The Y1-axis units of measure.")

    # The style or shape of the curve.
    curveStyle = CurveStyle(desc="The style or shape of the curve.")

    # Multiplier for Y2-axis.
    y2Multiplier = UnitMultiplier(desc="Multiplier for Y2-axis.")

    # The Y2-axis units of measure.
    y2Unit = UnitSymbol(desc="The Y2-axis units of measure.")

    # Multiplier for Y1-axis
    y1Multiplier = UnitMultiplier(desc="Multiplier for Y1-axis")

    # Multiplier for X-axis.
    xMultiplier = UnitMultiplier(desc="Multiplier for X-axis.")

    # The X-axis units of measure.
    xUnit = UnitSymbol(desc="The X-axis units of measure.")

    #--------------------------------------------------------------------------
    #  Begin "Curve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.Curve",
        title="Curve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Curve" user definitions:
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

    PowerSystemResource = List(Instance("CIM13r19.Core.PowerSystemResource"))

    ReportingSuperGroup = Instance("CIM13r19.Core.ReportingSuperGroup",
        transient=True,
        opposite="ReportingGroup",
        editor=InstanceEditor(name="_reportingsupergroups"))

    def _get_reportingsupergroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.ReportingSuperGroup" ]
        else:
            return []

    _reportingsupergroups = Property(fget=_get_reportingsupergroups)

    BusNameMarker = List(Instance("CIM13r19.Topology.BusNameMarker"))

    TopologicalNode = List(Instance("CIM13r19.Topology.TopologicalNode"))

    #--------------------------------------------------------------------------
    #  Begin "ReportingGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PowerSystemResource", "ReportingSuperGroup", "BusNameMarker", "TopologicalNode",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.ReportingGroup",
        title="ReportingGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ReportingGroup" user definitions:
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
    IdentifiedObjects = List(Instance("CIM13r19.Core.IdentifiedObject"),
        desc="An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.")

    # A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
    ModelingAuthority = Instance("CIM13r19.Core.ModelingAuthority",
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
                    "CIM13r19.Core.ModelingAuthority" ]
        else:
            return []

    _modelingauthoritys = Property(fget=_get_modelingauthoritys)

    #--------------------------------------------------------------------------
    #  Begin "ModelingAuthoritySet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "IdentifiedObjects", "ModelingAuthority",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.ModelingAuthoritySet",
        title="ModelingAuthoritySet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ModelingAuthoritySet" user definitions:
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

    OperatingShare = List(Instance("CIM13r19.Core.OperatingShare"))

    #--------------------------------------------------------------------------
    #  Begin "OperatingParticipant" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "OperatingShare",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.OperatingParticipant",
        title="OperatingParticipant",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OperatingParticipant" user definitions:
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

    ReportingGroup = List(Instance("CIM13r19.Core.ReportingGroup"))

    #--------------------------------------------------------------------------
    #  Begin "ReportingSuperGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ReportingGroup",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.ReportingSuperGroup",
        title="ReportingSuperGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ReportingSuperGroup" user definitions:
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
    Regions = List(Instance("CIM13r19.Core.SubGeographicalRegion"),
        desc="The association is used in the naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "GeographicalRegion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Regions",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.GeographicalRegion",
        title="GeographicalRegion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GeographicalRegion" user definitions:
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

    Controls = List(Instance("CIM13r19.Meas.Control"))

    # The Protection Equipments having the Unit.
    ProtectionEquipments = List(Instance("CIM13r19.Protection.ProtectionEquipment"),
        desc="The Protection Equipments having the Unit.")

    Measurements = List(Instance("CIM13r19.Meas.Measurement"))

    #--------------------------------------------------------------------------
    #  Begin "Unit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Controls", "ProtectionEquipments", "Measurements",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.Unit",
        title="Unit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Unit" user definitions:
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
    ModelingAuthoritySets = List(Instance("CIM13r19.Core.ModelingAuthoritySet"),
        desc="A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.")

    #--------------------------------------------------------------------------
    #  Begin "ModelingAuthority" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ModelingAuthoritySets",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.ModelingAuthority",
        title="ModelingAuthority",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ModelingAuthority" user definitions:
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
    ConductingEquipment = List(Instance("CIM13r19.Core.ConductingEquipment"),
        desc="Use association to ConductingEquipment only when there is no VoltageLevel container used.")

    VoltageLevel = List(Instance("CIM13r19.Core.VoltageLevel"))

    # The PowerSystemResource's base voltage.
    nominalVoltage = Float(desc="The PowerSystemResource's base voltage.")

    # If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current.
    isDC = Bool(desc="If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current.")

    #--------------------------------------------------------------------------
    #  Begin "BaseVoltage" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "nominalVoltage", "isDC",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ConductingEquipment", "VoltageLevel",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.BaseVoltage",
        title="BaseVoltage",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BaseVoltage" user definitions:
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
    value2Unit = UnitSymbol(desc="Value2 units of measure.")

    # The time for the first time point.
    startTime = Str(desc="The time for the first time point.")

    # Multiplier for value2.
    value2Multiplier = UnitMultiplier(desc="Multiplier for value2.")

    # Value1 units of measure.
    value1Unit = UnitSymbol(desc="Value1 units of measure.")

    # Multiplier for value1.
    value1Multiplier = UnitMultiplier(desc="Multiplier for value1.")

    #--------------------------------------------------------------------------
    #  Begin "BasicIntervalSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "value2Unit", "startTime", "value2Multiplier", "value1Unit", "value1Multiplier",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.BasicIntervalSchedule",
        title="BasicIntervalSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BasicIntervalSchedule" user definitions:
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
    TimePoints = List(Instance("CIM13r19.Core.RegularTimePoint"),
        desc="A RegularTimePoint belongs to a RegularIntervalSchedule.")

    # The time between each pair of subsequent RegularTimePoints.
    timeStep = Float(desc="The time between each pair of subsequent RegularTimePoints.")

    # The time for the last time point.
    endTime = Str(desc="The time for the last time point.")

    #--------------------------------------------------------------------------
    #  Begin "RegularIntervalSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "value2Unit", "startTime", "value2Multiplier", "value1Unit", "value1Multiplier", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.RegularIntervalSchedule",
        title="RegularIntervalSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegularIntervalSchedule" user definitions:
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
    TimePoints = List(Instance("CIM13r19.Core.IrregularTimePoint"),
        desc="An IrregularTimePoint belongs to an IrregularIntervalSchedule.")

    #--------------------------------------------------------------------------
    #  Begin "IrregularIntervalSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "value2Unit", "startTime", "value2Multiplier", "value1Unit", "value1Multiplier",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.IrregularIntervalSchedule",
        title="IrregularIntervalSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IrregularIntervalSchedule" user definitions:
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
    TieFlow = List(Instance("CIM13r19.ControlArea.TieFlow"),
        desc="A terminal may participate in zero, one, or two control areas as a tie flow.")

    OperationalLimitSet = List(Instance("CIM13r19.OperationalLimits.OperationalLimitSet"))

    BranchGroupTerminal = List(Instance("CIM13r19.OperationalLimits.BranchGroupTerminal"))

    # ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
    ConductingEquipment = Instance("CIM13r19.Core.ConductingEquipment",
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
                    "CIM13r19.Core.ConductingEquipment" ]
        else:
            return []

    _conductingequipments = Property(fget=_get_conductingequipments)

    RegulatingControl = List(Instance("CIM13r19.Wires.RegulatingControl"))

    # One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.
    Measurements = List(Instance("CIM13r19.Meas.Measurement"),
        desc="One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.")

    TopologicalNode = Instance("CIM13r19.Topology.TopologicalNode",
        transient=True,
        opposite="Terminal",
        editor=InstanceEditor(name="_topologicalnodes"))

    def _get_topologicalnodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Topology.TopologicalNode" ]
        else:
            return []

    _topologicalnodes = Property(fget=_get_topologicalnodes)

    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
    ConnectivityNode = Instance("CIM13r19.Topology.ConnectivityNode",
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
                    "CIM13r19.Topology.ConnectivityNode" ]
        else:
            return []

    _connectivitynodes = Property(fget=_get_connectivitynodes)

    #--------------------------------------------------------------------------
    #  Begin "Terminal" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "TieFlow", "OperationalLimitSet", "BranchGroupTerminal", "ConductingEquipment", "RegulatingControl", "Measurements", "TopologicalNode", "ConnectivityNode",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.Terminal",
        title="Terminal",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Terminal" user definitions:
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
    Region = Instance("CIM13r19.Core.GeographicalRegion",
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
                    "CIM13r19.Core.GeographicalRegion" ]
        else:
            return []

    _geographicalregions = Property(fget=_get_geographicalregions)

    # A Line can be contained by a SubGeographical Region.
    Lines = List(Instance("CIM13r19.Wires.Line"),
        desc="A Line can be contained by a SubGeographical Region.")

    # The association is used in the naming hierarchy.
    Substations = List(Instance("CIM13r19.Core.Substation"),
        desc="The association is used in the naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "SubGeographicalRegion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Region", "Lines", "Substations",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.SubGeographicalRegion",
        title="SubGeographicalRegion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SubGeographicalRegion" user definitions:
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

    PSRType = Instance("CIM13r19.Core.PSRType",
        transient=True,
        opposite="PowerSystemResource",
        editor=InstanceEditor(name="_psrtypes"))

    def _get_psrtypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.PSRType" ]
        else:
            return []

    _psrtypes = Property(fget=_get_psrtypes)

    # A power system resource may be part of one or more companies
    OperatedBy_Companies = List(Instance("CIM13r19.Core.Company"),
        desc="A power system resource may be part of one or more companies")

    ReportingGroup = List(Instance("CIM13r19.Core.ReportingGroup"))

    OperatingShare = List(Instance("CIM13r19.Core.OperatingShare"))

    PsrLists = List(Instance("CIM13r19.Core.PsrList"))

    # A power system resource may have an outage schedule
    OutageSchedule = Instance("CIM13r19.Outage.OutageSchedule",
        desc="A power system resource may have an outage schedule",
        transient=True,
        opposite="PSR",
        editor=InstanceEditor(name="_outageschedules"))

    def _get_outageschedules(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Outage.OutageSchedule" ]
        else:
            return []

    _outageschedules = Property(fget=_get_outageschedules)

    # Measurement-PSR defines the measurements in the naming hierarchy.
    Contains_Measurements = List(Instance("CIM13r19.Meas.Measurement"),
        desc="Measurement-PSR defines the measurements in the naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "PowerSystemResource" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.PowerSystemResource",
        title="PowerSystemResource",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PowerSystemResource" user definitions:
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
    basePower = Float(desc="Definition of base power.")

    #--------------------------------------------------------------------------
    #  Begin "BasePower" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "basePower",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.BasePower",
        title="BasePower",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BasePower" user definitions:
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

    PowerSystemResource = List(Instance("CIM13r19.Core.PowerSystemResource"))

    #--------------------------------------------------------------------------
    #  Begin "PSRType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PowerSystemResource",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.PSRType",
        title="PSRType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PSRType" user definitions:
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

    PowerSystemResources = List(Instance("CIM13r19.Core.PowerSystemResource"))

    # Type of power system resources in this list.
    typePSRList = Str(desc="Type of power system resources in this list.")

    #--------------------------------------------------------------------------
    #  Begin "PsrList" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "typePSRList",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PowerSystemResources",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.PsrList",
        title="PsrList",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PsrList" user definitions:
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
    Operates_PSRs = List(Instance("CIM13r19.Core.PowerSystemResource"),
        desc="A power system resource may be part of one or more companies")

    # The type of company.
    companyType = CompanyType(desc="The type of company.")

    #--------------------------------------------------------------------------
    #  Begin "Company" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "companyType",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Operates_PSRs",
                label="References"),
            dock="tab"),
        id="CIM13r19.Core.Company",
        title="Company",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Company" user definitions:
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

    TopologicalNode = List(Instance("CIM13r19.Topology.TopologicalNode"))

    ConnectivityNodes = List(Instance("CIM13r19.Topology.ConnectivityNode"))

    #--------------------------------------------------------------------------
    #  Begin "ConnectivityNodeContainer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "TopologicalNode", "ConnectivityNodes",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Core.ConnectivityNodeContainer",
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
    Contains_Equipments = List(Instance("CIM13r19.Core.Equipment"),
        desc="The association is used in the naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "EquipmentContainer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "TopologicalNode", "ConnectivityNodes", "Contains_Equipments",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Core.EquipmentContainer",
        title="EquipmentContainer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquipmentContainer" user definitions:
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

    OperationalLimitSet = List(Instance("CIM13r19.OperationalLimits.OperationalLimitSet"))

    ContingencyEquipment = List(Instance("CIM13r19.Contingency.ContingencyEquipment"))

    # The association is used in the naming hierarchy.
    MemberOf_EquipmentContainer = Instance("CIM13r19.Core.EquipmentContainer",
        desc="The association is used in the naming hierarchy.",
        transient=True,
        opposite="Contains_Equipments",
        editor=InstanceEditor(name="_equipmentcontainers"))

    def _get_equipmentcontainers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.EquipmentContainer" ]
        else:
            return []

    _equipmentcontainers = Property(fget=_get_equipmentcontainers)

    # The equipment is normally in service.
    normalIlyInService = Bool(desc="The equipment is normally in service.")

    #--------------------------------------------------------------------------
    #  Begin "Equipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Core.Equipment",
        title="Equipment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Equipment" user definitions:
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
    MemberOf_Substation = Instance("CIM13r19.Core.Substation",
        desc="The association is used in the naming hierarchy.",
        transient=True,
        opposite="Contains_Bays",
        editor=InstanceEditor(name="_substations"))

    def _get_substations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.Substation" ]
        else:
            return []

    _substations = Property(fget=_get_substations)

    # The association is used in the naming hierarchy.
    MemberOf_VoltageLevel = Instance("CIM13r19.Core.VoltageLevel",
        desc="The association is used in the naming hierarchy.",
        transient=True,
        opposite="Contains_Bays",
        editor=InstanceEditor(name="_voltagelevels"))

    def _get_voltagelevels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.VoltageLevel" ]
        else:
            return []

    _voltagelevels = Property(fget=_get_voltagelevels)

    # Bus bar configuration.
    busBarConfiguration = BusbarConfiguration(desc="Bus bar configuration.")

    # Indicates the presence/absence of active/reactive power measurements.
    bayPowerMeasFlag = Bool(desc="Indicates the presence/absence of active/reactive power measurements.")

    # Breaker configuration.
    breakerConfiguration = BreakerConfiguration(desc="Breaker configuration.")

    # Indicates the presence/absence of energy measurements.
    bayEnergyMeasFlag = Bool(desc="Indicates the presence/absence of energy measurements.")

    #--------------------------------------------------------------------------
    #  Begin "Bay" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "busBarConfiguration", "bayPowerMeasFlag", "breakerConfiguration", "bayEnergyMeasFlag",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "TopologicalNode", "ConnectivityNodes", "Contains_Equipments", "MemberOf_Substation", "MemberOf_VoltageLevel",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Core.Bay",
        title="Bay",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Bay" user definitions:
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
    Contains_Bays = List(Instance("CIM13r19.Core.Bay"),
        desc="The association is used in the naming hierarchy.")

    BaseVoltage = Instance("CIM13r19.Core.BaseVoltage",
        transient=True,
        opposite="VoltageLevel",
        editor=InstanceEditor(name="_basevoltages"))

    def _get_basevoltages(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.BaseVoltage" ]
        else:
            return []

    _basevoltages = Property(fget=_get_basevoltages)

    # The association is used in the naming hierarchy.
    MemberOf_Substation = Instance("CIM13r19.Core.Substation",
        desc="The association is used in the naming hierarchy.",
        transient=True,
        opposite="Contains_VoltageLevels",
        editor=InstanceEditor(name="_substations"))

    def _get_substations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.Substation" ]
        else:
            return []

    _substations = Property(fget=_get_substations)

    # The bus bar's low voltage limit
    lowVoltageLimit = Float(desc="The bus bar's low voltage limit")

    # The bus bar's high voltage limit
    highVoltageLimit = Float(desc="The bus bar's high voltage limit")

    #--------------------------------------------------------------------------
    #  Begin "VoltageLevel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "lowVoltageLimit", "highVoltageLimit",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "TopologicalNode", "ConnectivityNodes", "Contains_Equipments", "Contains_Bays", "BaseVoltage", "MemberOf_Substation",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Core.VoltageLevel",
        title="VoltageLevel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VoltageLevel" user definitions:
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
    Contains_VoltageLevels = List(Instance("CIM13r19.Core.VoltageLevel"),
        desc="The association is used in the naming hierarchy.")

    # The association is used in the naming hierarchy.
    Contains_Bays = List(Instance("CIM13r19.Core.Bay"),
        desc="The association is used in the naming hierarchy.")

    # The association is used in the naming hierarchy.
    Region = Instance("CIM13r19.Core.SubGeographicalRegion",
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
                    "CIM13r19.Core.SubGeographicalRegion" ]
        else:
            return []

    _subgeographicalregions = Property(fget=_get_subgeographicalregions)

    #--------------------------------------------------------------------------
    #  Begin "Substation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "TopologicalNode", "ConnectivityNodes", "Contains_Equipments", "Contains_VoltageLevels", "Contains_Bays", "Region",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Core.Substation",
        title="Substation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Substation" user definitions:
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
    Terminals = List(Instance("CIM13r19.Core.Terminal"),
        desc="ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes")

    # Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
    ProtectionEquipments = List(Instance("CIM13r19.Protection.ProtectionEquipment"),
        desc="Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.")

    # Use association to ConductingEquipment only when there is no VoltageLevel container used.
    BaseVoltage = Instance("CIM13r19.Core.BaseVoltage",
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
                    "CIM13r19.Core.BaseVoltage" ]
        else:
            return []

    _basevoltages = Property(fget=_get_basevoltages)

    # Conducting equipment may have multiple clearance tags for authorized field work
    ClearanceTags = List(Instance("CIM13r19.Outage.ClearanceTag"),
        desc="Conducting equipment may have multiple clearance tags for authorized field work")

    # Describes the phases carried by a conducting equipment.
    phases = PhaseCode(desc="Describes the phases carried by a conducting equipment.")

    #--------------------------------------------------------------------------
    #  Begin "ConductingEquipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Core.ConductingEquipment",
        title="ConductingEquipment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConductingEquipment" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
