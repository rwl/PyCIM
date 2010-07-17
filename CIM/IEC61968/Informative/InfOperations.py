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

""" TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'The Documentation package is used for the modeling of business documents. Some of these may be electronic realizations of legacy paper document, and some may be electronic information exchanges or collections. Documents will typically reference or describe one or more CIM objects. The DataSets package is used to describe documents tyically used for exchange of collections of object descriptions (e.g., NetworkDataSet). The operational package is used to define documents related to distribution operations business processes (e.g., OperationalRestriction, SwitchingSchedule). TroubleTickets are used by Customers to report problems related to the elctrical distribution network. TroubleTickets may be grouped and be related to a PlannedOutage, OutageNotification and/or PowerSystemResource. The Outage package defines classes related to outage management (OutageStep, OutageRecord, OutageReport).'
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61968.Informative.InfCommon import Role
from CIM.IEC61968.Common import Document
from CIM.IEC61968.Common import ActivityRecord
from CIM.IEC61970.Core import EquipmentContainer
from CIM.IEC61970.Domain import Minutes



from enthought.traits.api import Instance, List, Property, Enum, Str, Date, Bool, Int
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Connection kind of a circuit.
CircuitConnectionKind = Enum("electricallyConnected", "nominallyConnected", "other", "asBuilt", desc="Connection kind of a circuit.")
# Kind of power system resource event.
PSREventKind = Enum("inService", "unknown", "pendingAdd", "outOfService", "pendingRemove", "other", "pendingReplace", desc="Kind of power system resource event.")
# Kind of SwitchingStep status.
SwitchingStepStatusKind = Enum("confirmed", "skipped", "aborted", "instructed", "proposed", desc="Kind of SwitchingStep status.")
# Kind of outage.
OutageKind = Enum("flexible", "fixed", "forced", desc="Kind of outage.")
# Kind of trouble reporting.
TroubleReportingKind = Enum("letter", "other", "call", "email", desc="Kind of trouble reporting.")
# Possible kinds of changes.
ChangeItemKind = Enum("add", "modify", "delete", desc="Possible kinds of changes.")

#------------------------------------------------------------------------------
#  "SwitchingStep" class:
#------------------------------------------------------------------------------

class SwitchingStep(IdentifiedObject):
    """ A single step within a SwitchingSchedule. Could be a switching operation (applying a network alteration), or issuing a safety document. Note: Inherited attribute IdentifiedObject.name is used to hold the sequence number.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Interval between 'requiredControlAction' was issued and completed.
    requiredControlActionInterval = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Interval between 'requiredControlAction' was issued and completed.",
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

    SafetyDocument = Instance("CIM.IEC61968.Informative.InfOperations.SafetyDocument",
        transient=True,
        opposite="ScheduleSteps",
        editor=InstanceEditor(name="_safetydocuments"))

    def _get_safetydocuments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfOperations.SafetyDocument" ]
        else:
            return []

    _safetydocuments = Property(fget=_get_safetydocuments)

    SwitchingSchedule = Instance("CIM.IEC61968.Informative.InfOperations.SwitchingSchedule",
        transient=True,
        opposite="ScheduleSteps",
        editor=InstanceEditor(name="_switchingschedules"))

    def _get_switchingschedules(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfOperations.SwitchingSchedule" ]
        else:
            return []

    _switchingschedules = Property(fget=_get_switchingschedules)

    ErpPersonRole = Instance("CIM.IEC61968.Informative.InfOperations.ErpPersonScheduleStepRole",
        transient=True,
        opposite="SwitchingStep",
        editor=InstanceEditor(name="_erppersonschedulesteproles"))

    def _get_erppersonschedulesteproles(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfOperations.ErpPersonScheduleStepRole" ]
        else:
            return []

    _erppersonschedulesteproles = Property(fget=_get_erppersonschedulesteproles)

    PowerSystemResources = List(Instance("CIM.IEC61970.Core.PowerSystemResource"))

    # Status of this SwitchingStep.
    statusKind = SwitchingStepStatusKind(desc="Status of this SwitchingStep.")

    # Desired end state for the associated PowerSystemResource as a result of this schedule step.
    desiredEndState = Str(desc="Desired end state for the associated PowerSystemResource as a result of this schedule step.")

    # Information regarding this switching schedule step.
    text = Str(desc="Information regarding this switching schedule step.")

    # Control actions required to perform this step.
    requiredControlAction = Str(desc="Control actions required to perform this step.")

    #--------------------------------------------------------------------------
    #  Begin "SwitchingStep" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "statusKind", "desiredEndState", "text", "requiredControlAction",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "requiredControlActionInterval", "SafetyDocument", "SwitchingSchedule", "ErpPersonRole", "PowerSystemResources",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.SwitchingStep",
        title="SwitchingStep",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SwitchingStep" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpPersonScheduleStepRole" class:
#------------------------------------------------------------------------------

class ErpPersonScheduleStepRole(Role):
    """ Roles played between Persons and Schedule Steps.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SwitchingStep = Instance("CIM.IEC61968.Informative.InfOperations.SwitchingStep",
        transient=True,
        opposite="ErpPersonRole",
        editor=InstanceEditor(name="_switchingsteps"))

    def _get_switchingsteps(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfOperations.SwitchingStep" ]
        else:
            return []

    _switchingsteps = Property(fget=_get_switchingsteps)

    ErpPerson = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson",
        transient=True,
        opposite="SwitchingStepRoles",
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

    #--------------------------------------------------------------------------
    #  Begin "ErpPersonScheduleStepRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "SwitchingStep", "ErpPerson",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.ErpPersonScheduleStepRole",
        title="ErpPersonScheduleStepRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpPersonScheduleStepRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OperationalRestriction" class:
#------------------------------------------------------------------------------

class OperationalRestriction(Document):
    """ A document that can be associated with a device to describe any sort of restrictions compared with the original manufacturer's specification e.g. temporary maximum loadings, maximum switching current, do not operate if bus couplers are open etc etc.  Since it is used in the network operations domain, it is associated with ConductingEquipment. In the UK, for example, if a breaker or switch ever mal-operates, this is reported centrally and utilities use their asset systems to identify all the installed devices of the same manufacturer's type. They then apply operational restrictions in the operational systems to warn operators of potential problems. After appropriate inspection and maintenance, the operational restrictions may be removed.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Interval during which the restriction is applied.
    activePeriod = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Interval during which the restriction is applied.",
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
    #  Begin "OperationalRestriction" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "activePeriod",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.OperationalRestriction",
        title="OperationalRestriction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OperationalRestriction" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SafetyDocument" class:
#------------------------------------------------------------------------------

class SafetyDocument(Document):
    """ A document restricting or authorising works on electrical equipment (for example a permit to work, sanction for test, limitation of access, or certificate of isolation), defined based upon organisational practices. Note: SafetyDocument may refer to ClearanceTag-s associated with ConductingEquipment for which the SafetyDocument is issued.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    PowerSystemResource = Instance("CIM.IEC61970.Core.PowerSystemResource",
        transient=True,
        opposite="SafetyDocuments",
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

    ScheduleSteps = List(Instance("CIM.IEC61968.Informative.InfOperations.SwitchingStep"))

    ClearanceTags = List(Instance("CIM.IEC61970.Outage.ClearanceTag"))

    #--------------------------------------------------------------------------
    #  Begin "SafetyDocument" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "PowerSystemResource", "ScheduleSteps", "ClearanceTags",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.SafetyDocument",
        title="SafetyDocument",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SafetyDocument" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OutageStep" class:
#------------------------------------------------------------------------------

class OutageStep(IdentifiedObject):
    """ Holds an outage start and end time for each supply point of an outage record. The supply point for a given step is the associated PowerSystemResource instance.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Crews = List(Instance("CIM.IEC61968.Informative.InfWork.Crew"))

    # Multiple outage codes may apply to an outage step.
    OutageCodes = List(Instance("CIM.IEC61968.Informative.InfOperations.OutageCode"),
        desc="Multiple outage codes may apply to an outage step.")

    OutageRecord = Instance("CIM.IEC61968.Informative.InfOperations.OutageRecord",
        transient=True,
        opposite="OutageSteps",
        editor=InstanceEditor(name="_outagerecords"))

    def _get_outagerecords(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfOperations.OutageRecord" ]
        else:
            return []

    _outagerecords = Property(fget=_get_outagerecords)

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

    # Date and time interval between loss and restoration of power.
    noPowerInterval = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Date and time interval between loss and restoration of power.",
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

    ConductingEquipmentRoles = List(Instance("CIM.IEC61968.Informative.InfOperations.OutageStepPsrRole"))

    jobPriority = Str

    # Total Customer Minutes Lost (CML) for this supply point for this outage.
    totalCml = Minutes(desc="Total Customer Minutes Lost (CML) for this supply point for this outage.")

    # Estimated time of restoration.
    estimatedRestoreDateTime = Date(desc="Estimated time of restoration.")

    # Average Customer Minutes Lost (CML) for this supply point for this outage.
    averageCml = Minutes(desc="Average Customer Minutes Lost (CML) for this supply point for this outage.")

    # True if shocks reported by caller or engineer.
    shockReported = Bool(desc="True if shocks reported by caller or engineer.")

    # Number of customers with high reliability required.
    specialCustomerCount = Int(desc="Number of customers with high reliability required.")

    # Number of customers phoning in.
    callerCount = Int(desc="Number of customers phoning in.")

    # True if damage reported by caller or engineer.
    damage = Bool(desc="True if damage reported by caller or engineer.")

    # Number of customers with critical needs, e.g., with a dialysis machine.
    criticalCustomerCount = Int(desc="Number of customers with critical needs, e.g., with a dialysis machine.")

    # True if fatalities reported by caller or engineer.
    fatality = Bool(desc="True if fatalities reported by caller or engineer.")

    # Number of customers connected to the PowerSystemResource.
    totalCustomerCount = Int(desc="Number of customers connected to the PowerSystemResource.")

    # True if injuries reported by caller or engineer.
    injury = Bool(desc="True if injuries reported by caller or engineer.")

    #--------------------------------------------------------------------------
    #  Begin "OutageStep" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "jobPriority", "totalCml", "estimatedRestoreDateTime", "averageCml", "shockReported", "specialCustomerCount", "callerCount", "damage", "criticalCustomerCount", "fatality", "totalCustomerCount", "injury",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Crews", "OutageCodes", "OutageRecord", "status", "noPowerInterval", "ConductingEquipmentRoles",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.OutageStep",
        title="OutageStep",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OutageStep" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ComplianceEvent" class:
#------------------------------------------------------------------------------

class ComplianceEvent(ActivityRecord):
    """ Compliance events are used for reporting regulatory or contract compliance issues and/or variances. These might be created as a consequence of local business processes and associated rules. It is anticipated that this class will be customised extensively to meet local implementation needs. Use inherited 'category' to indicate that, for example, expected performance will not be met or reported as mandated.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Type of compliance event indicating, for example, types of regulatory and/or contractual compliance events where expected performance will not be met or reported as mandated.
    complianceType = Str(desc="Type of compliance event indicating, for example, types of regulatory and/or contractual compliance events where expected performance will not be met or reported as mandated.")

    # The deadline for compliance.
    deadline = Date(desc="The deadline for compliance.")

    #--------------------------------------------------------------------------
    #  Begin "ComplianceEvent" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "reason", "category", "severity", "createdDateTime", "complianceType", "deadline",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "MarketFactors", "Documents", "Organisations", "ScheduledEvent", "Assets", "ErpPersons", "Locations", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.ComplianceEvent",
        title="ComplianceEvent",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ComplianceEvent" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PSREvent" class:
#------------------------------------------------------------------------------

class PSREvent(ActivityRecord):
    """ Event recording the change in operational status of a PowerSystemResource.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Power system resource that generated this event.
    PowerSystemResource = Instance("CIM.IEC61970.Core.PowerSystemResource",
        desc="Power system resource that generated this event.",
        transient=True,
        opposite="PSREvent",
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

    # Kind of event.
    kind = PSREventKind(desc="Kind of event.")

    #--------------------------------------------------------------------------
    #  Begin "PSREvent" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "reason", "category", "severity", "createdDateTime", "kind",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MarketFactors", "Documents", "Organisations", "ScheduledEvent", "Assets", "ErpPersons", "Locations", "status", "PowerSystemResource",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.PSREvent",
        title="PSREvent",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PSREvent" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OutageCode" class:
#------------------------------------------------------------------------------

class OutageCode(IdentifiedObject):
    """ Classification of outage types. Multiple outage codes may apply to a given outage or outage step.The primary overall outage type is recorded in OutageRecord.outageType. There may be more than one classification per outage step and/or per outage record. Example codes/subcodes include: weather/ice, weather/lightning, wildlife/squirrel, wildlife/bird, burned/overload, burned/weather, wire down/accident, wire down/tree, wire down/vandalism, etc. The typical 'outage code' is in the inherited 'name' attribute. The code is described in the inherited 'description' attribute.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    OutageRecords = List(Instance("CIM.IEC61968.Informative.InfOperations.OutageRecord"))

    OutageSteps = List(Instance("CIM.IEC61968.Informative.InfOperations.OutageStep"))

    # The main code is stored in the inherited .name. This sub-code provides an additional level of classification detail.
    subCode = Str(desc="The main code is stored in the inherited .name. This sub-code provides an additional level of classification detail.")

    #--------------------------------------------------------------------------
    #  Begin "OutageCode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subCode",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "OutageRecords", "OutageSteps",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.OutageCode",
        title="OutageCode",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OutageCode" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OutageStepPsrRole" class:
#------------------------------------------------------------------------------

class OutageStepPsrRole(Role):
    """ Roles played between Power System Resources and Outage Steps. Examples roles include: normal supply, actual supply, interrupting device, restoration device.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ConductingEquipment = Instance("CIM.IEC61970.Core.ConductingEquipment",
        transient=True,
        opposite="OutageStepRoles",
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

    OutageStep = Instance("CIM.IEC61968.Informative.InfOperations.OutageStep",
        transient=True,
        opposite="ConductingEquipmentRoles",
        editor=InstanceEditor(name="_outagesteps"))

    def _get_outagesteps(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfOperations.OutageStep" ]
        else:
            return []

    _outagesteps = Property(fget=_get_outagesteps)

    #--------------------------------------------------------------------------
    #  Begin "OutageStepPsrRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "ConductingEquipment", "OutageStep",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.OutageStepPsrRole",
        title="OutageStepPsrRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OutageStepPsrRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "NetworkDataSet" class:
#------------------------------------------------------------------------------

class NetworkDataSet(IdentifiedObject):
    """ Categorized as a type of document, model of a portion of the electrical network that includes a list of the equipment, along with relevant connectivity, electrical characteristics, geographical location, and various parameters associated with the equipment.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Documents = List(Instance("CIM.IEC61968.Common.Document"))

    # A NetworkDataSet may contain sections of circuits (vs. whole circuits).
    CircuitSections = List(Instance("CIM.IEC61968.Informative.InfOperations.CircuitSection"),
        desc="A NetworkDataSet may contain sections of circuits (vs. whole circuits).")

    LandBases = List(Instance("CIM.IEC61968.Informative.InfOperations.LandBase"))

    ChangeSets = List(Instance("CIM.IEC61968.Informative.InfOperations.ChangeSet"))

    PowerSystemResources = List(Instance("CIM.IEC61970.Core.PowerSystemResource"))

    ChangeItems = List(Instance("CIM.IEC61968.Informative.InfOperations.ChangeItem"))

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

    # Category of network data set.
    category = Str(desc="Category of network data set.")

    #--------------------------------------------------------------------------
    #  Begin "NetworkDataSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Documents", "CircuitSections", "LandBases", "ChangeSets", "PowerSystemResources", "ChangeItems", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.NetworkDataSet",
        title="NetworkDataSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "NetworkDataSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CircuitSection" class:
#------------------------------------------------------------------------------

class CircuitSection(IdentifiedObject):
    """ Section of circuit located between two sectionalizing devices. It may contain other circuit sections, for example, a lateral tapped off a primary.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ConductorAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.ConductorAsset"))

    NetworkDataSets = List(Instance("CIM.IEC61968.Informative.InfOperations.NetworkDataSet"))

    PowerSystemResources = List(Instance("CIM.IEC61970.Core.PowerSystemResource"))

    Circuits = List(Instance("CIM.IEC61968.Informative.InfOperations.Circuit"))

    # Kind of this circuit section.
    connectionKind = CircuitConnectionKind(desc="Kind of this circuit section.")

    #--------------------------------------------------------------------------
    #  Begin "CircuitSection" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "connectionKind",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ConductorAssets", "NetworkDataSets", "PowerSystemResources", "Circuits",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.CircuitSection",
        title="CircuitSection",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CircuitSection" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OutageRecord" class:
#------------------------------------------------------------------------------

class OutageRecord(Document):
    """ A document describing details of an outage in part of the electrical network, typically produced by a SCADA system following a breaker trip, or within a Trouble Call System by grouping customer calls. This has an associated OutageStep for each supply point. Primary cause of the outage is captured in 'category'. In some countries all outage restoration is performed using a SwitchingSchedule which complements the OutageRecord and records the ErpPersons (crew) and any planned Work. In other systems, it may be acceptable to manage outages including new WorkTasks without switching schedules. Note: The relationship between OutageRecord and ErpPerson and Crew is inherited as each is a type of Document.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    OutageReport = Instance("CIM.IEC61968.Informative.InfOperations.OutageReport",
        transient=True,
        opposite="OutageRecord",
        editor=InstanceEditor(name="_outagereports"))

    def _get_outagereports(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfOperations.OutageReport" ]
        else:
            return []

    _outagereports = Property(fget=_get_outagereports)

    # Multiple outage codes may apply to an outage record.
    OutageCodes = List(Instance("CIM.IEC61968.Informative.InfOperations.OutageCode"),
        desc="Multiple outage codes may apply to an outage record.")

    OutageSteps = List(Instance("CIM.IEC61968.Informative.InfOperations.OutageStep"))

    # Value of ErpOrganisation.mode at the time of OutageRecord.startDateTime.
    mode = Str(desc="Value of ErpOrganisation.mode at the time of OutageRecord.startDateTime.")

    # The damage code relative to the associated PowerSystemResource(s) and/or Asset(s). Examples include broken, burnout, failure, flashed (burned), manually operated, wire down, no damage - rolling blackout, none.
    damageCode = Str(desc="The damage code relative to the associated PowerSystemResource(s) and/or Asset(s). Examples include broken, burnout, failure, flashed (burned), manually operated, wire down, no damage - rolling blackout, none.")

    # Overall action taken to resolve outage (details are in 'WorkTasks').
    actionTaken = Str(desc="Overall action taken to resolve outage (details are in 'WorkTasks').")

    # Date and time restoration was completed for all customers impacted by this outage.
    endDateTime = Date(desc="Date and time restoration was completed for all customers impacted by this outage.")

    # True if planned, false otherwise (for example due to a breaker trip).
    isPlanned = Bool(desc="True if planned, false otherwise (for example due to a breaker trip).")

    #--------------------------------------------------------------------------
    #  Begin "OutageRecord" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "mode", "damageCode", "actionTaken", "endDateTime", "isPlanned",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "OutageReport", "OutageCodes", "OutageSteps",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.OutageRecord",
        title="OutageRecord",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OutageRecord" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CallBack" class:
#------------------------------------------------------------------------------

class CallBack(IdentifiedObject):
    """ Information about a planned CallBack or a CallBack that has occurred, from the utility to a customer regarding the status and plans about resolving trouble, performing work, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpPersons = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson"))

    Appointments = List(Instance("CIM.IEC61968.Informative.InfWork.Appointment"))

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

    TroubleTickets = List(Instance("CIM.IEC61968.Informative.InfOperations.TroubleTicket"))

    # Advice already given to the customer during this call back.
    advice = Str(desc="Advice already given to the customer during this call back.")

    # Additional contact details that are not provided for ErpPerson with ErpTelephoneNumber.
    contactDetail = Str(desc="Additional contact details that are not provided for ErpPerson with ErpTelephoneNumber.")

    # Comments by customer during this call back.
    comment = Str(desc="Comments by customer during this call back.")

    # Descriptiion of the problem reported during this call back.
    problemInfo = Str(desc="Descriptiion of the problem reported during this call back.")

    # (if callback already occured) Date and time when this call back occurred.
    dateTime = Date(desc="(if callback already occured) Date and time when this call back occurred.")

    #--------------------------------------------------------------------------
    #  Begin "CallBack" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "advice", "contactDetail", "comment", "problemInfo", "dateTime",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ErpPersons", "Appointments", "status", "TroubleTickets",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.CallBack",
        title="CallBack",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CallBack" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ChangeItem" class:
#------------------------------------------------------------------------------

class ChangeItem(IdentifiedObject):
    """ Description for a single change within an ordered list of changes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    PowerSystemResource = Instance("CIM.IEC61970.Core.PowerSystemResource",
        transient=True,
        opposite="ChangeItems",
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

    Location = Instance("CIM.IEC61968.Common.Location",
        transient=True,
        opposite="ChangeItems",
        editor=InstanceEditor(name="_locations"))

    def _get_locations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Location" ]
        else:
            return []

    _locations = Property(fget=_get_locations)

    Organisation = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation",
        transient=True,
        opposite="ChangeItems",
        editor=InstanceEditor(name="_erporganisations"))

    def _get_erporganisations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation" ]
        else:
            return []

    _erporganisations = Property(fget=_get_erporganisations)

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

    Asset = Instance("CIM.IEC61968.Assets.Asset",
        transient=True,
        opposite="ChangeItems",
        editor=InstanceEditor(name="_assets"))

    def _get_assets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Assets.Asset" ]
        else:
            return []

    _assets = Property(fget=_get_assets)

    Document = Instance("CIM.IEC61968.Common.Document",
        transient=True,
        opposite="ChangeItems",
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

    GmlObservation = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlObservation",
        transient=True,
        opposite="ChangeItems",
        editor=InstanceEditor(name="_gmlobservations"))

    def _get_gmlobservations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlObservation" ]
        else:
            return []

    _gmlobservations = Property(fget=_get_gmlobservations)

    ErpPerson = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson",
        transient=True,
        opposite="ChangeItems",
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

    Measurement = Instance("CIM.IEC61970.Meas.Measurement",
        transient=True,
        opposite="ChangeItems",
        editor=InstanceEditor(name="_measurements"))

    def _get_measurements(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.Measurement" ]
        else:
            return []

    _measurements = Property(fget=_get_measurements)

    GmlSelector = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlSelector",
        transient=True,
        opposite="ChangeItems",
        editor=InstanceEditor(name="_gmlselectors"))

    def _get_gmlselectors(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlSelector" ]
        else:
            return []

    _gmlselectors = Property(fget=_get_gmlselectors)

    ChangeSet = Instance("CIM.IEC61968.Informative.InfOperations.ChangeSet",
        transient=True,
        opposite="ChangeItems",
        editor=InstanceEditor(name="_changesets"))

    def _get_changesets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfOperations.ChangeSet" ]
        else:
            return []

    _changesets = Property(fget=_get_changesets)

    NetworkDataSet = Instance("CIM.IEC61968.Informative.InfOperations.NetworkDataSet",
        transient=True,
        opposite="ChangeItems",
        editor=InstanceEditor(name="_networkdatasets"))

    def _get_networkdatasets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfOperations.NetworkDataSet" ]
        else:
            return []

    _networkdatasets = Property(fget=_get_networkdatasets)

    # Kind of change for the associated object.
    kind = ChangeItemKind(desc="Kind of change for the associated object.")

    # Relative order of this ChangeItem in an ordered sequence of changes.
    sequenceNumber = Int(desc="Relative order of this ChangeItem in an ordered sequence of changes.")

    #--------------------------------------------------------------------------
    #  Begin "ChangeItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "kind", "sequenceNumber",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PowerSystemResource", "Location", "Organisation", "status", "Asset", "Document", "GmlObservation", "ErpPerson", "Measurement", "GmlSelector", "ChangeSet", "NetworkDataSet",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.ChangeItem",
        title="ChangeItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ChangeItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OrgPsrRole" class:
#------------------------------------------------------------------------------

class OrgPsrRole(Role):
    """ Roles played between Organisations and Power System Resources.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    PowerSystemResource = Instance("CIM.IEC61970.Core.PowerSystemResource",
        transient=True,
        opposite="ErpOrganisationRoles",
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

    ErpOrganisation = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation",
        transient=True,
        opposite="PowerSystemResourceRoles",
        editor=InstanceEditor(name="_erporganisations"))

    def _get_erporganisations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation" ]
        else:
            return []

    _erporganisations = Property(fget=_get_erporganisations)

    #--------------------------------------------------------------------------
    #  Begin "OrgPsrRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "PowerSystemResource", "ErpOrganisation",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.OrgPsrRole",
        title="OrgPsrRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OrgPsrRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OutageNotification" class:
#------------------------------------------------------------------------------

class OutageNotification(Document):
    """ A document containing information to be sent to customers notifying that an outage will take place. This is used to generate mailing lists for customers.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CustomerDatas = List(Instance("CIM.IEC61968.Customers.Customer"))

    # Likely duration of the interruption(s).
    duration = Minutes(desc="Likely duration of the interruption(s).")

    # Details of the outage 'reason'.
    reason = Str(desc="Details of the outage 'reason'.")

    # Number of possible interruptions that the customer may expect for this event.
    expectedInterruptionCount = Int(desc="Number of possible interruptions that the customer may expect for this event.")

    #--------------------------------------------------------------------------
    #  Begin "OutageNotification" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "duration", "reason", "expectedInterruptionCount",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CustomerDatas",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.OutageNotification",
        title="OutageNotification",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OutageNotification" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SwitchingSchedule" class:
#------------------------------------------------------------------------------

class SwitchingSchedule(Document):
    """ Document describing a sequence of steps to perform an item of work, for example to isolate some plant with regard to safety, equipment ratings, and standards of customer service. Note 1: SwitchingSchedule is intended to describe the full operational details for switching for real time operation which includes other operations such as grounding, applying safety documents etc.  Note 2: The association to ErpPerson suits the UK practice of quoting specific names (e.g the crew foreman). The association to Crew is for US practice.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Interval between starting and completion of the switching.
    interval = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Interval between starting and completion of the switching.",
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

    ScheduleSteps = List(Instance("CIM.IEC61968.Informative.InfOperations.SwitchingStep"))

    # All Crews executing this SwitchingSchedule.
    Crews = List(Instance("CIM.IEC61968.Informative.InfWork.Crew"),
        desc="All Crews executing this SwitchingSchedule.")

    WorkTask = Instance("CIM.IEC61968.Informative.InfWork.WorkTask",
        transient=True,
        opposite="SwitchingSchedules",
        editor=InstanceEditor(name="_worktasks"))

    def _get_worktasks(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.WorkTask" ]
        else:
            return []

    _worktasks = Property(fget=_get_worktasks)

    # Reason for switching.
    reason = Str(desc="Reason for switching.")

    #--------------------------------------------------------------------------
    #  Begin "SwitchingSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "reason",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "interval", "ScheduleSteps", "Crews", "WorkTask",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.SwitchingSchedule",
        title="SwitchingSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SwitchingSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "IncidentCode" class:
#------------------------------------------------------------------------------

class IncidentCode(IdentifiedObject):
    """ Classification of incident types. Multiple incident codes may apply to a given incident. The primary overall incident cause is recorded in 'IncidentRecord.category', and the main code in 'name'.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    IncidentRecords = List(Instance("CIM.IEC61968.Informative.InfOperations.IncidentRecord"))

    # Additional level of classification detail (as extension to the main code found in 'name').
    subCode = Str(desc="Additional level of classification detail (as extension to the main code found in 'name').")

    #--------------------------------------------------------------------------
    #  Begin "IncidentCode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subCode",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "IncidentRecords",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.IncidentCode",
        title="IncidentCode",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IncidentCode" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PlannedOutage" class:
#------------------------------------------------------------------------------

class PlannedOutage(Document):
    """ Planned outage involves network operations which will affect the supply of power to customers. Note that the list of Power System Resources for the PlannedOutage may be the same or a superset of the ones per OutageStep.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All customers affected by this work. Derived from WorkOrder.connectedCustomers
    CustomerDatas = List(Instance("CIM.IEC61968.Customers.Customer"),
        desc="All customers affected by this work. Derived from WorkOrder.connectedCustomers")

    OutageSchedules = List(Instance("CIM.IEC61970.Outage.OutageSchedule"))

    # Kind of outage.
    kind = OutageKind(desc="Kind of outage.")

    #--------------------------------------------------------------------------
    #  Begin "PlannedOutage" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "kind",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CustomerDatas", "OutageSchedules",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.PlannedOutage",
        title="PlannedOutage",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PlannedOutage" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TroubleTicket" class:
#------------------------------------------------------------------------------

class TroubleTicket(Document):
    """ A document used to report electrical trouble. The trouble may either be an outage or non-outage problem, such as power quality. It must always be associated with an Incident Record. Note that a separate Activity Record is created for each call associated with an instance of Trouble Ticket. The time of a call is stored in ActivityRecord.createdOn and comments are recorded in ActivityRecord.remarks.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CustomerData = Instance("CIM.IEC61968.Customers.Customer",
        transient=True,
        opposite="TroubleTickets",
        editor=InstanceEditor(name="_customers"))

    def _get_customers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Customers.Customer" ]
        else:
            return []

    _customers = Property(fget=_get_customers)

    # Period between this source of trouble started and was resolved.
    troublePeriod = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Period between this source of trouble started and was resolved.",
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

    CallBacks = List(Instance("CIM.IEC61968.Informative.InfOperations.CallBack"))

    IncidentRecord = Instance("CIM.IEC61968.Informative.InfOperations.IncidentRecord",
        transient=True,
        opposite="TroubleTickets",
        editor=InstanceEditor(name="_incidentrecords"))

    def _get_incidentrecords(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfOperations.IncidentRecord" ]
        else:
            return []

    _incidentrecords = Property(fget=_get_incidentrecords)

    # Means the customer used to report trouble (default is 'call').
    reportingKind = TroubleReportingKind(desc="Means the customer used to report trouble (default is 'call').")

    # Advice already given to the customer at time when trouble was first reported.
    advice = Str(desc="Advice already given to the customer at time when trouble was first reported.")

    # True if requested to customer when someone is about to arrive at their premises.
    callBack = Bool(desc="True if requested to customer when someone is about to arrive at their premises.")

    # Priority of trouble call.
    priority = Str(desc="Priority of trouble call.")

    # True if person reporting trouble requested a call back to confirm power has been restored. The person and their contact information is maintained in the assoicated Customer informaiton. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'.
    informAfterRestored = Bool(desc="True if person reporting trouble requested a call back to confirm power has been restored. The person and their contact information is maintained in the assoicated Customer informaiton. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'.")

    # Estimated restoration date and time last provided to the customer.
    estimatedRestoreDateTime = Date(desc="Estimated restoration date and time last provided to the customer.")

    # True if person reporting trouble requested a call back when sigificant information became available about cause of the outage and the estimated restoration time. The person and their contact information are maintained in the assoicated Customer information. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'.
    informBeforeRestored = Bool(desc="True if person reporting trouble requested a call back when sigificant information became available about cause of the outage and the estimated restoration time. The person and their contact information are maintained in the assoicated Customer information. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'.")

    # Code for a reported hazard condition.
    hazardCode = Str(desc="Code for a reported hazard condition.")

    # Date and time trouble call first received. The date and time of subsequent calls by the same customer for the same trouble are recorded in associated Activity Records.
    firstCallDateTime = Date(desc="Date and time trouble call first received. The date and time of subsequent calls by the same customer for the same trouble are recorded in associated Activity Records.")

    #--------------------------------------------------------------------------
    #  Begin "TroubleTicket" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "reportingKind", "advice", "callBack", "priority", "informAfterRestored", "estimatedRestoreDateTime", "informBeforeRestored", "hazardCode", "firstCallDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CustomerData", "troublePeriod", "CallBacks", "IncidentRecord",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.TroubleTicket",
        title="TroubleTicket",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TroubleTicket" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "IncidentRecord" class:
#------------------------------------------------------------------------------

class IncidentRecord(Document):
    """ Document describing the incident reported in a TroubleTicket. If the incident has to do with an outage, this will be associated with an OutageRecord. Primary cause of the incident is captured in 'category'.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    IncidentCodes = List(Instance("CIM.IEC61968.Informative.InfOperations.IncidentCode"))

    # Period between the first customer impacted by the incident and the incident resolution for all customers impacted.
    period = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Period between the first customer impacted by the incident and the incident resolution for all customers impacted.",
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

    TroubleTickets = List(Instance("CIM.IEC61968.Informative.InfOperations.TroubleTicket"))

    #--------------------------------------------------------------------------
    #  Begin "IncidentRecord" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "IncidentCodes", "period", "TroubleTickets",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.IncidentRecord",
        title="IncidentRecord",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IncidentRecord" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ChangeSet" class:
#------------------------------------------------------------------------------

class ChangeSet(IdentifiedObject):
    """ The updates required in a transaction for an existing data set are grouped into a single ChangeSet. In data sets (e.g., NetworkDataSet), each major step in the ChangeSet is described through a separate ChangeItem associated with the data set. Within each data set, each inidividual object change is described with a seperate ChangeItem associated with the object.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    LandBases = List(Instance("CIM.IEC61968.Informative.InfOperations.LandBase"))

    NetworkDataSets = List(Instance("CIM.IEC61968.Informative.InfOperations.NetworkDataSet"))

    ChangeItems = List(Instance("CIM.IEC61968.Informative.InfOperations.ChangeItem"))

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

    #--------------------------------------------------------------------------
    #  Begin "ChangeSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "LandBases", "NetworkDataSets", "ChangeItems", "status", "Documents",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.ChangeSet",
        title="ChangeSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ChangeSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OutageReport" class:
#------------------------------------------------------------------------------

class OutageReport(Document):
    """ Document with statistics of an outage.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # reference to related document
    OutageRecord = Instance("CIM.IEC61968.Informative.InfOperations.OutageRecord",
        desc="reference to related document",
        transient=True,
        opposite="OutageReport",
        editor=InstanceEditor(name="_outagerecords"))

    def _get_outagerecords(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfOperations.OutageRecord" ]
        else:
            return []

    _outagerecords = Property(fget=_get_outagerecords)

    # OutageHistory of a customer, which may include this OutageReport.
    OutageHistory = Instance("CIM.IEC61968.Informative.InfCustomers.OutageHistory",
        desc="OutageHistory of a customer, which may include this OutageReport.",
        transient=True,
        opposite="OutageReports",
        editor=InstanceEditor(name="_outagehistorys"))

    def _get_outagehistorys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfCustomers.OutageHistory" ]
        else:
            return []

    _outagehistorys = Property(fget=_get_outagehistorys)

    # Average Customer Minutes Lost (CML) for this outage.
    averageCml = Minutes(desc="Average Customer Minutes Lost (CML) for this outage.")

    # Total outage duration.
    outageDuration = Minutes(desc="Total outage duration.")

    # Total number of outaged customers.
    customerCount = Int(desc="Total number of outaged customers.")

    # Total Customer Minutes Lost (CML).
    totalCml = Minutes(desc="Total Customer Minutes Lost (CML).")

    #--------------------------------------------------------------------------
    #  Begin "OutageReport" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "averageCml", "outageDuration", "customerCount", "totalCml",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "OutageRecord", "OutageHistory",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.OutageReport",
        title="OutageReport",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OutageReport" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LandBase" class:
#------------------------------------------------------------------------------

class LandBase(Document):
    """ Land base data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "LandBase" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.LandBase",
        title="LandBase",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LandBase" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Circuit" class:
#------------------------------------------------------------------------------

class Circuit(EquipmentContainer):
    """ EquipmentContainer that will typically include conductors, energy consumers, transformers and transformer windings, switches, shunt compensators, etc., likely at different voltages. Circuit extends from a substation to a set of open points (radial circuit), or to a second substation (looped circuit). It generally starts with a switching device, located in a substation. Membership in a Circuit is based on the nominal or design system configuration, but the electrical connectivity will change during switching operations.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "Circuit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "TopologicalNode", "ConnectivityNodes", "Equipments",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfOperations.Circuit",
        title="Circuit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Circuit" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
