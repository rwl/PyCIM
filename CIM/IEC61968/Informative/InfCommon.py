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

""" This package contains functions common for distribution management.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'Locations are logical entities which are related to a geographical position. Locations can be defined as points, lines or polygons. Location serves as a parent class for e.g. Zone, WorkLocation or ServiceLocation. Both Assets and PowerSystemResources are typically associated to a location. Aside from coordinates, useful properties of Locations can include Directions (i.e. driving instructions) and relationships to Organizations. ActivityRecord is a generalized class used to track the history of an object (e.g. Asset, PowerSystemResource, Customer, Location, Organisation or ErpContact). An ActivityRecord is a type of Document. Key properties of an ActivityRecord include statusDate, status, statusReason and remarks. TODO: Update attribute names. The graphical and geographical aspects of Assets, Locations and PowerSystemResources are managed using Graphical Markup Language (GML), which was defined by the Open GIS Consortium.  Using GML, a diagram is a collection of presentation objects. This package defines the classes Diagram and Presentation. TODO: These are now under Common package.'
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61968.Common import Document
from CIM import Element
from CIM.IEC61970.Domain import Seconds



from enthought.traits.api import Instance, List, Property, Enum, Str, Date, Int, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Enumeration of phase identifiers.
DCPolarityKind = Enum("plusMinus", "plusN", "plus", "minusN", "minus", desc="Enumeration of phase identifiers.")
# Kind of market role an organisation can have.
MarketRoleKind = Enum("other", "transmissionServiceProvider", "planningAuthority", "reliabilityAuthority", "transmissionOwner", "transmissionPlanner", "generatorOperator", "energyServiceConsumer", "generatorOwner", "transmissionOperator", "complianceMonitor", "distributionProvider", "loadServingEntity", "interchangeAuthority", "purchasingSellingEntity", "resourcePlanner", "balancingAuthority", "competitiveRetailer", "standardsDeveloper", desc="Kind of market role an organisation can have.")
# Kind of skill level.
SkillLevelKind = Enum("master", "other", "standard", "apprentice", desc="Kind of skill level.")
# Kind of a diagram.
DiagramKind = Enum("geographic", "schematic", "designSketch", "internalView", "other", desc="Kind of a diagram.")

#------------------------------------------------------------------------------
#  "Role" class:
#------------------------------------------------------------------------------

class Role(IdentifiedObject):
    """ Enumeration of potential roles that might be played by one object relative to another.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # Category of role.
    category = Str(desc="Category of role.")

    #--------------------------------------------------------------------------
    #  Begin "Role" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCommon.Role",
        title="Role",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Role" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ScheduledEvent" class:
#------------------------------------------------------------------------------

class ScheduledEvent(IdentifiedObject):
    """ Signifies an event to trigger one or more activities, such as reading a meter, recalculating a bill, requesting work, when generating units must be scheduled for maintenance, when a transformer is scheduled to be refurbished, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Document = Instance("CIM.IEC61968.Common.Document",
        transient=True,
        opposite="ScheduledEvents",
        editor=InstanceEditor(name="_documents"))

    def _get_documents(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Document" ]
        else:
            return []

    _documents = Property(fget=_get_documents)

    Assets = List(Instance("CIM.IEC61968.Assets.Asset"))

    ActivityRecord = Instance("CIM.IEC61968.Common.ActivityRecord",
        transient=True,
        opposite="ScheduledEvent",
        editor=InstanceEditor(name="_activityrecords"))

    def _get_activityrecords(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.ActivityRecord" ]
        else:
            return []

    _activityrecords = Property(fget=_get_activityrecords)

    ScheduleParameterInfo = Instance("CIM.IEC61968.Informative.InfCommon.ScheduleParameterInfo",
        transient=True,
        opposite="ScheduledEvents",
        editor=InstanceEditor(name="_scheduleparameterinfos"))

    def _get_scheduleparameterinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfCommon.ScheduleParameterInfo" ]
        else:
            return []

    _scheduleparameterinfos = Property(fget=_get_scheduleparameterinfos)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    TimePoint = Instance("CIM.IEC61968.Common.TimePoint",
        transient=True,
        opposite="ScheduledEvents",
        editor=InstanceEditor(name="_timepoints"))

    def _get_timepoints(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.TimePoint" ]
        else:
            return []

    _timepoints = Property(fget=_get_timepoints)

    # Duration of the scheduled event, for example, the time to ramp between values.
    duration = Seconds(desc="Duration of the scheduled event, for example, the time to ramp between values.")

    # Category of scheduled event.
    category = Str(desc="Category of scheduled event.")

    #--------------------------------------------------------------------------
    #  Begin "ScheduledEvent" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "duration", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Document", "Assets", "ActivityRecord", "ScheduleParameterInfo", "status", "TimePoint",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCommon.ScheduledEvent",
        title="ScheduledEvent",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ScheduledEvent" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Skill" class:
#------------------------------------------------------------------------------

class Skill(Document):
    """ Proficiency level of a craft, which is required to operate or maintain a particular type of asset and/or perform certain types of work.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Crafts = List(Instance("CIM.IEC61968.Informative.InfCommon.Craft"))

    QualificationRequirements = List(Instance("CIM.IEC61968.Informative.InfWork.QualificationRequirement"))

    ErpPerson = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson",
        transient=True,
        opposite="Skills",
        editor=InstanceEditor(name="_erppersons"))

    def _get_erppersons(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpPerson" ]
        else:
            return []

    _erppersons = Property(fget=_get_erppersons)

    # Interval between the certification and its expiry.
    certificationPeriod = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Interval between the certification and its expiry.",
        transient=True,
        editor=InstanceEditor(name="_datetimeintervals"))

    def _get_datetimeintervals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.DateTimeInterval" ]
        else:
            return []

    _datetimeintervals = Property(fget=_get_datetimeintervals)

    # Level of skill for a Craft.
    level = SkillLevelKind(desc="Level of skill for a Craft.")

    # Date and time the skill became effective.
    effectiveDateTime = Date(desc="Date and time the skill became effective.")

    #--------------------------------------------------------------------------
    #  Begin "Skill" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "level", "effectiveDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Crafts", "QualificationRequirements", "ErpPerson", "certificationPeriod",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCommon.Skill",
        title="Skill",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Skill" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BankAccount" class:
#------------------------------------------------------------------------------

class BankAccount(Document):
    """ Bank account.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # ServiceSupplier that is owner of this BankAccount.
    ServiceSupplier = Instance("CIM.IEC61968.PaymentMetering.ServiceSupplier",
        desc="ServiceSupplier that is owner of this BankAccount.",
        transient=True,
        opposite="BankAccounts",
        editor=InstanceEditor(name="_servicesuppliers"))

    def _get_servicesuppliers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.ServiceSupplier" ]
        else:
            return []

    _servicesuppliers = Property(fget=_get_servicesuppliers)

    # Bank that provides this BankAccount.
    Bank = Instance("CIM.IEC61968.Informative.InfPaymentMetering.Bank",
        desc="Bank that provides this BankAccount.",
        transient=True,
        opposite="BankAccounts",
        editor=InstanceEditor(name="_banks"))

    def _get_banks(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfPaymentMetering.Bank" ]
        else:
            return []

    _banks = Property(fget=_get_banks)

    # All bank statements generated from this bank account.
    BankStatements = List(Instance("CIM.IEC61968.Informative.InfPaymentMetering.BankStatement"),
        desc="All bank statements generated from this bank account.")

    # Account reference number.
    accountNumber = Str(desc="Account reference number.")

    #--------------------------------------------------------------------------
    #  Begin "BankAccount" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "accountNumber",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ServiceSupplier", "Bank", "BankStatements",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCommon.BankAccount",
        title="BankAccount",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BankAccount" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MarketRole" class:
#------------------------------------------------------------------------------

class MarketRole(IdentifiedObject):
    """ Role an organisation plays in a market. Examples include one or more of values defined in MarketRoleKind.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    Organisations = List(Instance("CIM.IEC61968.Common.Organisation"))

    # Kind of role an organisation plays in a market.
    kind = MarketRoleKind(desc="Kind of role an organisation plays in a market.")

    #--------------------------------------------------------------------------
    #  Begin "MarketRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "kind",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "Organisations",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCommon.MarketRole",
        title="MarketRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MarketRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Diagram" class:
#------------------------------------------------------------------------------

class Diagram(Document):
    """ GML and/or other means are used for rendering objects on various types of displays(geographic, schematic, other) and maps associated with various coordinate systems.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlDiagramObjects = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlDiagramObject"))

    DesignLocations = List(Instance("CIM.IEC61968.Informative.InfWork.DesignLocation"))

    GmlCoordinateSystem = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlCoordinateSystem",
        transient=True,
        opposite="Diagrams",
        editor=InstanceEditor(name="_gmlcoordinatesystems"))

    def _get_gmlcoordinatesystems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlCoordinateSystem" ]
        else:
            return []

    _gmlcoordinatesystems = Property(fget=_get_gmlcoordinatesystems)

    # Kind of this diagram.
    kind = DiagramKind(desc="Kind of this diagram.")

    #--------------------------------------------------------------------------
    #  Begin "Diagram" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "kind",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "GmlDiagramObjects", "DesignLocations", "GmlCoordinateSystem",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCommon.Diagram",
        title="Diagram",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Diagram" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Ratio" class:
#------------------------------------------------------------------------------

class Ratio(Element):
    """ Fraction specified explicitly with a numerator and denominator, which can be used to calculate the quotient.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The part of a fraction that is below the line and that functions as the divisor of the numerator.
    denominator = Float(desc="The part of a fraction that is below the line and that functions as the divisor of the numerator.")

    # The part of a fraction that is above the line and signifies the number to be divided by the denominator.
    numerator = Float(desc="The part of a fraction that is above the line and signifies the number to be divided by the denominator.")

    #--------------------------------------------------------------------------
    #  Begin "Ratio" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "denominator", "numerator",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCommon.Ratio",
        title="Ratio",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Ratio" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BusinessPlan" class:
#------------------------------------------------------------------------------

class BusinessPlan(Document):
    """ A BusinessPlan is an organized sequence of predetermined actions required to complete a future organizational objective. It is a type of document that typically references a schedule, physical and/or logical resources (assets and/or PowerSystemResources), locations, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "BusinessPlan" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCommon.BusinessPlan",
        title="BusinessPlan",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BusinessPlan" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BusinessRole" class:
#------------------------------------------------------------------------------

class BusinessRole(IdentifiedObject):
    """ A business role that this organisation plays. A single organisation typically performs many functions, each one described as a role.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Organisations = List(Instance("CIM.IEC61968.Common.Organisation"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # Category by utility's corporate standards and practices.
    category = Str(desc="Category by utility's corporate standards and practices.")

    #--------------------------------------------------------------------------
    #  Begin "BusinessRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Organisations", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCommon.BusinessRole",
        title="BusinessRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BusinessRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Craft" class:
#------------------------------------------------------------------------------

class Craft(IdentifiedObject):
    """ Craft of a person or a crew. Examples include overhead electric, underground electric, high pressure gas, etc. This ensures necessary knowledge and skills before being allowed to perform certain types of work.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Skills = List(Instance("CIM.IEC61968.Informative.InfCommon.Skill"))

    ErpPersons = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    Capabilities = List(Instance("CIM.IEC61968.Informative.InfWork.Capability"))

    # Category by utility's work mangement standards and practices.
    category = Str(desc="Category by utility's work mangement standards and practices.")

    #--------------------------------------------------------------------------
    #  Begin "Craft" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Skills", "ErpPersons", "status", "Capabilities",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCommon.Craft",
        title="Craft",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Craft" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ScheduleParameterInfo" class:
#------------------------------------------------------------------------------

class ScheduleParameterInfo(IdentifiedObject):
    """ Schedule parameters for an activity that is to occur, is occurring, or has completed.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ForInspectionDataSet = Instance("CIM.IEC61968.Informative.InfWork.InspectionDataSet",
        transient=True,
        opposite="AccordingToSchedules",
        editor=InstanceEditor(name="_inspectiondatasets"))

    def _get_inspectiondatasets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.InspectionDataSet" ]
        else:
            return []

    _inspectiondatasets = Property(fget=_get_inspectiondatasets)

    # Estimated date and time for activity execution (with earliest possibility of activity initiation and latest possibility of activity completion).
    estimatedWindow = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Estimated date and time for activity execution (with earliest possibility of activity initiation and latest possibility of activity completion).",
        transient=True,
        editor=InstanceEditor(name="_datetimeintervals"))

    def _get_datetimeintervals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.DateTimeInterval" ]
        else:
            return []

    _datetimeintervals = Property(fget=_get_datetimeintervals)

    ScheduledEvents = List(Instance("CIM.IEC61968.Informative.InfCommon.ScheduledEvent"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    Documents = List(Instance("CIM.IEC61968.Common.Document"))

    # Requested date and time interval for activity execution.
    requestedWindow = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Requested date and time interval for activity execution.",
        transient=True,
        editor=InstanceEditor(name="_datetimeintervals"))

    def _get_datetimeintervals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.DateTimeInterval" ]
        else:
            return []

    _datetimeintervals = Property(fget=_get_datetimeintervals)

    #--------------------------------------------------------------------------
    #  Begin "ScheduleParameterInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ForInspectionDataSet", "estimatedWindow", "ScheduledEvents", "status", "Documents", "requestedWindow",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCommon.ScheduleParameterInfo",
        title="ScheduleParameterInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ScheduleParameterInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Map" class:
#------------------------------------------------------------------------------

class Map(Diagram):
    """ A type of diagram that is usually printed on paper. It normally depicts part of the earth's surface, showing utility assets, right of ways, topological data, coordinates, grids, etc. Maps vary depending on whether they are used for dispatch, design, schematic, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Map grid number.
    mapLocGrid = Str(desc="Map grid number.")

    # Page number for particular set of maps specified by 'category'.
    pageNumber = Int(desc="Page number for particular set of maps specified by 'category'.")

    #--------------------------------------------------------------------------
    #  Begin "Map" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "kind", "mapLocGrid", "pageNumber",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "GmlDiagramObjects", "DesignLocations", "GmlCoordinateSystem",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCommon.Map",
        title="Map",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Map" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DocPsrRole" class:
#------------------------------------------------------------------------------

class DocPsrRole(Role):
    """ Potential roles that might played by a document relative to a type of PowerSystemResource.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Document = Instance("CIM.IEC61968.Common.Document",
        transient=True,
        opposite="PowerSystemResourceRoles",
        editor=InstanceEditor(name="_documents"))

    def _get_documents(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Document" ]
        else:
            return []

    _documents = Property(fget=_get_documents)

    PowerSystemResource = Instance("CIM.IEC61970.Core.PowerSystemResource",
        transient=True,
        opposite="DocumentRoles",
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

    #--------------------------------------------------------------------------
    #  Begin "DocPsrRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "Document", "PowerSystemResource",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCommon.DocPsrRole",
        title="DocPsrRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DocPsrRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DocDocRole" class:
#------------------------------------------------------------------------------

class DocDocRole(Role):
    """ Roles played between Documents and other Documents.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ToDocument = Instance("CIM.IEC61968.Common.Document",
        transient=True,
        opposite="FromDocumentRoles",
        editor=InstanceEditor(name="_documents"))

    def _get_documents(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Document" ]
        else:
            return []

    _documents = Property(fget=_get_documents)

    FromDocument = Instance("CIM.IEC61968.Common.Document",
        transient=True,
        opposite="ToDocumentRoles",
        editor=InstanceEditor(name="_documents"))

    def _get_documents(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Document" ]
        else:
            return []

    _documents = Property(fget=_get_documents)

    #--------------------------------------------------------------------------
    #  Begin "DocDocRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "ToDocument", "FromDocument",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCommon.DocDocRole",
        title="DocDocRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DocDocRole" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
